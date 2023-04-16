from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO
from accounts.models import SellerProfile
from product.models import Category
from product.models import Product
from django.test import override_settings
from tempfile import TemporaryDirectory
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from seller.decorators import is_seller_approved

class TestAddProductView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.tmp_media = TemporaryDirectory()
        cls.media_root_override = override_settings(MEDIA_ROOT=cls.tmp_media.name)
        cls.media_root_override.enable()

    @classmethod
    def tearDownClass(cls):
        cls.media_root_override.disable()
        cls.tmp_media.cleanup()
        super().tearDownClass()

    def setUp(self):
        self.client = Client()
        self.add_product_url = reverse('seller:add-product')

        # Create test user and seller profile
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword',
            role='seller'
        )
        self.seller_profile = SellerProfile.objects.create(
            user=self.user,
            company_name='Test Company',
            is_approved=True
        )

        # Create test category
        self.category = Category.objects.create(title='Test Category', slug='test-category')
        def test_get_absolute_url():
            return f'/product/test-category/'
        self.category.get_absolute_url = test_get_absolute_url

        # Create test image
        self.image = self._create_test_image()

    def test_add_product_view_uses_correct_template(self):
        self.client.login(email='test@example.com', password='testpassword')
        response = self.client.get(self.add_product_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'seller/add_product.html')

    def test_add_product_view_creates_product(self):
        self.client.login(email='test@example.com', password='testpassword')
        response = self.client.post(self.add_product_url, {
            'category': self.category.pk,
            'title': 'Test Product',
            'description': 'Test description',
            'price': 100,
            'quantity': 10,
            'image': self.image
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Product.objects.filter(title='Test Product').exists())

    def _create_test_image(self):
        img = Image.new('RGB', (100, 100), color=(73, 109, 137))
        buf = BytesIO()
        img.save(buf, 'jpeg')
        buf.seek(0)
        return SimpleUploadedFile('test_image.jpg', buf.getvalue(), content_type='image/jpeg')