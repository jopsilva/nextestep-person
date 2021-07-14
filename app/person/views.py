from django.http import JsonResponse

def pessoas(request):
    if request.method == 'GET':
        pessoa = {'id':1, 'nome': 'Josimar'}
        return JsonResponse(pessoa)