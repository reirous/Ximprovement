from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from frigobar.serializers.userSerializer import UserSerializer, RegisterSerializer
from rest_framework.decorators import action
from rest_framework.schemas import ManualSchema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

    @action(
        methods=["get"],
        detail=False,
        url_path="current",
        schema=ManualSchema(
            fields=[], description="Get the data from the currently logged user"
        ),
    )
    def get(self, request: Request):
        """
        Get the data from the currently logged user
        """
        if request.user.is_authenticated:
            aux = {'user': request.user.id, 'email' : request.user.email, 'perm_admin' : request.user.is_staff}
            return JsonResponse({'perfil': aux})
        else:
            return Response(status=status.HTTP_200_OK)