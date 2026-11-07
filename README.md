# Portal de Estudios Bíblicos RVR1960

Sitio web estático (HTML/CSS/JS puro, sin servidor) para publicar y leer en
línea los estudios bíblicos en PDF generados con la app de escritorio del
proyecto **Sistema de Estudios Bíblicos RVR1960**.

## 1. Cómo probarlo en tu computadora

No necesitas instalar nada especial. Dos formas:

- **La más simple:** doble clic en `index.html` y se abre en el navegador.
  (El buscador y el catálogo funcionan; algunas funciones de formulario
  pueden pedir un servidor local, ver más abajo).
- **Recomendada:** si tienes Python instalado, abre una terminal en esta
  carpeta y ejecuta:
  ```
  python3 -m http.server 8000
  ```
  Luego abre `http://localhost:8000` en el navegador.

## 2. Cómo publicarlo gratis en internet

Cualquiera de estas tres opciones aloja sitios estáticos **sin costo**:

### Opción A — Cloudflare Pages (recomendada, muy rápida en Bolivia/Latam)
1. Crea una cuenta gratuita en https://pages.cloudflare.com
2. Sube esta carpeta completa (arrastrando los archivos) o conéctala a un
   repositorio de GitHub.
3. Cloudflare te da una dirección como `tu-sitio.pages.dev` de inmediato.
4. Opcional: puedes conectar un dominio propio (`.org`, `.com`) más adelante,
   también gratis si usas el dominio gratuito que da Cloudflare.

### Opción B — GitHub Pages
1. Crea una cuenta gratuita en https://github.com
2. Crea un repositorio nuevo (por ejemplo `estudios-biblicos`).
3. Sube todos los archivos de esta carpeta al repositorio.
4. Ve a **Settings → Pages**, elige la rama `main` y la carpeta raíz.
5. En un par de minutos el sitio queda publicado en
   `https://tu-usuario.github.io/estudios-biblicos/`.

### Opción C — Netlify
1. Crea una cuenta gratuita en https://netlify.com
2. Arrastra esta carpeta directamente a la web de Netlify ("Deploy manually").
3. Netlify publica el sitio al instante con una dirección gratuita.

En cualquiera de las tres, cada vez que agregues nuevos PDFs solo tienes que
volver a subir la carpeta (o hacer `git push` si usas GitHub).

## 3. Cómo agregar un nuevo estudio en PDF (lo más importante)

El catálogo completo (1427 estudios: 66 libros completos — 39 del Antiguo
Testamento y 27 del Nuevo Testamento —, 1189 capítulos agrupados por
testamento y libro, 10 estudios temáticos, 52 estudios de las parábolas,
9 estudios de las bienaventuranzas, 33 ayudas bíblicas solicitadas y 68
ayudas bíblicas) ya está generado en `js/catalogo.js`. Cada estudio tiene
una ruta de archivo fija, por ejemplo:

```
pdfs/por-capitulo/juan/juan-3.pdf
pdfs/libro-completo/genesis.pdf
pdfs/parabolas/parabola-1.pdf
pdfs/bienaventuranzas/bienaventuranza-1.pdf
pdfs/ayudas-solicitadas/ayuda-solicitada-1.pdf
pdfs/ayudas-biblicas/ayuda-biblica-1.pdf
```

Para publicar un estudio nuevo:

1. Exporta el PDF desde la app de escritorio (`estudio_biblico_app`).
2. Ponle exactamente el nombre de archivo indicado arriba y colócalo en la
   carpeta `pdfs/` correspondiente (respetando mayúsculas/minúsculas).
3. Abre `js/catalogo.js`, busca la entrada de ese estudio (por su `id` o
   `titulo`) y cambia `"disponible": false` por `"disponible": true`.
4. Vuelve a subir los archivos al hosting (paso 2). Listo — el estudio
   aparecerá automáticamente en el buscador, en la lista de capítulos y
   se podrá leer en línea, sin tocar ningún archivo HTML.

Si en el futuro cambias la estructura del catálogo (agregas una categoría
nueva, por ejemplo), puedes regenerar `js/catalogo.js` editando y
volviendo a correr `gen_catalogo.py` (incluido en el proyecto original que
armó Claude).

## 4. Peso de los PDFs

El catálogo está pensado para archivos de ~900 KB cada uno. Con 1427
estudios eso es un máximo teórico de ~1.3 GB si algún día se sube todo el
catálogo — muy por debajo de los límites gratuitos de Cloudflare Pages,
GitHub Pages o Netlify (todos permiten varios GB gratis). No hay que
preocuparse por el espacio mientras el catálogo se va completando poco a
poco.

## 5. Formularios que necesitan un servicio externo gratuito

Este sitio es 100% estático (no tiene servidor propio), así que tres
funciones necesitan conectarse a un servicio externo **gratuito** para
funcionar de verdad con todos los visitantes:

| Función | Archivo | Servicio gratuito sugerido |
|---|---|---|
| Formulario de contacto | `contacto.html` | [Formspree](https://formspree.io) (plan gratuito, 50 mensajes/mes) — reemplazar `TU_ID_DE_FORMSPREE` en el `action` del formulario |
| Boletín por correo | `comunidad.html` | [Buttondown](https://buttondown.email) o Mailchimp (planes gratuitos) |
| Muro de oración compartido entre visitantes | `comunidad.html` | Hoy guarda las peticiones solo en el navegador de cada visitante (`localStorage`), como demostración. Para que todos vean las mismas peticiones hace falta una base de datos simple gratuita, por ejemplo Google Sheets + Formspree, o Firebase (plan gratuito) |
| Comentarios en cada estudio (`visor.html`) | — | [Giscus](https://giscus.app) (gratuito, usa GitHub Discussions) es la opción más simple para un sitio ya alojado en GitHub Pages |

Ninguno de estos es obligatorio para publicar el sitio: sin conectarlos,
el catálogo de estudios, el buscador y la lectura de PDFs funcionan
igual. Son mejoras para cuando haya tiempo de configurarlas.

## 6. Estructura del proyecto

```
index.html          Inicio (héroe, declaración de fe, buscador, redes)
estudios.html        Catálogo por libro/capítulo/tema/ayudas
visor.html            Lector de PDF en línea
multimedia.html      Audio, video, infografías (espacios reservados)
comunidad.html       Devocional, muro de oración, boletín, ofrendas
contacto.html         Formulario de contacto y redes sociales
css/estilos.css       Estilos de todo el sitio
js/catalogo.js         Datos de los 1427 estudios (generado por gen_catalogo.py)
js/componentes.js    Cabecera y pie de página compartidos
js/buscador.js         Buscador interno
js/estudios.js         Lógica de la página de estudios
js/main.js              Utilidades varias
pdfs/                     Aquí van los archivos PDF reales, organizados por carpeta
gen_catalogo.py       Script que regenera catalogo.js si cambia la estructura
```
