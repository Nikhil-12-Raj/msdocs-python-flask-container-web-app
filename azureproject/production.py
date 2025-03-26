import os

# SECURITY WARNING: keep the secret key used in production secret! 
# Do not embed secret in this file
# For deployment to production, create an app setting, `SECRET_KEY`. Use this command to generate an appropriate value:
# Generate a new one with `python -c "import secrets; print(secrets.token_hex())"`
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
