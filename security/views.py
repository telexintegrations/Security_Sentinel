# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from django.http import JsonResponse
# from django.views import View


# from django.http import HttpResponseForbidden

# SUSPICIOUS_PATTERNS = ["--", ";", "/*", "*/", "xp_cmdshell", "UNION SELECT"]

# class SQLiMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         query_params = request.GET.dict()
#         for value in query_params.values():
#             if any(pattern in value for pattern in SUSPICIOUS_PATTERNS):
#                 return HttpResponseForbidden("Suspicious activity detected.")
#         return self.get_response(request)





# import ssl
# import socket
# import datetime

# def check_ssl_expiry(hostname):
#     context = ssl.create_default_context()
#     with socket.create_connection((hostname, 443)) as sock:
#         with context.wrap_socket(sock, server_hostname=hostname) as ssock:
#             cert = ssock.getpeercert()
#             expiry_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
#             return expiry_date

# hostname = "youtube.com"
# expiry = check_ssl_expiry(hostname)
# print(f"SSL Expiry Date: {expiry}")
# print("Expired!" if expiry < datetime.datetime.utcnow() else "Valid SSL")



# import subprocess
# from datetime import datetime
# from security.models import VulnerabilityScan

# def check_ssl_expiry(domain):
#     try:
#         # Run OpenSSL command to get certificate expiry
#         cmd = f"openssl s_client -connect {domain}:443 -servername {domain} 2>/dev/null | openssl x509 -noout -enddate"
#         output = subprocess.check_output(cmd, shell=True).decode()
#         expiry_date_str = output.split("=")[1].strip()
#         expiry_date = datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y %Z")
        
#         # Calculate days remaining
#         days_left = (expiry_date - datetime.now()).days
#         return days_left
#     except Exception as e:
#         return None

# def scan_domains(domains=["example.com"]):
#     results = {}
#     for domain in domains:
#         days_left = check_ssl_expiry(domain)
#         if days_left and days_left <= 7:
#             results[domain] = f"EXPIRING_IN_{days_left}_DAYS"
    
#     # Save to database
#     VulnerabilityScan.objects.create(
#         scan_type="SSL",
#         results=results
#     )
#     return results

# import subprocess
# import json
# from security.models import VulnerabilityScan

# def scan_dependencies():
#     try:
#         # Run pip-audit to get vulnerable packages
#         result = subprocess.run(
#             ["pip-audit", "--format", "json"],
#             capture_output=True,
#             text=True
#         )
#         vulnerabilities = json.loads(result.stdout)
        
#         # Filter only critical vulnerabilities
#         critical = [
#             f"{v['name']} ({v['version']}): {v['vuln']}"
#             for v in vulnerabilities.get("vulnerabilities", [])
#             if "CRITICAL" in v["vuln"].upper()
#         ]
        
#         # Save to database
#         VulnerabilityScan.objects.create(
#             scan_type="Dependencies",
#             results={"critical": critical}
#         )
#         return critical
#     except Exception as e:
#         return []
