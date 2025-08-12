// CONFIGURA TU USUARIO Y REPO
const usuario = "eliasmonzon"; // ejemplo: "eliasmonzon"
const repo = "pico_bot";// ejemplo: "pico_bot"

const contenedorLecciones = document.querySelector(".lessons-container");
const contenedorPDF = document.querySelector(".doc-section");

// Orden específico de archivos
let orden = ["Pico_bot"];
for (let i = 1; i <= 99; i++) {
    orden.push(`Leccion_${i}`);
}
orden.push("motores_y_servo", "mando", "ssd1306");

function formatearNombre(nombre) {
    // Quitar extensión
    let base = nombre.replace(/\.[^/.]+$/, "");
    // Reemplazar "Leccion_" por "Lección "
    base = base.replace(/^Leccion_/, "Lección ");
    // Reemplazar guiones bajos por espacios
    base = base.replace(/_/g, " ");
    // Mayúscula en primera letra
    base = base.charAt(0).toUpperCase() + base.slice(1);
    return base;
}

function forzarDescarga(url, nombre) {
    fetch(url)
        .then(res => res.blob())
        .then(blob => {
            const enlace = document.createElement("a");
            enlace.href = URL.createObjectURL(blob);
            enlace.download = nombre;
            document.body.appendChild(enlace);
            enlace.click();
            enlace.remove();
        });
}

fetch(`https://api.github.com/repos/${usuario}/${repo}/contents/`)
    .then(response => response.json())
    .then(data => {
        let archivosPy = [];
        let archivosPDF = [];

        data.forEach(file => {
            if (file.name.endsWith(".py")) {
                archivosPy.push({
                    nombre: file.name.replace(/\.[^/.]+$/, ""),
                    url: file.download_url
                });
            } else if (file.name.endsWith(".pdf")) {
                archivosPDF.push({
                    nombre: file.name.replace(/\.[^/.]+$/, ""),
                    url: file.download_url
                });
            }
        });

        // Ordenar según lista
        archivosPy.sort((a, b) => {
            let ia = orden.indexOf(a.nombre.replace(/\.[^/.]+$/, ""));
            let ib = orden.indexOf(b.nombre.replace(/\.[^/.]+$/, ""));
            ia = ia === -1 ? Number.MAX_SAFE_INTEGER : ia;
            ib = ib === -1 ? Number.MAX_SAFE_INTEGER : ib;
            return ia - ib;
        });

        // Crear botones para .py
        archivosPy.forEach(archivo => {
            let boton = document.createElement("a");
            boton.href = "#";
            boton.className = "boton";
            boton.innerHTML = `<i class="fas fa-book"></i> ${formatearNombre(archivo.nombre)}`;
            boton.addEventListener("click", e => {
                e.preventDefault();
                forzarDescarga(archivo.url, archivo.nombre + ".py");
            });
            contenedorLecciones.appendChild(boton);
        });

        // Crear botón para cada PDF
        archivosPDF.forEach(pdf => {
            let boton = document.createElement("a");
            boton.href = "#";
            boton.className = "boton pdf-btn";
            boton.innerHTML = `<i class="fas fa-file-pdf"></i> ${formatearNombre(pdf.nombre)}`;
            boton.addEventListener("click", e => {
                e.preventDefault();
                forzarDescarga(pdf.url, pdf.nombre + ".pdf");
            });
            contenedorPDF.appendChild(boton);
        });
    })
    .catch(error => {
        console.error("Error al cargar archivos:", error);
        contenedorLecciones.innerHTML = "<p>No se pudieron cargar los archivos.</p>";
    });
