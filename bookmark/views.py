from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Bookmark
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # Temporarily for testing; remove this in production
def add_bookmark(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Ensure that all required fields are present
            if not all(key in data for key in ['title', 'description', 'url', 'image_url']):
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Create the bookmark entry
            bookmark = Bookmark.objects.create(
                user=request.user,
                title=data['title'],
                description=data['description'],
                url=data['url'],
                image_url=data['image_url']
            )

            return JsonResponse({'message': 'Bookmark added successfully!'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@login_required
def list_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmark/bookmark.html', {'bookmarks': bookmarks})


def user_bookmarks(request):
    if request.user.is_authenticated:
        # Fetch bookmarks for the logged-in user
        bookmarks = Bookmark.objects.filter(user=request.user)
        return render(request, 'bookmark/bookmarks.html', {'bookmarks': bookmarks})
    else:
        # Redirect to login page if the user is not authenticated
        return redirect('accounts/login.html')

def remove_bookmark(request, bookmark_id):
    if request.user.is_authenticated:
        bookmark = get_object_or_404(Bookmark, id=bookmark_id, user=request.user)
        bookmark.delete()
        return redirect('user_bookmarks')  # Redirect back to the bookmarks page
    else:
        return redirect('login')