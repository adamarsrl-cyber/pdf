// Buscador interno. Recorre CATALOGO (definido en catalogo.js) y muestra
// resultados por título de libro, capítulo o palabra clave.
// No requiere servidor: todo corre en el navegador del visitante.

function normalizar(txt) {
  return txt
    .toString()
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '');
}

function construirIndiceBusqueda() {
  const indice = [];

  CATALOGO.libro_completo.forEach(e => indice.push({
    tipo: 'Libro completo', titulo: e.titulo, ref: e.libro,
    disponible: e.disponible, archivo: e.archivo, id: e.id
  }));

  CATALOGO.por_capitulo.forEach(e => indice.push({
    tipo: 'Por capítulo', titulo: `${e.libro} ${e.capitulo}`, ref: e.libro,
    disponible: e.disponible, archivo: e.archivo, id: e.id
  }));

  CATALOGO.tematicos.forEach(e => indice.push({
    tipo: 'Panorama temático', titulo: e.titulo, ref: e.libros.join(', '),
    disponible: e.disponible, archivo: e.archivo, id: e.id
  }));

  ['ayudas_solicitadas', 'ayudas_biblicas', 'parabolas', 'bienaventuranzas'].forEach(clave => {
    CATALOGO[clave].forEach(e => indice.push({
      tipo: e.categoria, titulo: e.titulo, ref: e.categoria,
      disponible: e.disponible, archivo: e.archivo, id: e.id
    }));
  });

  return indice;
}

let INDICE_BUSQUEDA = null;

function buscarEnCatalogo(consulta, maximo = 40) {
  if (!INDICE_BUSQUEDA) INDICE_BUSQUEDA = construirIndiceBusqueda();
  const q = normalizar(consulta.trim());
  if (q.length < 2) return [];
  return INDICE_BUSQUEDA
    .filter(item => normalizar(item.titulo).includes(q) || normalizar(item.ref).includes(q))
    .slice(0, maximo);
}

function iniciarBuscador(inputId, resultadosId) {
  const input = document.getElementById(inputId);
  const caja = document.getElementById(resultadosId);
  if (!input || !caja) return;

  input.addEventListener('input', () => {
    const resultados = buscarEnCatalogo(input.value);
    if (input.value.trim().length < 2) {
      caja.innerHTML = '';
      return;
    }
    if (resultados.length === 0) {
      caja.innerHTML = '<p class="nota-formulario">No se encontraron estudios con esa palabra. Prueba con el nombre de un libro bíblico, por ejemplo "Juan" o "Salmos".</p>';
      return;
    }
    caja.innerHTML = resultados.map(r => `
      <div class="resultado-item">
        <div>
          <span class="etiqueta">${r.tipo}</span><br>
          <strong>${r.titulo}</strong>
        </div>
        ${r.disponible
          ? `<a class="boton boton-primario" href="visor.html?archivo=${encodeURIComponent(r.archivo)}&titulo=${encodeURIComponent(r.titulo)}">Leer en línea</a>`
          : etiquetaEstado(false)}
      </div>
    `).join('');
  });
}
