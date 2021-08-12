from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors

def index(request):
  book = Books.objects.all()
  author = Authors.objects.all()

  context = {
      'books' : book,
      'authors': author
  }
  return render(request, 'books.html', context)

def createbook(request):
  tit = request.POST["tit"]
  des = request.POST["des"]

  Books.objects.create(title=f'{tit}', desc=f'{des}')

  return redirect('/books')

def addauthor(request):
  firstname = request.POST["firstname"]
  lastname = request.POST["lastname"]

  Authors.objects.create(first_name=f'{firstname}', last_name=f'{lastname}')

  return redirect('/books')

def bookinfo(request, bookid):

  book = Books.objects.get(id=bookid)
  author_yes = [author.id for author in book.authors.all()]
  author_not = [author for author in Authors.objects.all() if author.id not in author_yes]

  context ={
    'book_title' : book.title,
    'book_id' : int(book.id),
    'book_desc' : book.desc,
    'book_author': book.authors.all(),
    'authors_add': author_not,
  }
  return render(request, 'bookinfo.html', context)

def authorinfo(request, authorid):

  author = Authors.objects.get(id=authorid)
  books_yes = [book.id for book in author.books.all()]
  books_not = [book for book in Books.objects.all() if book.id not in books_yes]

  context ={
    'author_first_name' : author.first_name,
    'author_id' : int(author.id),
    'author_last_name' : author.last_name,
    'author_book': author.books.all(),
    'books_add' : books_not,
  }
  return render(request, 'authorinfo.html', context)

def booktoauthor(request, authorid):
  # import pdb; pdb.set_trace()
  book = Books.objects.get(id=request.POST['idbook'])
  author = Authors.objects.get(id=authorid)
  book.authors.add(author)

  return redirect(f'/books/author/{authorid}')