# Formula SAE UFERSA - Electric Racing Team

Site oficial de portfólio e showcase da equipe **Formula SAE UFERSA**, competindo na categoria **Electric Vehicle (EV)**. O projeto apresenta o carro de competição, especificações técnicas, equipe e oportunidades de patrocínio.

## 🏎️ Sobre o Projeto

Este é um site de alta performance visual, projetado para transmitir **alta tecnologia, velocidade, energia e engenharia de ponta**. O design utiliza uma paleta "high-voltage" com amarelo elétrico sobre fundos escuros de carbono, tipografia fluida e um cursor customizado interativo.

### Destaques Técnicos
- **Design System:** CSS custom properties (HSL) com paleta de alto contraste
- **Tipografia Fluida:** Escala com `clamp()` para responsividade suave entre mobile e desktop
- **Cursor Customizado:** Cursor interativo com `mix-blend-mode: difference` que reage dinamicamente às cores de fundo
- **Arquitetura Modular:** Templates divididos em partials reutilizáveis (header, footer, seções)
- **Animações:** Transições CSS suaves em cards, botões e elementos interativos

## 📁 Estrutura do Projeto

```
site_formula/
├── core/                          # Django App (lógica principal)
│   ├── static/core/
│   │   ├── css/style.css          # Folha de estilos principal
│   │   └── js/cursor.js           # Cursor customizado
│   ├── templates/core/
│   │   ├── home.html              # Template principal
│   │   └── partials/              # Componentes reutilizáveis
│   │       ├── header.html
│   │       ├── footer.html
│   │       ├── hero.html
│   │       ├── section-about.html
│   │       ├── section-specs.html
│   │       ├── section-team.html
│   │       └── section-contact.html
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── admin.py
├── formula_sae/                   # Django Project (configurações)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── db.sqlite3
└── AGENTS.md                      # Instruções para agentes IA
```

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.10+
- pip

### Setup

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd site_formula

# 2. Crie e ative o ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Aplique as migrações
python manage.py migrate

# 5. Inicie o servidor de desenvolvimento
python manage.py runserver
```

Acesse `http://localhost:8000` no navegador.

## 🎨 Design System

### Paleta de Cores (HSL)

| Variável | Valor | Uso |
|----------|-------|-----|
| `--clr-primary-base` | `hsl(48, 100%, 55%)` | Amarelo alta voltagem (destaques, botões) |
| `--clr-primary-lt` | `hsl(48, 100%, 70%)` | Hover states |
| `--clr-primary-dk` | `hsl(40, 90%, 40%)` | Bordas e detalhes |
| `--clr-bg-base` | `hsl(220, 10%, 8%)` | Fundo principal (carbono escuro) |
| `--clr-bg-surface` | `hsl(220, 8%, 12%)` | Cards e seções alternadas |
| `--clr-text-base` | `hsl(0, 0%, 95%)` | Texto principal |
| `--clr-text-muted` | `hsl(220, 5%, 70%)` | Texto secundário |

### Tipografia

| Família | Fontes | Uso |
|---------|--------|-----|
| `--ff-regular` | Inter, Roboto, system-ui | Corpo de texto |
| `--ff-headings` | Oswald, Bebas Neue, Impact | Títulos e headings |
| `--ff-mono` | JetBrains Mono, Fira Code | Dados técnicos |

### Cursor Customizado

O cursor substitui o padrão do sistema em todos os elementos:
- **Dot:** segue o mouse instantaneamente
- **Ring:** segue com interpolação linear (efeito elástico)
- **Estados:** hover (expande), click (encolhe), text (barra vertical)
- **Blend Mode:** `difference` para contraste dinâmico com qualquer fundo

## 📄 Seções do Site

1. **Hero:** Apresentação impactante com tagline, título e estatísticas rápidas
2. **O Carro:** Cards dos componentes principais (chassi, powertrain, aerodinâmica, suspensão)
3. **Especificações Técnicas:** Grid com dados numéricos (massa, potência, torque, 0-100, bateria, entre-eixos)
4. **Equipe:** Membros da equipe com avatar, nome, cargo e formação
5. **Contato:** Cards para patrocínio e recrutamento
6. **Footer:** Logo, copyright e links sociais

## 🛠️ Tecnologias

- **Backend:** Django 6.0.3
- **Database:** SQLite
- **Frontend:** HTML5, CSS3 (Custom Properties, Grid, Flexbox, clamp()), JavaScript vanilla
- **Fontes:** Google Fonts (Inter + Oswald)

## 📝 Convenções de Desenvolvimento

- Novas views devem ser mapeadas em `core/urls.py` e incluídas em `formula_sae/urls.py`
- Novos modelos devem ser registrados em `core/admin.py`
- Templates usam caminhos relativos ao app (`core/home.html`, não `core/templates/core/home.html`)
- Componentes reutilizáveis ficam em `core/templates/core/partials/`
- Verifique o arquivo `.TODO` para tarefas pendentes

## 📄 Licença

Todos os direitos reservados © 2026 Formula SAE UFERSA.
