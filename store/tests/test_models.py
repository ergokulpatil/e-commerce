from django.test import TestCase
from store.models import Category,Product
from django.contrib.auth.models import User

class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.data1=Category.objects.create(name='django',slug='django')

    def test_category_model_entry(self):
        data=self.data1
        self.assertTrue(isinstance(data,Category))

    def test_category_model_entry(self):
        """
        Test Category default name
        """
        data=self.data1
        self.assertEqual(str(data),'django')

class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django',slug='django')
        User.objects.create(username='admin')
        self.data1=Product.objects.create(category_id=1,title='django beginner',created_by_id=1,
                                          slug='django',price=30,image='django beginner')
    def test_product_model_entry(self):
        """
        Test product data insertion
        """
        data=self.data1
        self.assertTrue(isinstance(data,Product))
        self.assertEqual(str(data),'django beginner')

