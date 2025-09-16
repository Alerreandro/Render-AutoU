from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .gemini_api import analisar_email
import json


def home_view(request):
    return render(request, 'email/email.html')

@csrf_exempt
def classificar_email_view(request):
    if request.method == 'POST':
        if 'email_file' in request.FILES:
            uploaded_file = request.FILES['email_file']

            try:
                texto_email = uploaded_file.read().decode('utf-8')
            except Exception:
                return JsonResponse({'erro': 'Não foi possível ler o arquivo. Envie um arquivo .txt válido.'}, status=400)
        
        else:
            try:
                data = json.loads(request.body)
                texto_email = data.get('email_text', '')
            except json.JSONDecodeError:
                 return JsonResponse({'erro': 'Requisição mal formatada.'}, status=400)

        if not texto_email:
            return JsonResponse({'erro': 'Nenhum texto de email fornecido.'}, status=400)


        resultado_analise = analisar_email(texto_email)
        
        if "erro" in resultado_analise:
            return JsonResponse(resultado_analise, status=500)

        return JsonResponse(resultado_analise)

    return JsonResponse({'erro': 'Método não permitido, use POST.'}, status=405)
