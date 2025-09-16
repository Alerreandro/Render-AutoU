document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('email-form');
    const resultContainer = document.getElementById('result-container');
    const loader = document.getElementById('loader');
    const resultContent = document.getElementById('result-content');
    const classificationResult = document.getElementById('classification-result');
    const responseSuggestion = document.getElementById('response-suggestion');
    const errorMessage = document.getElementById('error-message');
    const emailTextInput = document.getElementById('email-text');
    const emailFileInput = document.getElementById('email-file');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        resultContainer.classList.remove('hidden');
        loader.classList.remove('hidden');
        resultContent.classList.add('hidden');
        errorMessage.classList.add('hidden');
        
        let requestBody;
        let headers = {};
        
        const file = emailFileInput.files[0];

        if (file) {
            const formData = new FormData();
            formData.append('email_file', file);
            requestBody = formData;
        } else {
            const text = emailTextInput.value;
            if (!text) {
                showError("Por favor, insira o texto de um email ou envie um arquivo.");
                return;
            }
            requestBody = JSON.stringify({ email_text: text });
            headers['Content-Type'] = 'application/json';
        }

        try {
            const response = await fetch('/api/classify/', {
                method: 'POST',
                headers: headers,
                body: requestBody,
            });

            const data = await response.json();
            
            if (response.ok) {
                displayResults(data);
            } else {
                showError(data.erro || "Ocorreu um erro desconhecido.");
            }

        } catch (error) {
            showError("Erro de conexão. Verifique se o servidor está rodando.");
        } finally {
            loader.classList.add('hidden');
            resultContent.classList.remove('hidden');
        }
    });
    
    function displayResults(data) {
        classificationResult.textContent = data.classificacao;
        responseSuggestion.textContent = data.sugestao_resposta;
        errorMessage.classList.add('hidden'); 
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.remove('hidden');
        loader.classList.add('hidden');
        resultContent.classList.add('hidden');
    }
});