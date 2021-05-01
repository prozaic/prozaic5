from django import forms

from .models import Topic, Book, TopicHome, TopicPost

class TopicForm(forms.ModelForm):

    class Meta: 

        model = Topic
        fields =['title', 'text', 'image','urllink']

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter title here'
        self.fields['text'].widget.attrs['placeholder'] = 'Enter text here'

class TopicHomeForm(forms.ModelForm):

    class Meta: 

        model = TopicHome
        fields =['title', 'text', 'image','urllink']

    def __init__(self, *args, **kwargs):
        super(TopicHomeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter title here'
        self.fields['text'].widget.attrs['placeholder'] = 'Enter text here'    


class TopicPostForm(forms.ModelForm):

    class Meta: 

        model = TopicPost
        fields =['title', 'text', 'image']

    def __init__(self, *args, **kwargs):
        super(TopicPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter title here'
        self.fields['text'].widget.attrs['placeholder'] = 'Enter text here'    

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields =['title', 'author', 'link', 'cover']



class ContactForm(forms.Form):

	contact_name = forms.CharField(required = True, label ='Name', widget=forms.TextInput(attrs={'placeholder': 'Enter Name', 'class':'inputarea'}))
	contact_email = forms.EmailField(required = True, label = 'Email', widget=forms.TextInput(attrs={'placeholder': 'Enter Email', 'class':'inputarea'}))

	content = forms.CharField(

		required = True,
		widget = forms.Textarea(attrs ={'placeholder': "Enter Message Here"}), label = '',

	)

