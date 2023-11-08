from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.files.storage import FileSystemStorage 

from django.core.mail import EmailMessage
from django.template.loader import get_template 
from django.core.mail import send_mail

from django.forms import modelformset_factory

from .models import Videos, Book, TopicPost, TopicHome, TopicPost2
from .forms import VideoForm, BookForm, ContactForm, MainPostForm, TopicPostForm, TopicHomeForm, MainPost, TopicPostForm2


import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import json 
from difflib import get_close_matches 

import subprocess 
import requests 





#Home page 
def index(request):

    topics = TopicHome.objects.all().order_by('-id')[:10]
    context = {'topics': topics}

    return render(request, 'new_sites/index.html', context)

#def word_definition(request):
    word = request.GET.get('q', '')  # Get the 'q' parameter from the URL

    if word:
        # Define the URL of your EC2 instance
        ec2_ip = 'http://18.234.63.98'

        # Specify the endpoint or route on your EC2 instance
        endpoint = '/dictionary/pythondefinition.py'


        # Build the full URL
        url = ec2_ip + endpoint

        # Make an HTTP GET request to your EC2 instance
        response = requests.get(url, params={'word': word})

        if response.status_code == 200:
            definitions = response.text
        else:
            #Handle the case when the request to the EC2 instance fails
            definitions = "Error: Unable to fetch definitions."
    else:
        definitions = ""

    return render(request, 'new_sites/word_definition.html', {'word': word, 'definitions': definitions})

#def word_definition(request):
    word = request.GET.get('q', '')  # Get the 'q' parameter from the URL

    if word:
        ec2_ip = '18.234.63.98'
        # Call the modified external Python script to get word definitions
        ec2_path = '/home/ec2-user/dictionary/pythondefinition.py'


        cmd = ['ssh', f'ec2-user@{ec2_ip}', 'python3', ec2_path, word]
        result = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        definitions = result.stdout
    else:
        definitions = ""

    return render(request, 'new_sites/word_definition.html', {'word': word, 'definitions': definitions})


def word_definition(request):
    word = request.GET.get('q', '')  # Get the 'q' parameter from the URL

    if word:
        # Call the modified external Python script to get word definitions
        cmd = ['python3', '/home/ec2-user/prozaicgit/prozaic5/pythondefinition.py', word]
        result = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        definitions = result.stdout
    else:
        definitions = ""

    return render(request, 'new_sites/word_definition.html', {'word': word, 'definitions': definitions})

#List all of the videos 
def videos(request):

    topics = Videos.objects.all().order_by('-id')[:10]
    context = {'topics': topics}
    return render(request, 'new_sites/videos.html', context)


def show(request):

    topics = TopicPost2.objects.all().order_by('-id')[:10]
    context = {'topics': topics}
    return render(request, 'new_sites/show.html', context)


@login_required
def topic(request, topic_id):

    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'new_sites/topic.html', context)
    
@login_required
def new_topic(request):

    if request.method == "POST":
       form = VideoForm(request.POST, request.FILES)
       
       if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()

            form.save()
            return redirect('new_sites:videos')
    else:
        form = VideoForm()
        
    context = {'form':form}
    return render(request, 'new_sites/new_topic.html', context)

@login_required
def new_topichome(request):
    if request.method == "POST":
       form = TopicHomeForm(request.POST, request.FILES)
    
       
       if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()

            form.save()
            return redirect('new_sites:index')
    else:
        form = TopicHomeForm()
        
    context = {'form':form}
    return render(request, 'new_sites/new_topichome.html', context)
    
#Adding a new post 
@login_required
def new_post(request):

    if request.method == "POST":
       form = MainPostForm(request.POST, request.FILES)
    
       
       if form.is_valid():
            new_post = form.save(commit = False)
            new_post.owner = request.user
            new_post.save()

            form.save()
            return redirect('new_sites:index')
    else:
        form = MainPostForm()
        
    context = {'form':form}
    return render(request, 'new_sites/new_mainpost.html', context)


        
def search_word(request): 


    with open('new_sites/static/css/data.json', 'r') as f: 
        data = json.load(f)
    word = TopicPost2.objects.all().order_by('-id')[:10]
    if word in data:
        return data[word]



def search_word2(request): 
    if request.method == "POST":
        form = TopicPostForm2(request.POST, request.FILES)

        if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.save()

            form.save()
            return redirect('new_sites:search_word')

        else:  
            form = TopicPostForm2()

        context = {'form':form}
        return render(request, 'new_sites/searchdic.html', context)

def article_view(request): 
    print(request.GET)
    query_dict = request.GET #this is a dictionary 
    query = query_dict.get("q")
    context = {} 
    return render(request, "new_sites/search.html", context=context)

