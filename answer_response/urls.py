from django.urls import path
from answer_response.views import HomeView,ValidateQuestionView


urlpatterns=[
    path('',HomeView.as_view()),
    path('api/user/',ValidateQuestionView.as_view()),
]