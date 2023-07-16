1) Install Django
    - pip install django

2) create a django project
    - django-admin startproject RESTDemo
      (It will create a direct named ad RESTDemo, and inside that direct we will be having project containing a
      manage.py file and a package named RESTDemo and inside that package we will having setting of project)

3) Install Django Rest Framework
    - pip install djangorestframework
      (IT will install packages inside virtual env.)

4) After installing Django Rest Framework, add 'rest_framework' as app name inside 'INSTALLED APPS' of settings.py.

5) We will create a app inside our project
    - Let's name it as 'restapp'
        - django-admin startapp restapp
        - (This will create a package named as restapp in current directory of manage.py)

6) After creating a 'restapp' need to add in 'INSTALLED APPS' of settings.py

7) Now create a urls.py file in restapp and inside 'urls.py' of RESTDemo we are going include newly created urls of
   restapp
   `path('api/', include('restapp.urls')),`
    - Inside restapp/urls.py we will write our APIS.

8) Now in models.py we will create a model for Course
   `   class Course(models.Model):
   Name = models.CharField(max_length=100)
   author = models.CharField(max_length=3)
   price = models.IntegerField()
   discount = models.IntegerField(default=0)
   duration = models.IntegerField()`

9) Now after creating a model inside models.py we will create a CourseSerializer by importing serializers from
   django_restframework, Inheriting ModelSerializer inside CourseSerializer class as below  
`from rest_framework import serializers 
class CourseSerializer(serializers.ModelSerializer):
   class Meta: 
   model = Course fields = '__all__'`

10) Use restframework and create views 
11) also using decorator @api_view we can request methods as GET, POST, PUT, DELETE  
12) Refer above project.
   
    