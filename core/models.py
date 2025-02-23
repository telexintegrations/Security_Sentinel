from django.db import models
# from django_cryptography.fields import encrypt

class CoreIntegration(models.Model):
    INTEGRATION_TYPES = [
        ('interval', 'Interval'),
        ('modifier', 'Modifier'),
        ('output', 'Output')
    ]
    
    name = models.CharField(max_length=100)
    integration_type = models.CharField(max_length=20, choices=INTEGRATION_TYPES)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    settings = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     abstract = True

class SecurityIntegration(CoreIntegration):
    # Security-specific fields
    monitored_events = models.JSONField(default=list)  # e.g., ["SQLi", "BruteForce"]
    scan_schedule = models.JSONField(default=dict)     # {"ssl": 86400, "dependencies": 43200}

class VulnerabilityScan(models.Model):
    integration = models.ForeignKey(CoreIntegration, on_delete=models.CASCADE)
    scan_type = models.CharField(max_length=50)
    results = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

class SecurityEvent(models.Model):
    integration = models.ForeignKey(CoreIntegration, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    source_ip = models.GenericIPAddressField()
    details = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

