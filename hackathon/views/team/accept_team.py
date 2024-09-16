import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from dotenv import load_dotenv

from hackathon.tasks import send_team_approval_email_to_students
from hackathon.models import Team, Edition

load_dotenv()


@api_view(["GET"])
def approve_team(request, verification_token) -> Response:
    try:
        team = Team.objects.get(verification_token=verification_token)
    except team.DoesNotExist:
        return Response(
            {"error": "Time não encontrado."},
            status=status.HTTP_404_NOT_FOUND,
        )

    edition = Edition.objects.get(id=team.edition.id)

    if edition.registration_deadline > timezone.now().date():
        team.verification_token = None
        team.valid_registration = True
        team.save()

        send_team_approval_email_to_students.delay(team.id)
        return Response(
            {"message": "Trabalho aceito."},
            status=status.HTTP_200_OK,
        )

    return Response(
        {"error": "Data limite para aceitar o time expirou."},
    )
