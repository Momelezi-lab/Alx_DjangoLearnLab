# Add at the bottom
AUTH_USER_MODEL = 'relationship_app.CustomUser'

# Make sure MEDIA settings exist for profile_photo
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
