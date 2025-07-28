from django.shortcuts import render
import requests
from colchoes.models import Product

def home_page(request):
    featured_products = Product.objects.filter(is_active=True).order_by('-user_rating_score')[:3]
    context = {
        'featured_products': featured_products
    }
    return render(request, 'web/home.html', context)

def contact_page(request):
    return render(request, 'web/contact.html')

def about_page(request):
    return render(request, 'web/about.html')

def faq_page(request):
    return render(request, 'web/faq.html')

def privacy_policy_page(request):
    return render(request, 'web/privacy_policy.html')

def terms_of_service_page(request):
    return render(request, 'web/terms_of_service.html')

def product_detail(request, slug):
    api_url = f'http://localhost:8000/api/colchoes/{slug}/'
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        product_data = response.json()
        context = {
            'product': product_data
        }
        return render(request, 'web/product_detail.html', context)
    except requests.HTTPError as http_err:
        if http_err.response.status_code == 404:
            return render(request, 'web/404.html', status=404)
        return render(request, 'web/error.html', {'error': str(http_err)}, status=500)
    
    except requests.exceptions.RequestException as e:
        return render(request, 'web/error.html', {'error': str(e)}, status=500)
