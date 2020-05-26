from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import All_map
from .serializers import All_mapSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("HelloWorld!")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = All_map.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = All_mapSerializer(randomQuizs, many = True)
    return Response(serializer.data)