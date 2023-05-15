log='''\033[1;31m
 _____       _       ___   __   _   _____   _____  
|  _  \     | |     /   | |  \ | | /  ___| /  _  \ 
| | | |     | |    / /| | |   \| | | |     | | | | 
| | | |  _  | |   / / | | | |\   | | |  _  | | | | 
| |_| | | |_| |  / /  | | | | \  | | |_| | | |_| | 
|_____/ \_____/ /_/   |_| |_|  \_| \_____/ \_____/ 
                      MR DARK
'''
print(log)
import os
name_folder = input('Enter The Folder Name  : ')
name_project = input('Enter The Project Name : ')
name_app = input('Enter The Apps Name : ')
os.system('python -m venv '+name_folder)
os.chdir(name_folder)
os.system('.\Scripts\activate')
os.system('pip install django')
os.system('django-admin startproject '+name_project)
os.chdir(name_project)
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
print('Creat User And Password ')
os.system('python manage.py createsuperuser')
os.system('python manage.py startapp '+name_app)
os.system('code .')
os.system('python manage.py runserver')
