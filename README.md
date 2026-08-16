# Tillas Lab — Página web

**En vivo:** https://ricardoalvarez10.github.io/zapaslab/

## Tres propuestas, un solo sitio

Arriba de todo hay una barra con tres botones: **Común**, **Street** y
**Grafity**. Cambian la piel al instante, sin recargar, y la elección se
recuerda al navegar entre páginas. Es para que el dueño compare.

| Modo | Cómo se ve |
|---|---|
| `comun` | Papel claro, tipografía neutra, sin color de acento. La que el dueño aprobó antes de que existiera el logo |
| `street` | Muro de cemento, naranja aerosol, esquinas rectas, títulos en Anton |
| `grafity` | Fondo oscuro, verde volt, títulos anchos en mayúscula y sombras duras corridas |

Las tres tienen exactamente el mismo contenido y las mismas funciones: mapa
real, promo con perillas, comparador antes/después, preguntas frecuentes, las
ocho localidades y el logo grafiteado.

Se puede forzar un modo por dirección: `index.html?modo=street`.

**Cuando el dueño elija:** poné `data-modo="grafity"` (o el que sea) fijo en la
etiqueta `<html>` de las cuatro páginas, borrá el bloque `<div class="modo-bar">`
y el script del selector. La barra desaparece y queda una sola web.

## Las páginas

| Archivo | Qué es |
|---|---|
| `index.html` | La home |
| `pedido.html` | Pedido en 3 pasos: calcula el total, guarda la ficha y arma el mensaje de WhatsApp |
| `ficha.html` | Seguimiento del par con los 5 pasos del taller. Se abre con `ficha.html?id=42` |
| `taller.html` | Panel interno: fichas, avanzar pasos, marcar entregada |
| `tema.css` | Los tres modos y los componentes compartidos. **Los colores se tocan solo acá** |
| `marca/` | El logo en PNG: redondo, avatar, portada, lockup sobre blanco |
| `viejo/` | Las versiones anteriores, archivadas |

Antes de tocar el aspecto, leer `DESIGN-SYSTEM.md`.

**Ojo con `taller.html`:** si publicás el sitio, ese panel queda accesible.
Renombralo a algo difícil de adivinar y no lo enlaces desde la home, o dejalo
solo en tu máquina.

## Cómo funciona el pedido hoy

Sin backend. El cliente carga el pedido, la ficha se guarda en **su** navegador
y el botón abre WhatsApp con todo el detalle escrito. Vos trabajás con ese
mensaje. `taller.html` lee las fichas de **tu** navegador, así que sirve para
probar el flujo completo, no para que cliente y taller compartan datos. Para
eso hace falta base de datos: es el siguiente paso.

Se publica sola con cada `git push` a `main`. Tarda un par de minutos en
reflejar los cambios.

> Ojo: el número de WhatsApp y los precios que se ven son de ejemplo.
> No difundir el enlace hasta reemplazarlos (ver más abajo).

Landing informativa de una sola página para el servicio de lavado de zapatillas con retiro y entrega en el Gran San Miguel de Tucumán. Todo el funnel termina en WhatsApp.

**Un solo archivo:** `index.html` (HTML + CSS + JS embebidos, sin build). Cargas externas: Google Fonts (Archivo, Lobster y Kaushan Script) y Leaflet + tiles oscuros de OpenStreetMap/CARTO para el mapa de cobertura (gratis, sin API key). El logo de la web está hecho con CSS sobre la fuente Lobster, no es imagen; los PNG de `marca/` son para redes.

**Mapa de cobertura:** el límite de la zona de servicio es el array `zona` dentro del script de `index.html` (pares lat/lng). Cuando el dueño defina la cobertura real, se ajustan esas coordenadas.

## Manejar las promos de apertura

Son dos y van una detrás de la otra. Todo se controla desde el bloque
`APERTURA Y PROMO` al inicio del script de `index.html`. No hace falta tocar el
HTML.

| Promo | Qué es | Vence |
|---|---|---|
| 1 | Los primeros **10 pares gratis**, el día de apertura, llevando el par al local | 1 de septiembre |
| 2 | Los siguientes **50 al 50%** por inauguración | 15 de septiembre |

La web muestra la primera que siga vigente. Cuando se le acaban los cupos o
vence, pasa sola a la segunda. Agotadas las dos, aparece el mensaje permanente
"Tus zapas listas en el día".

```js
var PROMOS=[
  { bloque:'promo-gratis', activa:true, hasta:new Date('2026-09-01T23:59:00-03:00'), lugares:10 },
  { bloque:'promo-mitad',  activa:true, hasta:new Date('2026-09-15T23:59:00-03:00'), lugares:50 }
];
```

