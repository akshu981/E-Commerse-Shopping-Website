from django.shortcuts import render
from django.views import View

from .models import Product


# Create your views here.

def index(request):
    return render(request, 'app/index.html')

class ProductView(View):
    def get(self, request):
        laptops=Product.objects.filter(category='L')
        television = Product.objects.filter(category='TV')
        mobiles = Product.objects.filter(category='M')
        washing_machine = Product.objects.filter(category='WM')
        return render(request,'app/home.html',{'laptops':laptops,
                                               'television': television,
                                               'mobiles': mobiles,
                                               'washing_machine': washing_machine})



