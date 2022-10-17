from django.urls import path
from rest_framework import routers
from .views import (
    CategoryView,
    BrandView,
    ProductView,
    FirmView,
    TransactionView
)


router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('brand', BrandView)
router.register('product', ProductView)
router.register('firm', FirmView)
router.register('transc', TransactionView)

urlpatterns = [

] + router.urls
