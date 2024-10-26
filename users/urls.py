from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.UserListCreate.as_view(), name='user_list_create'),
    path('<int:pk>/', views.UserRetrieveUpdateDestroy.as_view(), name='user_detail_update_destroy'),
    path('<str:email>/', views.UserEmailRetrieveUpdateDestroy.as_view(), name='user_by_email_detail_update_destroy'),
]
