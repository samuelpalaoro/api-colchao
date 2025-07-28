from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
   path('', views.home_page, name='home'),
   path('contact/', views.contact_page, name='contact'),
   path('about/', views.about_page, name='about'),
   path('faq/', views.faq_page, name='faq'),
   path('privacy-policy/', views.privacy_policy_page, name='privacy_policy'),
   path('terms-of-service/', views.terms_of_service_page, name='terms_of_service'),
   path('colchao/<slug:slug>/', views.product_detail, name='product_detail'),
   
]
