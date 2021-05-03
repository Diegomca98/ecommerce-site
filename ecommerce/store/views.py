from django.shortcuts import render
from .models import ProductModel, OrderModel
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

def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items', '')
        total = request.POST.get('total', '')
        name = request.POST.get('firstName', '')
        last_name = request.POST.get('lastName', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        address2 = request.POST.get('address2', '')
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        same_address = request.POST.get('same-address', '')
        save_info = request.POST.get('save-info', '')
        """payment_method = request.POST.get('paymentMethod', '')
        cc_name = request.POST.get('cc-name', '')
        cc_number = request.POST.get('cc-number', '')
        cc_expiration = request.POST.get('cc-expiration', '')
        cc_cvv = request.POST.get('cc-cvv', '')"""

        order = OrderModel(
            items=items,
            name=name, 
            last_name=last_name, 
            email=email, 
            address=address, 
            address2=address2,
            country=country,
            state=state,
            zip_code=zip_code,
            total=total
        )
        order.save()
    return render(request, "checkout.html")