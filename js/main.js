function loadComponent(selector, archivo) {
    fetch(archivo)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error al cargar el archivo: ${response.status}`);
            }
            return response.text();
        })
        .then(html => {
            const elemento = document.querySelector(selector);
            if (elemento) {
                elemento.innerHTML = html;
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
}

function goToSection(section) {
    location.href = `/Proyecto.html#${section}`;
}

