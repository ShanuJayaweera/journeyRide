from django.urls import path
from django.contrib import admin
from rest_framework import routers
from api.registration import views
from django.conf.urls import url, include
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'Passenger', views.PassengerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]