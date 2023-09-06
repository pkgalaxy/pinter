from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
    
def home(requests):
    data = post.objects.all().order_by('-create_date')
    paginator=Paginator(data,12)
    page_number = requests.GET.get('page')
    page = paginator.get_page(page_number)
    return render(requests, 'home.html', { 'page' : page})

@login_required
def po_st(requests,pk):  #single post
   blog= post.objects.get(id=pk)
   owner_profile = Profile.objects.get(car=blog.var)  # Get the profile of the owner

   cost = get_object_or_404(post, id=pk)   #comment section
   
   comments = Comment.objects.filter(related=cost)
   if requests.method == 'POST':
        comment_form = CommentForm(requests.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.related = cost
            new_comment.author = requests.user   
            
            try:     
             # Retrieve the commentator's profile
              commentator_profile = Profile.objects.get(car=requests.user)
            # Assign the commentator's profile picture to the comment
              new_comment.author_dp = commentator_profile
            #   new_comment.author = requests.user
            except Profile.DoesNotExist:
                pass          
            new_comment.save()
            
   else:
        comment_form = CommentForm()
   return render(requests, 'single-post.html', {'cost': cost, 'comments': comments, 'comment_form': comment_form,'blog': blog, 'owner_profile': owner_profile})


@login_required
def user_post(requests):   #author
    user_posts = post.objects.filter(var=requests.user).order_by('-create_date')
    xyz=Profile.objects.filter(car=requests.user)
    return render(requests, 'author.html', {'user_posts': user_posts, 'xyz':xyz})

@login_required
def post_upload(requests):
    
    if requests.method == 'POST':        
        form = UserData(requests.POST, requests.FILES)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.var = requests.user  # Assign the currently logged-in user as the author
            post.save()           
            
            return redirect('user-post/')  # Redirect to a success page or another view
    else:
        form = UserData()
    return render(requests, 'post-upload.html', {'form': form})

def log_in(requests):
   
    if requests.method == 'POST':
        uname=requests.POST.get('username')
        pass1=requests.POST.get('password')
        user=authenticate(requests,username=uname, password=pass1)
                
        if user is not None:
            login(requests,user)
            return redirect('home/')
        else:
            return HttpResponse("Username and Password is incorrect")
        
    return render (requests, 'login.html')
                
def sign_up(requests):
    if requests.method == 'POST' :
        uname=requests.POST.get('username')
        email=requests.POST.get('email')        
        pass1=requests.POST.get('password1')
        pass2=requests.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Password are not same")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('home/')
        
    return render (requests, 'signup.html')

def log_out(requests):
    logout(requests)
    messages.success(requests, ("You were Logged out"))
    return redirect('home/')

@login_required
def owner(requests, abc):
    user=User.objects.get(username=abc)
    lata=post.objects.filter(var=user)
    zata=Profile.objects.filter(car=user)
    return render(requests, 'owner.html', {'lata':lata, 'nata':lata[0], 'zata':zata[0]})

@login_required
def edit_profile(requests):
    if requests.method == 'POST':        
        form = EditProfile(requests.POST, requests.FILES)
        if form.is_valid(): 
            
            user = requests.user
            
            profile, created = Profile.objects.get_or_create(car=user)

            # Assign the profile picture and bio
            profile.profile_picture = form.cleaned_data['profile_picture']
            profile.bio = form.cleaned_data['bio']
            profile.save()          
            
            return redirect('user-post/')  # Redirect to a success page or another view
    else:
        form = EditProfile()
    return render(requests, 'edit-profile.html', {'form': form})

    
def explore(request):  #search 
    zata = post.objects.all()
    search_query = request.GET.get('q')  # Retrieve the search query from the GET request
    search_query2 = request.GET.get('name')  # Retrieve the search query from the GET request
    
    if search_query:
         zata = zata.filter(title__icontains=search_query) | zata.filter(desc__icontains=search_query)
         
    if search_query2:
            zata = zata.filter(title__icontains=search_query2) | zata.filter(desc__icontains=search_query2)
    
    context = {
        'zata': zata,
        'search_query': search_query,
        'search_query2': search_query2,
    }
    return render(request, 'home.html', context)

@login_required
def like_post(request, post_id):
    post_to_like = get_object_or_404(post, pk=post_id)
    
    if request.user in post_to_like.likes.all():
        post_to_like.likes.remove(request.user)
    else:
        post_to_like.likes.add(request.user)
    
    return redirect('single-post', pk=post_id)




 
