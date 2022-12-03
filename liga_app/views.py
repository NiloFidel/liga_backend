from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from liga_app.serializers import UserSerializer, GroupSerializer
from liga_app.models import *
from liga_app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import Permission


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    http_method_names = ['get', 'post', 'delete']
    permission_classes = [DjangoModelPermissions]

    @action(detail=True, methods=['get'])
    def unavailable(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.status = True
        return Response({'status': 'unavailable'})

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter
