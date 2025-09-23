from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from mdq.serializers import MdqUserRegisterSerializer

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def user_registration(request):
    serializer = MdqUserRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
