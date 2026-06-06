/*script para login*/
    function togglePassword() {
        const input = document.getElementById('contrasena');
        const icono = document.getElementById('icono-ojo');
        if (input.type === 'password') {
            input.type = 'text';
            icono.className = 'bi bi-eye-slash';
        } else {
            input.type = 'password';
            icono.className = 'bi bi-eye';
        }
    }
/*Script mesas*/
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

/*Script para las reservas admin*/
    let reservaIdActual = null;

    function abrirModalCancelar(boton) {
        reservaIdActual = boton.dataset.plato;
        document.getElementById('modal-cancelar').style.display = 'flex';
    }

    function cerrarModal() {
        reservaIdActual = null;
        document.getElementById('modal-cancelar').style.display = 'none';
        document.getElementById('motivo-cancelacion').value = '';
    }

    async function confirmarCancelacion() {
        if (!reservaIdActual) return;
        const motivo = document.getElementById('motivo-cancelacion').value;
        const res = await fetch(`/api/reservas/${reservaIdActual}/cancelar-cliente`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ motivo })
        });
        if (res.ok) {
            cerrarModal();
            location.reload();
        } else {
            alert('No se pudo cancelar la reserva.');
        }
    }

    document.getElementById('buscador').addEventListener('input', function() {
        const filtro = this.value.toLowerCase();
        document.querySelectorAll('#tabla-reservas tbody tr').forEach(fila => {
            fila.style.display = fila.textContent.toLowerCase().includes(filtro) ? '' : 'none';
        });
    });

    /*Script para los cambios de menu de parte del admin*/
        function abrirModalAgregar() {
        document.getElementById('modal-plato-titulo').textContent = '+ AGREGAR PLATO';
        document.getElementById('plato-id').value = '';
        document.getElementById('plato-nombre').value = '';
        document.getElementById('plato-precio').value = '';
        document.getElementById('plato-descripcion').value = '';
        document.getElementById('plato-restricciones').value = '';
        document.getElementById('plato-categoria').value = '';
        document.getElementById('modal-plato').style.display = 'flex';
    }

    function abrirModalEditar(plato) {
        document.getElementById('modal-plato-titulo').textContent = 'EDITAR PLATO';
        document.getElementById('plato-id').value = plato.id;
        document.getElementById('plato-nombre').value = plato.nombre;
        document.getElementById('plato-precio').value = plato.precio;
        document.getElementById('plato-descripcion').value = plato.descripcion || '';
        document.getElementById('plato-categoria').value = plato.categoria_id;
        document.getElementById('modal-plato').style.display = 'flex';
    }

    function cerrarModalPlato() {
        document.getElementById('modal-plato').style.display = 'none';
    }

    function previewImagen(input) {
        const preview = document.getElementById('imagen-preview');
        if (input.files && input.files[0]) {
            const reader = new FileReader();
            reader.onload = e => {
                preview.innerHTML = `<img src="${e.target.result}" style="max-width:100%;border-radius:8px;">`;
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    async function guardarPlato() {
        const id = document.getElementById('plato-id').value;
        const datos = {
            nombre: document.getElementById('plato-nombre').value,
            precio: document.getElementById('plato-precio').value,
            descripcion: document.getElementById('plato-descripcion').value,
            categoria_id: document.getElementById('plato-categoria').value,
        };
        const url = id ? `/api/admin/menu/${id}` : '/api/admin/menu';
        const method = id ? 'PUT' : 'POST';
        const res = await fetch(url, {
            method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(datos)
        });
        if (res.ok) { cerrarModalPlato(); location.reload(); }
        else alert('Error al guardar el plato.');
    }

    async function eliminarPlato(boton) {
        const id = boton.dataset.id;
        if (!confirm('¿Seguro que querés eliminar este plato?')) return;
            const res = await fetch(`/api/admin/menu/${id}`, { method: 'DELETE' });
        if (res.ok) location.reload();
        else alert('Error al eliminar el plato.');
    }

/*Edicion de las resenas del admin*/
    async function cambiarEstado(id, estado) {
        const res = await fetch(`/api/admin/resenas/${id}/estado`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ estado })
        });
        if (res.ok) location.reload();
        else alert('Error al cambiar el estado.');
    }

    async function eliminarResena(id) {
        if (!confirm('¿Seguro que querés eliminar esta reseña?')) return;
        const res = await fetch(`/api/admin/resenas/${id}`, { method: 'DELETE' });
        if (res.ok) location.reload();
        else alert('Error al eliminar la reseña.');
    }

/*SCRIPT PARA CONFIGURACION*/

    function mostrarTab(tab, boton) {
        document.querySelectorAll('.admin-config-section').forEach(s => s.style.display = 'none');
        document.querySelectorAll('.admin-tab').forEach(b => b.classList.remove('active'));
        document.getElementById('tab-' + tab).style.display = 'block';
        boton.classList.add('active');
    }

    function previewBanner(input) {
        if (input.files && input.files[0]) {
            const reader = new FileReader();
            reader.onload = e => document.getElementById('preview-banner').src = e.target.result;
            reader.readAsDataURL(input.files[0]);
        }
    }

    function guardarGeneral() {
        alert('Función de guardar configuración general pendiente de implementar en el backend.');
    }

    function guardarApariencia() {
        alert('Función de guardar apariencia pendiente de implementar en el backend.');
    }