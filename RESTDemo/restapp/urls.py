from django.urls import path

from . import views

urlpatterns = [
    path('courses/', views.getcourse),
    path('addcourse/', views.addcourse),
    path('getonecourse/<int:pk>', views.getonecourse),
    path('updatecourse/<int:pk>', views.updatecourse),
    path('deletecourse/<int:pk>', views.deletecourse),
]
