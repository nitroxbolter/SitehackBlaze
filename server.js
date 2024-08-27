const express = require('express');
const request = require('request');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/api/data', (req, res) => {
    const url = 'https://www.tipminer.com/historico/blaze/double?limit=1500&t=1723641349463&subject=filter';
    request({ url, json: true }, (error, response, body) => {
        if (error) {
            return res.status(500).json({ error: 'Erro ao buscar dados' });
        }
        res.json(body);
    });
});

app.listen(port, () => {
    console.log(`Servidor proxy rodando na porta ${port}`);
});
