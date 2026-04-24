# AGENTS.md - site_e_cactus

## Project

- **Framework:** Django 6.0.3 with SQLite (`db.sqlite3`)
- **Active Apps:** `website/` (main views), `core/` (index only), others installed but minimal (`members`, `tasks`, `hr`)
- **Project Config:** `formula_sae/settings.py` and `formula_sae/urls.py`
- **Language:** Portuguese (pt-br)
- **URL Routing:** `formula_sae/urls.py` → `website/urls.py` (primary app)

## Commands

- **Run server:** `python manage.py runserver`
- **Migrations:** `python manage.py makemigrations` then `python manage.py migrate`
- **Install deps:** `pip install -r requirements.txt`

## Critical Rules

- **Routing:** New views in any app must be mapped in that app's `urls.py` AND included in `formula_sae/urls.py`
- **Admin:** Register new models in respective app's `admin.py` (django-summernote enabled)
- **Templates:** Use app-relative paths (`core/home.html`), NOT full paths (`core/templates/core/home.html`)
- **Custom cursor:** Site uses custom cursor via `core/static/core/js/cursor.js`. Native cursor hidden with `cursor: none !important;` globally

## Structure

- **Static:** `core/static/core/css/style.css`, `core/static/core/js/cursor.js`
- **Templates:** `core/templates/core/` with reusable partials in `core/templates/core/partials/`
- **CSS:** Single stylesheet using HSL custom properties (primary: `hsl(48, 100%, 55%)`, bg: `hsl(220, 10%, 8%)`)
- **Media uploads:** Stored in `media/` directory (MEDIA_ROOT configured)

## Workflow

- Check `.TODO` in root for pending tasks
- Never modify `venv/`, `.git/`, or `__pycache__/`
- Wait ~5 seconds between server requests to avoid rate limits

## Agent Guidelines

- Batch file reads together (never sequentially)
- Avoid recursive glob/grep for discovery—specify exact paths
- Group logic into minimal tool calls
