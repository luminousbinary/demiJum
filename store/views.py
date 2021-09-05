from django.shortcuts import render
from .models import Order, Product 
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    product_objects = Product.objects.all()

    # serch 
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains = item_name)

    #paginator
    paginator = Paginator(product_objects,14)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'store/home.html', {'product_objects':product_objects})

def item(request, id):
    product_object = Product.objects.get(id=id)
    return render(request, 'store/item.html', {'product_object': product_object} )

def checkout(request):

    if request.method == "POST":
        name = request.POST.get('name'),
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        items = request.POST.get('items')
        totalPrice = request.POST.get('totalPrice')
        order = Order(name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, items=items , totalPrice=totalPrice )
        order.save()

    return render(request,'store/checkout.html')


## just incase ineed to do it manually
# from djangoflutterwave.models import FlwPlanModel


# class SignUpView(TemplateView):
#     """Sign Up view"""

#     template_name = "my_payment_template.html"

#     def get_context_data(self, **kwargs):
#         """Add payment type to context data"""
#         kwargs = super().get_context_data(**kwargs)
#         kwargs["pro_plan"] = FlwPlanModel.objects.filter(
#             name="Pro Plan"
#         ).first()
#         return kwargs