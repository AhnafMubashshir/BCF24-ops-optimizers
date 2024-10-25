from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HealthCheckView(APIView):
    def get(self, request):
        return Response({'message':'Order Server Running'}, status=status.HTTP_200_OK)