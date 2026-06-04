document.addEventListener("DOMContentLoaded", () => {
    const inputFecha = document.getElementById("fecha");
    const inputHorario = document.getElementById("horario");
    const inputCantidad = document.getElementById("cantidad_personas");
    const inputMesaId = document.getElementById("mesa_id");
    const textoMesaSeleccionada = document.getElementById("textoMesaSeleccionada");

    const botonesMesa = document.querySelectorAll(".mesa");

    if (!inputFecha || !inputHorario || !inputCantidad || !inputMesaId || botonesMesa.length === 0) {
        console.error("No se encontraron elementos necesarios para el mapa de mesas.");
        return;
    }

    function limpiarSeleccion() {
        inputMesaId.value = "";

        if (textoMesaSeleccionada) {
            textoMesaSeleccionada.textContent = "Todavía no seleccionaste ninguna mesa.";
        }

        botonesMesa.forEach((boton) => {
            boton.classList.remove("seleccionada");
        });
    }

    function bloquearTodasLasMesas() {
        botonesMesa.forEach((boton) => {
            boton.disabled = true;
            boton.classList.remove("disponible", "reservada", "no-apta", "seleccionada");
            boton.classList.add("no-apta");
            boton.title = "Primero seleccioná fecha, horario y cantidad de personas.";
        });
    }

    function actualizarMesaVisual(boton, mesa) {
        boton.classList.remove("disponible", "reservada", "no-apta", "seleccionada");

        boton.disabled = false;
        boton.title = "";

        const textoCapacidad = boton.querySelector("small");

        if (textoCapacidad) {
            textoCapacidad.textContent = `${mesa.capacidad} personas`;
        }

        if (mesa.reservada) {
            boton.classList.add("reservada");
            boton.disabled = true;
            boton.title = "Esta mesa ya está reservada.";
            return;
        }

        if (!mesa.capacidad_suficiente) {
            boton.classList.add("no-apta");
            boton.disabled = true;
            boton.title = "La capacidad de esta mesa no alcanza.";
            return;
        }

        if (mesa.estado !== "disponible") {
            boton.classList.add("reservada");
            boton.disabled = true;
            boton.title = "Esta mesa no está disponible.";
            return;
        }

        boton.classList.add("disponible");
    }

    async function cargarDisponibilidadMesas() {
        const fecha = inputFecha.value;
        const horario = inputHorario.value;
        const cantidadPersonas = inputCantidad.value;

        limpiarSeleccion();

        if (!fecha || !horario || !cantidadPersonas) {
            bloquearTodasLasMesas();
            return;
        }

        try {
            const params = new URLSearchParams({
                fecha: fecha,
                horario: horario,
                cantidad_personas: cantidadPersonas
            });
            const url = `http://127.0.0.1:5000/api/mesas-disponibles?${params.toString()}`;

            const respuesta = await fetch(url);

            if (!respuesta.ok) {
                console.error("Error al consultar disponibilidad:", respuesta.status);
                bloquearTodasLasMesas();
                return;
            }

            const mesas = await respuesta.json();

            botonesMesa.forEach((boton) => {
                const idMesa = Number(boton.dataset.mesa);
                const mesa = mesas.find((m) => Number(m.id) === idMesa);

                if (mesa) {
                    actualizarMesaVisual(boton, mesa);
                }
            });

        } catch (error) {
            console.error("Error al cargar mesas:", error);
            bloquearTodasLasMesas();
        }
    }

    botonesMesa.forEach((boton) => {
        boton.addEventListener("click", () => {
            if (boton.disabled) {
                return;
            }

            botonesMesa.forEach((b) => {
                b.classList.remove("seleccionada");
            });

            boton.classList.add("seleccionada");

            const idMesa = boton.dataset.mesa;
            const nombreMesa = boton.querySelector("span")?.textContent || "Mesa";
            const capacidadMesa = boton.querySelector("small")?.textContent || "";

            inputMesaId.value = idMesa;

            if (textoMesaSeleccionada) {
                textoMesaSeleccionada.textContent = `${nombreMesa} seleccionada - ${capacidadMesa}.`;
            }

            console.log("Mesa seleccionada:", idMesa);
        });
    });

    inputFecha.addEventListener("change", cargarDisponibilidadMesas);
    inputHorario.addEventListener("change", cargarDisponibilidadMesas);
    inputCantidad.addEventListener("change", cargarDisponibilidadMesas);

    bloquearTodasLasMesas();
});