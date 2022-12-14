# wanted-pre-onboarding-backend

[원티드 프리 온보딩 백엔드 과정 과제](https://bow-hair-db3.notion.site/5-1850bca26fda4e0ca1410df270c03409)

# 요구사항 및 선택사항

다음을 만족하는 API를 작성하시오.

-   [x] 채용공고 등록
-   [x] 채용공고 수정
-   [x] 채용공고 삭제
-   [x] 채용공고 가져오기
    -   [x] 채용공고 읽기
    -   [ ] 채용공고 검색 (선택사항)
-   [x] 채용공고 상세 페이지 가져오기
    -   [x] 공고를 올린 회사의 다른 채용공고 가져오기
-   [x] 채용공고 지원 (선택사항)
-   [x] 필요한 모델
    -   [x] 회사
    -   [x] 사용자
    -   [x] 채용공고
    -   [x] 지원내역 (선택사항)
-   [x] 필수 기술요건
    -   [x] ORM
    -   [x] RDBMS
-   [ ] 가산점 요소
    -   [ ] 선택사항 요구사항 해결
        -   [ ] 채용공고 검색
        -   [x] 채용공고 지원
        -   [x] 지원내역 모델
    -   [x] Unit Test 구현
    -   [ ] README 요구사항 분석 및 구현과정 작성
    -   [x] Git commit 메세지
-   생략 및 임의 생성 가능
    -   필드 명
    -   회사 및 사용자 등록 절차
    -   로그인 등 사용자 인증절차
    -   Frontend 요소
    -   이외 명시되지 않은 조건

# DB 모델

-   COMPANY
    |attr|type|
    |---|---|
    |id|`int`, `primary`|
    |name|`string`|
    |signed|`date`|
    |info|`string`|
-   USER
    |attr|type|
    |---|---|
    |id|`int`, `primary`|
    |name|`string`|
    |signed|`date`|
    |info|`string`|
-   NOTICE
    |attr|type|
    |---|---|
    |id|`int`, `primary`|
    |name|`string`|
    |signed|`date`|
    |company|`int`|
    |info|`string`|
-   APPLICATION
    |attr|type|
    |---|---|
    |id|`int`, `primary`|
    |applied|`date`|
    |notice|`int`|
    |user|`int`|

```mermaid
erDiagram
    COMPANY {
        id int
        name string
        date date
        info string
    }
    USER {
        id int
        name string
        date date
        info string
    }
    NOTICE {
        id int
        name string
        date date
        company int
        info string
    }
    APPLICATION {
        id int
        applied date
        notice int
        user int
    }
    COMPANY ||--o{ NOTICE : post
    NOTICE ||--o{ APPLICATION : applied
    USER ||--o{ APPLICATION : apply
```
