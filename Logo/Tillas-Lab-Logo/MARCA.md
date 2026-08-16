# Tillas Lab, especificacion de marca

Lavado y restauracion de zapatillas. Gran San Miguel de Tucuman.
Apertura prevista: 1 de septiembre de 2026.

Estado del logo: CERRADO. El 16 de agosto de 2026 el dueño eligio Sigmar One
para el arco superior, sobre las nueve opciones de `Logo/comparativa-tipografias.png`.

## Paleta

| Rol | HEX | Uso |
|---|---|---|
| Crema | `F2ECE1` | Anillo exterior, relleno de las letras, empeine de la zapatilla, espuma |
| Tinta | `131417` | Contornos, disco interior, tipografia del arco inferior |
| Naranja | `FF5A2D` | Puntera, cuello, entresuela, contorno exterior de las letras |

El naranja se eligio a criterio de quien armo el logo. Si la web ya tiene su
paleta definida, hay que reemplazar ese valor en los tres lugares donde aparece
y regenerar los archivos.

## Tipografia

| Elemento | Fuente | Cuerpo | Notas |
|---|---|---|---|
| Arco superior, "TILLAS LAB" | Sigmar One Regular | 66 | Convertida a curvas |
| Arco inferior, "LIMPIAS · FRESCAS · IMPECABLES" | Archivo Black Regular | 34 | Convertida a curvas |

Las dos son de Google Fonts, licencia SIL Open Font, uso comercial permitido.
Los archivos .ttf estan en la carpeta `Fuentes`.

Alternativas evaluadas y descartadas: Luckiest Guy, Bowlby One, Modak, Bagel Fat
One, Bungee, Lilita One, Anton, Rubik Bubbles. Estan todas montadas sobre el
sello en `Logo/comparativa-tipografias.png`.

PENDIENTE TECNICO: el .ttf de Sigmar One no esta en `Fuentes/`, y la imagen base
del sello vacio (el JPG que apunta `SRC` en final_luckiest.py) ya no existe. Los
PNG de `marca/` se compusieron tomando el arco superior de la lamina de
comparacion, que es de menor resolucion que el resto del sello. Para tener el
sello definitivo a 3000 px hay que bajar Sigmar One de Google Fonts, dejarlo en
`Fuentes/`, recuperar la imagen base y volver a correr el script.

## Geometria del sello

Medida sobre la imagen base de 1408 x 768 px.

| Elemento | Valor |
|---|---|
| Centro | x 704, y 386 |
| Radio del anillo negro exterior | 357 |
| Banda crema | de 240 a 344, ancho 104 |
| Centro de la banda | 292 |
| Disco negro interior | radio 231 |
| Linea de base del arco superior | radio 269, texto crece hacia afuera |
| Linea de base del arco inferior | radio 304, texto crece hacia adentro |
| Apertura de los dos arcos | 160 grados, centrados |

Tratamiento del texto superior, en unidades de la imagen base:

- Sombra tinta, contorno 32, desplazada 6 en x y 8 en y
- Contorno naranja de 32
- Contorno tinta de 19
- Relleno crema

El texto inferior va en tinta plena, sin contorno ni sombra.

## Archivos

| Archivo | Para que sirve |
|---|---|
| `Logo/tillas-lab-logo.png` | Version principal, 3000 px, fondo blanco |
| `Logo/tillas-lab-logo-transparente.png` | Para montar sobre cualquier color |
| `Logo/tillas-lab-perfil-512.png` | Foto de perfil de Instagram y Facebook |
| `Logo/tillas-lab-perfil-180.png` | WhatsApp Business y favicon |
| `Logo/tillas-lab-logo.svg` | Texto vectorial, zapatilla en mapa de bits |
| `Logo/comparativa-tipografias.png` | Las nueve opciones tipograficas |
| `Fuentes/` | Los .ttf usados |
| `Fuente-editable/` | Los scripts que generan todo |

## Limitaciones que conviene tener presentes

El SVG es hibrido. El texto son curvas vectoriales de verdad y se puede editar,
pero la zapatilla sigue siendo la imagen generada con Nano Banana, incrustada en
mapa de bits. Sirve para cambiar la tipografia o la frase. No sirve para imprimir
en vinilo de corte ni para bordado.

Para llegar a un vector completo hay dos caminos. Uno es vectorizar la zapatilla
con Image Trace de Illustrator o con vectorizer.ai y despues limpiar los trazos a
mano. El otro es encargarle el dibujo a un ilustrador, que da mejor resultado y
cuesta entre 30 y 80 mil pesos.

La imagen base vino en JPG, asi que los contornos negros tienen algo de ruido de
compresion. En pantalla no se percibe. Si en algun momento hace falta la version
impecable, hay que regenerar el sello vacio en PNG y volver a componer con los
mismos parametros de este documento.

## Como regenerar

En `Fuente-editable` estan `arc.py`, que convierte los glifos en curvas y los
distribuye sobre un arco, y `final_luckiest.py`, que arma el sello completo y
exporta los cinco archivos.

Para cambiar la tipografia alcanza con apuntar a otro .ttf en la linea donde se
instancia `top`. El cuerpo se recalcula solo: el script busca el tamaño que deja
la altura de mayuscula en 46 unidades, de modo que cualquier fuente entra en la
banda sin tocar nada mas.

Dependencias: `fonttools`, `cairosvg`, `pillow`, `numpy`.
