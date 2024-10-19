<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>White Hunter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-image: url('arquivos/telahome.png');
            background-size: cover;
            background-position: center;
            color: #000000;
            display: flex;
            height: 100vh;
        }
        .menu {
            width: 200px;
            background-color: rgba(255, 255, 255, 0.8);
            border-right: 2px solid #0056b3;
            position: fixed;
            top: 0;
            left: 0;
            bottom: 0;
            overflow-y: auto;
            padding: 10px;
            transition: background-color 0.3s, color 0.3s;
            text-align: center; /* Adicionado para centralizar o texto */
        }
        
        .menu ul {
            list-style-type: none; /* Remove a bolinha da lista */
            padding: 0; /* Remove o padding padrão */
        }
        .menu li {
            margin-bottom: 10px; /* Adiciona espaçamento entre os itens */
        }
        .menu a {
            text-decoration: none;
            color: #0056b3;
            display: block;
            padding: 10px;
            border-radius: 5px; /* Adiciona borda arredondada aos links */
        }
        .menu a:hover {
            background-color: #e9ecef;
        }
        .menu table {
            width: 100%;
            border-collapse: collapse;
        }
        .menu th {
            background-color: #0056b3;
            color: white;
            padding: 10px;
        }
        .menu td {
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        .menu td a {
            text-decoration: none;
            color: #0056b3;
            display: block;
        }
        .menu td a:hover {
            background-color: #e9ecef;
        }
        .main-content {
            margin-left: 220px;
            padding: 20px;
            flex-grow: 1;
        }
        .theme-toggle {
            background-color: rgb(47, 47, 218); /* Cor de fundo roxa */
            color: white; /* Cor do texto */
            border: none; /* Remova a borda */
            padding: 10px 20px; /* Ajuste o preenchimento */
            cursor: pointer; /* Cursor em forma de mão ao passar sobre o botão */
            border-radius: 5px; /* Bordas arredondadas (opcional) */
            transition: background-color 0.3s; /* Transição suave ao passar o mouse */
            position: absolute; /* Para permitir o posicionamento absoluto */
            top: 20px; /* Distância do topo */
            right: 10px; /* Distância da direita */
        }
        
        .theme-toggle:hover {
            background-color: rgb(47, 47, 218); /* Cor de fundo ao passar o mouse */
        }
        .theme-toggle.transparent {
            background-color: rgba(255, 255, 255, 0);
            color: #007bff;
            border: 2px solid #007bff;
        }
        .frame {
            border: 2px solid #0056b3;
            padding: 20px;
            border-radius: 10px;
            background-color: rgba(240, 240, 240, 0.8);
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s, border-color 0.3s;
            text-align: center;
        }
        h1 {
            color: #0056b3;
            margin: 20px 0;
        }
        .frame img {
            display: block;
            margin: 0 auto;
            max-width: 100px;
        }
        .frame p {
            margin-bottom: 20px;
        }
        .button-container {
            text-align: center;
            margin-bottom: 20px;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            margin: 0 10px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #0056b3;
        }
        table.results-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #ffffff;
            color: #000000;
            transition: color 0.3s;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #0056b3;
            color: white;
        }
        tbody tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        tbody tr:nth-child(odd) {
            background-color: #ffffff;
        }
        .result-input {
            background-color: #e9ecef;
            color: #000000;
        }
        .result6 {
            background-color: #28a745;
            color: #000000;
        }
        .result10 {
            background-color: #ffc107;
            color: #000000;  
        }
        .result12 {
            background-color: #dc3545;
            color: #000000;       
        }
        .pago-cell {
            cursor: pointer;
        }
        .dark-theme body {
            background-color: #343a40;
            color: #ffffff;
        }
        .dark-theme .menu {
            background-color: rgba(0, 0, 0, 0.8);
            border-right: 2px solid #007bff;
        }
        .dark-theme .menu th {
            background-color: #007bff;
        }
        .dark-theme .results-table th {
            background-color: rgb(47, 47, 218);
        }
        .dark-theme .frame {
            background-color: rgba(50, 50, 50, 0.8);
        }
        .dark-theme .result-input {
            background-color: #6c757d;
        }
        .dark-theme .result6 {
            background-color: #218838;
        }
        .dark-theme .result10 {
            background-color: #e0a800;
        }
        .dark-theme .result12 {
            background-color: #c82333;
        }
        .dark-theme .pago-cell {
            color: #ffffff;
        }
    </style>
    <script>
        function padZero(value) {
            return value < 10 ? '0' + value : value;
        }

        function addRow(number, result6, result10, result12) {
            const table = document.getElementById("resultsTable").getElementsByTagName('tbody')[0];
            const row = table.insertRow(0); // Insere a nova linha no topo

            const numberCell = row.insertCell();
            numberCell.textContent = padZero(number);
            numberCell.className = 'result-input';

            const altaCell = row.insertCell();
            altaCell.textContent = padZero(result6);
            altaCell.className = 'result6';

            const mediaCell = row.insertCell();
            mediaCell.textContent = padZero(result10);
            mediaCell.className = 'result10';

            const baixaCell = row.insertCell();
            baixaCell.textContent = padZero(result12);
            baixaCell.className = 'result12';

            const pagoCell = row.insertCell();
            pagoCell.textContent = '?'; // Texto inicial
            pagoCell.className = 'pago-cell';

            pagoCell.addEventListener('click', function() {
    if (pagoCell.textContent === 'Win') {
        pagoCell.textContent = 'Loss';
        pagoCell.style.backgroundColor = 'red';
        pagoCell.style.color = 'white';
    } else if (pagoCell.textContent === 'Loss') {
        pagoCell.textContent = 'robou';
        pagoCell.style.backgroundColor = 'orange';
        pagoCell.style.color = 'black';
    } else {
        pagoCell.textContent = 'Win';
        pagoCell.style.backgroundColor = 'green';
        pagoCell.style.color = 'white';
    }
});
            // Verifica valores iguais nas colunas
            checkForEqualValues();
        }

        // função que verifica os numeros iguais nas colunas ---- 
        
        // Verifica valores iguais nas colunas
