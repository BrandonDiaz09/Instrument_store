from django.urls import path
from instruments.views.catalogs_views import TypeList, TypeDetail, BrandList, BrandDetail, MaterialList, MaterialDetail, UseList, UseDetail
from instruments.views.instruments_view import InstrumentList, InstrumentDetail

urlpatterns = [
    path('types/', TypeList.as_view(), name='type-list'),
    path('types/<int:pk>/', TypeDetail.as_view(), name='type-detail'),
    path('brands/', BrandList.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetail.as_view(), name='brand-detail'),
    path('materials/', MaterialList.as_view(), name='material-list'),
    path('materials/<int:pk>/', MaterialDetail.as_view(), name='material-detail'),
    path('uses/', UseList.as_view(), name='use-list'),
    path('uses/<int:pk>/', UseDetail.as_view(), name='use-detail'),
    path('instruments/', InstrumentList.as_view(), name='instrument-list'),
    path('instruments/<int:pk>/', InstrumentDetail.as_view(), name='instrument-detail'),
]
