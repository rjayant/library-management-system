#from django.shortcuts import render
from django.views.generic.edit import FormView
from LibraryManagement.forms import *
from LibraryManagement.models import *
from django.views.generic.edit import CreateView
from django.views.generic.dates import YearArchiveView
from django.views.generic.dates import WeekArchiveView
from django.shortcuts import render, redirect
from django.forms.formsets import formset_factory
from django.views.generic import DetailView

# Create your views here.
class contactView(FormView):
    template_name = 'contact.html'
    form_class = contactForm
    success_url = '/thanks/'
    
    def get(self, request, *args, **kwargs):
        form = contactForm()
        return render(request, 'contact.html', {'form':form})

    def post(self, request, *args, **kwargs):
        import pdb ; pdb.set_trace
        form = contactForm(request.POST)
        if form.is_valid():
            return redirect(self.get_success_url())
        return render(request, 'contact.html', {'form':form})

    def form_valid(self, form):
        # This method is called when form data has been posted
        # It should return HTTP responce
        form = contactForm
        return super(contactView, self).form_valid(form)

class AuthorCreate(CreateView):
    model = Author
    fields = ['name']

class ArticleYearArchiveView(YearArchiveView):
    model = Article
    date_field = "pub_date"
    make_object_list = True
    allow_future = True

class ArticleWeekArchiveView(WeekArchiveView):
    model = Article
    date_field = 'pub_date'
    week_format = '%W'
    allow_future = True

class UserDetailView(DetailView):
    model = UserInfo
    form = UserInfoForm

def AddLinksToProfile(request):
    link_form_set = formset_factory(LinkForm, formset=BaseLinkFormSet)
    import pdb ; pdb.set_trace()
    user = request.user
    links = UserLink.objects.filter(id=user).order_by('anchor')
    link_data = [{'anchor':l.anchor, 'url':l.url} for l in links]

    if request.method=='POST':
        profile_form = UserProfile(request.POST, user=user)
        links_form = link_form_set(request.POST)
        if profile_form.is_valid() and links_form.is_valid():
            pass
            
