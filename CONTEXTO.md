# Tillas Lab · Contexto del proyecto

Documento de traspaso. Sirve para que cualquiera, persona o asistente, se ponga
al día sin haber estado en las conversaciones anteriores. Si vas a trabajar en
este proyecto, leé esto primero.

Última actualización: 15 de agosto de 2026.

---

## 1. El negocio

Lavado y restauración de zapatillas con **retiro y entrega a domicilio** en el
Gran San Miguel de Tucumán, Argentina. El diferencial no es el lavado en sí,
es que el cliente no se mueve de su casa.

- **Marca:** TILLAS LAB
- **Bajada:** Sneaker Cleaning & Restoration
- **Apertura:** martes 1 de septiembre de 2026
- **Cómo lavan:** a máquina, con máquinas hechas para calzado. No a mano.
  Esto cambió sobre la marcha y está corregido en toda la web.
- **Canal de venta:** WhatsApp. No hay carrito ni pagos en línea. La web es la
  vidriera, el chat es la caja.
- **Cobro:** al entregar. Efectivo, transferencia o Mercado Pago. Sin señas.

**Zona de cobertura:** San Miguel de Tucumán, Yerba Buena, Tafí Viejo, Las
Talitas, Banda del Río Salí, Alderetes, El Manantial y Lomas de Tafí.

**Roles:** Ricardo hace la web y la campaña. El dueño del negocio es otra
persona, y es quien define nombre, precios, promociones y servicios. Varias
decisiones dependen de datos que el dueño todavía no pasó.

---

## 2. Estado actual

La web está hecha y publicada. Desde el 15 de agosto de 2026 es **un solo
sitio de cuatro páginas con tres pieles intercambiables**, para que el dueño
elija la estética sin que eso frene el desarrollo.

| Archivo | Qué es |
|---|---|
| `index.html` | La home |
| `pedido.html` | Pedido en 3 pasos, arma la ficha y el mensaje de WhatsApp |
| `ficha.html` | Seguimiento del par, los 5 pasos del taller |
| `taller.html` | Panel interno de fichas |
| `tema.css` | Los tres modos. Los colores se tocan solo acá |
| `marca/` | El logo en PNG |
| `viejo/` | Las dos versiones anteriores, archivadas |
| `Design/`, `Proyecto aparte/` | Lo que devolvió Claude Design, tal cual salió |

Dirección publicada: https://ricardoalvarez10.github.io/zapaslab/

Repositorio: `github.com/RicardoAlvarez10/zapaslab` (público). Conserva el
nombre viejo del proyecto para no romper la dirección publicada. Se publica
solo con cada `git push` a `main`.

**Las tres propuestas.** Arriba de todo hay una barra con tres botones que
cambian la piel al instante. El modo se recuerda al navegar entre páginas.

- `comun`: papel claro, tipografía neutra, sin acento. Respeta los dos rechazos
  registrados del dueño: nada de neones, nada de mayúsculas gritonas.
- `street`: muro de cemento, naranja aerosol, esquinas rectas, Anton.
- `grafity`: fondo oscuro, verde volt, mayúsculas anchas y sombras duras.

Las tres tienen el mismo contenido y las mismas funciones. El dueño elige solo
por gusto.

**El flujo de pedido.** Funciona sin backend: la ficha se guarda en el navegador
del cliente y el botón abre WhatsApp con el detalle escrito. `taller.html` lee
las fichas del navegador propio. Para que cliente y taller compartan datos hace
falta base de datos, y es el siguiente paso.

**Decisión pendiente, pero ya no bloquea.** Cuál de las tres queda depende del
dueño. Mientras tanto el desarrollo sigue, porque las tres corren sobre el mismo
código. Cuando elija, se fija `data-modo` en el `<html>` y se borra la barra
selectora: no hay que rehacer nada.

---

## 3. Lo que ya está decidido

- El funnel entero termina en WhatsApp, con mensajes previamente escritos según
  desde qué botón se entre.
- Las promos de apertura son dos y van encadenadas: los primeros 10 pares
  gratis el día de apertura llevándolos al local, y después los 50 clientes
  siguientes al 50% hasta el 15 de septiembre. Cada una tiene interruptor,
  fecha de vencimiento y contador de cupos. Cuando se agotan las dos, el bloque
  se reemplaza solo por un mensaje permanente, así la web nunca queda con una
  promo vencida.
- El mapa de cobertura es real, con OpenStreetMap, y marca la zona con un
  polígono. Las coordenadas son aproximadas y hay que ajustarlas.
- El usuario de redes es el mismo en las tres: `@tillaslab`. Falta confirmar
  que esté libre, porque no se puede verificar desde afuera.

---

## 4. Gustos del cliente

Esto se aprendió a base de rechazos. Conviene respetarlo para no volver atrás:

