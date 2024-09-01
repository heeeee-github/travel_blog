# 01. 프로젝트 개요(Project Overview)

**(목표)** Django를 활용한 여행(Travel) 블로그 웹 페이지 제작

**(기간)** 2024.08.26.(월) ~ 2024.09.01.(일), 7일간

**(역할)** 기획/디자인/개발(1인 프로젝트)

# 02. 구현 기능(Implemented Features)
웹 페이지 제작에서 구현한 기능은 아래와 같습니다.

## 가. 기본 기능
### 01) 관리자 계정(Admin)
관리자 전용 페이지를 생성하여 사용자 관리 및 시스템 설정 기능을 구현합니다. 
### 02) 글 생성/읽기/수정/삭제(CRUD)
게시글의 생성, 조회, 수정, 삭제 기능을 구현합니다.
### 03) 사용자 인증(Auth)
사용자 로그인 및 회원가입 기능을 구현하고 데코레이터도 사용자별 권한을 지정합니다.


## 나. 추가 기능
### 01) 파일 업로드(Upload file)
사용자가 서버에 파일을 업로드하고 관리할 수 있도록 파일 처리 기능을 구현합니다.
### 02) 댓글(comment)
게시글에 댓글을 추가, 수정, 삭제할 수 있는 기능을 구현하여 사용자 간의 상호작용을 지원합니다.



# 03. WBS(Work Breakdown Structure)

```mermaid
gantt
    title Scuba Diving Blog Project Plan
    dateFormat  YYYY-MM-DD
    section 프로젝트 계획 수립
    프로젝트 목표 정의            :done, a1, 2024-08-26, 1d
    요구사항 수집 및 분석         :done, a2, 2024-08-26, 1d
    WBS 작성 및 일정 수립         :done, a3, 2024-08-26, 1d

    section 환경 설정
    개발 환경 구축                : done, b1, 2024-08-26, 1d
    Django 프로젝트 생성          : done, b2, 2024-08-26, 1d
    앱 생성                      : done, b3, 2024-08-26, 1d

    section Main-page
    url 설정                     : done, c1, 2024-08-26, 1d
    '입장하기' 생성               : done, c2, 2024-08-26, 1d
    
    section Admin
    계정 생성                     : done,  d1, 2024-08-26, 1d
    페이지 생성                   : done,  d2, 2024-08-26, 1d
    게시글 작성                   : done,  d3, 2024-08-27, 1d

    section Model
    ERD 작성                     : done, e1, 2024-08-26, 1d
    Model 생성                   : done, e2, 2024-08-27, 1d
    마이그레이션                  : done, e3, 2024-08-27, 1d
    
    section CRUD 기능
    View 작성                   : done, f1, 2024-08-27, 1d
    (C)글 작성                   : done, f2, 2024-08-27, 1d
    (R)글 읽기                   : done, f3, 2024-08-27, 1d
    (U)글 수정                   : done, f4, 2024-08-27, 1d
    (D)글 삭제                   : done, f5, 2024-08-27, 1d
    Form 작성                   : done, f6, 2024-08-27, 1d
    Url 패턴 설정                 : done,  f7, 2024-08-27, 1d
    Template 작성                   : done, f8, 2024-08-27, 1d
    Create-T                   : done, f9, 2024-08-27, 1d
    Read-T                     : done, f10, 2024-08-27, 1d
    Update-T                   : done, f11, 2024-08-27, 1d
    Delete-T                   : done, f12, 2024-08-27, 1d

    section 사용자 계정
    회원가입                   : done, g1, 2024-08-27, 1d
    로그인/아웃                 : done, g2, 2024-08-27, 1d
    글 작성(로그인)             : done, g3, 2024-08-27, 1d
    글 수정(작성자)             : done, g4, 2024-08-27, 1d
    글 삭제(작성자)             : done, g5, 2024-08-27, 1d

    section 파일 업로드
    영상                   : done, h1, 2024-08-28, 1d
    음악                   : done, h2, 2024-08-28, 1d
    이미지                   : done, h3, 2024-08-28, 1d

    section 추가 기능 개발
    글 상세보기                   : done, i1, 2024-08-27, 1d
    조회수                      : done, i2, 2024-08-28, 3d
    글 삭제 후 글 목록 화면      : done, i3, 2024-08-27, 1d
    삭제글 접근불가 + 404에러   : done, i4, 2024-08-27, 1d
    게시글 검색(주제, 카테고리)   : done, i5, 2024-08-27, 1d
    시간순에 따라 게시글 정렬   : done, i6, 2024-08-28, 1d
    컨텐츠 필터링               : done, i7, 2024-08-30, 1d

    마이페이지 기능                   : done, i8, 2024-08-29, 1d
    비밀번호 변경                    : i9, 2024-08-30, 1d
    프로필 수정                   : done,i10, 2024-08-29, 1d
    닉네임 추가                    : i11, 2024-08-30, 1d

    댓글 기능                    : done, i12, 2024-08-29, 1d
    댓글 추가                    : done, i13, 2024-08-29, 1d
    댓글 수정                    : done, i14, 2024-08-29, 1d
    댓글 삭제                    : done, i15, 2024-08-29, 1d
    답글                        : done, i16, 2024-08-29, 2d

    section 디자인 및 UI/UX 개발
    기본 템플릿 디자인                       : done, j1, 2024-08-28, 4d
    사용자 프로필 페이지 디자인                 : done, j2, 2024-08-30, 3d
    반응형 웹 디자인 적용                    : done, j3, 2024-08-30, 3d

    section 프로젝트 마무리
    프로젝트 문서화                : done, k1, 2024-08-26, 5d
    프로젝트 평가 및 회고         : active, k2, 2024-09-02, 1d
```

