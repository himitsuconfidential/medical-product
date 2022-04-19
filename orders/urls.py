from django.urls import path, include
from orders import views
from .api_views import ProductViewSet, OrdersView
#from .api_views import total_products, all_products, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, 'product')
urlpatterns = [
    path('hello', views.hello),
    path('view_all', views.ViewAll.as_view()),
    path('managerOrders/<int:manager_id>', views.ManagerViewOrders.as_view(), name='manager-orders'),
    path('managers', views.ManagersViewAll.as_view(), name='managers'),
    path('order/manager=<str:manager__name> product=<str:products__name> time=<str:time>', OrdersView),
    #path('api/products/total', total_products),
    #path('api/products/', all_products.as_view(), name='all_products'),
    path('api/', include(router.urls))

]
