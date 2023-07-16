from django.urls import path

from . import views

urlpatterns = [
    # CRUD Course
    path('courses/', views.get_course),
    path('add_course/', views.add_course),
    path('get_one_course/<int:pk>', views.get_one_course),
    path('update_course/<int:pk>', views.update_course),
    path('delete_course/<int:pk>', views.delete_course),
]
