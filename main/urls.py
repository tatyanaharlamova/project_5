from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import (contact, StudentDetailView, StudentCreateView, StudentUpdateView,
                        StudentDeleteView, toggle_activity, index)

app_name = MainConfig.name

urlpatterns = [
    # redis,
    path("contact/", contact,  name='contact'),
    path("", cache_page(60)(index), name='index'),
    # path('view/<int:pk>/', view_student, name='student_detail'),
    path('view/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('create/', StudentCreateView.as_view(), name='create_student'),
    path('edit/<int:pk>/', StudentUpdateView.as_view(), name='update_student'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    path('activity<int:pk>/', toggle_activity, name='toggle_activity'),

]
