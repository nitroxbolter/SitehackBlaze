<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciamento</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #0a0a0a;
        }
        .container {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 800px; /* Largura da caixa */
        }
        h1 {
            text-align: center;
            font-size: 1.3em;
            background-color: red; /* Tarja vermelha */
            color: white; /* Texto branco */
            padding: 10px; /* Espaçamento interno */
            margin: -15px -15px 15px; /* Margem negativa para sobrepor a borda */
            border-radius: 8px 8px 0 0; /* Bordas arredondadas apenas no topo */
        }
        .input-container {
            display: flex; /* Usar flexbox para dispor os campos lado a lado */
            justify-content: space-between; /* Espaço entre os campos */
            margin-bottom: 15px; /* Espaço inferior */
        }
        .input-item {
            flex: 1; /* Cada campo ocupará espaço igual */
            margin-right: 10px; /* Espaço entre os campos */
        }
        .input-item:last-child {
            margin-right: 0; /* Remove margem do último item */
        }
        label {
            display: block;
            margin-top: 8px;
            font-size: 1.1em; /* Aumenta a fonte */
            font-weight: bold; /* Texto em negrito */
        }
        input[type="number"] {
            width: 100%; /* Largura total do campo */
            padding: 6px;
            margin-top: 4px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 0.8em;
            -moz-appearance: textfield; /* Remove as setas no Firefox */
        }
        /* Remove as setas de inputs de número */
        input[type="number"]::-webkit-inner-spin-button,
        input[type="number"]::-webkit-outer-spin-button {
            -webkit-appearance: none; /* Remove as setas no Chrome e Safari */
            margin: 0; /* Remove margens */
        }
        button {
            width: 38%; /* Largura dos botões reduzida para 38% */
            padding: 6px;
            margin-top: 10px;
            border: none;
            border-radius: 4px;
            background-color: #28a745;
            color: white;
            cursor: pointer;
            font-size: 0.8em;
            display: block; /* Tornar o botão um bloco */
            margin-left: auto; /* Alinhamento central */
            margin-right: auto; /* Alinhamento central */
        }
        button:hover {
            background-color: #218838;
        }
        .clear-button {
            background-color: #dc3545;
        }
        .clear-button:hover {
            background-color: #c82333;
        }
        table {
            width: 100%; /* Largura total da tabela */
            border-collapse: collapse;
            font-size: 0.7em;
            background-color: #242121;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 5px;
            text-align: center;
            color: white;
        }
        #resultTable1, #resultTable2 {
            display: none;
        }
        .alert {
            color: red;
            font-size: 0.8em;
            margin-top: 10px;
            text-align: center;
        }
        .profit-banner {
            background-color: #28a745; /* Tarja verde */
            color: white; /* Texto branco */
            padding: 10px;
            text-align: center;
            margin-top: 10px;
            display: none; /* Ocultar inicialmente */
            border-radius: 4px;
        }
        .tables-container {
            max-height: 300px; /* Altura máxima do contêiner */
            overflow-y: auto; /* Habilita a rolagem vertical */
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Gerenciamento</h1>
        <div class="input-container">
            <div class="input-item">
                <label for="banca">Banca (R$):</label>
                <input type="number" id="banca" name="banca" step="0.01" required>
            </div>
            <div class="input-item">
                <label for="entradas">Número de Tiros:</label>
                <input type="number" id="entradas" name="entradas" required>
            </div>
            <div class="input-item">
                <label for="brancos">Meta de Brancos:</label>
                <input type="number" id="brancos" name="brancos" min="0" value="0" required>
            </div>
        </div>
        <button type="button" onclick="calcularTabela()">Calcular</button>
        <button type="button" class="clear-button" onclick="limparTabela()">Limpar</button>

        <div class="alert" id="alertMessage"></div> <!-- Mensagem de alerta -->
        <div class="profit-banner" id="profitMessage"></div> <!-- Tarja verde para lucro -->
        <div class="profit-banner" id="profit30DaysMessage"></div> <!-- Tarja verde para lucro 30 dias -->
        <div class="profit-banner" id="totalProfitMessage"></div> <!-- Tarja verde para lucro total da meta de brancos -->

        <div class="tables-container">
    <table id="resultTable1">
        <thead>
            <tr>
                <th>Entrada</th>
                <th>Aposta (R$)</th>
                <th>Total Acumulado (R$)</th>
            </tr>
        </thead>
        <tbody></tbody>
    </table>
</div>


<script>
    function calcularTabela() {
        const banca = parseFloat(document.getElementById('banca').value);
        const entradas = parseInt(document.getElementById('entradas').value);
        const brancos = parseInt(document.getElementById('brancos').value); // Novo campo para brancos
        const multiplicador = 1.08;

        let tableBody1 = document.querySelector('#resultTable1 tbody');
        tableBody1.innerHTML = ''; // Limpa a tabela
        document.getElementById('alertMessage').innerText = ''; // Limpa a mensagem de alerta
        document.getElementById('profitMessage').style.display = 'none'; // Oculta a tarja verde inicialmente
        document.getElementById('profit30DaysMessage').style.display = 'none'; // Oculta a tarja verde de lucro 30 dias
        document.getElementById('totalProfitMessage').style.display = 'none'; // Oculta a tarja verde de lucro total da meta de brancos

        let aposta = banca / ((Math.pow(multiplicador, entradas) - 1) / (multiplicador - 1));
        let total = 0;

        if (aposta < 0.20) {
            document.getElementById('alertMessage').innerText = 'A banca não suporta o valor mínimo de entrada de R$ 0,20.';
            return; // Sai da função se a aposta for menor que 0.20
        }

        for (let i = 1; i <= entradas; i++) {
            if (total + aposta > banca) {
                let row = document.createElement('tr');
                row.innerHTML = `<td colspan="3">Excedeu a banca</td>`;
                tableBody1.appendChild(row);
                break;
            }

            total += aposta;

            let row = document.createElement('tr');
            row.innerHTML = `
                <td>${i}</td>
                <td>${aposta.toFixed(2)}</td>
                <td>${total.toFixed(2)}</td>
            `;

            tableBody1.appendChild(row);
            aposta *= multiplicador;
        }

        document.getElementById('resultTable1').style.display = 'table';

        // Cálculo do lucro por brancos
        const lucroPorBranco = (parseFloat(document.getElementById('banca').value) / ((Math.pow(multiplicador, entradas) - 1) / (multiplicador - 1))) * 14;

        // Cálculo do lucro total pela meta de brancos
        const totalLucroMetaBrancos = lucroPorBranco * brancos;

        // Cálculo do lucro estimado em 30 dias com base no lucro total da meta
        const lucro30Dias = totalLucroMetaBrancos * 30; // Aqui você calcula o lucro total da meta x 30 dias

        document.getElementById('profitMessage').innerText = `Lucro por branco: R$ ${lucroPorBranco.toFixed(2)}`;
        document.getElementById('profitMessage').style.display = 'block';
        document.getElementById('profit30DaysMessage').innerText = `Lucro estimado em 30 dias: R$ ${lucro30Dias.toFixed(2)}`;
        document.getElementById('profit30DaysMessage').style.display = 'block';
        document.getElementById('totalProfitMessage').innerText = `Lucro total pela meta de brancos: R$ ${totalLucroMetaBrancos.toFixed(2)}`;
        document.getElementById('totalProfitMessage').style.display = 'block';
    }

    function limparTabela() {
        document.getElementById('banca').value = '';
        document.getElementById('entradas').value = '';
        document.getElementById('brancos').value = 0; // Limpa o campo de brancos
        document.getElementById('resultTable1').style.display = 'none';
        document.querySelector('#resultTable1 tbody').innerHTML = '';
        document.getElementById('alertMessage').innerText = '';
        document.getElementById('profitMessage').style.display = 'none'; // Oculta a tarja verde
        document.getElementById('profit30DaysMessage').style.display = 'none'; // Oculta a tarja verde de lucro 30 dias
        document.getElementById('totalProfitMessage').style.display = 'none'; // Oculta a tarja verde de lucro total da meta de brancos
    }
</script>


</body>
</html>
