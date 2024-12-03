from user.models import CustomUser
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from hackathon.tasks.forget_password import send_forget_password_email
import secrets
import datetime
import pytz


@api_view(["POST"])
@permission_classes([AllowAny])
@authentication_classes([])
def forget_password(request):
    email = request.data.get("email")
    try:
        user = CustomUser.objects.get(email=email)

        if user.password_reset_token_created is not None:
            user.password_reset_token = None

        desired_length = 8
        token_size = (desired_length + 1) // 2
        token = secrets.token_hex(token_size)
        user.password_reset_token = token
        user.password_reset_token_created = pytz.utc.localize(datetime.datetime.now())
        user.save()

        print(user.password_reset_token)

        send_forget_password_email.delay(email, token)

        return Response(
            status=status.HTTP_200_OK, data={"message": "Email enviado com sucesso."}
        )

    except CustomUser.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={"message": "Usuário não encontrado."},
        )
