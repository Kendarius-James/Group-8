from django.test import TestCase, Client

# Create your tests here.
from django.contrib.auth.models import User
from accounts.models import BuyerProfile

class BuyerProfileAdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test@example.com', password='password')
        self.buyer_profile = BuyerProfile.objects.create(user=self.user)

    def test_buyer_profile_list_display(self):
        self.client.login(email='test@gmail.com', password='password')
        response = self.client.get('/admin/buyerprofile/')
        self.assertContains(response, self.user.email)
        self.assertContains(response, self.user.password)