document.addEventListener("DOMContentLoaded", () => {
    const inputFecha = document.getElementById("fecha");
    const inputHorario = document.getElementById("horario");
    const inputCantidad = document.getElementById("cantidad_personas");
    const inputMesaId = document.getElementById("mesa_id");
    const textoMesaSeleccionada = document.getElementById("textoMesaSeleccionada");

    const botonesMesa = document.querySelectorAll(".mesa");

    if (!inputMesaId || botonesMesa.length === 0) {
        return;
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
});