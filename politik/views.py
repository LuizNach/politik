from django.contrib.auth.models import User, Group

from rest_framework.views import APIView

from rest_framework import viewsets
from .serialiazers import UserSerializer, GroupSerializer, PoliticianSerializer, LawSerializer
from politik.models import Politician, LawProject
from django.core import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .tasks import task_number_one



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class PoliticianViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Politician.objects.all().order_by('id')
    serializer_class = PoliticianSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view()
def hello_world(request):
    pol = Politician.objects.filter(user_id=23)
    serializer = PoliticianSerializer(pol, many=True)
    return Response(serializer.data)

@api_view()
def get_followed_politicians(request):
    username = request.user.username
    politicians = Politician.objects.filter(followers__username=username)
    serializer = PoliticianSerializer(politicians, many=True)
    return Response(serializer.data)



class LawsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LawProject.objects.all().order_by('id')
    serializer_class = LawSerializer

