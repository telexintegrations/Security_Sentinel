from django.db import models

# class SecurityEvent(models.Model):
#     EVENT_CHOICES = [
#         ("SQLi", "SQL Injection Attempt"),
#         ("BruteForce", "Failed Login Attempts"),
#         ("SSLExpired", "SSL Certificate Expired"),
#     ]
#     event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
#     source_ip = models.GenericIPAddressField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     resolved = models.BooleanField(default=False)
#     details = models.JSONField(default=dict)  # Store raw logs or attack payloads

#     def __str__(self):
#         return f"{self.event_type} from {self.source_ip}"

# class VulnerabilityScan(models.Model):
#     SCAN_TYPES = [("SSL", "SSL Check"), ("Dependencies", "Dependency Check")]
#     scan_type = models.CharField(max_length=50, choices=SCAN_TYPES)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     results = models.JSONField()  # e.g., {"example.com": "EXPIRING_IN_7_DAYS"}

#     def __str__(self):
#         return f"{self.scan_type} Scan at {self.timestamp}"
    
