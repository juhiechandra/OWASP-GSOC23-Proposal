from flask import Flask, request, jsonify
import subprocess
import re

app = Flask(__name__)

SANS_TOP_25 = [
    'Injection', 'Broken Authentication and Session Management', 'Cross-Site Scripting (XSS)',
    'Broken Access Control', 'Security Misconfiguration', 'Insecure Cryptographic Storage',
    'Insufficient Transport Layer Protection', 'Unvalidated Redirects and Forwards',
    'Insecure Communication Between Components', 'Poor Coding Practices', 'Code Injection',
    'Memory Leak and Buffer Overflow', 'Race Conditions', 'Malicious File Execution',
    'Insecure Initialization and Termination', 'Insufficient Authorization',
    'SQL Injection (SQLi)', 'LDAP Injection', 'Command Injection', 'XPath Injection',
    'CSRF (Cross-Site Request Forgery)', 'OS Command Injection', 'DOM-Based XSS',
    'Security Decisions Via Untrusted Inputs', 'Web and Application Server Misconfiguration'
]

@app.route('/scan', methods=['POST'])
def scan_website():
    # Get the URL to scan from the request data
    url = request.json['url']

    # Run the Nikto scanner and capture the output
    output = subprocess.check_output(['nikto', '-h', url, '-o', '-', '-Format', 'txt'])

    # Extract the vulnerability information from the Nikto output
    vulnerabilities = []
    for line in output.splitlines():
        # Check if the line contains a vulnerability description
        match = re.search(r'\+[^\n]*\b(OSVDB-\d+|CVE-\d+-\d+)\b', line.decode('utf-8'))
        if not match:
            continue

        # Extract the severity level and vulnerability name from the line
        severity = re.search(r'\s+Severity: ([^,]+),', line.decode('utf-8')).group(1)
        vulnerability = match.group(1)

        # Check if the vulnerability matches any of the SANS Top 25 list items
        for item in SANS_TOP_25:
            if item.lower() in line.decode('utf-8').lower():
                # Add the vulnerability to the list
                vulnerabilities.append({
                    'name': vulnerability,
                    'severity': severity,
                    'description': line.decode('utf-8').strip()
                })
                break

    # Return the list of vulnerabilities found
    return jsonify(vulnerabilities)


if __name__ == '__main__':
    app.run(debug=True)
