# Tillas Lab · Contexto del proyecto

Documento de traspaso. Sirve para que cualquiera, persona o asistente, se ponga
al día sin haber estado en las conversaciones anteriores. Si vas a trabajar en
este proyecto, leé esto primero.

Última actualización: 13 de agosto de 2026.

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

La web está hecha y publicada. Existe en **dos versiones con el mismo contenido
y distinta piel**:

| Versión | Dirección | Estilo |
|---|---|---|
| Sobria | https://ricardoalvarez10.github.io/zapaslab/ | Papel claro, tipografía neutra. La que aprobó el dueño en su momento |
| Grafitera | https://ricardoalvarez10.github.io/zapaslab/street.html | Muro de cemento, afiches con cinta, aerosol, tipografía de póster |

Repositorio: `github.com/RicardoAlvarez10/zapaslab` (público). Conserva el
nombre viejo del proyecto para no romper la dirección publicada. Se publica
solo con cada `git push` a `main`.

Archivos del repo:

- `index.html` y `street.html`: las dos versiones, cada una autocontenida.
- `README.md`: cómo tocar la web, manejar la promo y publicar.
- `REDES.md`: material listo para dar de alta Instagram y Facebook.
- `CONTEXTO.md`: este documento.

**Decisión abierta:** cuál de las dos versiones queda como principal. Ricardo
prefiere la grafitera, porque el logo del negocio va a ser grafiteado. El dueño
había aprobado la sobria antes de que existiera la otra. Hasta que se defina,
la sobria es la que abre en la dirección principal.

---

## 3. Lo que ya está decidido

- El funnel entero termina en WhatsApp, con mensajes previamente escritos según
  desde qué botón se entre.
- La promo de apertura es "primeros 50 pares al 50%", y se controla desde un
  bloque de configuración con tres perillas: interruptor manual, fecha de
  vencimiento y contador de cupos. Vence el 15 de septiembre, dos semanas
  después de abrir. Cuando termina, el bloque se reemplaza solo por un mensaje
  permanente, así la web nunca queda con una promo vencida.
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
- Precios reales. Los que se ven ($12.000, $18.000, $25.000) son inventados.
- Dirección del local.
- Confirmación de los nombres de los planes: Básico, Completo y Premium.
- El logo grafiteado.
- Si suman o no un servicio de restauración de verdad. La bajada dice
  "Restoration" pero los tres planes son solo de limpieza.
- Fotos reales de pares lavados, con la misma luz, fondo y ángulo en el antes y
  el después. Sin eso no hay contenido para redes.

---

## 6. La campaña, como quedó pensada

Tres semanas antes de abrir: intriga, revelación y lanzamiento. Publicidad de
Meta segmentada al Gran San Miguel de Tucumán con destino a WhatsApp, porque la
conversión es un chat y no una compra. TikTok orgánico con antes y después, que
es el formato que más rinde en este rubro. Se recomendó además crear el perfil
de Google Business, que para un negocio local rinde más que Facebook.

Los textos de las primeras seis publicaciones ya están escritos en `REDES.md`.
