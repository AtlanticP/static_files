from django.test import TestCase

class MyTest(TestCase):

  def test_template_used(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'home.html')
