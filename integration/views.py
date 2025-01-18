from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from integration.serializer import HookSerializer
from rest_framework.response import Response
from integration.task import *
from .models import *


class HookAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = HookSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data['message']
            callback_url = serializer.validated_data['callback']

            try:

                object_create = HookRequest.objects.create(
                    message=message,
                    callback_url=callback_url,
                )

                process_hook_celery_task.delay(object_create.id)

                return Response({
                    "message": message,
                    "callback_url": callback_url,
                })

            except Exception as e:
                return Response({
                    "error": str(e),
                })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


