/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,jsx}',
  ],
  theme: {
    extend: {
      colors: {
        // ── Design System skincaremaysha ────────────────────────
        primario:       '#C9A87C',
        'primario-dark':'#A07850',
        secundario:     '#F5EDE0',
        acento:         '#D4A5A5',
        'acento-verde': '#8FAF8C',
        alerta:         '#C0392B',
        advertencia:    '#E67E22',
        exito:          '#27AE60',
        texto:          '#3D2B1F',
        'texto-suave':  '#7D6355',
        superficie:     '#FDFAF6',
        borde:          '#E8D5C0',
      },
      fontFamily: {
        titulo: ['"Playfair Display"', 'serif'],
        cuerpo:  ['"DM Sans"', 'Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
