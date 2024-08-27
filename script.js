document.addEventListener('DOMContentLoaded', () => {
    const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
    const targetUrl = 'https://www.tipminer.com/historico/blaze/double?limit=1500&t=1723641349463&subject=filter';
    const url = proxyUrl + targetUrl;
    const resultadoDiv = document.getElementById('resultado');
    const fetchDataButton = document.getElementById('fetchData');

    fetchDataButton.addEventListener('click', () => {
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Rede não está ok');
                }
                return response.json();
            })
            .then(data => {
                // Displaying data in a readable format
                resultadoDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
            })
            .catch(error => {
                console.error('Erro ao buscar dados:', error);
                resultadoDiv.innerHTML = 'Erro ao buscar dados';
            });
    });
});
