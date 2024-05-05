from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

#unedited
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=90, inventory=10)
        
        
    def test_getall(self):
        new_data = Menu.objects.all()
        self.assertEqual(str(new_data[0]), "IceCream : 80.00")
        self.assertEqual(str(new_data[1]), "Pizza : 90.00")
