from django.shortcuts import render, get_object_or_404
from .models import Author, Book, Library, Profile

# List all books
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# List all authors and their books
def list_authors(request):
    authors = Author.objects.prefetch_related('book_set').all()
    return render(request, 'relationship_app/list_authors.html', {'authors': authors})

# View one author's profile
def author_profile(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    profile = get_object_or_404(Profile, author=author)
    return render(request, 'relationship_app/author_profile.html', {'author': author, 'profile': profile})

# List all libraries and books they hold
def list_libraries(request):
    libraries = Library.objects.prefetch_related('books').all()
    return render(request, 'relationship_app/list_libraries.html', {'libraries': libraries})

# View books in one specific library
def library_detail(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    return render(request, 'relationship_app/library_detail.html', {'library': library})
