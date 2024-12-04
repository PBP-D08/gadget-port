import  json
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound, HttpRequest
from django.urls import reverse
from products.models import *
from review.models import *
from django.core import serializers
from .forms import ReviewForm
from django.shortcuts import render
from products.models import Katalog

# Create your views here.
@login_required(login_url='authentication:login')
def show_product_reviews(request, id):
    """ View to show product detail with all reviews """
    product = get_object_or_404(Katalog, pk=id)
    reviews = Review.objects.filter(product=product)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0 
    # Tambahkan logging untuk debug
    print(f"Product: {product.name}, Reviews Count: {reviews.count()}")
    # print(request.user, " " ,product," ", request.POST.get('rating')," ", request.POST.get('review_text'))
    context = {
        'product': product,
        'reviews': reviews,
        'average_rating' : f"{average_rating:.1f}"
    }

    return render(request, 'detail_and_review.html', context)

# Create your views here.
@login_required(login_url='authentication:login')
def show_product_admin(request, id):
    """ View to show product detail with all reviews """
    product = get_object_or_404(Katalog, pk=id)
    reviews = Review.objects.filter(product=product)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0 
    # Tambahkan logging untuk debug
    print(f"Product: {product.name}, Reviews Count: {reviews.count()}")
    # print(request.user, " " ,product," ", request.POST.get('rating')," ", request.POST.get('review_text'))
    context = {
        'product': product,
        'reviews': reviews,
        'average_rating' : f"{average_rating:.1f}"
        
    }

    return render(request, 'detail_admin.html', context)

@login_required(login_url='authentication:login')
@csrf_exempt
def add_review(request, id):
    """ View to add review """
    
    if request.method == 'POST':
        user = request.user
        product = Katalog.objects.get(pk=id)
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')
        print("review text " , review_text)

        review = Review(
            user=user,
            product=product,
            rating= rating,
            review_text=review_text,
            timestamp=datetime.now()
        )
        # Update the product's average rating
        # review.update_rating()
        print(user, product, rating, review_text)
        review.save()
        print("berhasil bnag")
        return JsonResponse({'Success':''}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required(login_url='authentication:login')
@csrf_exempt
def delete_review(request, id):
    """ View for admin to delete a review """
    if request.method == 'DELETE':
        try:
            # Ambil review berdasarkan ID
            review = Review.objects.get(id=id, user=request.user)
            review.delete()
            return JsonResponse({'message': 'Review deleted successfully'}, status=200)
        except Review.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def delete_review_admin(request, review_id):
    if request.method == 'DELETE':
        review = get_object_or_404(Review, id=review_id)
        review.delete()
        return JsonResponse({'message': 'Review deleted successfully!'}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required(login_url='authentication:login')
def get_review_data(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
        data = {
            'rating': review.rating,
            'review_text': review.review_text,
            'productId': review.product.id  # Jika Review memiliki hubungan dengan Product
        }
        return JsonResponse(data)
    except Review.DoesNotExist:
        return JsonResponse({'error': 'Review not found'}, status=404)

    
@login_required(login_url='authentication:login')
@csrf_exempt
def edit_review(request, review_id):
    print(review_id)
    if request.method == 'POST':
        try:
            review = Review.objects.get(id=review_id, user=request.user)
            # Perbaiki pengambilan nilai rating dan review_text
            rating = request.POST.get('rating')  # Menggunakan request.POST
            review_text = request.POST.get('review_text')  # Menggunakan request.POST

            # Pastikan rating adalah angka sebelum menyimpannya
            if rating is not None:
                review.rating = int(rating)  # Konversi ke integer
            if review_text is not None:
                review.review_text = review_text
            
            review.save()
            return JsonResponse({'message': 'Review updated successfully!'})
        except Review.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


    
def show_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_review_by_id(request, id):
    data = Katalog.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_review_json(request, product_id):
    reviews = Review.objects.filter(product_id=product_id).select_related('user')  # Menambahkan select_related
    data = []
    for review in reviews:
        data.append({
            'id': review.id,  # Pastikan ID review dikirim
            'fields': {
                'rating': review.rating,
                'review_text': review.review_text,
                'timestamp': review.timestamp,  # jika ada
            },
            'user': {
                'username': review.user.username,
                'id': review.user.id,  # Tambahkan ID pengguna jika perlu
            }
        })
    return JsonResponse(data, safe=False)