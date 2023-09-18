let image = document.querySelectorAll("img.rounded-full.w-12")
let ul = document.querySelector("ul.flex-col.bg-white")
let copyImages = document.querySelectorAll("img.absolute.w-5")
let contents = document.querySelectorAll(".my-p")
let copyMsg = document.querySelectorAll(".copy-div")
let profileImage = document.querySelectorAll("img.image_profile")
let inputSearch = document.querySelector(".my-input")
let postsBoxes = document.querySelectorAll(".my-post")
// let postsBoxesP = document.querySelectorAll(".my-post p.text-blue-500")

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // تحقق مما إذا كان الاسم المطلوب متطابقًا مع الاسم في العنصر
        if (cookie.substring(0, name.length + 1) === name + '=') {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

image[0].onclick = () => {
    ul.classList.toggle("hidden")
    ul.classList.toggle("flex")
}
image[1].onclick = () => {
    window.location.pathname = "/profile"
}

copyImages.forEach((image) => {
    image.addEventListener("click", (ele) => {
        copyMsg[ele.target.dataset.num - 1].classList.remove("opacity-0")
        copyMsg[ele.target.dataset.num - 1].classList.add("opacity-1")
        navigator.clipboard.writeText(contents[ele.target.dataset.num - 1].innerHTML)
        setTimeout(() => {
            copyMsg[ele.target.dataset.num - 1].classList.remove("opacity-1")
            copyMsg[ele.target.dataset.num - 1].classList.add("opacity-0")
        }, 500);
    })
})

profileImage.forEach((image) => {
    image.addEventListener("click", (ele) => {
fetch('/user-profile/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': getCookie('csrftoken'), // تضمين رمز CSRF (تحتاج إلى تنفيذ دالة getCookie للحصول على قيمة الرمز)
  },
  body: JSON.stringify({"postId":ele.target.dataset.id}),
})
.then(() => {
  window.location.href = `/user-profile/${ele.target.dataset.id}/`;
})
.catch(error => {
  console.error('Error:', error);
});
    })
})
// let postsData;

// fetch('/api/')
// .then(response => response.json())
// .then(data => {
//   // استخدم البيانات المستلمة هنا
//   postsData= data;
// })
// .catch(error => {
//   console.error('Error:', error);
// });

postsBoxes.forEach((post) => {
  post.children[2].onclick = (e) => {
    inputSearch.value = e.target.innerHTML.slice(1)
    search()
  }

})
function search() {
  let val = inputSearch.value.toLowerCase()
  if (val != "") {
    postsBoxes.forEach((post) => {
      post.classList.add("hidden")
      post.children[2].innerHTML.toLowerCase().match(val) !== null ? post.classList.remove("hidden") : false;
      post.children[0].children[1].children[0].innerHTML.toLowerCase().match(val) !== null ? post.classList.remove("hidden") : false;
    })
  } else {
    postsBoxes.forEach((post) => {
      post.classList.remove("hidden")
    })
  }
}

  inputSearch.onfocus = () => {
    document.onkeyup = () => {
        search()
    }
  }
