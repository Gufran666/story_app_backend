from django.urls import path 
from .views import GenerateStory, StoryList

urlpatterns = [
    path('generate/', GenerateStory.as_view(), name='generate-story'),
    path('stories/', StoryList.as_view(), name='story-list'),
]
