import datetime, json
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

    # Tambahkan logging untuk debug
    print(f"Product: {product.name}, Reviews Count: {reviews.count()}")
    print(request.user, " " ,product," ", request.POST.get('rating')," ", request.POST.get('review_text'))
    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'review.html', context)


@csrf_exempt
def add_review(request, id):
    """ View to add review """
    
    if request.method == 'POST':
        user = request.user
        product = Katalog.objects.get(pk=id)
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')
        print("testest")

        review = Review(
            user=user,
            product=product,
            rating=rating,
            review_text=review_text,
            timestamp=datetime.datetime.now()
        )
        # Update the product's average rating
        # review.update_rating()
        print(user, product, rating, review_text)
        review.save()
        print("berhasil bnag")
        return JsonResponse({'Success':''}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# @csrf_exempt
# @login_required(login_url='/login')
# def add_review(request, id):
#     if request.method == 'POST':
#         rating = request.POST.get("rating")
#         review = request.POST.get("review")
#         user = request.user
#         product = Katalog.objects.get(pk = id)
#         new_review = Review(rating=rating, review=review, user=user, product=product)
#         new_review.save()

#         return HttpResponse(b"CREATED", 201)
#     return HttpResponseNotFound()

def show_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='authentication:login')
def get_product_reviews(request, id):
    """ View to get all reviews for a product """
    reviews = Review.objects.filter(pk=id)
    review_data = [{
        'id': review.id,
        'user': {
            'username': review.user.username,
        },
        'rating': review.rating,
        'review_text': review.review_text,
        'timestamp': review.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    } for review in reviews]

    return JsonResponse({'reviews': review_data})


def get_product_review_by_id(request, id):
    data = Katalog.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='authentication:login')
@csrf_exempt
def delete_review(request, id):
    """ View for admin to delete a review """
    if request.method == 'DELETE':
        try:
            # Only allow admins to delete reviews
            if request.user.is_superuser:
                review = Review.objects.get(pk=id)
                review.delete()
                return JsonResponse({'message': 'Review successfully deleted!'}, status=200)
            else:
                return JsonResponse({'error': 'You are not authorized to delete this review.'}, status=403)
        except Review.DoesNotExist:
            return JsonResponse({'error': 'Review not found.'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_product_review_json(request, id):
    product = Katalog.objects.get(pk = id)
    review = Review.objects.filter(product=product)
    return HttpResponse(serializers.serialize('json', review))


def get_user_review(request, id):
    product = Katalog.objects.get(pk = id)
    review = Review.objects.filter(user=request.user, product=product)
    return HttpResponse(serializers.serialize('json', review))