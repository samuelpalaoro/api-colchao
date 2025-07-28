from django.urls import path
from .views import ColchaoCreateListView, ColchaoRetrieveUpdateDestroyView
   
urlpatterns = [
    path('', ColchaoCreateListView.as_view(), name='colchao-create-list'),
    path('<slug:slug>/', ColchaoRetrieveUpdateDestroyView.as_view(), name='colchao-detail-view'),
]

