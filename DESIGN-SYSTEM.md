# Tillas Lab · Sistema de diseño

Fuente de verdad del aspecto de la web. Los colores viven en `tema.css` y en
ningún otro lado: si tocás uno ahí, cambia en las cuatro páginas.

Última actualización: 15 de agosto de 2026.

---

## 0. Tres modos

El sitio se pinta según el atributo `data-modo` del `<html>`. Hay tres
propuestas para que el dueño elija, y comparten contenido, estructura y
funciones. Lo único que cambia es la piel.

| | **comun** | **street** | **grafity** |
|---|---|---|---|
| Carácter | Editorial, sobrio | Muro y afiche | Graffiti nocturno |
| Fondo | `#ededea` claro | `#e8e3d7` papel cálido | `#0f1216` oscuro |
| Acento | Ninguno: la tinta | `#ff4d17` aerosol | `#b6e534` volt |
| Títulos | Archivo, caja normal | Anton, mayúscula | Archivo ancho, mayúscula |
| Esquinas | 16 px | Rectas | 16 px |
| Botón | Plano | Contorno y sombra naranja | Contorno y sombra negra |
| Rótulos | Etiqueta chica en mayúscula | Manuscrita | Manuscrita |

**Sobre el modo común.** Es el único sin color de acento y sin mayúsculas en
los títulos. Respeta al pie de la letra los dos rechazos registrados del dueño:
nada de neones y nada de mayúsculas gritonas. Los otros dos los desafían a
propósito, para que pueda ver la alternativa y decidir.

**Cuando elija uno:** se fija `data-modo` en el `<html>` de las cuatro páginas,
se borra el `<div class="modo-bar">` y el script del selector. Los otros dos
bloques de `tema.css` pueden quedarse: no molestan y sirven de registro.

---

## 1. Identidad

- **Marca:** Tillas Lab
- **Bajada:** Limpias. Frescas. Impecables.
- **Promesa:** *Tus zapas, como recién sacadas de la caja.*
- **Diferencial:** retiro y entrega a domicilio. El cliente no se mueve de su casa.
- **Zona:** Gran San Miguel de Tucumán, Argentina.
- **Canal:** WhatsApp. La web es la vidriera, el chat es la caja.

**Tono de voz.** Segunda persona del singular, voseo rioplatense. Frases cortas,
afirmativas, sin signos de exclamación ni emojis. Habla de zapas, no de calzado.
Promete plazos concretos y no adjetiva de más.

---

## 2. De dónde viene

El logo y la dirección **grafity** salieron de Claude Design. El **común** es la
versión que el dueño ya había aprobado, repintada con los mismos tokens. El
**street** es la versión de muro y aerosol, también reconstruida sobre el tema.

El cian `#2ee6d6` vive **solo dentro del logo**, en los tres modos. No se usa en
la interfaz de ninguno.

---

## 3. Tipografía

| Fuente | Uso |
|---|---|
| **Archivo** (variable, `wdth 62..125`, `wght 100..900`) | Todo el texto: títulos, cuerpo, botones |
| **Lobster** | Solo el logo y los números del proceso |
| **Kaushan Script** | Rótulos de sección, bajada y apuntes al margen |
| **Anton** | Solo en street: títulos de póster, siempre en mayúscula |

```css
--font:        "Archivo", system-ui, sans-serif;
--font-logo:   "Lobster", cursive;
--font-script: "Kaushan Script", cursive;
--font-title:  var(--font);            /* "Anton" en street */
```

Pesos: 400 cuerpo, 600 énfasis, 700 títulos, 800 botón principal.

---

## 4. Color

### 4.1 Superficies, de la más honda a la más alta

```css
--bg:     #0f1216;  /* fondo de la página */
--strong: #0b0e11;  /* proceso, cierre y pie */
--paper:  #161a1f;  /* hoja de sección */
--card:   #1d2229;  /* tarjeta */
--band:   #262b31;  /* superficie elevada, íconos */
```

### 4.2 Texto

```css
--ink:   #f3f5f7;  /* principal */
--soft:  #a9b2bd;  /* secundario */
--faint: #7b848f;  /* terciario, metadatos */
```

### 4.3 Bordes

```css
--hairline:   #272c33;
--hairline-2: #39404a;
```

### 4.4 Acentos

```css
--volt:     #b6e534;  /* único color de marca en la interfaz */
--volt-dim: #9ccc22;
--wa:       #1da851;  /* verde WhatsApp */
```

**Regla del volt.** Es el único acento. Se usa en el logo, el botón principal,
los tildes de las listas, el subrayado del menú activo, el polígono del mapa y
los rótulos manuscritos. Nada más.

**Regla del verde WhatsApp.** Si algo es `--wa`, se toca y abre WhatsApp. Nunca
decorativo.

