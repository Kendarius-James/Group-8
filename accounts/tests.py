from django.test import TestCase
from accounts.forms import BuyerUserCreationForm, SellerUserCreationForm, CustomUserCreationForm, UserCreationForm
from django.test import TestCase, Client
from accounts.models import SellerProfile, BuyerProfile, CustomUser
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.sites import AdminSite
from seller.admin import SellerProfileAdmin

class AdminTestForm(TestCase):
    # test to create a superuser
    def test_create_superuser(self):
        User = get_user_model()
        email = 'admin@example.com'
        password = 'password123'
        superuser = User.objects.create_superuser(email, password)
        self.assertEqual(superuser.email, email)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    # test for admin to create a user
    def test_create_user(self):
        User = get_user_model()
        email = 'lauren@example.com'
        password = 'password123'
        user = User.objects.create_user(email, password)
        self.assertEqual(user.email, email)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


# tests for admin functionalities on seller profile
class SellerProfileAdminTestCase(TestCase):
    def setUp(self):
        # Create a user with superuser permissions
        content_type = ContentType.objects.get_for_model(SellerProfile)
        permission = Permission.objects.get(
            codename='change_sellerprofile',
            content_type=content_type,
        )
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='password',
            is_staff=True,
            is_superuser=True,
        )
        self.user.user_permissions.add(permission)
        self.client.force_login(self.user)

    # test for admin functionalities on seller profile
    def test_seller_profile_admin(self):
        # Create a seller profile
        seller = SellerProfile.objects.create(
            user=CustomUser.objects.create_user(
                email='seller@example.com',
                password='password',
                role='seller',
            ),
            company_name='Test Company',
            company_description='Test description',
        )

        # Verify that the seller profile is displayed in the changelist
        site = AdminSite()
        seller_admin = SellerProfileAdmin(SellerProfile, site)
        changelist_url = reverse('admin:accounts_sellerprofile_changelist')
        response = self.client.get(changelist_url)

        # Verify that the seller profile can be edited
        edit_url = reverse('admin:accounts_sellerprofile_change', args=[seller.id])
        response = self.client.get(edit_url)
        self.assertContains(response, seller.company_name)

        # Verify that the seller profile can be deleted
        delete_url = reverse('admin:accounts_sellerprofile_delete', args=[seller.id])
        response = self.client.post(delete_url, {'post': 'yes'})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(SellerProfile.objects.filter(id=seller.id).exists())



# test for admin functionalities for buyer
User = get_user_model()
class TestBuyerAdmin(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            email='admin@test.com', password='testpass'
        )
        self.buyer = User.objects.create_user(
            email='buyer@test.com', password='testpass', role='buyer'
        )
        self.buyer_profile = BuyerProfile.objects.create(
            phone_number='1234567890',
            address='Test Address',
            user=self.buyer,
            first_name='John',
            last_name='Doe',
        )

    def test_buyer_profile_is_displayed_in_admin(self):
        # tests if buyer profile is on admin page
        self.client.force_login(self.admin_user)
        url = reverse('admin:accounts_buyerprofile_change', args=(self.buyer_profile.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.buyer_profile.first_name)
        self.assertContains(response, self.buyer_profile.last_name)
        self.assertContains(response, self.buyer_profile.phone_number)
        self.assertContains(response, self.buyer_profile.address)

    def test_cannot_access_buyer_profile_page_as_non_admin(self):
        # test to make sure only admin can view all buyer profiles
        self.client.force_login(self.buyer)
        url = reverse('admin:accounts_buyerprofile_change', args=(self.buyer_profile.id,))
        response = self.client.get(url)
        self.assertRedirects(response, '/admin/login/?next=' + url)
class TestForms(TestCase):
    
    def test_Seller_creation_form_fail_number(self):
        form = SellerUserCreationForm(data={
           'company_name': 'Walmart',
            'company_description': 'Low prices everyday',
            'phone_number': '6625981845184545145234', 
            'address': 'Starkvile, MS',
        }
        )
        #Seller Creation form have fixed length buy buyer do not
        self.assertFalse(form.is_valid())

    def test_buyer_creation_form_validate(self):
        form = BuyerUserCreationForm(data={
            'first_name': 'test',
            'last_name': 'rest',
            'phone': '6629986875',
            'address': 'test for best avenue',
        }
        )
        self.assertFalse(form.is_valid())
    def test_buyer_creation_invalid_form(self):
        form = BuyerUserCreationForm(data={
            'first_name': '',
            'last_name': '',
            'phone_number': '123456',
            'address': '',
        }
        )
        self.assertFalse(form.is_valid())

    def test_seller_creation_form_validate(self):
        form = SellerUserCreationForm(data={
            'company_name': 'Walmart',
            'company_description': 'Low prices everyday',
            'phone_number': '6625981234', 
            'address': 'Starkvile, MS',
        }
        )
       # form = CheckoutForm(data = form)
        self.assertTrue(form.is_valid())
    def test_invalid_phone_number(self):
        form = SellerUserCreationForm(data ={
            'company_name': 'Test Company',
            'company_description': 'Test Company Description',
            'phone_number': '123-456',
            'address': 'Test Address'
        })
        #form = SellerUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


# Create your tests here.

