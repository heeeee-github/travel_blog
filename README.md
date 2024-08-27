# 01. 프로젝트 개요(Project Overview)

**(목표)** Django를 활용한 여행(Travel) 블로그 웹 페이지 제작

**(기간)** 2024.08.26.(월) ~ 2024.08.30.(금), 5일간

**(역할)** 기획/디자인/개발/배포(1인 프로젝트)

# 02. 구현 기능(Implemented Features)
웹 페이지 제작에서 구현한 기능은 아래와 같습니다.

## 가. 기본 기능
### 01) 관리자 계정(Admin)
### 02) 글 생성/읽기/수정/삭제(CRUD)
### 03) 사용자 인증(Auth)


## 나. 추가 기능
### 01) 파일 업로드(Upload file)
### 02) 댓글(comment)
### 03) 생성형 AI 사용(Using Generative AI)



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
    Medel 생성                   : done, e2, 2024-08-27, 1d
    마이그레이션                  : done, e2-1, 2024-08-27, 1d
    
    section CRUD 기능
    View 작성                   : done, e1, 2024-08-27, 1d
    (C)글 작성                   : done, e1-1, 2024-08-27, 1d
    (R)글 읽기                   : done, e1-2, 2024-08-27, 1d
    (U)글 수정                   : done, e1-3, 2024-08-27, 1d
    (D)글 삭제                   : done, e1-4, 2024-08-27, 1d
    Form 작성                   : done, e2, 2024-08-27, 1d
    Url 패턴 설정                 : done,  e3, 2024-08-27, 1d
    Template작성                   : done, e4, 2024-08-27, 1d
    Create-T                   : done, e4-1, 2024-08-27, 1d
    Read-T                   : done, e4-1, 2024-08-27, 1d
    Update-T                   : done, e4-1, 2024-08-27, 1d
    Delete-T                   : done, e4-1, 2024-08-27, 1d

    section 사용자 계정
    회원가입                   : done, f1, 2024-08-27, 1d
    로그인/아웃                   : done, f2, 2024-08-27, 1d
    회원 인증                   : active, f3, 2024-08-27, 1d
    글 작성                   : active, f3-1, 2024-08-27, 1d
    글 수정                   : active, f3-2, 2024-08-27, 1d
    글 삭제                   : active, f3-3, 2024-08-27, 1d


    section 추가 기능 개발
    글 상세보기                   : done, g1, 2024-08-27, 1d
    파일 업로드                   : g2, 2024-08-28, 1d
    조회수                      : g3, 2024-08-28, 1d
    글 삭제 후 글 목록 화면      : done, g4, 2024-08-27, 1d
    삭제글 접근불가 + 404에러   : done, g5, 2024-08-27, 1d
    게시글 검색(주제, 카테고리)   : done, g6, 2024-08-27, 1d
    시간순에 따라 게시글 정렬   : g7, 2024-08-28, 1d
    마이페이지 기능                   : g8, 2024-08-28, 2d
    비밀번호 변경                    : g8-1, 2024-08-28, 2d
    프로필 수정                   : g8-1, 2024-08-28, 2d
    닉네임 추가                    : g8-1, 2024-08-28, 2d
    댓글 기능                    : g9, 2024-08-28, 2d
    댓글 추가                    : g9-1, 2024-08-28, 2d
    댓글 삭제                    : g9-2, 2024-08-28, 2d
    대댓글                    : g9-3, 2024-08-28, 2d
    댓글 수정                    : g9-4, 2024-08-28, 2d
    소셜 미디어 연동               : g10, 2024-08-29, 2d
    좋아요 기능                    : g11, 2024-08-29, 2d
    북마크 기능                    : g12, 2024-08-29, 2d
    AI 연동                       : g13, 2024-08-29, 2d

    section 디자인 및 UI/UX 개발
    기본 템플릿 디자인                       : h1, 2024-08-28, 2d
    사용자 프로필 페이지 디자인                 : h2, 2024-08-28, 2d
    반응형 웹 디자인 적용                    : h3, 2024-08-28, 2d

    section 테스트 및 배포
    유닛 테스트 작성 및 실행                  : i1, 2024-08-27, 4d
    통합 테스트 실행                         : i2, 2024-08-29, 2d
    디버깅 및 최종 수정                      : i3, 2024-08-29, 2d
    환경 설정                           : i4, 2024-08-29, 1d
    도메인 설정                      : i5, 2024-08-29, 1d
    최종 점검 및 사용자 피드백 수집     : i6, 2024-08-29, 5d

    section 프로젝트 마무리
    프로젝트 문서화                : active, j1, 2024-08-26, 5d
    유지보수 계획 수립             : j2, 2024-08-30, 2d
    프로젝트 평가 및 회고         : j3, 2024-09-02, 1d