**El logo de WhatsApp va pintado.** Es un graffiti de bloque: relleno `#25d366`,
contorno parejo de 8 px en `#0b0e11`, sombra dura corrida de 9 px y un reflejo
en `#84f2b0`, el mismo brillo que se les pinta a las letras de bloque. Se dibuja
una sola vez como `<symbol id="wa-pintado">` y se usa con `<use href="#wa-pintado">`
en los seis lugares donde aparece. Nunca el ícono plano de 24×24.

Necesita más caja que un ícono corriente para que el trazo se lea: `1.85em` en
los botones, `1.95em` en la barra, 26 px en el pie y 72 px en el flotante. El
botón flotante es el logo solo, sin círculo verde debajo: ya trae su contorno y
su sombra.

**Regla del cian.** `#2ee6d6` vive únicamente en las capas de sombra del logo y
de los números del proceso. Fuera de ahí no existe.

---

## 5. El logo

Lockup de dos líneas en Lobster: *Tillas* en volt, *Lab* en blanco. Cada línea
lleva contorno blanco de 9 px, una escalera de sombras duras en `#14171c` y dos
capas finales en cian. Rotación de −4° y −3°.

```html
<a class="lk lk-sm"><span class="t">Tillas</span><span class="l">Lab</span></a>
<div class="lk lk-xl"><span class="t">Tillas</span><span class="l">Lab</span></div>
```

`lk-xl` para el hero, `lk-sm` para la barra y el pie. Los PNG están en `marca/`:
`logo-redondo.png`, `avatar.png`, `portada.png` y `lockup-sobre-blanco.png`.

---

## 6. La ficha antes/después

Es el único bloque de papel claro de toda la página, y por eso funciona: ancla
el contraste y se lee como una ficha de taller real.

```css
background:#fafaf8; border:1px solid #e7e7e2; color:#14171c;
box-shadow:0 24px 60px -24px rgba(0,0,0,.75);
```

Adentro va el SVG de zapatilla, dibujado una sola vez como `<symbol id="shoe">`
y pintado por capas con variables CSS. El estado *después* pone `--sh-scuff`,
`--sh-stain` y `--sh-bg` en `transparent` y sube todo a blancos; el estado
*antes* usa marrones sucios sobre fondo `#e9e3d7`.

Capas: `--sh-bg`, `--sh-up`, `--sh-mid`, `--sh-out`, `--sh-collar`,
`--sh-tongue`, `--sh-eyestay`, `--sh-lace`, `--sh-lace-line`, `--sh-cap`,
`--sh-heel`, `--sh-flash`, `--sh-line`, `--sh-open`, `--sh-shadow`,
`--sh-scuff`, `--sh-stain`.

---

## 7. Componentes

| Clase | Uso |
|---|---|
| `.btn-dark` | Acción principal. Volt, contorno `2.5px` y sombra dura `4px 5px 0` |
| `.btn-wa` | WhatsApp. Verde pleno |
| `.btn-ghost` | Terciaria. Solo borde, pasa a volt al pasar el mouse |
| `.card` | Tarjeta de servicio. `.featured` suma borde volt y fondo más hondo |
| `.card .pop` | Etiqueta "El más pedido", manuscrita sobre volt, rotada −2° |
| `.lbl` | Rótulo de sección, manuscrito en volt |
| `.tagline` | "Limpias. Frescas. Impecables.", manuscrita rotada −2° |
| `.proto` | Bloque de proceso. Muro de cemento con rasante y halo volt |
| `.sheet` | Hoja de sección, radio 32 px |

---

## 8. Movimiento

Todo entra **cuando ya está a la vista**, nunca antes. La clase `.reveal` sube
24 px y desenfoca 8 px, con retraso escalonado por `--d`. El disparo está al
86% del alto de pantalla en escritorio y al 70% en celular.

Hay tres respaldos porque hay webviews donde `IntersectionObserver` no entrega
callbacks: observador, evento de scroll y un sondeo cada 600 ms.

Todo se apaga con `prefers-reduced-motion`.

---

## 9. Layout

```css
--pad-x: 44px;  /* escritorio */
--pad-x: 36px;  /* ≤900px */
--pad-x: 26px;  /* ≤640px */
--radius: 16px;
```

Riel de 1272 px para las hojas, 1080 px para el contenido. Breakpoints: 1300,
900, 640 y 600 px.

---

## 10. Reglas al generar

1. **Un solo acento.** Volt. Si aparece un segundo color, está mal.
2. **Sin mayúsculas en títulos.** Solo en etiquetas diminutas con interletrado.
3. **Sin exclamaciones ni emojis.**
4. **El antes/después es el formato estrella.**
5. **Mobile primero.** El público llega por Instagram en el teléfono.
6. **Aire entre secciones.** El dueño pidió "limpio y ordenado, con aire".

---

## 11. Pendientes

Nada de esto se puede inventar. Depende del dueño:

- Número real de WhatsApp. Hoy hay 11 apariciones de `5493810000000`.
- Precios reales. Los tres visibles son inventados.
- Fotos reales de pares lavados, con la misma luz, fondo y ángulo.
- Dirección del local y confirmación de los nombres de los planes.
