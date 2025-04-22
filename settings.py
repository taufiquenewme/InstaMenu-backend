import os

DEBUG = 'RENDER' not in os.environ  # Disable DEBUG in production

ALLOWED_HOSTS = ['*']  # Update with your Render domain in production

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add this for Render's health check
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com']
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True