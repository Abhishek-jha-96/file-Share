from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .serializers import FileSerializer, ClientSerializer
from rest_framework import authentication, permissions
from .models import OperationalUser, File, ClientUser
import uuid

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# import hashlib
# from django.core.mail import send_mail
 
# Create your views here.

class OpsUserLogin(APIView):
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        user = None
        user = OperationalUser.objects.get(email=email, password=password)

        if user is not None:
            # token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": 'Invalid credential'}, status=status.HTTP_401_UNAUTHORIZED)


class OpsUserView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def post(self, request, format=None):
        uploaded_file = request.data.get('file')
        if not uploaded_file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
        
        ops_user = request.user
        print(ops_user)
        if not ops_user:
            return Response({"error": "Invalid/NO email address"}, status=status.HTTP_400_BAD_REQUEST)
        file_data = {
                     'uploaded_by': ops_user.id,
                     'file': uploaded_file,
                     'name': uploaded_file.name,
                     'file_type': uploaded_file.name.split('.')[-1]
                     }
        file_serializer = FileSerializer(data=file_data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientSignup(APIView):
    def post(self, request, format=None):
        data = request.data

        if not data:
            return Response({"error": "Missing data"}, status=status.HTTP_400_BAD_REQUEST)

        if ClientUser.objects.filter(email=data['email']).exists():
            return Response({"Error": "Email already in use"}, status=status.HTTP_400_BAD_REQUEST)
        
        verification_token = str(uuid.uuid4())

        client_data = {
            'email': data['email'],
            'password': data['password'],
            'is_active': True,
            'is_verified': False,
            'verification_token': verification_token,
        }
        client_serializer = ClientSerializer(data=client_data)

        if client_serializer.is_valid():
            client_serializer.save()
            #not working without any third party mail sending pluggin or without a domain
            # verification_url = self.generate_verification_url(verification_token)
            # self.send_verification_email(data['email'], verification_url)

            return Response({"message": "Account create succefully. Verification email sent."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        
    # def generate_verification_url(self, token):
    #     hashed_token = hashlib.sha256(token.encode()).hexdigest()
    #     return f"http://127.0.0.1:8000/client/{hashed_token}/"

    # def send_verification_email(self, email, verification_url):
    #     subject = "Account Verification"
    #     message = f"Please click the following link to verify your mail: {verification_url}"
    #     send_mail(subject, message, 'abhishekjha96500@gmail.com', [email])    

class ClientListall(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        files = File.objects.all()
        file_serializer = FileSerializer(files, many=True)
        #serialized data
        serialized_data = file_serializer.data

        return Response(serialized_data, status=status.HTTP_200_OK)

class ClientFileDownload(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            file = File.objects.get(pk=pk)
            file_path = file.file.path


            download_link = f"{file_path}"
            response = JsonResponse({
                'download_link': download_link,
                'message': 'success'
            })
            return response
        except File.DoesNotExist:
            return JsonResponse({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)