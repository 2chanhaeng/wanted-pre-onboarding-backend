from email.mime import application
from rest_framework import serializers, viewsets
from .models import Company, User, Notice, Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ("notice", "user")


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class NoticeSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = ("name", "company", "application")


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class CompanySerializer(serializers.ModelSerializer):
    notice = NoticeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ("name", "notice")


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UserSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("name", "application")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
