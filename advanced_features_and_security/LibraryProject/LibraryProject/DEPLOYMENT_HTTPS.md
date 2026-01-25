# HTTPS Deployment Configuration

This Django application is configured to enforce HTTPS using Django's
built-in security settings.

## Web Server Configuration (Example: Nginx)

- SSL/TLS certificates are obtained using Let's Encrypt.
- All HTTP traffic is redirected to HTTPS.
- SSL certificates are configured in the server block.

Example:
- listen 443 ssl;
- ssl_certificate /etc/letsencrypt/fullchain.pem
- ssl_certificate_key /etc/letsencrypt/privkey.pem

## Django Configuration

- SECURE_SSL_REDIRECT is enabled
- HSTS is enabled with a one-year duration
- Secure cookies are enforced
- Security headers prevent XSS and clickjacking
