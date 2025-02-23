import subprocess
from datetime import datetime
from security.models import VulnerabilityScan

def check_ssl_expiry(domain):
    try:
        # Run OpenSSL command to get certificate expiry
        cmd = f"openssl s_client -connect {domain}:443 -servername {domain} 2>/dev/null | openssl x509 -noout -enddate"
        output = subprocess.check_output(cmd, shell=True).decode()
        expiry_date_str = output.split("=")[1].strip()
        expiry_date = datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y %Z")
        
        # Calculate days remaining
        days_left = (expiry_date - datetime.now()).days
        return days_left
    except Exception as e:
        return None

def scan_domains(domains=["example.com"]):
    results = {}
    for domain in domains:
        days_left = check_ssl_expiry(domain)
        if days_left and days_left <= 7:
            results[domain] = f"EXPIRING_IN_{days_left}_DAYS"
    
    # Save to database
    VulnerabilityScan.objects.create(
        scan_type="SSL",
        results=results
    )
    return results