function checkForEqualValues() {
    const table = document.getElementById("resultsTable");
    const rows = table.getElementsByTagName('tbody')[0].rows;
    
    // Armazenar os valores das células nas colunas
    let valueCells = {};

    // Itera sobre todas as linhas e colunas relevantes
    for (let i = 0; i < rows.length; i++) {
        const result6Value = rows[i].cells[1].textContent;
        const result10Value = rows[i].cells[2].textContent;
        const result12Value = rows[i].cells[3].textContent;

        // Adiciona os valores e suas células correspondentes ao armazenamento
        [result6Value, result10Value, result12Value].forEach((value, index) => {
            if (!valueCells[value]) {
                valueCells[value] = [];
            }
            valueCells[value].push(rows[i].cells[index + 1]);
        });
    }

    // Verifica e aplica estilos para valores repetidos
    for (const value in valueCells) {
        if (valueCells[value].length > 1) {
            valueCells[value].forEach(cell => {
                cell.style.backgroundColor = 'black';
                cell.style.color = 'white';
            });
        }
    }
}

        
       // função que calcula os resultados
function calculate() {
    const input = prompt("Digite o número:");
    if (input !== null && !isNaN(input)) {
        const number = parseInt(input);
        
        const result6 = (number + 6) % 60;
        const result10 = (number + 10) % 60;
        const result12 = (number + 12) % 60;

        addRow(number, result6, result10, result12);
    }
}


        function clearTable() {
            const tableBody = document.getElementById("resultsTable").getElementsByTagName('tbody')[0];
            tableBody.innerHTML = '';
        }

        function toggleTheme() {
            document.body.classList.toggle('dark-theme');
            document.querySelector('.theme-toggle').classList.toggle('transparent');
        }

        function openGenPage() {
        window.open('gerenciamento.php', 'Gerenciamento', 'width=600,height=400');
        }

        function openmenPage() {
        
        window.open('https://drive.google.com/file/d/1GxqejD4ByY5nZdI16LQFo7LVeB3hsYta/view?usp=sharing', 'Mentoria', 'width=600,height=400');
        }

        function openinstaPage() {
        
        window.open('https://www.instagram.com/whitehunter14x/', 'Instagram', 'width=600,height=400');
        }

        function opentelePage() {
        
        window.open('https://t.me/+LpcnAY71meYyOTgx', 'Chat Oficial', 'width=600,height=400');
        }

        function opensala24() {
        
        window.open('https://t.me/+6ZcO1CrVHXZiODk5', 'Sala 24H', 'width=600,height=400');
        }

        function opensalacores() {
        
        window.open('https://t.me/+Cjii4fwI9ZZhMDBh', 'Sala Cores', 'width=600,height=400');
        }

        function openrobin() {
        window.open('https://robinblaze.com.br/', 'Robin', 'width=600,height=400');
        }
        

        function openlogoutPage() {
        window.location.href = 'login.php';
        }
        

        

