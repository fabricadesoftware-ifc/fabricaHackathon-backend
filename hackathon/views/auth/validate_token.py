import pytz
from typing import Any, Dict, Optional
from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.request import Request
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from user.models import CustomUser
from config.settings import TOKEN_EXPIRATION_SECONDS

extend_schema(tags=["forget_password"])


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def validate_token(request: Request, *args: Any, **kwargs: Dict[str, Any]) -> Response:
    token: Optional[str] = request.data.get("token")

    if not token:
        return Response(
            {"message": "Token não fornecido."}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user: CustomUser = CustomUser.objects.get(password_reset_token=token)
    except CustomUser.DoesNotExist:
        return Response(
            {"message": "Token inválido ou esgotado."}, status=status.HTTP_404_NOT_FOUND
        )

    if user.password_reset_token_created:
        token_expiration = user.password_reset_token_created + timedelta(
            seconds=TOKEN_EXPIRATION_SECONDS
        )

        if token_expiration < datetime.now(pytz.utc):
            user.password_reset_token = None
            user.password_reset_token_created = None
            user.save()
            return Response(
                {"message": "Token inválido ou esgotado."},
                status=status.HTTP_404_NOT_FOUND,
            )

    return Response({"message": "Token válido."}, status=status.HTTP_200_OK)
