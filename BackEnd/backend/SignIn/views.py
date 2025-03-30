from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from .models import Account, University_Official_DB, University_Certify_me, Companies_Certify_me, Ministry_Certify_me
from .serializers import AccountSerializer, UniversityCertifySerializer, CompaniesCertifySerializer, MinistryCertifySerializer

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        role = data.get("role")

        if Account.objects.filter(email=data["email"]).exists():
            return Response({"error": "Cet email est déjà utilisé"}, status=status.HTTP_400_BAD_REQUEST)

        # Vérification spécifique pour l'université
        if role == "university":
            university = University_Official_DB.objects.filter(email=data["email"]).first()
            if not university:
                return Response({"error": "L'université n'est pas reconnue"}, status=status.HTTP_400_BAD_REQUEST)

            if university.name != data["name"] or university.phone != data["phone"]:
                return Response({"error": "Les informations ne correspondent pas"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Génération du token unique
        verification_token = get_random_string(32)


        account = Account.objects.create(
            username=data["username"],
            email=data["email"],
            password=make_password(data["password"]),
            role=role,
            is_verified=False
        )

        # Création des entrées spécifiques à chaque rôle
        if role == "university":
            University_Certify_me.objects.create(University_acount=account, name=data["name"], address=data["address"], phone=data["phone"])
        elif role == "companies":
            Companies_Certify_me.objects.create(Companies_acount=account, name=data["name"], address=data["address"], phone=data["phone"])
        elif role == "minister":
            Ministry_Certify_me.objects.create(Ministry_acount=account, name=data["name"], address=data["address"])

        
        # Envoi de l'email de validation
        verification_link = f"http://localhost:8000/auth/verify-email/{verification_token}/"
        send_mail(
            "Validation de votre compte",
            "Cliquez sur ce lien pour valider votre compte : http://localhost:8000/auth/verify-email/",
            "nazimhablal004@gmail.com",
            [account.email],
            fail_silently=False,
        )

        return Response({"message": "Un email de validation a été envoyé"}, status=status.HTTP_201_CREATED)
