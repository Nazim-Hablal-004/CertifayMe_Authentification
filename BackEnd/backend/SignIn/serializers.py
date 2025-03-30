from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ["id", "username", "email", "password", "role", "is_verified", "created_at"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

class UniversityCertifySerializer(serializers.ModelSerializer):
    class Meta:
        model = University_Certify_me
        fields = "__all__"

class CompaniesCertifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies_Certify_me
        fields = "__all__"

class MinistryCertifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry_Certify_me
        fields = "__all__"
