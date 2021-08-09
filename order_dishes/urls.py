import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from order_dishes.config import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('dish/', include('dish.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