</script>
</head>
<body>
    <div class="menu">
        <h2 style="background-color: rgb(47, 47, 218); color: white; padding: 10px; border-radius: 5px; display: inline-block;">Menu</h2>
        <ul>
            <li><a class="corfundomenu" href="#" onclick="openGenPage()">Gerenciamento</a></li>
            <li><a class="corfundomenu" href="#" onclick="openmenPage()">Mentoria</a></li>
            <li><a class="corfundomenu" href="#" onclick="openinstaPage()">Instagram</a></li>
            <li><a class="corfundomenu" href="#" onclick="opentelePage()">Chat Oficial</a></li>     
            <li><a class="corfundomenu" href="#" onclick="opensala24()">Sala 24h</a></li>
            <li><a class="corfundomenu" href="#" onclick="opensalacores()">Sala Cores</a></li>
            <li><a class="corfundomenu" href="#" onclick="openrobin()">Robin</a></li>
            <li><a class="corfundomenu" href="#" onclick="openlogoutPage()">Logout</a></li>           
        </ul>
    </div>
    
        
    
        <div class="main-content">
            <div class="frame" style="text-align: center;"> <!-- Adiciona centralização ao container -->
                <h1 class="titulo-vermelho" style="background-color: red; color: white; padding: 10px; border-radius: 5px; display: inline-block;">White Hunter 14x</h1>
                
                <!-- Coloque os botões em um novo bloco abaixo do título -->
                <div style="margin-top: 10px;"> <!-- Adiciona um espaço entre o título e os botões -->
                    <button class="botao-vermelho" onclick="calculate()">Calcular</button>
                    <button class="botao-vermelho" onclick="clearTable()">Limpar</button>
                </div>
        
                <table id="resultsTable" class="results-table">
                    <thead>
                        <tr>
                            <th class="corfundomenu">Minuto</th>
                            <th class="corfundomenu">Alta</th>
                            <th class="corfundomenu">Média</th>
                            <th class="corfundomenu">Baixa</th>
                            <th class="corfundomenu">Pago</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- As linhas serão inseridas aqui -->
                    </tbody>
                </table>
                <button class="theme-toggle" onclick="toggleTheme()">Alternar Tema</button>
            </div>
        </div>
        
        
    
        <style>
            .botao-vermelho {
                background-color: red; /* Cor de fundo vermelha */
                color: white; /* Cor do texto branca */
                font-weight: bold; /* Texto em negrito */
                border: none; /* Remover bordas */
                padding: 10px 20px; /* Espaço interno */
                cursor: pointer; /* Mão ao passar o mouse */
                border-radius: 5px; /* Cantos arredondados */
                font-size: 16px; /* Tamanho da fonte */
                text-decoration: none; /* Remove o sublinhado do link */
                display: inline-block; /* Permite aplicar padding e margin */
            }
        
            .botao-vermelho:hover {
                background-color: darkred; /* Cor de fundo ao passar o mouse */
            }
        
            /* Estilo específico para os links no menu */
            .menu a {
                color: white; /* Cor do texto branca para os links do menu */
                font-weight: bold; /* Texto em negrito */
                text-decoration: none; /* Remove o sublinhado dos links */
            }
        
            .menu a:hover {
                background-color: darkred; /* Cor de fundo ao passar o mouse nos links do menu */
            }
        
            /* Estilo para o título */
            .titulo-vermelho {
                color: red; /* Ajuste para cor vermelha */
                font-weight: bold; /* Texto em negrito */
            }
        
            .corfundomenu {
                background-color: rgb(47, 47, 218); /* Cor de fundo para o cabeçalho */
                color: white; /* Cor do texto branca */
                font-weight: bold; /* Texto em negrito */
                text-align: center; /* Alinhamento do texto à esquerda */
                padding: 10px; /* Espaço interno */
            }
        
            /* Estilo para a tabela personalizada */
            .custom-table {
                width: 100%; /* A tabela ocupará toda a largura disponível */
                border-collapse: collapse; /* Para que as bordas não tenham espaçamento */
            }
        
            .custom-table th {
                background-color: rgb(47, 47, 218); /* Usando a mesma cor da classe corfundomenu */
                padding: 10px; /* Espaçamento interno dos cabeçalhos */
                text-align: left; /* Alinhamento do texto à esquerda */
                border: 1px solid #ddd; /* Borda para as células do cabeçalho */
            }
        
            /* Ajustar a largura das colunas */
            .custom-table th:nth-child(1) {
                width: 20%; /* Largura para a coluna "Minuto" */
            }
        
            .custom-table th:nth-child(2) {
                width: 20%; /* Largura para a coluna "Alta" */
            }
        
            .custom-table th:nth-child(3) {
                width: 20%; /* Largura para a coluna "Média" */
            }
        
            .custom-table th:nth-child(4) {
                width: 20%; /* Largura para a coluna "Baixa" */
            }
        
            .custom-table th:nth-child(5) {
                width: 20%; /* Largura para a coluna "Pago" */
            }
        
            /* Estilo para as células */
            .custom-table td {
                padding: 20px; /* Espaçamento interno das células */
                border: 1px solid #ddd; /* Borda para as células */
            }
        </style>