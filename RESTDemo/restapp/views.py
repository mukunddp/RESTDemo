from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course, CourseSerializer


@api_view(['GET'])
def getcourse(request):
    courses = Course.objects.all()
    courseSerializer = CourseSerializer(courses, many=True)
    return Response(courseSerializer.data)


@api_view(['POST'])
def addcourse(request):
    courseserializer = CourseSerializer(data=request.data)
    if courseserializer.is_valid():
        courseserializer.save()
        return Response(courseserializer.data)
    return Response(courseserializer.errors)


@api_view(['GET'])
def getonecourse(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        courseserializer = CourseSerializer(course)
        return Response(courseserializer.data)
    except:
        msg = 'DATA Not Found'
        return Response(msg)


@api_view(['PUT'])
def updatecourse(request, pk):
    course = Course.objects.get(pk=pk)
    courseserializer = CourseSerializer(course, data=request.data)
    if courseserializer.is_valid():
        courseserializer.save()
    return Response(courseserializer.errors)


@api_view(['DELETE'])
def deletecourse(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


