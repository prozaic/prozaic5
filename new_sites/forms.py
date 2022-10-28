from django import forms

from .models import Videos, Book, TopicHome, TopicPost, MainPost, TopicPost2

class VideoForm(forms.ModelForm):

    class Meta: 

        model = Videos
        fields =['title', 'text', 'urllink']

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
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

#Form for posts 
class MainPostForm(forms.ModelForm):

   
    
    title = forms.CharField(required = True, label ='', widget=forms.TextInput(attrs={'placeholder': 'Enter Title Here', 'class':'inputarea'}))
    summary = forms.CharField(widget = forms.Textarea(attrs ={'placeholder': "Summary Here"}), label = '',) 
    text = forms.CharField(widget = forms.Textarea(attrs ={'placeholder': "Body Paragraph Here"}), label = '',) 
    
 
    class Meta: 
        model = MainPost
        fields =['title', 'summary', 'text', 'image','urllink']




class TopicPostForm(forms.ModelForm):

    class Meta: 

        model = TopicPost
        fields =['title']

    def __init__(self, *args, **kwargs):
        super(TopicPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter title here'
        

class TopicPostForm2(forms.ModelForm):

    class Meta: 

        model = TopicPost2
        fields =['title']

    def __init__(self, *args, **kwargs):
        super(TopicPostForm2, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter title here'

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

 