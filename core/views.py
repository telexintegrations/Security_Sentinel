from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse
from django.views import View

class CoreIntegration(View):
    

    def get(self, request, *args, **kwargs):
        data = {
                "data": {
                    "date": {
                    "created_at": "YYYY-MM-DD",
                    "updated_at": "YYYY-MM-DD"
                    },
                    "descriptions": {
                    "app_description": "A brief description of the application functionality.",
                    "app_logo": "URL to the application logo.",
                    "app_name": "Name of the application.",
                    "app_url": "URL to the application or service.",
                    "background_color": "#HEXCODE"
                    },
                    "integration_category": "Monitoring & Logging",
                    "integration_type": "interval",
                    "is_active": False,
                    "output": [
                    {
                        "label": "output_channel_1",
                        "value": True
                    },
                    {
                        "label": "output_channel_2",
                        "value": False
                    }
                    ],
                    "key_features": [
                    "Feature description 1.",
                    "Feature description 2.",
                    "Feature description 3.",
                    "Feature description 4."
                    ],
                    "permissions": {
                    "monitoring_user": {
                        "always_online": True,
                        "display_name": "Performance Monitor"
                    }
                    },
                    "settings": [
                    {
                        "label": "interval",
                        "type": "text",
                        "required": True,
                        "default": "* * * * *"
                    },
                    {
                        "label": "Key",
                        "type": "text",
                        "required": True,
                        "default": "1234567890"
                    },
                    {
                        "label": "Do you want to continue",
                        "type": "checkbox",
                        "required": True,
                        "default": "Yes"
                    },
                    {
                        "label": "Provide Speed",
                        "type": "number",
                        "required": True,
                        "default": "1000"
                    },
                    {
                        "label": "Sensitivity Level",
                        "type": "dropdown",
                        "required": True,
                        "default": "Low",
                        "options": ["High", "Low"]
                    },
                    {
                        "label": "Alert Admin",
                        "type": "multi-checkbox",
                        "required": True,
                        "default": "Super-Admin",
                        "options": ["Super-Admin", "Admin", "Manager", "Developer"]
                    }
                    ],
                    "tick_url": "URL for subscribing to Telex's clock.",
                    "target_url": "Optional URL for getting data from the Telex channel"
                }
            }
        return JsonResponse(data)
