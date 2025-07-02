document.addEventListener('DOMContentLoaded', function () {
    const estadoSelect = document.getElementById('id_estado');
    const cidadeSelect = document.getElementById('id_cidade');

    if (!estadoSelect || !cidadeSelect) return;

    estadoSelect.addEventListener('change', function () {
        const estadoId = this.value;

        fetch(`/ajax/carrega-cidades/?estado=${estadoId}`)
            .then(response => response.json())
            .then(data => {
                cidadeSelect.innerHTML = '';

                // Adiciona uma opção vazia
                const emptyOption = new Option('---------', '');
                cidadeSelect.add(emptyOption);

                data.forEach(function (cidade) {
                    const option = new Option(cidade.nome, cidade.id);
                    cidadeSelect.add(option);
                });
            });
    });
});