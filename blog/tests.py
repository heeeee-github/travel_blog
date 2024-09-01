from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category, Image

class BlogPostTest(TestCase):
    def setUp(self):
        # 테스트에 필요한 사용자와 카테고리 생성
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Travel')

    def test_create_blog_posts(self):
        # 여행 블로그 포스트 생성
        posts = [
            {
                'title': '아름다운 파리 여행기',
                'content': '에펠탑, 루브르 박물관 등 파리의 명소를 둘러보았습니다...',
            },
            {
                'title': '도쿄의 숨은 맛집 탐방',
                'content': '현지인들이 추천하는 라멘집, 스시집을 방문했습니다...',
            },
            {
                'title': '뉴욕 센트럴 파크에서의 하루',
                'content': '센트럴 파크의 아름다운 풍경과 다양한 활동을 즐겼습니다...',
            }
        ]

        for post_data in posts:
            post = Post.objects.create(
                title=post_data['title'],
                content=post_data['content'],
                category=self.category,
                author=self.user
            )
            # 각 포스트에 대한 이미지 추가 (실제 이미지 파일 대신 더미 데이터 사용)
            Image.objects.create(
                post=post,
                image='default_thumbnail.jpg'  # 실제 테스트에서는 적절한 이미지 파일을 사용해야 합니다
            )

        # 생성된 포스트 확인
        self.assertEqual(Post.objects.count(), 3)
        self.assertEqual(Image.objects.count(), 3)

        # 첫 번째 포스트의 내용 확인
        first_post = Post.objects.first()
        self.assertEqual(first_post.title, '아름다운 파리 여행기')
        self.assertTrue(first_post.content.startswith('에펠탑, 루브르 박물관'))
        self.assertEqual(first_post.category, self.category)
        self.assertEqual(first_post.author, self.user)

        # 이미지 연결 확인
        self.assertTrue(first_post.images.exists())

    def test_post_str_representation(self):
        post = Post.objects.create(
            title='테스트 포스트',
            content='테스트 내용',
            category=self.category,
            author=self.user
        )
        self.assertEqual(str(post), '테스트 포스트')