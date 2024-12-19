from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ['name', 'short_description', 'description', 'price', 'stock', 'image_url']