# Social Media API

## Setup Instructions
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Run migrations
5. Start server

## Authentication
- Register: POST /api/accounts/register/
- Login: POST /api/accounts/login/
- Token-based authentication

## User Model
- Username
- Email
- Bio
- Profile Picture
- Followers (Many-to-Many)

## Technologies Used
- Django
- Django REST Framework
- Token Authentication
