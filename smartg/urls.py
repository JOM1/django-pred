from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.upload_file, name='upload_file'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
]