```

# 04. 웹페이지 구조(Website Structure)
```mermaid
graph TD
    A[메인 페이지 home] --> B[블로그 입장 페이지 enter_blog]
    B --> C[블로그 게시글 목록 post_list]
    C --> D[게시글 상세 post_detail]
    C --> |로그인 사용자|E[게시글 작성 post_create]
    D --> |작성자|F[게시글 수정 post_update]
    D --> |작성자|G[게시글 삭제 post_delete]
    A --> |관리자|H[관리자 페이지 admin]
    H --> I[카테고리 관리 blog_category]
    H --> J[게시글 관리 blog_post]

    subgraph 로그인 사용자 영역
        E
    end

    subgraph 작성자 영역
        F
        G
    end

    subgraph 관리자 영역
        H
        I
        J
    end

    classDef default fill:#001d35,stroke:#333,stroke-width:2px;
    classDef loggedIn fill:#522064,stroke:#333,stroke-width:2px;
    classDef admin fill:#20645f,stroke:#333,stroke-width:2px;
    class E,F,G loggedIn;
    class H,I,J admin;
```

# 05. Wire Frame (with Figma)
- (작성 예정)


# 06. ERD(Entity Relationship Diagram)
```mermaid
erDiagram
    User ||--o{ Post : writes
    User ||--o{ Comment : writes
    Post ||--o{ Comment : has

    User {
        int id PK
        string username
        string email
        string password
        datetime created_at
        datetime updated_at
    }

    Post {
        int id PK "Comment"
        int user_id FK
        string title
        text content
        string main_file_name
        string main_file_path
        string main_file_type
        int main_file_size
        json additional_files "Save in json format "
        datetime created_at
        datetime updated_at
    }

    Comment {
        int id PK
        int user_id FK
        int post_id FK
        text content
        datetime created_at
        datetime updated_at
    }

```

# 07. 배포(Release)
- (작성 예정)


# 08. 시연 영상(Demo Version)

| 카테고리      | 기능                   | 설명                  | 영상              |
|---------------|------------------------|-----------------------|-------------------|
| **메인화면**   | 입장                   | 앱의 시작 화면 | (영상 삽입 예정)   |
|               | 메인페이지             | 블로그의 주요 페이지 | (영상 삽입 예정)   |
| **사용자**     | 로그인                 | 사용자의 로그인 절차 | (영상 삽입 예정)   |
|               | 로그아웃               | 사용자의 로그아웃 절차 | (영상 삽입 예정)   |
|               | 게시글                 | 블로그 게시글 관련 기능 |                   |
|               | 글 생성                | 새 게시글을 작성하는 방법 | (영상 삽입 예정)   |
|               | 파일 첨부              | 게시글에 파일을 첨부하는 방법 | (영상 삽입 예정)   |
|               | 글 읽기 (조회 수)       | 게시글을 읽고 조회 수를 확인하는 방법 | (영상 삽입 예정)   |
|               | 글 수정                | 기존 게시글을 수정하는 방법 | (영상 삽입 예정)   |
|               | 글 삭제                | 게시글을 삭제하는 방법 | (영상 삽입 예정)   |
|               | 댓글                   | 댓글 관련 기능 |                   |
|               | 댓글 작성              | 새 댓글을 작성하는 방법 | (영상 삽입 예정)   |
|               | 댓글 수정              | 기존 댓글을 수정하는 방법 | (영상 삽입 예정)   |
|               | 댓글 삭제              | 댓글을 삭제하는 방법 | (영상 삽입 예정)   |
| **관리자**     | 로그인                 | 관리자의 로그인 절차 | (영상 삽입 예정)   |
|               | 로그아웃               | 관리자의 로그아웃 절차 | (영상 삽입 예정)   |
|               | 관리자페이지           | 관리자 페이지의 기능 | (영상 삽입 예정)   |



# 09. 기술 스택(Tech Stack)

| 카테고리          | 기술 스택                | 설명                                                |
|------------------|--------------------------|-----------------------------------------------------|
| **백엔드 (Backend)**   | Django (Python)       | ORM, 관리자 인터페이스, URL 라우팅, 템플릿 엔진 기능 개발 |
| **프론트엔드 (Frontend)** | HTML                 | 블로그 글의 내용과 레이아웃을 설계 |
|                  | CSS                      | 블로그 스타일과 글의 시각적 표현을 스타일링 |
|                  | JavaScript               |  |
| **생성 AI (Generative AI)** | Chat GPT            | 블로그 포스트의 콘텐츠를 생성하거나 작성 |
|                  | Midjourney               | 블로그 포스트에 사용할 이미지를 생성 |
| **데이터 (Database)**     | Lightsql3            | 블로그의 데이터(포스트, 댓글 등)를 저장하고 관리 |
| **배포 (Release)**       | AWS Lightsail        | AWS의 VPS 서비스로, 블로그 애플리케이션을 배포하고 호스팅 |
| **문서 (Document)**      | GitHub                | 블로그 프로젝트의 소스 코드를 관리 |
|                  | Mermaid                 | 프로젝트 구조와 데이터 흐름을 문서화 |
|                  | Figma                   | 블로그의 디자인 프로토타입을 작성하고 사용자 경험을 설계 |

# 10. 회고(Retrospect)


