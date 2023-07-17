from django.test import TestCase

# Create your tests here.

class ApartementTest(TestCase):
    def test_add_apartment(self):
        # Test in TDD, we check there's no apartment created
        self.assertEqual(ApartementTest.objects.count(), 0)