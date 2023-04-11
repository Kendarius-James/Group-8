
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
            'phone': '6629986875',
            'address': 'test for best',
            'zipcode': '62847',
            'place': 'apart',
            #'stripe_token': 'token'
        }
        )
       # form = CheckoutForm(data = form)
        self.assertTrue(form.is_valid())
        #return form

    def test_checkout_form_validate_incorrect(self):
        form1 = CheckoutForm(data={ 
            'first_name': 'John',
            'last_name': 'Cena',
            'email': 'cena@gmail.com',
            'phone': 'what is a phone number',
            'address': 'West Newberry, Mass.',
            'zipcode': '39499',
            'place': 'Appartment 111',
            #'stripe_token': 'token'

        })
        self.assertTrue(form1.is_valid())


    def test_checkout_form_no_data(self):
        form3 = CheckoutForm(data={
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone': '',
            'address': '',
            'zipcode': '',
            'place': '',
            #'stripe_token': '',
        })
        self.assertFalse(form3.is_valid())

    def test_checkout_form_half_data(self):
        form4 = CheckoutForm(data={
            'first_name': 'Benjaman',
            'last_name': 'Frank',
            'email': 'benfrank@gmail.com',
            'phone': '9046529879',
            'address': '',
            'zipcode': '',
            'place': '',
            #'stripe_token': '',
        })
        self.assertFalse(form4.is_valid())

    def test_checkout_form_invalid_email_data(self):
        form4 = CheckoutForm(data={
            'first_name': 'Linda',
            'last_name': 'Johnson',
            'email': '123',
            'phone': '5223562541',
            'address': 'Trust street, Texas',
            'zipcode': '56689',
            'place': 'Appartment View',
            #'stripe_token': '',
        })
        self.assertFalse(form4.is_valid())

    '''
    def test_checkout_form_validate(self):
        form = CheckoutForm(data={})

        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_checkout_form_validate_incorrect(self):
        form1 = CheckoutForm(data={})

        self.assertFalse(form1.is_valid())
        self.assertEquals(len(form1.errors), 7)

    def test_checkout_form_no_data(self):
        form2 = CheckoutForm(data={})

        self.assertFalse(form2.is_valid())
        self.assertEquals(len(form2.errors), 7)'''

# Create your tests here.
