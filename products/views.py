from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect
#from .forms import ProductForm,RawProductForm
#from .models import products
#def products_create_view(request):
#	my_form=RawProductForm()
#	if request.method=="POST":
#		my_form=RawProductForm(request.POST)
#		if my_form.is_valid():
#			print(my_form.cleaned_data)
#			products.objects.create(title=my_new_title)
#		else:
#			print(my_form.errors)
#	context={		'form': my_form
#	}
#	return render(request,"create.html",context)		






#def products_create_view(request):
#    if request.method=="POST":
#    	my_new_title=request.POST.get('title')
#    	print(my_new_title)
#    context={}
#    return render(request,"create.html",context)


def products_delete_view(request,my_id):
	print("aslkdjalsjdlk")
	obj=get_object_or_404(products,id=my_id)
	if request.method=="POST":
		obj.delete()
		return redirect('../../')
	context={
	    'objects': obj
	}
	return render(request,"products_delete.html",context)  







def dynamic_lookup_view(request,my_id):
	obj=get_object_or_404(products,id=my_id)
	obj=products.objects.get(id=my_id)

	try:
		obj=products.objects.get(id=my_id)
	except product.DoesNotExist:
		raise Http404
	context={
	   "objects":obj
	}
	return render(request,"detail.html",context)









def render_initial_data(request):
	initial_data={
	    'title': "this is my new title"
	}
	obj=products.objects.get(id=1)
	form=ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
	context={
	'form': form
	}
	return render(request,"create.html",context)


def products_create_view(request):
	form=ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form=ProductForm()

	context={
	'form': form
	}
	return render(request,"create.html",context)
def products_detail_view(request):
   obj=products.objects.get(id=1)
   context={
   'objects':obj
   }			
   return render(request,"detail.html",context)
