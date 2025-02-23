import subprocess
import json
from security.models import VulnerabilityScan

def scan_dependencies():
    try:
        # Run pip-audit to get vulnerable packages
        result = subprocess.run(
            ["pip-audit", "--format", "json"],
            capture_output=True,
            text=True
        )
        vulnerabilities = json.loads(result.stdout)
        
        # Filter only critical vulnerabilities
        critical = [
            f"{v['name']} ({v['version']}): {v['vuln']}"
            for v in vulnerabilities.get("vulnerabilities", [])
            if "CRITICAL" in v["vuln"].upper()
        ]
        
        # Save to database
        VulnerabilityScan.objects.create(
            scan_type="Dependencies",
            results={"critical": critical}
        )
        return critical
    except Exception as e:
        return []