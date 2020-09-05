from django.shortcuts import render, get_object_or_404, redirect
from board.models import Board
from user.models import CustomUser

def write_create(request):
    if request.method == 'POST' and request.session.get('user', False):
        title = request.POST['title']
        author = get_object_or_404(CustomUser, username=request.session['user'])
        content = request.POST['content']

        write = Board(
            title = title,
            author = author,
            content = content,
        )
        write.save()

        return redirect('write_read')
    else:
        return render(request, 'write/create.html')

def write_read(request):
    writes = Board.objects.all()
    context = {'writes' : writes }
    # print (writes)
    return render(request, 'write/read.html', context)

def write_read_one(request, pk):
    write = get_object_or_404(Board, pk = pk)
    context = {'write' : write }
    return render(request, 'write/read_one.html', context)

def write_update(request, pk):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        wri = Board.objects.get(pk=pk)
        wri.title = title
        wri.content = content

        wri.save()
        return redirect('write_read')

    else:
        wri = get_object_or_404(Board, pk = pk)
        context = {"wri" : wri}
        return render(request, 'write/update.html', context)

def write_delete(request, pk):
    wri = Board.objects.get(pk = pk)
    wri.delete()
    return redirect('write_read')