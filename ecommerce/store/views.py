from django.shortcuts import render
from .models import ProductModel
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

# Create your views here.
def index(request):
    product_list = ProductModel.objects.all()

    guitar_brand = request.GET.get('guitar_brand')
    if guitar_brand != '' and guitar_brand is not None:
        product_list = product_list.filter(category__icontains=guitar_brand)

    paginator = Paginator(product_list, 4)
    page = request.GET.get('page')
    product_list = paginator.get_page(page)

    return render(request, 'index.html', {
        'product_list': product_list,
    })

class Details(DetailView):
    model = ProductModel
    template_name = "details.html"