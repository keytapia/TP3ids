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

function togglePassword(inputId, iconId) {

    const input = document.getElementById(inputId);
    const icono = document.getElementById(iconId);

    if (input.type === 'password') {
        input.type = 'text';
        icono.className = 'bi bi-eye-slash';
    } else {
        input.type = 'password';
        icono.className = 'bi bi-eye';
    }
}
document.addEventListener("DOMContentLoaded", () => {
   const slider = document.querySelector(".resenas-slider");
   const nextBtn = document.querySelector(".next-btn");
   const prevBtn = document.querySelector(".prev-btn");

   if (!slider || !nextBtn || !prevBtn) return;

   const card = document.querySelector(".resena-card");

   if (!card) return;

   const gap = 20; 
   const scrollAmount = card.offsetWidth * 3 + gap * 3;

   nextBtn.addEventListener("click", () => {
       slider.scrollBy({
           left: scrollAmount,
           behavior: "smooth"
       });
   });

   prevBtn.addEventListener("click", () => {
       slider.scrollBy({
           left: -scrollAmount,
           behavior: "smooth"
       });
   });
});
