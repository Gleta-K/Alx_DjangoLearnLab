# Security Review

The application enforces HTTPS across all connections to protect data
in transit. HTTP Strict Transport Security (HSTS) ensures browsers
communicate securely with the server.

Secure cookies prevent session hijacking, and additional headers protect
against XSS, MIME sniffing, and clickjacking.

Potential improvements:
- Use a Web Application Firewall (WAF)
- Enable Content Security Policy (CSP)
- Regularly rotate SSL certificates
