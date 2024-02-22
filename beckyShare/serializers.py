from rest_framework import serializers
from .models import OperationalUser, File, ClientUser


class OpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationalUser
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ClientUser
        fields = '__all__'       