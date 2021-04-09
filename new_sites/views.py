from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.files.storage import FileSystemStorage 

from django.core.mail import EmailMessage
from django.template.loader import get_template 
from django.core.mail import send_mail

from django.forms import modelformset_factory

from .models import Topic, Book, TopicHome
from .forms import TopicForm, BookForm, ContactForm, TopicHomeForm

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail





# Create your views here.

def index(request):

    topics = TopicHome.objects.all().order_by('-id')[:10]
    context = {'topics': topics}


    return render(request, 'new_sites/index.html', context)

def topics(request):

    topics = Topic.objects.all().order_by('-id')[:10]
   
    
    context = {'topics': topics}

    return render(request, 'new_sites/topics.html', context)


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

    entry=Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':

        form = EntryForm(instance = entry)

    else:

        form = EntryForm(instance = entry, data = request.POST)

        if form.is_valid():
            form.save()

            return redirect('new_sites:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic':topic, 'form':form}

    return render(request, 'new_sites/edit_entry.html', context)

@login_required
def topic_edit(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':

        form = TopicForm(instance=topic)

    else: 

        form = TopicForm(instance = topic, data = request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('new_sites:topics')
    
    context = {'topic': topic, 'form':form}

    return render(request, 'new_sites/topic_edit.html', context)
    

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


@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id) 
    topic.delete()
    
    return redirect('new_sites:topics')

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


