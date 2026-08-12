# Zapas Lab — Página web

**En vivo:** https://ricardoalvarez10.github.io/zapaslab/

Se publica sola con cada `git push` a `main`. Tarda un par de minutos en
reflejar los cambios.

> Ojo: el número de WhatsApp y los precios que se ven son de ejemplo.
> No difundir el enlace hasta reemplazarlos (ver más abajo).

Landing informativa de una sola página para el servicio de lavado de zapatillas con retiro y entrega en el Gran San Miguel de Tucumán. Todo el funnel termina en WhatsApp.

**Un solo archivo:** `index.html` (HTML + CSS + JS embebidos, sin build). Cargas externas: Google Fonts (Archivo) y Leaflet + tiles de OpenStreetMap/CARTO para el mapa de cobertura (gratis, sin API key).

**Mapa de cobertura:** el límite de la zona de servicio es el array `zona` dentro del script de `index.html` (pares lat/lng). Cuando el dueño defina la cobertura real, se ajustan esas coordenadas.

## Manejar la promo de apertura

Todo se controla desde el bloque `APERTURA Y PROMO` al inicio del script de `index.html`. No hace falta tocar el HTML.

```js
var APERTURA=new Date('2026-08-31T09:00:00-03:00');
var PROMO={
  activa:true,
  hasta:new Date('2026-09-14T23:59:00-03:00'),
  lugares:null
};
```

| Campo | Qué hace |
|---|---|
| `APERTURA` | Fecha de apertura. El cartel del hero cuenta los días solo y, pasada la fecha, muestra "Abierto · lunes a sábado de 9 a 20 hs". |
| `PROMO.activa` | `false` saca la promo al instante. Es el corte manual, para cuando se llega a los 50 pares. |
| `PROMO.hasta` | Fecha en que la promo se saca sola, sin que nadie toque nada. |
| `PROMO.lugares` | `null` no muestra contador. Con un número muestra "Quedan N lugares" y al llegar a `0` saca la promo sola. Hay que actualizarlo a mano. |

Cuando la promo termina, el bloque final se reemplaza solo por el mensaje permanente "Tus zapas listas en 48 horas", con el botón "Pedir retiro". La página nunca queda con un hueco ni con una promo vencida.

**Importante:** la web es estática, no tiene base de datos ni cuenta pedidos. Nadie descuenta los pares vendidos automáticamente: el corte es por fecha, o manual cambiando `activa` o `lugares`.

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

El usuario es **el mismo en las tres redes** (`@zapaslab.tuc`), y la página lo comunica así: "En todas somos @zapaslab.tuc". Si el dueño elige usuarios distintos en cada red, hay que corregir esa frase, porque quedaría diciendo algo falso.

**Antes de difundir la web**, las tres cuentas tienen que existir y tener al menos tres o cuatro publicaciones. Un perfil vacío enlazado desde la web resta credibilidad.

## Datos a reemplazar antes de publicar

Buscar y reemplazar en `index.html`:

| Placeholder | Reemplazar por |
|---|---|
| `5493810000000` (aparece en todos los links `wa.me`) | Número real de WhatsApp Business, formato `549381XXXXXXX` |
| `+54 9 381 000-0000` (footer) | Número real formateado |
| Precios `$12.000 / $18.000 / $25.000` | Precios reales |
| Nombres de los planes (Básico / Completo / Premium) | Los que use el dueño. Aparecen en el título, el botón, el mensaje de WhatsApp, la ficha del hero y en "Todo lo del Completo" del plan Premium |
| `31 · 08` / "Abrimos el 31" | Fecha real de apertura |
| `@zapaslab.tuc` (Instagram, TikTok y Facebook) | Usuario real, más la frase "En todas somos @zapaslab.tuc" de la sección de redes |
| "Primeros 50 pares al 50%" | Promo elegida |
| Nombre "Zapas Lab" | Si el dueño elige otro nombre (está en `<title>`, meta tags, logo, footer) |

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
gh repo create zapaslab --public --description "Landing de Zapas Lab"
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
