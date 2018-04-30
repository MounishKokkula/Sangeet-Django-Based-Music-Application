from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from .models import Album,Song
from music.forms import UserForm

class IndexView(generic.ListView):
   template_name = 'music/index.html'
   context_object_name = 'object_list'

   def get_queryset(self):
       return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('index')


class UserFormView(View):

    form_class = UserForm
    template_name = 'music/registrationform.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    # process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit = False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password= form.cleaned_data['password']
            user.set_password(password)
            user.save()


            #return User objects if credentials are correct
            user = authenticate(username=username,password=password)

            if user is not None:
                # check if user is not banned od blocked
                if user.is_active:
                    # now they are logedin
                    login(request,user)
                    return redirect('index')


        return render(request, self.template_name,{'form':form})


# Using generic views instead of the below
# from music.models import Album,Song
# # from django.http import HttpResponse
# from django.shortcuts import render,get_object_or_404
# # from django.template import loader
# # from django.http import Http404
#
# def index(request):
#     html = ""
#     all_albums = Album.objects.all()
#     # create template dir and music dir(same name as the app) then create index.html in it to write your display code
#     # template = loader.get_template('music/index.html')
#     context =  {'all_albums':all_albums }
#
#     # connecting to a database
#     # for album in all_albums:
#     #     url = '/music/'+str(album.id)+'/'
#     #     html += '<a href="' + url + '">' + album.album_title + '</a><br>'
#     # return HttpResponse(html)
#
#     # using  HttpResponse and loader instead of render
#     # return HttpResponse(template.render(context,request))
#     return render(request,'music/index.html', context)
#
# def detail(request,album_id):
#     album =  get_object_or_404(Album,pk=album_id)
#
#     # instead of the below code, we can call get_object_or_404
#     # try:
#     #     album = Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album Does Not Exist")
#     # return HttpResponse("<h2> Details for Album Id: "+ str(album_id) +"</h2>")
#     return render(request,'music/detail.html', {'album':album})
#
#
# def favorite(request,album_id):
#     album =  get_object_or_404(Album,pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request,'music/detail.html', {
#             'album':album,
#             'error_message':"You did not select a valid song."
#         })
#     else:
#         if selected_song.is_favorite == True:
#             selected_song.is_favorite = False
#             selected_song.save()
#             return render(request, 'music/detail.html', {'album': album})
#         else:
#             selected_song.is_favorite = True
#             selected_song.save()
#             return render(request, 'music/detail.html', {'album': album})