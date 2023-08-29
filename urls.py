from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/', include('accounts.api_urls')),
    path('auth/', include('accounts.urls')),

    path('home/', include('home.urls')),

    # path('api/v1/sysloginputs/', include('sysloginputs.api_urls')),
    # path('sysloginputs/', include('sysloginputs.urls')),

    # path('splunkhecinputs/', include('splunkhecinputs.urls')),

    path('api/v1/in_syslog/', include('in_syslog.api_urls')),
    path('in_syslog/', include('in_syslog.urls')),

    path('api/v1/in_splunk_hec/', include('in_splunk_hec.api_urls')),
    path('in_splunk_hec/', include('in_splunk_hec.urls')),

]
