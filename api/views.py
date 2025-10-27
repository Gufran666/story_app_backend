from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import Story 
from .serializers import StorySerializer

class GenerateStory(APIView):
    def post(self, request):
        prompt = request.data.get('prompt')
        if not prompt:
            return Response({'error': 'Prompt is required'}, status=status.HTTP_400_BAD_REQUEST)

        generated_text = f"Mock story based on: {prompt}"
        choices = ["Choice 1: Continue the adventure.", "Choice 2: Turn back."]
        story = Story.objects.create(prompt=prompt, full_text=generated_text)
        response_data = {
            'id': story.id,
            'text': generated_text,
            'choices': choices
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

class StoryList(APIView):
    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)
