async function getReviews() {
    return fetch(`get-reviews/${product.id}`).then((res) => res.json())
}

// review.js

// Function to add review
async function addReview() {
    const productId = document.getElementById("productId").value;
    const rating = document.getElementById("rating").value;
    const reviewText = document.getElementById("reviewText").value;

    fetch(`/review/add-review-ajax/${productId}/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCookie('csrftoken')  // CSRF token added here
        },
        body: `rating=${rating}&review_text=${reviewText}`
    })
    .then(response => {
        if (response.status === 201) {
            refreshReviews();
            document.getElementById("reviewForm").reset();
            document.getElementById("addModal").classList.remove("show");
            document.querySelector(".modal-backdrop").remove();
        } else {
            alert("Failed to add review.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}


// Function to refresh reviews
async function refreshReviews() {
    const reviews = await getReviews();
    document.getElementById("reviews").innerHTML = "";
    let htmlString = "";
    reviews.forEach((review) => {
        htmlString += `
            <div class="flex items-center mb-2">
                <img alt="User   pp" class="rounded-full mr-2" height="40" width="40" />
                <div>
                <div class="font-bold">${review.user.username}</div>
                <div class="text-sm text-gray-500">Diulas pada ${review.timestamp}</div>
                </div>
            </div>
            <div class="text-sm">${review.review}</div>
        `;
    });
    document.getElementById("reviews").innerHTML = htmlString;
}

// Event listener for submit review form
document.getElementById("reviewForm").addEventListener("submit", function (e) {
    e.preventDefault();
    addReview();
});

// Function to get cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Initial call to refresh reviews
refreshReviews();