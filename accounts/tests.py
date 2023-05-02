from django.test import TestCase
from accounts.forms import BuyerUserCreationForm, SellerUserCreationForm, CustomUserCreationForm, UserCreationForm

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
        self.assertTrue(form.is_valid())
    def test_buyer_creation_form_empty(self):
        form = BuyerUserCreationForm(data={
            'first_name': '',
            'last_name': '',
            'phone': '',
            'address': '',
        }
        )
        #Fields are not required
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
    def test_seller_creation_form_empty(self):
        form = SellerUserCreationForm(data={
            'company_name': '',
            'company_description': '',
            'phone_number': '', 
            'address': '',
        }
        )
       # form = CheckoutForm(data = form)
        self.assertTrue(form.is_valid())


# Create your tests here.

