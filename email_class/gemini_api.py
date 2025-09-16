import google.generativeai as genai
from decouple import config
import json


try:
    GOOGLE_API_KEY = config('GEMINI_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:

    raise ValueError("A chave da API do Gemini não foi encontrada. Verifique seu arquivo .env") from e


model = genai.GenerativeModel('gemini-1.5-flash')

def analisar_email(texto_do_email: str) -> dict:
    """
    Analisa o texto de um email usando a API do Gemini para classificar
    e sugerir uma resposta.

    Args:
        texto_do_email: O conteúdo completo do email a ser analisado.

    Returns:
        Um dicionário Python com a "classificacao" e a "sugestao_resposta".
        Retorna um dicionário de erro se a análise falhar.
    """

    prompt = f"""
    Analise o conteúdo do email abaixo e retorne um objeto JSON válido com exatamente duas chaves: "classificacao" e "sugestao_resposta".

    1.  **"classificacao"**: Deve ser "Produtivo" se o email exigir uma ação, acompanhamento, ou for relacionado a trabalho. Deve ser "Improdutivo" se for um email social, spam, ou de baixa prioridade.
    2.  **"sugestao_resposta"**: Crie uma resposta curta, profissional e adequada à classificação. Para emails improdutivos, uma resposta simples e educada é suficiente.

    Não adicione nenhuma formatação extra como "```json" no início ou "```" no final. A saída deve ser apenas o JSON puro.

    --- CONTEÚDO DO EMAIL ---
    {texto_do_email}
    --- FIM DO EMAIL ---
    """

    try:
        response = model.generate_content(prompt)

        resultado_json = json.loads(response.text)


        if "classificacao" in resultado_json and "sugestao_resposta" in resultado_json:
            return resultado_json
        else:
            return {"erro": "A resposta da IA não contém as chaves esperadas."}

    except json.JSONDecodeError:
        return {"erro": "Falha ao decodificar a resposta da IA. A resposta não era um JSON válido."}
    except Exception as e:

        print(f"Ocorreu um erro na API do Gemini: {e}")
        return {"erro": "Ocorreu um erro ao se comunicar com a API do Gemini."}

if __name__ == '__main__':

    email_produtivo = """
    Olá equipe,
    Gostaria de saber o status da requisição #4532. Poderiam me dar uma atualização?
    Preciso apresentar os resultados na sexta-feira.
    Obrigado,
    João Silva
    
    """
    resultado1 = analisar_email(email_produtivo)
    print("--- Teste 1: Email Produtivo ---")
    print(resultado1)

    print("\n" + "="*30 + "\n")

    email_improdutivo = """
    E aí pessoal,
    Só passando pra desejar um feliz natal e um próspero ano novo a todos!
    Abraços,
    Maria
    """
    resultado2 = analisar_email(email_improdutivo)
    print("--- Teste 2: Email Improdutivo ---")
    print(resultado2)