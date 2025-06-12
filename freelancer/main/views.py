from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from .forms import OrderForm  # не забудь імпорт форми

def index(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id and category_id.isdigit():
        products = Product.objects.filter(category_id=category_id)
        selected_category = int(category_id)
    else:
        products = Product.objects.all()
        selected_category = None

    return render(request, 'index.html', {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {
        'category': category,
        'products': products
    })

def place_order(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return render(request, 'order_success.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'place_order.html', {'form': form, 'product': product})
