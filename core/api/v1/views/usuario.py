from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, viewsets
from core.api.v1.serializer.user import UserSerializer
from core.models import User


class UserViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(UserViewSet, self).get_permissions()
