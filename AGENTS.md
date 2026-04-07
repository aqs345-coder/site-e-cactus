# OpenCode Agents Rules - site_formula

## Project Architecture
- **Framework:** Python / Django 6.0.3.
- **Main Logic:** The core business logic, models, and views reside in the `core/` directory (Django app).
- **Global Config:** The main application configuration, settings, and root URLs are located in `formula_sae/` (Django project).
- **Database:** SQLite (`db.sqlite3`).
- **Static Files:** `core/static/core/` — CSS in `css/`, JS in `js/`.
- **Templates:** `core/templates/core/` — main pages and `partials/` for reusable components (header, footer, sections).

## Environment & Execution
Always assume the virtual environment (`venv/`) is required for execution, but do not attempt to modify it.
- **Run Server:** `python manage.py runserver`
- **Migrations:** `python manage.py makemigrations` followed by `python manage.py migrate`
- **Dependency Management:** `pip install -r requirements.txt`

## Coding Guidelines & Constraints
- **Routing:** Whenever a new view is created in `core/views.py`, immediately map its URL in `core/urls.py` and ensure the base route is included in `formula_sae/urls.py`.
- **Admin:** Automatically register new models from `core/models.py` into `core/admin.py`.
- **Template Paths:** When rendering templates, use the app-relative path (e.g., `core/home.html`), NOT the full filesystem path (e.g., `core/templates/core/home.html`). Django's template loader already searches inside `core/templates/`.
- **Task Tracking:** Always check the `.TODO` file in the root directory for pending tasks before proposing structural changes.
- **Restricted Areas:** Never read from or write to `venv/`, `.venv/`, `.git/`, or `__pycache__/`.

## Design & Frontend Conventions
- **CSS Architecture:** Single stylesheet at `core/static/core/css/style.css` using CSS custom properties (HSL palette).
- **Color Palette:** High-voltage theme — primary yellow (`hsl(48, 100%, 55%)`), dark carbon backgrounds (`hsl(220, 10%, 8%)`), technical grays.
- **Typography:** Fluid scaling with `clamp()` for all font sizes. Headings use Oswald/Impact; body uses Inter/system-ui.
- **Custom Cursor:** Site uses a custom cursor (JS: `core/static/core/js/cursor.js`). Native cursor is hidden everywhere via `cursor: none !important;` on all elements.
- **Partials:** Page sections are split into `core/templates/core/partials/` (header, footer, hero, section-about, section-specs, section-team, section-contact). Include via `{% include 'core/partials/<name>.html' %}`.

## Agent Execution & Rate Limit Prevention
- **Batch File Reading:** NUNCA leia arquivos um por vez em sequência. Passe todos os caminhos de uma só vez.
- **No Blind Exploration:** Não use busca recursiva (`Glob` ou `Grep`) para "descobrir" onde o código está, a menos que seja estritamente necessário.
- **One-Shot Actions:** Agrupe análise lógica na menor quantidade de tool calls possíveis.
- **Rate Limits:** Espere ~5 segundos entre requests ao servidor para evitar erros de rate limit.
