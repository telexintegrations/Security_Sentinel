import re
from security.models import SecurityEvent

def analyze_django_logs(log_path="/var/log/django.log"):
    sql_keywords = r"(SELECT|UNION|DROP|INSERT|DELETE|ALTER|EXEC|--|;)"
    
    try:
        with open(log_path, "r") as f:
            logs = f.readlines()
        
        for line in logs:
            if re.search(sql_keywords, line, re.IGNORECASE):
                SecurityEvent.objects.create(
                    event_type="SQLi",
                    source_ip="N/A",  # Extract IP from logs if possible
                    details={"log_entry": line.strip()}
                )
        return True
    except Exception as e:
        return False