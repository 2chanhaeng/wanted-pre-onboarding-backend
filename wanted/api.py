from email.mime import application
from rest_framework import serializers, viewsets
from .models import Company, User, Notice, Application
import json


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
        fields = "__all__"

    def validate(self, data):
        # name이 없는지, 제한을 넘지 않는 지 검사
        if "name" not in data or len(data["name"]) > 256:
            raise serializers.ValidationError("Notice name is required")
        # 자동으로 생성되는 속성은 금지
        if {"id", "date", "application", "other_notice"} & set(self.initial_data):
            raise serializers.ValidationError(
                "Notice date and application are not allowed"
            )
        # rawdata에서 제외할 데이터
        not_from_rawdata = {"name", "company", "csrfmiddlewaretoken"}
        # rawdata에서 제외한 데이터를 data에 추가 후 반환
        return data | {
            k: v for k, v in self.initial_data.items() if k not in not_from_rawdata
        }

    def create(self, validated_data):
        # name을 제외한 모든 데이터를 info에 json 문자열로 저장
        name = validated_data.pop("name")
        company = validated_data.pop("company")
        info = json.dumps(validated_data)
        return Notice.objects.create(name=name, company=company, info=info)

    def update(self, instance, validated_data):
        # name을 제외한 모든 데이터를 info에 json 문자열로 업데이트하여 저장
        # info가 없다면 빈 dict로 초기화 후 업데이트
        instance.name = validated_data.get("name", instance.name)
        instance.company = validated_data.get("company", instance.company)
        instance.info = (
            json.loads(instance.info)
            if instance.info
            else {} | json.dumps(validated_data)
        )
        instance.save()
        return instance

    def to_representation(self, instance: Notice):
        # info를 json 문자열에서 dict로 변환하여 다른 데이터와 합쳐서 반환
        # info가 없다면 빈 dict로 초기화 후 합침
        return {
            "id": instance.id,
            "name": instance.name,
            "company": self.fields["company"].to_representation(instance.company),
            # 현재 공고를 제외한 회사의 모든 공고를 가져오기
            "other_notice": [
                notice.id
                for notice in instance.company.notice_set.exclude(id=instance.id)
            ],
            "date": instance.date,
        } | (json.loads(instance.info) if instance.info else {})

    @staticmethod
    def to_representation_in_company(instance: Notice):
        # Company 요소에서 Notice를 표현할 때 사용
        # company와 other_notice를 제외한 데이터를 반환
        return {
            "id": instance.id,
            "name": instance.name,
            "date": instance.date,
        } | (json.loads(instance.info) if instance.info else {})


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class CompanySerializer(serializers.ModelSerializer):
    notice = NoticeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"

    def validate(self, data):
        # name이 없는지, 제한을 넘지 않는 지 검사
        if "name" not in data or len(data["name"]) > 256:
            raise serializers.ValidationError("User name is required")
        # 자동으로 생성되는 속성은 금지
        if {"id", "date", "notice"} & set(self.initial_data):
            raise serializers.ValidationError("User date and notice are not allowed")
        # 문제가 없다면 raw data를 반환
        return self.initial_data

    def create(self, validated_data):
        # name을 제외한 모든 데이터를 info에 json 문자열로 저장
        name = validated_data.pop("name")
        info = json.dumps(validated_data)
        return Company.objects.create(name=name, info=info)

    def update(self, instance, validated_data):
        # name을 제외한 모든 데이터를 info에 json 문자열로 업데이트하여 저장
        # info가 없다면 빈 dict로 초기화 후 업데이트
        instance.name = validated_data.get("name", instance.name)
        instance.info = (
            json.loads(instance.info)
            if instance.info
            else {} | json.dumps(validated_data)
        )
        instance.save()
        return instance

    def to_representation(self, instance: Company):
        # info를 json 문자열에서 dict로 변환하여 다른 데이터와 합쳐서 반환
        # info가 없다면 빈 dict로 초기화 후 합침
        return {
            "id": instance.id,
            "name": instance.name,
            "date": instance.date,
            # notice는 NoticeSerializer에서 처리
            "notice": [
                NoticeSerializer.to_representation_in_company(notice)
                for notice in instance.notice_set.all()
            ],
        } | (json.loads(instance.info) if instance.info else {})


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UserSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        # name이 없는지, 제한을 넘지 않는 지 검사
        if "name" not in data or len(data["name"]) > 256:
            raise serializers.ValidationError("Company name is required")
        # 자동으로 생성되는 속성은 금지
        if {"id", "date", "application"} & set(self.initial_data):
            raise serializers.ValidationError("Company date and info are not allowed")
        # 문제가 없다면 raw data를 반환
        return self.initial_data

    def create(self, validated_data):
        # name을 제외한 모든 데이터를 info에 json 문자열로 저장
        name = validated_data.pop("name")
        info = json.dumps(validated_data)
        return User.objects.create(name=name, info=info)

    def update(self, instance, validated_data):
        # name을 제외한 모든 데이터를 info에 json 문자열로 업데이트하여 저장
        # info가 없다면 빈 dict로 초기화 후 업데이트
        instance.name = validated_data.get("name", instance.name)
        instance.info = (
            json.loads(instance.info)
            if instance.info
            else {} | json.dumps(validated_data)
        )
        instance.save()
        return instance

    def to_representation(self, instance: Company):
        # info를 json 문자열에서 dict로 변환하여 다른 데이터와 합쳐서 반환
        # info가 없다면 빈 dict로 초기화 후 합침
        return {
            "id": instance.id,
            "name": instance.name,
            "date": instance.date,
            # application는 ApplicationSerializer에서 처리
            "application": self.fields["application"].to_representation(
                instance.application_set.all()
            ),
        } | (json.loads(instance.info) if instance.info else {})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
