import json
from django.shortcuts import redirect, render
from allauth.socialaccount.models import SocialAccount
from . import models
import json
from django.http import JsonResponse
# Create your views here.

def Home(request) :
    try:
        user_info = SocialAccount.objects.get(user=request.user.id)
        user_info = dict(user_info.extra_data)
    except :
        user_info = None
    try:
        posts = models.post.objects.all().order_by("-id")
        data_posts = []
        id = 1
        for post in posts:
            user_image = SocialAccount.objects.get(user=post.user.id)
            user_image = dict(user_image.extra_data)
            obj = {
                'id': id,
                'user': post.user,
                'content': post.content,
                'tag': post.tag,
                'image': user_image['picture'],
                'postId': post.id,
            }
            data_posts.append(obj)
            id += 1
    except:
        posts = None
        data_posts= None
    return render(request, 'home.html', {"login_user":request.user, 'user_info':user_info, 'posts': data_posts})

# def api(request):
#     try:
#         posts = models.post.objects.all().order_by("-id")
#         data = []
#         for post in posts:
#             obj = {
#                 'username': post.user.username,
#                 'tag': post.tag,
#             }
#             data.append(obj)
#     except:
#         data = None
#     return JsonResponse(data, safe=False)

def profile(request):
    try:
        user_info = SocialAccount.objects.get(user=request.user.id)
        user_info = dict(user_info.extra_data)
    except :
        user_info = None
    try:
        posts = models.post.objects.filter(user=request.user).order_by("-id")
        data_posts = []
        num = 1
        for post in posts:

            obj = {
                'id': post.id,
                'user': post.user,
                'content': post.content,
                'tag': post.tag,
                'num': num
            }
            data_posts.append(obj)
            num += 1
    except:
        posts = None
    return render(request, 'profile.html', {"login_user":request.user, 'user_info':user_info, "posts" : data_posts})


def user_profile(request, postId):
        data_posts = []
        data = postId
        user =  models.post.objects.get(id = data)
        try:
            posts = models.post.objects.filter(user=user.user).order_by("-id")
            num = 1
            for post in posts:
                user_image = SocialAccount.objects.get(user=post.user.id)
                user_image = dict(user_image.extra_data)
                
                obj = {
                'id': post.id,
                'user': post.user,
                'content': post.content,
                'tag': post.tag,
                'num': num,
                'image': user_image['picture'],
                }
                data_posts.append(obj)
                num += 1
        except:
            pass
        try:
            user_info = SocialAccount.objects.get(user=request.user.id)
            user_info = dict(user_info.extra_data)
        except :
            user_info = None
        
        return render(request, 'profile.html', {"login_user":request.user, 'user_info':user_info, "posts" : data_posts, "not_user": "1"})

def post(request):
    try:
        user_info = SocialAccount.objects.get(user=request.user.id)
        user_info = dict(user_info.extra_data)
    except :
        user_info = None
    if request.POST :
        models.post.objects.create(
            user = request.user,
            content = request.POST['content'],
            tag = request.POST['tag'],
        )
        return redirect('promptobia:home')
    return render(request, 'post.html', {"login_user":request.user, 'user_info':user_info})

def edit(request, postId):
    try:
        user_info = SocialAccount.objects.get(user=request.user.id)
        user_info = dict(user_info.extra_data)
    except :
        user_info = None
    try:
        post = models.post.objects.get(id=postId)
    except:
        redirect("promptobia:profile")
    if request.POST :
        post.content = request.POST['content']
        post.tag = request.POST['tag']
        post.save()
        return redirect('promptobia:profile')
    return render(request, 'post.html', {"login_user":request.user, 'user_info':user_info, 'post':post})

def delete(request, postId):
    try:
        user_info = SocialAccount.objects.get(user=request.user.id)
        user_info = dict(user_info.extra_data)
    except :
        user_info = None
    try:
        post = models.post.objects.get(id=postId)
    except:
        redirect("promptobia:profile")
    if request.POST :
        post.delete()
        return redirect('promptobia:profile')
    return render(request, 'delete.html', {"login_user":request.user, 'user_info':user_info, 'post':post})