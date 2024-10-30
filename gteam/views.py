from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def userlogin(request):
    return render(request, 'userlogin.html')

def mainmenu(request):
    items = [f"スクロールテストコンテンツ {i}" for i in range(1, 30)]  # 1から29までのリストを作成
    return render(request, 'mainmenu.html', {'items': items})