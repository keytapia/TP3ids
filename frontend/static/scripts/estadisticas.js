document.addEventListener("DOMContentLoaded", () => {

    const canvasHorarios = document.getElementById("graficoHorarios");
    const canvasDias = document.getElementById("graficoDias");

    if (canvasHorarios) {

        const labels = JSON.parse(
            canvasHorarios.dataset.labels
        );

        const values = JSON.parse(
            canvasHorarios.dataset.values
        );

        new Chart(canvasHorarios, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    data: values
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: false
                    }
                },
                responsive: true
            }
        });
    }

    if (canvasDias) {

        const labels = JSON.parse(
            canvasDias.dataset.labels
        );

        const values = JSON.parse(
            canvasDias.dataset.values
        );

        new Chart(canvasDias, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    data: values
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: false
                    }
                },
                responsive: true
            }
        });
    }

});