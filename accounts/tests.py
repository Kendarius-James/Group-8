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

