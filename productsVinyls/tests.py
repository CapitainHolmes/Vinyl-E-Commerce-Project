from django.test import TestCase
from .models import Vinyl

# Create your tests here.
class ProductTests(TestCase):
    """
    A simple Test to run against the Vinyl Model.
    """

    def test_str(self):
        test_artist = Vinyl(artist='A Artist')
        self.assertEqual(str(test_artist), 'A Artist')