- `activa` en `false` y esa promo desaparece al instante.
- `lugares` se baja a mano a medida que se usan. Al llegar a 0 la promo se cae sola.
- Con `lugares: null` no se muestra el contador.

## Ver en local

```bash
npx http-server . -p 4173
```

y abrir http://localhost:4173

## Elementos ocultos a propósito

Están en el HTML, comentados, listos para reactivar sacando el comentario:

| Qué | Dónde | Cuándo volver a mostrarlo |
|---|---|---|
| Bloque de **Extras** (cordones, impermeabilización, gorras, mochilas) | Al final de la sección `#servicios` | Cuando el dueño defina esos servicios y sus precios |

## Redes

La web enlaza **Instagram, TikTok y Facebook** en dos lugares: los botones de la sección "Seguinos" y los íconos del pie. WhatsApp aparece además como ícono en el pie y como botón flotante.

El usuario es **el mismo en las tres redes** (`@tillaslab`), y la página lo comunica así: "En todas somos @tillaslab". Si el dueño elige usuarios distintos en cada red, hay que corregir esa frase, porque quedaría diciendo algo falso.

**Antes de difundir la web**, las tres cuentas tienen que existir y tener al menos tres o cuatro publicaciones. Un perfil vacío enlazado desde la web resta credibilidad.

## Datos a reemplazar antes de publicar

Buscar y reemplazar en `index.html`:

| Placeholder | Reemplazar por |
|---|---|
| `5493810000000` (aparece en todos los links `wa.me`) | Número real de WhatsApp Business, formato `549381XXXXXXX` |
| `+54 9 381 000-0000` (footer) | Número real formateado |
| Precios `$12.000 / $18.000 / $25.000` | Precios reales |
| Nombres de los planes (Básico / Completo / Premium) | Los que use el dueño. Aparecen en el título, el botón, el mensaje de WhatsApp, la ficha del hero y en "Todo lo del Completo" del plan Premium |
| `@tillaslab` (Instagram, TikTok y Facebook) | Confirmar que el usuario esté libre en las tres. Si el dueño usa uno distinto en cada red, corregir también la frase "En todas somos @tillaslab" |
| "Primeros 50 pares al 50%" | Promo elegida |
| Dirección del local | Todavía no la pasaron. Cuando exista, va en el pie y en el bloque de datos estructurados del `<head>` |
| Logo | El lockup está hecho con CSS sobre la fuente Lobster (clase `.lk`). Si el dueño aprueba otro logo, se reemplaza esa clase y los PNG de `marca/` |

## Publicar la web gratis, sin dominio propio

Las tres opciones dan una dirección pública y no cuestan nada. Todas requieren
iniciar sesión una vez.

### 1. Netlify Drop (lo más rápido, sin comandos)

Entrar a app.netlify.com/drop y arrastrar **la carpeta** `zapaslab` a la página.
En menos de un minuto devuelve una dirección tipo `nombre-al-azar.netlify.app`,
que se puede cambiar por `zapaslab.netlify.app` desde *Site settings > Change site name*.

Para actualizar hay que volver a arrastrar la carpeta, salvo que se conecte el
repositorio de GitHub desde el panel.

### 2. GitHub Pages (la mejor si el repo ya está en GitHub)

Queda en `https://ricardoalvarez10.github.io/zapaslab/` y se actualiza sola con
cada `git push`. **Necesita que el repositorio sea público.**

```bash
gh repo create zapaslab --public --description "Landing de Tillas Lab"
git -C "C:/Users/Ricardo/.vscode/zapaslab" push -u origin main
gh api -X POST repos/RicardoAlvarez10/zapaslab/pages -f "source[branch]=main" -f "source[path]=/"
```

Sin la CLI: *Settings > Pages > Source: Deploy from a branch > main / (root)*.
La primera publicación tarda un par de minutos.

El archivo `.nojekyll` de este repo evita que GitHub procese la página con
Jekyll, que no hace falta acá.

### 3. Vercel

```bash
npx vercel --cwd "C:/Users/Ricardo/.vscode/zapaslab"
```

Pide iniciar sesión la primera vez y deja la web en `zapaslab.vercel.app`.
Si se conecta el repositorio, redespliega solo con cada push.

### Después, el dominio propio

Registrar el `.com.ar` en nic.ar (unos $8.000 por año) y apuntarlo desde el
panel del hosting elegido. Ninguna de las tres opciones obliga a migrar nada.

## Pendientes (cuando haya material real)

- Reemplazar la ilustración del slider antes/después por **fotos reales** (misma luz, mismo fondo, mismo ángulo)
- Galería de antes/después con casos reales
- Favicon y og:image (imagen para compartir en WhatsApp/redes)
- Google Business Profile + link a reseñas
