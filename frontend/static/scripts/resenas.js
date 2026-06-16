document.addEventListener("DOMContentLoaded", () => {

    const slider = document.querySelector(".resenas-slider");
    const nextBtn = document.querySelector(".next-btn");
    const prevBtn = document.querySelector(".prev-btn");

    if (!slider || !nextBtn || !prevBtn) return;

    const card = document.querySelector(".resena-card");

    if (!card) return;

    const scrollAmount = card.offsetWidth +25;

    nextBtn.addEventListener("click", () => {
        slider.scrollBy({
            left: scrollAmount,
            behavior: "smooth"
        })
    })

    prevBtn.addEventListener("click", () => {
        slider.scrollBy({
            left: -scrollAmount,
            behavior: "smooth"
        })
    })
})