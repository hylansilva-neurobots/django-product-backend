from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Product
# Create your views here.

def product_view(request):
    products = Product.objects.all()
    return render(
        request, 'product.html', {'products':products}
    )
    
def buy_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        
        product = get_object_or_404(Product, id=product_id)
        
        if product.quantity >= quantity:
            product.quantity -= quantity
            product.save()
            return JsonResponse({'success': True, 'message': 'Compra realizada com sucesso!', 'remaining_quantity': product.quantity})
        else:
            return JsonResponse({'success': False, 'message': 'Quantidade insuficiente em estoque.'})
    return JsonResponse({'success': False, 'message': 'Método inválido.'})