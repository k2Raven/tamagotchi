from django.shortcuts import render

cat = {
    'name': None,
    'age': 1,
    'satiety': 40,
    'happiness': 40,
}

def index(request):
    if cat['name']:
        print(cat)

    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        if name:
            cat['name'] = name
        return render(request, 'index.html')