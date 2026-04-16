# AGENTS.md - site_formula

## Project
- **Framework:** Django 6.0.3 with SQLite (`db.sqlite3`)
- **App:** `core/` contains all views, models, templates, and static files
- **Project Config:** `formula_sae/` contains settings and root URLs

## Commands
- **Run server:** `python manage.py runserver`
- **Migrations:** `python manage.py makemigrations` then `python manage.py migrate`
- **Install deps:** `pip install -r requirements.txt`

## Critical Rules
- **Routing:** New views in `core/views.py` MUST be mapped in `core/urls.py` AND included in `formula_sae/urls.py`
- **Admin:** Register new models in `core/admin.py`
- **Templates:** Use app-relative paths (`core/home.html`), NOT full paths (`core/templates/core/home.html`)
- **Custom cursor:** Site uses custom cursor via `core/static/core/js/cursor.js`. Native cursor hidden with `cursor: none !important;` globally

## Structure
- **Static:** `core/static/core/css/style.css`, `core/static/core/js/cursor.js`
- **Templates:** `core/templates/core/` with reusable partials in `core/templates/core/partials/`
- **CSS:** Single stylesheet using HSL custom properties (primary: `hsl(48, 100%, 55%)`, bg: `hsl(220, 10%, 8%)`)

## Workflow
- Check `.TODO` in root for pending tasks
- Never modify `venv/`, `.git/`, or `__pycache__/`
- Wait ~5 seconds between server requests to avoid rate limits

## Agent Guidelines
- Batch file reads together (never sequentially)
- Avoid recursive glob/grep for discovery—specify exact paths
- Group logic into minimal tool calls