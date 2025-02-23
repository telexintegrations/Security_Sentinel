from django.contrib import admin
from .models import CoreIntegration
from .models import SecurityIntegration
from .models import VulnerabilityScan
from .models import SecurityEvent




# Register your models here.
admin.site.register(CoreIntegration)
admin.site.register(SecurityIntegration)
admin.site.register(VulnerabilityScan)
admin.site.register(SecurityEvent)