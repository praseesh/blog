from django.urls import path
from .views import PostCreationView

urlpatterns = [
    path('', PostCreationView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostCreationView.as_view(), name='post-detail'),
]