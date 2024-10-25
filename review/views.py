import datetime
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
@login_required(login_url="authentication:login")
def show_main(request, id):
    form = ReviewForm(request.POST or None)
    product = get_object_or_404(Katalog, pk=id)
    last_login = request.COOKIES.get('last_login', 'Not available')

    context = {
        'form': form,
        'product': product,
        'last_login': last_login
    }
    return render(request, 'review.html', context)

# def show_review(request, id):
#     try:
#         review = Review.objects.get(id=id)
#         context = {
#             "review": review
#         }
#         return render(request, 'review_detail.html', context)
#     except Review.DoesNotExist:
#         return HttpResponseNotFound()
    
# @login_required(login_url='/login')
# @csrf_exempt
# def add_review(request, id):
#     form = ReviewForm(request.POST or None)
#     product = get_object_or_404(Katalog, pk=id)
    
#     if form.is_valid() and request.method == "POST":
#         review = form.save(commit=False)
#         review.product = product
#         review.user = request.user
#         review.timestamp = datetime.datetime.now()
#         review.save()
#         product.update_rating()
#         return HttpResponseRedirect(reverse('main:show_main'))
    
#     last_login = request.COOKIES.get('last_login', 'Not available')

#     context = {
#         'form': form,
#         'product': product,
#         'last_login': last_login
#     }

#     return render(request, 'review.html', context)


# @login_required(login_url='/login')
# @csrf_exempt
# def add_review(request, id):
#     if request.method == "POST":
#         user = request.user
#         product_review = Katalog.objects.get(pk=request.POST.get("id"))
#         rating = request.POST.get("rating")
#         review_message = request.POST.get("review_text")

#         new_review = Review(user=user, product = product_review, rating = rating, review_text = review_message)
#         new_review.save()

#         return HttpResponse(b"ADDED", status=201)
#     return HttpResponseNotFound()
@csrf_exempt
@login_required(login_url='/login')
def add_review(request, id):
    if request.method == 'POST':
        rating = request.POST.get("rating")
        review_text = request.POST.get("review_text")
        user = request.user
        product = get_object_or_404(Katalog, pk=id)

        # Validasi input
        if not rating or not review_text:
            return JsonResponse({"error": "Rating and review text are required."}, status=400)

        try:
            new_review = Review.objects.create(
                rating=rating,  # Ensure rating is integer
                review_text=review_text,
                user=user,
                product=product,
                timestamp=datetime.datetime.now()
            )
            return JsonResponse({"message": "Review successfully added!"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


def show_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_review(request):
    data = Katalog.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def get_product_review_by_id(request, id):
    data = Katalog.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def delete_review(request, id):
    if request.method == 'DELETE':
        review = Review.objects.filter(user=request.user).get(book=id)
        review.delete()
        return HttpResponse(b"DELETED", status=200)
    return HttpResponseNotFound()

def get_product_review_json(request, id):
    product = Katalog.objects.get(pk = id)
    review = Review.objects.filter(product=product)
    return HttpResponse(serializers.serialize('json', review))


def get_user_review(request, id):
    product = Katalog.objects.get(pk = id)
    review = Review.objects.filter(user=request.user, product=product)
    return HttpResponse(serializers.serialize('json', review))