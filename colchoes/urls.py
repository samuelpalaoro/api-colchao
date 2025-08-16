from django.urls import path
from .views import ColchaoCreateListView, ColchaoRetrieveUpdateDestroyView, comparison_detail_view
   
urlpatterns = [
    path('', ColchaoCreateListView.as_view(), name='colchao-create-list'),
    path('<slug:slug>/', ColchaoRetrieveUpdateDestroyView.as_view(), name='colchao-detail-view'),
    path('compare/<slug:slug>/', comparison_detail_view, name='comparison_detail'),
]
from . import views