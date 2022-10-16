from rest_framework import serializers, viewsets
from .models import Company, User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("name",)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name",)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer