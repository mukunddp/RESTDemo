from django.db import models
from rest_framework import serializers


class Course(models.Model):
    Name = models.CharField(max_length=100)
    author = models.CharField(max_length=3)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    duration = models.IntegerField()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class Batch(models.Model):
    batch_name = models.CharField(max_length=100)
    start_date = models.DateField()
    trainer_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
