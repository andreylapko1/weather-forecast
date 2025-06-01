from django.test import TestCase


class HomeViewTest(TestCase):
    def test_final_destination(self):
        response = self.client.get('/', follow=True)  # follow=True следует за редиректом
        self.assertEqual(response.status_code, 200)  # Проверяем конечную страницу
        self.assertContains(response, "Expected content")

# Create your tests here.
