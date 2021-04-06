from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.api.v1.serializer.user import UserSerializer
from core.models import User



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
   # permission_classes = (IsAuthenticated, )
