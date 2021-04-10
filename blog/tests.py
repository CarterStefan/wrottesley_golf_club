from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Blog

# Create your tests here.


class BlogModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='password',
            is_superuser=True,
        )

    def test_blog_post_fields(self):
        blog = Blog.objects.create(
            author=self.user,
            slug='test-title',
            main_image='image.jpg',
            title='test title',
            sub_title_one='sub title one',
            blog_content_one='content one',
            sub_title_two='sub title two',
            blog_content_two='content two',
            )

        expected_author = f'{blog.author}'
        expected_slug = f'{blog.slug}'
        expected_main_image = f'{blog.main_image}'
        expected_title = f'{blog.title}'
        expected_sub_title_one = f'{blog.sub_title_one}'
        expected_blog_content_one = f'{blog.blog_content_one}'
        expected_sub_title_two = f'{blog.sub_title_two}'
        expected_blog_content_two = f'{blog.blog_content_two}'

        self.assertEqual(expected_author, 'testuser')
        self.assertEqual(expected_slug, 'test-title')
        self.assertEqual(expected_main_image, 'image.jpg')
        self.assertEqual(expected_title, 'test title')
        self.assertEqual(expected_sub_title_one, 'sub title one')
        self.assertEqual(expected_blog_content_one, 'content one')
        self.assertEqual(expected_sub_title_two, 'sub title two')
        self.assertEqual(expected_blog_content_two, 'content two')


class BlogViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@test.com',
            password='password',
            is_superuser=True,
        )

    def test_blog_view_exists_at_location(self):
        self.client.force_login(self.user)
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/blog.html')

    def test_blog_view_url_name(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('blog_list'))
        self.assertEqual(resp.status_code, 200)

    def test_individual_blog_post_view(self):
        blog = Blog.objects.create(
            author=self.user,
            slug='test-title',
            main_image='image.jpg',
            title='test title',
            sub_title_one='sub title one',
            blog_content_one='content one',
            sub_title_two='sub title two',
            blog_content_two='content two',
            )
        self.client.force_login(self.user)
        resp = self.client.get(f'/blog/{blog.slug}/')
        no_resp = self.client.get('/blog/grjnfdlkmkrfd/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp, 'test title')
        self.assertTemplateUsed(resp, 'blog/blog_detail.html')

    def test_add_blog_post_view_exists_at_location(self):
        self.client.force_login(self.user)
        resp = self.client.get('/blog/add_blog/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/add_new_blog.html')

    def test_edit_blog_post_view(self):
        blog = Blog.objects.create(
            author=self.user,
            slug='test-title',
            main_image='image.jpg',
            title='test title',
            sub_title_one='sub title one',
            blog_content_one='content one',
            sub_title_two='sub title two',
            blog_content_two='content two',
            )
        self.client.force_login(self.user)
        resp = self.client.get(f'/blog/edit_blog/{blog.slug}/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/edit_blog.html')

    def test_add_blog_post(self):
        self.client.force_login(self.user)
        resp = self.client.post('/blog/add_blog/', {
            'slug': 'new-test-title',
            'main_image': 'new-image.jpg',
            'title': 'new test title',
            'sub_title_one': 'new sub title one',
            'blog_content_one': 'new content one',
            'sub_title_two': 'new sub title two',
            'blog_content_two': 'new content two',
        })
        self.assertRedirects(resp, '/blog/new-test-title/')
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.title, 'new test title')

    def test_delete_blog_item(self):
        blog = Blog.objects.create(
            author=self.user,
            slug='test-title',
            main_image='image.jpg',
            title='test title',
            sub_title_one='sub title one',
            blog_content_one='content one',
            sub_title_two='sub title two',
            blog_content_two='content two',
            )
        self.client.force_login(self.user)
        resp = self.client.get(f'/blog/delete_blog/{blog.slug}/')
        self.assertRedirects(resp, '/blog/')
        existing_blogs = Blog.objects.filter(id=blog.id)
        self.assertEqual(len(existing_blogs), 0)

    def test_edit_blog_item(self):
        blog = Blog.objects.create(
            author=self.user,
            slug='test-title',
            main_image='image.jpg',
            title='test title',
            sub_title_one='sub title one',
            blog_content_one='content one',
            sub_title_two='sub title two',
            blog_content_two='content two',
            )
        self.client.force_login(self.user)
        resp = self.client.post(f'/blog/edit_blog/{blog.slug}/', {
            'slug': 'updated-test-title',
            'main_image': 'updated-image.jpg',
            'title': 'updated test title',
            'sub_title_one': 'updated sub title one',
            'blog_content_one': 'updated content one',
            'sub_title_two': 'updated sub title two',
            'blog_content_two': 'updated content two',
        })
        self.assertRedirects(resp, '/blog/updated-test-title/')
