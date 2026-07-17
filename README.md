# Portfolio

Personal portfolio website built with vanilla HTML5, CSS3, and JavaScript.

**Live Demo:** [glaucosamaral.github.io/portfolio](https://glaucosamaral.github.io/portfolio)

---

## Features

- Responsive design (mobile, tablet, desktop)
- Smooth scroll navigation with active state tracking
- Mobile hamburger menu with animated toggle
- CSS custom properties (design tokens) for consistent theming
- Hero section with gradient text and decorative background
- Skills grid with categorized tech tags
- Project cards with hover effects
- Contact form integrated with Formspree
- Dark theme with accessibility-friendly contrast

## Tech Stack

- **HTML5** — Semantic markup, accessibility attributes (`aria-label`, `rel="noopener noreferrer"`)
- **CSS3** — Flexbox, CSS Grid, Custom Properties, `clamp()`, `backdrop-filter`, transitions
- **JavaScript** — DOM manipulation, scroll event listeners, `classList` API
- **Google Fonts** — Inter (UI) + Fira Code (monospace accents)
- **Formspree** — Serverless form handling

## Project Structure

```
portfolio/
├── index.html          # Main page
├── standalone.html     # Single-file version (all CSS/JS inlined)
├── css/
│   ├── style.css       # Core styles and design system
│   └── responsive.css  # Media queries (tablet + mobile)
├── js/
│   └── script.js       # Navigation, scroll spy, navbar effects
├── img/                # Image assets
└── README.md
```

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/glaucosamaral/portfolio.git
   ```
2. Open `index.html` in your browser, or use Live Server in VS Code.

## Deployment

This project is deployed on **GitHub Pages** from the `main` branch.

## Contact Form Setup

The contact form uses [Formspree](https://formspree.io). To configure:

1. Create a free account at formspree.io
2. Create a new form and get your form ID
3. Replace `seu-form-id` in the form action URL in `index.html`

---

## Sobre (PT-BR)

Portfolio pessoal desenvolvido com HTML5, CSS3 e JavaScript puro.

**Demo ao vivo:** [glaucosamaral.github.io/portfolio](https://glaucosamaral.github.io/portfolio)

### Funcionalidades

- Design responsivo (mobile, tablet, desktop)
- Navegação com scroll suave e rastreamento de estado ativo
- Menu hamburger mobile com toggle animado
- CSS Custom Properties (design tokens) para theming consistente
- Seção hero com texto em gradiente e decoração de fundo
- Grid de habilidades com tags categorizadas
- Cards de projetos com efeitos de hover
- Formulário de contato integrado com Formspree
- Tema escuro com contraste acessível

### Tech Stack

- **HTML5** — Semântica, atributos de acessibilidade
- **CSS3** — Flexbox, CSS Grid, Custom Properties, `clamp()`, `backdrop-filter`
- **JavaScript** — Manipulação do DOM, scroll events, `classList`
- **Google Fonts** — Inter + Fira Code
- **Formspree** — Formulário serverless

### Como Rodar

```bash
git clone https://github.com/glaucosamaral/portfolio.git
```

Abra `index.html` no navegador ou use o Live Server no VS Code.

### Deploy

Hospedado no **GitHub Pages** a partir da branch `main`.
