from django.test import TestCase
from cart.forms import CheckoutForm
# Create your tests here.

#This works
class TestForms(TestCase):

    def test_checkout_form_validate(self):
        form = CheckoutForm(data={
            'first_name': 'test',
            'last_name': 'rest',
            'email': 'a@gmail.com',
            'address': 'test for best',
            'phone': '6629986875',
            'zipcode': '62847',
            'place': 'apart',
            'stripe_token': 'token'
        }
        )

        self.assertTrue(form.is_valid())

    def test_checkout_form_no_data(self):
        form = CheckoutForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)

# Create your tests here.
