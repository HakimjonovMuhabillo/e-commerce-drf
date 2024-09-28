from .views import *
from rest_framework_nested import routers


router = routers.DefaultRouter()

router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('customers', CustomerViewSet)
router.register('carts', CartViewSet)
router.register('orders', OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + products_router.urls + carts_router.urls
