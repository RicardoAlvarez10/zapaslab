# Tillas Lab — Página web

**En vivo:** https://ricardoalvarez10.github.io/zapaslab/

## Cómo se ve

Un solo tema, derivado del sello de marca: fondo de papel crema `#F2ECE1`,
tinta `#131417`, naranja `#FF5A2D` como único acento, esquinas rectas y sombras
duras corridas. Títulos en Archivo Black y logo en Sigmar One.

Hasta el 15 de agosto había tres pieles intercambiables (`comun`, `street` y
`grafity`) con una barra selectora arriba, para que el dueño eligiera sin frenar
el desarrollo. **Eligió `street`.** El 16 de agosto se aplanó todo a un solo
tema: esa piel, repintada con los valores exactos del sello. Ya no hay
`data-modo` ni barra selectora.

La paleta y las tipografías salen de `Logo/Tillas-Lab-Logo/MARCA.md` y no se
inventan en el código. Cómo se aplican está en `DESIGN-SYSTEM.md`.

## Las páginas

| Archivo | Qué es |
|---|---|
| `index.html` | La home |
| `pedido.html` | Pedido en 3 pasos: calcula el total, guarda la ficha y arma el mensaje de WhatsApp |
| `ficha.html` | Seguimiento del par con los 6 pasos del taller. Se abre con `ficha.html?id=42` |
| `taller.html` | Panel interno: fichas, avanzar pasos, marcar entregada |
| `tema.css` | El tema y los componentes compartidos. **Los colores se tocan solo acá** |
| `marca/` | El sello listo para usar: web, favicon, avatar, portada y og |
| `Logo/Tillas-Lab-Logo/` | La fuente del logo: `MARCA.md`, los .ttf y los scripts que lo regeneran |
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

> Ojo: el número de WhatsApp es de ejemplo (`5493810000000`, 10 apariciones).
> No difundir el enlace hasta reemplazarlo (ver más abajo). Los precios ya son
> los reales: $8.000 el regular y $10.000 el express.

Landing informativa de una sola página para el servicio de lavado de zapatillas con retiro y entrega en el Gran San Miguel de Tucumán. Todo el funnel termina en WhatsApp.

**Un solo archivo:** `index.html` (HTML + CSS + JS embebidos, sin build). Cargas externas: Google Fonts (Archivo, Archivo Black y Sigmar One) y Leaflet + tiles claros de OpenStreetMap/CARTO para el mapa de cobertura (gratis, sin API key). El sello va como imagen (`marca/logo.png`) en el hero, el favicon y las redes; en la barra y el pie va un lockup de texto en Sigmar One (clase `.lk`), que escala mejor y pesa menos.

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

El usuario es **`@tillas.lab`, con punto**, y la página lo comunica así: "En todas somos @tillas.lab". El `tillaslab` sin punto estaba tomado en Instagram. Instagram y TikTok ya existen; **la Página de Facebook no**, así que ese enlace todavía no lleva a ningún lado.

**Antes de difundir la web**, las tres cuentas tienen que existir y tener al menos tres o cuatro publicaciones. Un perfil vacío enlazado desde la web resta credibilidad.

## Datos a reemplazar antes de publicar

Buscar y reemplazar en `index.html`:

| Placeholder | Reemplazar por |
|---|---|
| `5493810000000` (aparece en todos los links `wa.me`) | Número real de WhatsApp Business, formato `549381XXXXXXX` |
| `+54 9 381 000-0000` (footer) | Número real formateado |
| Enlace a Facebook | Apunta a `facebook.com/tillas.lab`, pero la Página no existe todavía: la tiene que crear el dueño desde su perfil. Hasta entonces el enlace del pie y el del bloque de redes van a dar error |
| Dirección del local | Todavía no la pasaron. **La promo de los 10 pares gratis es presencial y hoy la anuncia sin decir adónde ir.** Cuando exista, va en el pie, en el bloque de la promo y en los datos estructurados del `<head>` |
| Lámpara UV | El paso 4 del proceso ya anuncia desinfección con luz ultravioleta. Confirmar que esté comprada y operativa antes de difundir |
| Gamuza y cuero | El FAQ dice que se trabajan aparte. Al eliminarse el plan Premium se quedaron sin precio ni plazo propio |

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
