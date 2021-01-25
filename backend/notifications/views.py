from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, status, viewsets

from .models import Notification
from .serializers import NotificationSerializer
from .renderers import NotificationJSONRenderer

class NotificationsAPIViewSet(mixins.CreateModelMixin, 
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    lookup_field = 'id'
    queryset = Notification.objects.select_related('user').filter(seen=False)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (NotificationJSONRenderer,)
    serializer_class = NotificationSerializer

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.queryset.filter(user=request.user).order_by('created_at'))
        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def update(self, request, id):
        serializer_context = {'request': request}
        try:
            serializer_instance = self.queryset.filter(user=request.user).get(pk=id)
        except Notification.DoesNotExist:
            raise NotFound('A notification with this id does not exist.')
        serializer_data = request.data.get('notification', {})
        serializer = self.serializer_class(
            serializer_instance, 
            context=serializer_context,
            data=serializer_data, 
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)