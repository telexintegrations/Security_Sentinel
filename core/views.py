# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from django.http import JsonResponse
# from django.views import View

# class CoreIntegration(View):
    

#     def get(self, request, *args, **kwargs):
#         data = {
#                 "data": {
#                     "date": {
#                     "created_at": "YYYY-MM-DD",
#                     "updated_at": "YYYY-MM-DD"
#                     },
#                     "descriptions": {
#                     "app_description": "A brief description of the application functionality.",
#                     "app_logo": "URL to the application logo.",
#                     "app_name": "Name of the application.",
#                     "app_url": "URL to the application or service.",
#                     "background_color": "#HEXCODE"
#                     },
#                     "integration_category": "Monitoring & Logging",
#                     "integration_type": "interval",
#                     "is_active": False,
#                     "output": [
#                     {
#                         "label": "output_channel_1",
#                         "value": True
#                     },
#                     {
#                         "label": "output_channel_2",
#                         "value": False
#                     }
#                     ],
#                     "key_features": [
#                     "Feature description 1.",
#                     "Feature description 2.",
#                     "Feature description 3.",
#                     "Feature description 4."
#                     ],
#                     "permissions": {
#                     "monitoring_user": {
#                         "always_online": True,
#                         "display_name": "Performance Monitor"
#                     }
#                     },
#                     "settings": [
#                     {
#                         "label": "interval",
#                         "type": "text",
#                         "required": True,
#                         "default": "* * * * *"
#                     },
#                     {
#                         "label": "Key",
#                         "type": "text",
#                         "required": True,
#                         "default": "1234567890"
#                     },
#                     {
#                         "label": "Do you want to continue",
#                         "type": "checkbox",
#                         "required": True,
#                         "default": "Yes"
#                     },
#                     {
#                         "label": "Provide Speed",
#                         "type": "number",
#                         "required": True,
#                         "default": "1000"
#                     },
#                     {
#                         "label": "Sensitivity Level",
#                         "type": "dropdown",
#                         "required": True,
#                         "default": "Low",
#                         "options": ["High", "Low"]
#                     },
#                     {
#                         "label": "Alert Admin",
#                         "type": "multi-checkbox",
#                         "required": True,
#                         "default": "Super-Admin",
#                         "options": ["Super-Admin", "Admin", "Manager", "Developer"]
#                     }
#                     ],
#                     "tick_url": "URL for subscribing to Telex's clock.",
#                     "target_url": "Optional URL for getting data from the Telex channel"
#                 }
#             }
#         return JsonResponse(data)


from django.views import View
from django.http import JsonResponse
from django.utils import timezone

class CoreIntegration(View):
    pass
#     def get(self, request, *args, **kwargs):
#         current_date = timezone.now().date().isoformat()
        
#         data = {
#             "data": {
#                 "date": {
#                     "created_at": current_date,
#                     "updated_at": current_date
#                 },
#                 "descriptions": {
#                     "app_description": "Security monitoring integration that tracks vulnerabilities, SSL expiry, and suspicious activities.",
#                     "app_logo": "https://example.com/security-sentinel-logo.png",
#                     "app_name": "Security Sentinel",
#                     "app_url": "https://example.com/security-sentinel",
#                     "background_color": "#2C3E50"
#                 },
#                 "integration_category": "Monitoring & Logging",
#                 "integration_type": "interval",
#                 "is_active": False,
#                 "output": [
#                     {
#                         "label": "telex_alerts",
#                         "value": True
#                     },
#                     {
#                         "label": "email_notifications",
#                         "value": False
#                     }
#                 ],
#                 "key_features": [
#                     "Real-time security event monitoring",
#                     "Automated vulnerability scanning",
#                     "SSL/TLS certificate expiration tracking",
#                     "Customizable alert thresholds"
#                 ],
#                 "permissions": {
#                     "monitoring_user": {
#                         "always_online": True,
#                         "display_name": "Security Monitor"
#                     }
#                 },
#                 "settings": [
#                     {
#                         "label": "interval",
#                         "type": "text",
#                         "required": True,
#                         "default": "* * * * *"
#                     },
#                     {
#                         "label": "Key",
#                         "type": "text",
#                         "required": True,
#                         "default": "1234567890"
#                     },
#                     {
#                         "label": "Do you want to continue",
#                         "type": "checkbox",
#                         "required": True,
#                         "default": "Yes"
#                     },
#                     {
#                         "label": "Provide Speed",
#                         "type": "number",
#                         "required": True,
#                         "default": "1000"
#                     },
#                     {
#                         "label": "Sensitivity Level",
#                         "type": "dropdown",
#                         "required": True,
#                         "default": "Low",
#                         "options": ["High", "Low"]
#                     },
#                     {
#                         "label": "Alert Admin",
#                         "type": "multi-checkbox",
#                         "required": True,
#                         "default": "Super-Admin",
#                         "options": ["Super-Admin", "Admin", "Manager", "Developer"]
#                     }
#                 ],
#                 "tick_url": "https://api.telex.im/v1/tick/subscribe",
#                 "target_url": "https://api.telex.im/v1/channel/data"
#             }
#         }
#         return JsonResponse(data)
    

# from django.views import View
# from django.http import JsonResponse
# from .models import CoreIntegration

# class CoreIntegrationView(View):
#     def get(self, request, *args, **kwargs):
#         try:
#             integration = CoreIntegration.objects.get(name="Security Sentinel")
            
#             response_data = {
#                 "data": {
#                     "date": {
#                         "created_at": integration.created_at.isoformat(),
#                         "updated_at": integration.updated_at.isoformat()
#                     },
#                     "descriptions": {
#                         "app_description": integration.description,
#                         "app_logo": "https://example.com/logo.png",
#                         "app_name": integration.name,
#                         "app_url": "https://example.com/security-sentinel",
#                         "background_color": "#2C3E50"
#                     },
#                     "integration_category": "Monitoring & Logging",
#                     "integration_type": integration.integration_type,
#                     "is_active": integration.is_active,
#                     "output": self.get_output_config(integration),
#                     "key_features": [
#                         "Real-time security monitoring",
#                         "Automated vulnerability scanning",
#                         "Custom alert thresholds"
#                     ],
#                     "permissions": {
#                         "monitoring_user": {
#                             "always_online": True,
#                             "display_name": "Security Admin"
#                         }
#                     },
#                     "settings": self.get_settings(integration),
#                     "tick_url": "https://api.telex.im/v1/tick",
#                     "target_url": "https://api.telex.im/v1/data"
#                 }
#             }
#             return JsonResponse(response_data)
            
#         except CoreIntegration.DoesNotExist:
#             return JsonResponse({"error": "Integration not found"}, status=404)

#     def get_output_config(self, integration):
#         return [
#             {"label": "telex_alerts", "value": True},
#             {"label": "email_notifications", "value": False}
#         ]

#     def get_settings(self, integration):
#         return [
#             {
#                 "label": "interval",
#                 "type": "text",
#                 "required": True,
#                 "default": integration.settings.get("interval", "* * * * *")
#             },
#             # Add other settings fields similarly
#         ]