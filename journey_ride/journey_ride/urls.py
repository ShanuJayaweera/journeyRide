from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from passenger.views import startTourView
from owner.views import ownerView
from owner.views import driverView
from owner.views import vehicleView


urlpatterns = [
    path('login/', TemplateView.as_view(template_name="login.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', TemplateView.as_view(template_name="dashboard.html")),
    path('startTour/', startTourView),
    path('owner/', ownerView),
    path('driver/', driverView),
    path('vehicle/', vehicleView),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
