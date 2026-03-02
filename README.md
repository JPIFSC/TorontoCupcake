# Toronto Cupcake — Website

Reimagined homepage for [Toronto Cupcake](https://www.torontocupcake.com), built with vanilla HTML, CSS, and JS. No frameworks or build tools required — just open `index.html` in a browser.

---

## Project Structure

```
toronto-cupcake/
├── index.html              # Main HTML page
│
├── css/
│   ├── base.css            # CSS variables, reset, typography, shared utilities
│   ├── nav.css             # Fixed navigation bar
│   ├── hero.css            # Full-screen split hero section + animations
│   ├── sections.css        # Marquee, Why Us, Flavors, Occasions, Process,
│   │                       #   Testimonial, and CTA sections
│   ├── footer.css          # Footer layout and social links
│   └── responsive.css      # Mobile & tablet breakpoints (≤900px, ≤600px)
│
├── js/
│   ├── main.js             # Nav scroll behaviour + scroll-reveal observer
│   └── illustrations.js    # Exported SVG strings for cupcake illustrations
│                           #   (reference file — for use if migrating to a
│                           #    component system like React or Vue)
│
└── assets/                 # Place images, fonts, icons here
    └── (empty — ready for your images)
```

---

## Color Palette

| Name           | Hex       | Usage                          |
|----------------|-----------|--------------------------------|
| Shinshu        | `#8C1822` | Crimson — nav, CTA, accents    |
| Fig Balsamic   | `#590222` | Burgundy — hero bg, footer     |
| Persian Orange | `#C8874A` | Buttons, labels, marquee dots  |
| Valencia       | `#D95A4E` | Coral — hover states, frosting |
| Jaguar Rose    | `#F2B6B6` | Blush — highlights, testimonial|
| Cream          | `#FDF6F0` | Page background                |
| Dark           | `#1a0a0d` | Footer, body text              |

---

## Adding Real Images

Replace the SVG placeholder divs in `index.html` with `<img>` tags pointing to files in `assets/`:

```html
<!-- Hero right panel -->
<img src="assets/hero-cupcake.jpg" alt="Toronto Cupcake hero" style="width:100%;height:100%;object-fit:cover;">

<!-- Why Us main card -->
<img src="assets/box.jpg" alt="Cupcake box" class="why-img-main">
```

---

## Browser Support

Works in all modern browsers (Chrome, Firefox, Safari, Edge). No polyfills needed.