# 04. 구조도(Structure)

## 웹페이지 서비스 구조도
```mermaid
graph TD
    A[홈페이지 입장] --> B[메인 화면]
    B --> E[포스트 목록]
    B --> C[사용자 프로필]
```
## 기능 구조도
```mermaid
graph TD
    A[메인 기능] --> B[사용자 관리]
    A --> C[포스트 관리]
    A --> D[카테고리 관리]
    A --> E[미디어 관리]
    A --> F[댓글 관리]

    B --> B1[회원가입]
    B --> B2[로그인/로그아웃]
    B --> B3[프로필 관리]

    C --> C1[포스트 작성]
    C --> C2[포스트 수정]
    C --> C3[포스트 삭제]
    C --> C4[포스트 조회]

    D --> D1[카테고리 생성]
    D --> D2[카테고리 수정]
    D --> D3[카테고리 삭제]

    E --> E1[이미지 업로드]
    E --> E2[비디오 업로드]
    E --> E3[오디오 업로드]

    F --> F1[댓글 작성]
    F --> F2[댓글 수정]
    F --> F3[댓글 삭제]
    F --> F4[대댓글 작성]
```

# 05. ERD(Entity Relationship Diagram)
```mermaid
erDiagram

    Category ||--o| Post : has
    Post ||--o| Image : includes
    Post ||--o| Video : includes
    Post ||--o| Audio : includes
    Post ||--o| Comment : includes
    Comment ||--o| Comment : replies_to
    Post }|--|| Category : belongs_to
    Post }|--|| User : authored_by
    Comment }|--|| User : authored_by
    Profile }|--|| User : has

    Category {
        integer id PK
        string name
    }

    Post {
        integer id PK
        string title
        text content
        datetime created_at
        datetime updated_at
    }

    Image {
        integer id PK
        string image
    }

    Video {
        integer id PK
        file video
    }

    Audio {
        integer id PK
        file audio
    }

    Comment {
        integer id PK
        text content
        datetime created_at
    }

    Profile {
        integer id PK
        text bio
        string profile_picture
        string location
    }

    User {
        integer id PK
        string username
    }

```

# 06. 배포(Release)
- 미진행


# 07. 관련 화면(Demo Version)

| 카테고리      | 기능                   | 설명                  | 영상/이미지              |
|---------------|------------------------|-----------------------|-------------------|
| **메인화면**   | 입장                   | 앱의 시작 화면 |    |![입장](image.png)
|               | 메인페이지             | 블로그의 주요 페이지 |  ![메인](image-10.png)  |
| **사용자**     | 로그인                 | 사용자의 로그인 절차 | ![로그인](image-2.png)   |
|               | 회원가입               | 사용자의 회원가입 | ![회원가입](image-1.png) |
|               | 마이페이지               | 사용자의 마이페이지 | ![마이페이지](image-3.png) |
|               | 프로필 수정               | 사용자의 프로필 수정 | ![프로필수정](image-4.png) |
|               | 게시글 작성              | 블로그 게시글 관련 기능 | ![글 작성](image-5.png)  |
|               | 게시글 내용                | 작성한 게시글 확인 | ![글확인](image-7.png)   |
|               | 댓글              | 댓글을 작성/수정/삭제 | ![댓글](image-8.png)   |
| **관리자**     | 관리자페이지           | 관리자 페이지의 기능 | ![관리자페이지](image-9.png)   |



# 08. 기술 스택(Tech Stack)

| 카테고리          | 기술 스택                | 설명                                                |
|------------------|--------------------------|-----------------------------------------------------|
| **백엔드 (Backend)**   | Django (Python)       | ORM, 관리자 인터페이스, URL 라우팅, 템플릿 엔진 기능 개발 |
| **프론트엔드 (Frontend)** | HTML                 | 블로그 글의 내용과 레이아웃을 설계 |
|                  | CSS                      | 블로그 스타일과 글의 시각적 표현을 스타일링 |
| **데이터 (Database)**     | Lightsql3            | 블로그의 데이터(포스트, 댓글 등)를 저장하고 관리 |
| **문서 (Document)**      | GitHub                | 블로그 프로젝트의 소스 코드를 관리 |
|                  | Mermaid                 | 프로젝트 구조와 데이터 흐름을 문서화 |


# 10. 회고(Retrospect)

아직까지 필요한 개선점
* 검색 기능 구현
* 비밀번호 변경 기능 구현
* 썸네일 기능 구현
* 개발 완료 후 코드 가독성을 높이는 과정 진행
