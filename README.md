# Django Blog Platform

A full-stack blog application built with Django 6.1, featuring category-based browsing, search, user authentication, a threaded comment system, and a permission-gated admin dashboard for managing posts, categories, and users.

**Live Demo:** [https://kishor123.pythonanywhere.com/](https://kishor123.pythonanywhere.com/)

---

## Features

- **Blog browsing** — featured posts on the homepage, category filtering, and full-text search across titles and descriptions
- **User authentication** — registration, login, and logout using Django's built-in auth system
- **Comments** — authenticated users can comment on published posts
- **Admin dashboard** — a custom, permission-gated dashboard (separate from Django's default `/admin/`) for staff to:
  - Create, edit, and delete blog posts (with image upload)
  - Manage categories
  - Manage users and their permissions
- **Responsive UI** — styled with Bootstrap 4 and `django-crispy-forms` for clean, consistent form rendering
- **Slug-based URLs** — SEO-friendly post URLs generated automatically from titles

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.1 (Python 3.12) |
| Database | SQLite |
| Frontend | Bootstrap 4, django-crispy-forms |
| Deployment | PythonAnywhere |

---

## Project Structure

```
django-blog/
├── blog_main/          # Project settings, URLs, WSGI/ASGI config, global static files
├── blogs/               # Core blog app — models, views, and URLs for posts, categories, comments
├── assignments/         # "About" section and social links
├── dashboards/          # Admin dashboard app — CRUD for posts, categories, and users
├── templates/           # HTML templates (base, home, login, register, dashboard views, etc.)
├── db.sqlite3           # SQLite database
├── manage.py
└── requirements.txt
```

### Key Models

- **Category** — blog post categories
- **Blog** — post title, slug, category, author, featured image, description, body, status (Draft/Published), and featured flag
- **Comment** — user comments linked to a blog post
- **About** / **Sociallinks** — site-wide "about" content and social media links shown on the homepage and footer

---

## Getting Started (Local Setup)

### Prerequisites

- Python 3.12+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kishor-J-K/django-blog.git
   cd django-blog
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for accessing `/admin/` and dashboard permissions)
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   The site will be available at `http://127.0.0.1:8000/`.

---

## Configuration Notes

- `ALLOWED_HOSTS` in `blog_main/settings.py` must include your domain (e.g. `kishor123.pythonanywhere.com`) for production use.
- Set `DEBUG = False` before deploying to production.
- `SECRET_KEY` is currently hardcoded in `settings.py` for simplicity — for production use, move it to an environment variable.
- Static and media files are served via `STATIC_ROOT` / `MEDIA_ROOT` and must be mapped explicitly in the hosting provider's static files configuration (see deployment notes below).

---

## Deployment

This project is deployed on **PythonAnywhere**. General steps for deploying your own copy:

1. Clone/upload the repository to your PythonAnywhere account.
2. Create a virtualenv with Python 3.12 and install dependencies from `requirements.txt`.
3. Configure the WSGI file to point to the project path and `blog_main.settings`.
4. Map `/static/` and `/media/` URLs to their respective directories in the **Web** tab.
5. Run `collectstatic` and apply migrations.
6. Reload the web app.

---

## License

This project is open for personal and educational use. Feel free to fork and adapt it.

---

## Author

**Kishor J K**
[LinkedIn](https://linkedin.com/in/) · [GitHub](https://github.com/Kishor-J-K) · [Kaggle](https://kaggle.com/)
