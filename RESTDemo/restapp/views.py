from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course, CourseSerializer
# CRUD
# Read All Data
@api_view(['GET'])
def get_course(request):
    courses = Course.objects.all()
    course_serializer = CourseSerializer(courses, many=True)
    print('Courses : ', course_serializer.data)
    return Response(course_serializer.data)


@api_view(['POST'])
def add_course(request):
    course_serializer = CourseSerializer(data=request.data)
    if course_serializer.is_valid():
        course_serializer.save()
        return Response(course_serializer.data)
    return Response(course_serializer.errors)


@api_view(['GET'])
def get_one_course(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        course_serializer = CourseSerializer(course)
        return Response(course_serializer.data)
    except:
        msg = 'DATA Not Found'
        return Response(msg)


@api_view(['PUT'])
def update_course(request, pk):
    course = Course.objects.get(pk=pk)
    course_serializer = CourseSerializer(course, data=request.data)
    if course_serializer.is_valid():
        course_serializer.save()
        return Response(course_serializer.data)
    return Response(course_serializer.errors)


@api_view(['DELETE'])
def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