**No quiere:** neones, cintas de texto que giran ("muy china"), letras gigantes
de fondo, mayúsculas gritonas, emojis, guiones largos en los textos, textos
pegados a los bordes, ni nada que "parezca hecho por una máquina".

**Sí quiere:** limpio y ordenado, con aire; animaciones pausadas que se
disparen cuando el elemento ya está a la vista, no antes; secciones que se
sientan separadas; y ahora, una estética que converse con un logo grafiteado.

En la versión grafitera el lenguaje visual es: muro de cemento, afiches de
papel con cinta, aerosol como único color de acento, contornos gruesos y
sombras duras corridas. El logo de WhatsApp está resuelto como graffiti de
bloque, después de descartar una versión con capas de colores y chorreados por
recargada.

---

## 5. Lo que falta que pase el dueño

Nada de esto se puede inventar:

- Número real de WhatsApp. Hoy hay un teléfono de ejemplo (`5493810000000`) y
  **por eso la web todavía no se puede difundir**.
- ~~Precios reales~~ **resuelto el 15/08**: Lavado regular $8.000 y Lavado
  express $10.000, los dos con la misma lista de prestaciones. El Premium de
  materiales delicados se eliminó: el dueño definió dos servicios, no tres.
- Dirección del local. **Ahora urge:** la promo de los 10 lavados gratis pide
  que el cliente lleve el par al local, y no hay dirección que mostrar.
- ~~Nombres de los planes~~ **resuelto el 15/08**: Lavado regular y Lavado express.
- Aprobación del logo grafiteado. Ya existe y está puesto en la web, pero lo
  hizo Claude Design, no el dueño. Falta que lo apruebe.
- Si suman o no un servicio de restauración de verdad. La bajada dice
  "Restoration" pero los tres planes son solo de limpieza.
- Fotos reales de pares lavados, con la misma luz, fondo y ángulo en el antes y
  el después. Sin eso no hay contenido para redes.

---

## 5 bis. Corrección de textos del 15 de agosto

El dueño revisó la web por WhatsApp y corrigió casi todos los textos. Se aplicó
al pie de la letra en las tres propuestas, porque comparten el mismo HTML.

**Lo que cambió de fondo, no solo de redacción:**

- **El plazo.** Ya no son 48 a 72 horas. El regular se retira en el día y se
  entrega en el día o al día siguiente según la hora del pedido; el express se
  entrega a las dos horas. Cada servicio anuncia su propio plazo.
- **El pago.** Ya no es al recibir ni sin señas. Se paga al hacer el pedido, con
  billeteras virtuales, tarjetas de crédito o Apple Pay. El dueño lo dijo en
  futuro ("vamos a habilitar"), así que todavía no está operativo.
- **Los servicios.** De tres planes a dos: regular $8.000 y express $10.000, con
  las mismas prestaciones. Desapareció el Premium.
- **El ingreso.** Ya no es solo puerta a puerta: el cliente puede contactar por
  WhatsApp, teléfono, Instagram o Facebook, y también acercarse personalmente a
  dejar los pares.
- **La desinfección** pasó a primer plano: está en la volanta del título, en los
  tres pasos y como paso 4 del proceso, con luz ultravioleta. El proceso pasó de
  cinco pasos a seis, y eso se refleja en la ficha de seguimiento y en el panel.
- **El relavado sin cargo se eliminó.** El texto nuevo sobre manchas no lo
  menciona: ahora un colaborador explica qué no salió y por qué. Se sacó también
  de la línea de garantías del cierre.

- **Las promos.** Ya no es una sola. Son dos, encadenadas:
  1. **Los primeros 10 pares, gratis.** Solo el día de apertura y solo para
     quienes lleven el par **al local**. Se les pide una foto de recuerdo.
  2. **Los siguientes 50, al 50%.** Descuento de inauguración, hasta el 15 de
     septiembre.

  La web muestra la primera que siga vigente y, cuando se agota, pasa sola a la
  siguiente. Agotadas las dos, aparece el mensaje permanente. Los cupos se bajan
  a mano en el bloque `PROMOS` del script.

  **Ojo:** la promo de los 10 pares exige llevar el par al local, y la dirección
  del local sigue sin definirse. Hoy la web anuncia la promo sin poder decir
  adónde ir.

---

## 6. La campaña, como quedó pensada

Tres semanas antes de abrir: intriga, revelación y lanzamiento. Publicidad de
Meta segmentada al Gran San Miguel de Tucumán con destino a WhatsApp, porque la
conversión es un chat y no una compra. TikTok orgánico con antes y después, que
es el formato que más rinde en este rubro. Se recomendó además crear el perfil
de Google Business, que para un negocio local rinde más que Facebook.

Los textos de las primeras seis publicaciones ya están escritos en `REDES.md`.
