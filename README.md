# Tillas Lab

Sitio de Tillas Lab, lavado y desinfección de zapatillas con retiro y entrega a
domicilio en el Gran San Miguel de Tucumán.

En línea: https://tillaslab.com.ar

## Archivos

| Archivo | Qué es |
|---|---|
| `index.html` | La página principal |
| `pedido.html` | Pedido en tres pasos, arma el mensaje de WhatsApp |
| `ficha.html` | Seguimiento del estado de un par |
| `tema.css` | Colores, tipografías y estilos compartidos |
| `marca/` | Logo e íconos en sus distintas medidas |
| `robots.txt`, `sitemap.xml` | Indexación en buscadores |
| `CNAME` | El dominio propio |
| `.nojekyll` | Evita que GitHub procese el sitio con Jekyll |

Son páginas estáticas, sin dependencias ni compilación. Lo único que se carga
desde afuera son las tipografías de Google Fonts y la biblioteca Leaflet, que
dibuja el mapa de cobertura.

## Verlo en la computadora

```bash
npx http-server . -p 4173
```

Después abrir http://localhost:4173

## Publicar

Se publica con GitHub Pages desde la rama `main`. Cada `git push` actualiza el
sitio en un par de minutos, sin ningún paso adicional.
