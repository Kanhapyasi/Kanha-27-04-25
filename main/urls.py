# from rest_framework import routers
# from main.views import StoreViewSet
# from django.urls import path
# from .views import TriggerReportView

# default_router = routers.SimpleRouter()

# default_router.register("store", StoreViewSet, basename="store")

# #urlpatterns = default_router.urls 
# urlpatterns = [
#     path('store/<str:pk>/trigger_report/', TriggerReportView.as_view(), name='trigger_report'),
# ]

# from django.urls import path, include
# from rest_framework import routers
# from main.views import StoreViewSet

# router = routers.SimpleRouter()
# router.register(r'store', StoreViewSet, basename='store')

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from rest_framework import routers
from main.views import StoreViewSet

default_router = routers.SimpleRouter()

default_router.register("store", StoreViewSet, basename="store")

urlpatterns = default_router.urls 
