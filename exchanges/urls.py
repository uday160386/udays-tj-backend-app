
from django.conf.urls import url

from exchanges import views

urlpatterns = [
     url(r'', views.TestEndpoint.external_api_view)
]
