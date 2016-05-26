from django.test import TestCase
from django.core.urlresolvers import reverse


# Create your tests here.
class EmptyRealityNameTest(TestCase):
    def test_True(self):
        self.assertEqual(True, True)

    def test_view_index(self):
        response = self.client.get(reverse("reality:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Reality</title>")
