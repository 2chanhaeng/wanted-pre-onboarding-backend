from django.test import TestCase
from .models import Company, User, Notice, Application

test_len = 3


class CreateTestClass(TestCase):
    # 모델 별 생성 테스트
    def tearDown(self) -> None:
        # 지원내역, 채용공고, 유저, 회사 순으로 삭제
        Application.objects.all().delete()
        Notice.objects.all().delete()
        User.objects.all().delete()
        Company.objects.all().delete()

    def test_create_companies(self) -> None:
        # 회사 생성
        self.companies = [
            Company.objects.create(name=f'test_company_{i}')
            for i in range(1, 1 + test_len)
        ]
    
    def test_create_users(self) -> None:
        # 유저 생성
        self.users = [
            User.objects.create(name=f'test_user_{i}')
            for i in range(1, 1 + test_len)
        ]

    def test_create_notices(self) -> None:
        # 채용공고 생성
        self.test_create_companies()
        self.notices = [
            Notice.objects.create(
                name=f'test_notice_{i}', 
                company=company
            )
            for i in range(1, 1 + test_len)
            for company in self.companies
        ]
    
    def test_create_applications(self) -> None:
        # 지원내역 생성
        self.test_create_users()
        self.test_create_notices()
        self.applications = [
            Application.objects.create(notice=notice,user=user)
            for notice in self.notices for user in self.users
        ]


class ReadTestCase(TestCase):
    # 모델 별 조회 테스트
    def setUp(self) -> None:
        # 회사, 유저, 채용공고, 지원내역 순으로 생성
        self.companies = [
            Company.objects.create(name=f'test_company_{i}')
            for i in range(1, 1 + test_len)
        ]
        self.users = [
            User.objects.create(name=f'test_user_{i}')
            for i in range(1, 1 + test_len)
        ]
        self.notices = [
            Notice.objects.create(
                name=f'test_notice_{(company.id - 1) * test_len + i}',
                company=company
            )
            for company in self.companies
            for i in range(1, 1 + test_len)
        ]
        self.applications = [
            Application.objects.create(notice=notice, user=user)
            for notice in self.notices for user in self.users
        ]

    def tearDown(self) -> None:
        # 지원내역, 채용공고, 유저, 회사 순으로 삭제
        Application.objects.all().delete()
        Notice.objects.all().delete()
        User.objects.all().delete()
        Company.objects.all().delete()

    def test_read_companies(self) -> None:
        # 회사 조회
        self.assertEqual(len(self.companies), test_len)
    
    def test_read_users(self) -> None:
        # 유저 조회
        self.assertEqual(len(self.users), test_len)
    
    def test_read_notices(self) -> None:
        # 채용공고 조회
        self.assertEqual(len(self.notices), test_len ** 2)
    
    def test_read_applications(self) -> None:
        # 지원내역 조회
        self.assertEqual(len(self.applications), test_len ** 3)
    
    def test_read_user_applications(self) -> None:
        # 유저의 지원내역 조회
        for user in self.users:
            self.assertEqual(user.name, f'test_user_{user.id}')
            for application in user.application_set.all():
                self.assertEqual(application.notice.name, f'test_notice_{application.notice.id}')
    
    def test_read_company_notices_applications(self) -> None:
        # 회사의 채용공고와 채용공고의 지원내역 조회
        for company in self.companies:
            self.assertEqual(company.name, f'test_company_{company.id}')
            for notice in company.notice_set.all():
                self.assertEqual(notice.name, f'test_notice_{notice.id}')
                for application in notice.application_set.all():
                    self.assertEqual(application.user.name, f'test_user_{application.user.id}')

class UpdateTestCase(TestCase):
    # 모델 별 수정 테스트
    def setUp(self) -> None:
        # 회사, 유저, 채용공고, 지원내역 순으로 생성
        self.companies = [
            Company.objects.create(name=f'test_company_{i}')
            for i in range(1, 1 + test_len)
        ]
        self.users = [
            User.objects.create(name=f'test_user_{i}')
            for i in range(1, 1 + test_len)
        ]
        self.notices = [
            Notice.objects.create(
                name=f'test_notice_{i}',
                company=company
            )
            for company in self.companies
            for i in range(1, 1 + test_len)
        ]
        self.applications = [
            Application.objects.create(notice=notice, user=user)
            for notice in self.notices for user in self.users
        ]

    def tearDown(self) -> None:
        # 지원내역, 채용공고, 유저, 회사 순으로 삭제
        Application.objects.all().delete()
        Notice.objects.all().delete()
        User.objects.all().delete()
        Company.objects.all().delete()

    def test_update_user(self) -> None:
        # 유저 수정
        for i, user in enumerate(self.users):
            user.name = f'updated_user_{i}'
            user.save()
        for i, user in enumerate(self.users):
            self.assertEqual(user.name, f'updated_user_{i}')

    def test_update_company(self) -> None:
        # 회사 수정
        for i, company in enumerate(self.companies):
            company.name = f'updated_company_{i}'
            company.save()
        for i, company in enumerate(self.companies):
            self.assertEqual(company.name, f'updated_company_{i}')
    
    def test_update_notice(self) -> None:
        # 채용공고 수정
        for i, notice in enumerate(self.notices):
            notice.name = f'updated_notice_{i}'
            notice.save()
        for i, notice in enumerate(self.notices):
            self.assertEqual(notice.name, f'updated_notice_{i}')
    
    def test_update_application(self) -> None:
        for i, application in enumerate(self.applications):
            application.name = f'updated_application_{i}'
            application.save()
        for i, application in enumerate(self.applications):
            self.assertEqual(application.name, f'updated_application_{i}')


class DeleteTestCase(TestCase):
    # 모델 별 삭제 테스트
    def setUp(self) -> None:
        # 회사, 유저, 채용공고, 지원내역 순으로 생성
        self.companies = [
            Company.objects.create(name=f'test_company_{i}')
            for i in range(1, 1 + test_len)
        ]
        self.users = [
            User.objects.create(name=f'test_user_{i}')
            for i in range(1, 1 + test_len)
        ]
        self.notices = [
            Notice.objects.create(
                name=f'test_notice_{i}',
                company=company
            )
            for company in self.companies
            for i in range(1, 1 + test_len)
        ]
        self.applications = [
            Application.objects.create(notice=notice, user=user)
            for notice in self.notices for user in self.users
        ]

    def test_delete_user(self) -> None:
        # 유저 삭제
        for user in self.users:
            user.delete()
        self.assertEqual(len(User.objects.all()), 0)
    
    def test_delete_company(self) -> None:
        # 회사 삭제
        for company in self.companies:
            company.delete()
        self.assertEqual(len(Company.objects.all()), 0)
    
    def test_delete_notice(self) -> None:
        # 채용공고 삭제
        for notice in self.notices:
            notice.delete()
        self.assertEqual(len(Notice.objects.all()), 0)
    
    def test_delete_application(self) -> None:
        # 지원내역 삭제
        for application in self.applications:
            application.delete()
        self.assertEqual(len(Application.objects.all()), 0)
