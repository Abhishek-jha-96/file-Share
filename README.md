# file-Share

Brief description of your Django and DRF project.

## Table of Contents
- [Setup](#setup)
- [API Endpoints](#api-endpoints)

## Setup

### Prerequisites
Make sure you have the following installed:
- Python (3.x recommended)
- venv (for virtual environment management)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-project.git
2. Navigate to the project directory:
   ```bash
   cd your-project

3. Create and activate virtual environment:
   ```bash
   python -m venv myenv

4. Install django and drf
5. apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
6. Create a superuser and run dev server:
   ```bash
   python manage.py createsuperuser
   python manage.py runserver
The project should now be running at http://localhost:8000/.

### API Endpoints

- login/opsuser => for opsuser to login
- opsuser/ => for opsuser to upload files
- client/signup => for client to signup
- client/Lists/ => getting list of all uploaded files
- client/download/<int:pk> => getting the downloand link of the particular file


this project Uses basic-auth and proper permissions

**Note: - I was not able to send mail for verification without a domain or other third party pluggins.

         