@login_required
def new_topicpost(request):
    if request.method == "POST":
        form = TopicPostForm(request.POST, request.FILES)

        if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()

            form.save()
            return redirect('new_sites:index')

        else:  
            form = TopicPostForm()

        context = {'form':form}
        return render(request, 'new_sites/new_topichome.html', context)

def vupload(request):
    if request.method == "POST":
       form = TopicForm(request.POST, request.FILES)
    
       
       if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()

            form.save()
            return redirect('new_sites:topics')
    else:
        form = TopicForm()
        
    context = {'form':form}
    return render(request, 'new_sites/new_topic.html', context)



@login_required
def edit_entry(request, entry_id):

    entry=Videos.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':

        form = VideoForm(instance = entry)

    else:

        form = VideoForm(instance = entry, data = request.POST)

        if form.is_valid():
            form.save()

            return redirect('new_sites:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic':topic, 'form':form}

    return render(request, 'new_sites/edit_entry.html', context)

#Edit Video
@login_required
def video_edit(request, video_id):
    topic = Videos.objects.get(id=video_id)

    if request.method != 'POST':

        form = VideoForm(instance=topic)

    else: 

        form = VideoForm(instance = topic, data = request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('new_sites:videos')
    
    context = {'topic': topic, 'form':form}
    return render(request, 'new_sites/video_edit.html', context)

@login_required
def post_edit(request, topic_id):
    topic = MainPost.objects.get(id=topic_id)

    if request.method != 'POST':

        form = MainPostForm(instance=topic)

    else: 

        form = MainPostForm(instance = topic, data = request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('new_sites:post_list')
    
    context = {'topic': topic, 'form':form}

    return render(request, 'new_sites/edit_post.html', context)
    

@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        
    return render(request, 'new_sites/upload.html', context)

def book_list(request):
    books = Book.objects.all().order_by('-id')[:200]

    return render(request, 'new_sites/book_list.html', {
        'books': books
    })



#Lists all of the posts 
def post_list(request):

    topics = MainPost.objects.all().order_by('-id')[:10]
    context = {'topics': topics}
    
    return render(request, 'new_sites/post_list.html', context)


@login_required
def upload_book(request):

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            
            upload_book = form.save(commit = False)
            upload_book.owner = request.user
            upload_book.save()

            form.save()
            form = BookForm()
            return render(request, 'new_sites/morebooks.html',
         {
                'form': form
         })
 
    else:
        form = BookForm()
        return render(request, 'new_sites/upload_book.html',
    {
        'form': form

    })

def morebooks(request):

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            
            upload_book = form.save(commit = False)
            upload_book.owner = request.user
            upload_book.save()

            form.save()
            return redirect('new_sites:book_list')
 
    else:
        form = BookForm()
        return render(request, 'new_sites/morebooks.html',
    {
        'form': form

    })

#Delete Video 
@login_required
def delete_video(request, topic_id):
    topic = Videos.objects.get(id = topic_id) 
    topic.delete()
    
    return redirect('new_sites:videos')

#Delete's the posts 
@login_required
def delete_post(request, topic_id):

    topic = MainPost.objects.get(id = topic_id) 
    topic.delete()
    
    return redirect('new_sites:post_list')



def delete_topichome(request, topic_id):
    
   topic = TopicHome.objects.get(id = topic_id)
   topic.delete()
   return redirect('new_sites:index')

@login_required
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)

    book.delete()

    return redirect('new_sites:book_list')

def check_topic_owner(owner, user):

	if owner != user:

		raise Http404

def contact(request):
    
    

	form_class = ContactForm 

	if request.method == 'POST':


		form = form_class(data = request.POST)

		subject = 'Contact Form Received'
		from_email = settings.DEFAULT_FROM_EMAIL
		to_email = [settings.DEFAULT_FROM_EMAIL]

		if form.is_valid():

        
			contact_name = request.POST.get('contact_name', '')

			contact_email = request.POST.get('contact_email', '')

			form_content = request.POST.get('content', '')


		
	


			context = {'contact_name': contact_name, 'contact_email': contact_email, 
						'form_content': form_content,}

			contact_message = get_template('new_sites/contact_template.txt').render(context)

			email = EmailMessage(
				"New Contact form submission",

				contact_message, 

				"Your website" + '',

				['malcolmshar@gmail.com'],

				headers = {'Reply-To': contact_email}

			)



			send_mail(subject, contact_message, from_email, to_email, fail_silently = False)

				
			return redirect('new_sites:topics')

	return render(request, 'new_sites/contact.html', {'form': form_class})


