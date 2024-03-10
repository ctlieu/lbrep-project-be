# backend/feedback/urls.py
from django.urls import path
from .views import FeedbackFormView, SuccessView  # Replace YourView with the actual view you want to use

app_name = 'feedback'

urlpatterns = [
    path('submit/', FeedbackFormView.as_view(), name='submit-feedback'),
    path('success/', SuccessView.as_view(), name='success-feedback'),
    # Add more paths as needed
]


