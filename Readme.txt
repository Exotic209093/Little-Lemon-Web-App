==============================================================================
LITTLE LEMON RESTAURANT  -  Django Capstone (Meta Back-End Developer)
==============================================================================

A Django + Django REST Framework back-end for the fictional Little Lemon
restaurant. Features: a static homepage, a public Menu CRUD API, a token-
protected Table-Booking CRUD API, user registration via Djoser, and unit
tests covering models, the public API, and the protected API.

------------------------------------------------------------------------------
1. PROJECT LAYOUT
------------------------------------------------------------------------------
littlelemon/        Django project (settings, root URLs, WSGI/ASGI)
restaurant/         Restaurant app (models, serializers, views, tests, URLs)
restaurant/templates/index.html    Static HTML homepage
manage.py           Django management entry point
requirements.txt    Python dependencies (pinned)

------------------------------------------------------------------------------
2. REQUIREMENTS
------------------------------------------------------------------------------
- Python 3.10+   (developed against Python 3.14)
- MySQL 8.x      (the project is configured for MySQL per the rubric)
- pip / venv

Optional: peer reviewers without a local MySQL instance can run the project
against SQLite by setting the environment variable USE_SQLITE=1. The
DATABASES configuration in littlelemon/settings.py defaults to MySQL.

------------------------------------------------------------------------------
3. SETUP
------------------------------------------------------------------------------
# 1. Clone and enter the repo
git clone <repo-url> littlelemon
cd littlelemon

# 2. Create and activate a virtualenv
python -m venv venv
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4a. (MySQL) Create a database and set credentials
#     CREATE DATABASE littlelemon CHARACTER SET utf8mb4;
#     Then set the following environment variables (or edit settings.py):
#       DB_NAME=littlelemon
#       DB_USER=<your_mysql_user>
#       DB_PASSWORD=<your_mysql_password>
#       DB_HOST=127.0.0.1
#       DB_PORT=3306
# 4b. (SQLite fallback) export USE_SQLITE=1     # Linux/macOS
#     setx USE_SQLITE 1                          # Windows

# 5. Migrate and (optionally) create a superuser
python manage.py migrate
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
# -> http://127.0.0.1:8000/

------------------------------------------------------------------------------
4. RUN UNIT TESTS
------------------------------------------------------------------------------
python manage.py test

The suite (8 tests) covers:
  * Menu model __str__ output
  * Public Menu API: list, create, retrieve
  * Booking API: 401 when anonymous, 200 when token-authenticated, create
  * Static homepage renders successfully

------------------------------------------------------------------------------
5. API ENDPOINTS  (test these in Insomnia)
------------------------------------------------------------------------------
Base URL: http://127.0.0.1:8000

PUBLIC
  GET     /                                Static HTML homepage
  GET     /api/menu/                       List all menu items
  POST    /api/menu/                       Create a menu item
  GET     /api/menu/<id>/                  Retrieve a single menu item
  PUT     /api/menu/<id>/                  Update a menu item
  PATCH   /api/menu/<id>/                  Partial update
  DELETE  /api/menu/<id>/                  Delete a menu item

USER REGISTRATION & AUTH (Djoser + DRF Token)
  POST    /auth/users/                     Register: {"username","password"}
  POST    /auth/token/login/               Obtain token: {"username","password"}
  POST    /auth/token/logout/              Invalidate token (auth required)
  POST    /api-token-auth/                 Alternate DRF token endpoint

PROTECTED  (require:  Authorization: Token <token>)
  GET     /api/booking/tables/             List bookings
  POST    /api/booking/tables/             Create booking
                                           {"name","no_of_guests","bookingdate"}
  GET     /api/booking/tables/<id>/        Retrieve booking
  PUT     /api/booking/tables/<id>/        Update booking
  PATCH   /api/booking/tables/<id>/        Partial update
  DELETE  /api/booking/tables/<id>/        Delete booking

ADMIN
  /admin/                                  Django admin (use createsuperuser)

------------------------------------------------------------------------------
6. INSOMNIA QUICK GUIDE
------------------------------------------------------------------------------
1. Import or create a new collection "Little Lemon".
2. Set the base URL to http://127.0.0.1:8000.
3. Test the public Menu endpoints (no auth headers required).
4. Register a user:
     POST /auth/users/    body: { "username": "alice", "password": "secret123!" }
5. Log in to obtain a token:
     POST /auth/token/login/   body: { "username": "alice", "password": "secret123!" }
   -> response: { "auth_token": "<token>" }
6. For every booking request, add the header:
     Authorization: Token <token>
7. Verify that requests to /api/booking/tables/ return 401 without the
   header and 200/201 with it.

Sample booking POST body (JSON):
  {
    "name": "Anniversary",
    "no_of_guests": 2,
    "bookingdate": "2026-06-15T19:30:00Z"
  }

------------------------------------------------------------------------------
7. REPO COMMIT CHECKPOINTS  (suggested)
------------------------------------------------------------------------------
- Initial scaffold (project + app)
- Models + migrations
- Menu API
- Booking API + Djoser auth
- Static homepage + templates
- Unit tests
- Readme + final cleanup
