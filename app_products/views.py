from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms
from django.views import View


# products
class ListProducts(View):
    def get(self, request):
        products = models.Products.objects.all()
        context = {
            'products': products
        }
        return render(request, 'dashboard.html', context=context)


class AddProducts(View):
    def get(self, request):
        prod_form = forms.AddProductForm()
        context = {
            'prod_form': prod_form
        }
        return render(request, 'add_product.html', context=context)

    def post(self, request):
        prod_form = forms.AddProductForm(request.POST, request.FILES)
        if prod_form.is_valid():
            product = prod_form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('ListProducts')
        else:
            context = {
                'prod_form': prod_form
            }
            return render(request, 'add_product.html', context=context)


class EditProduct(View):
    def get(self, request, pk):
        product = models.Products.objects.get(pk=pk)
        prod_edit_form = forms.EditProductForm(instance=product)
        context = {
            'prod_edit_form': prod_edit_form
        }
        return render(request, 'edit_product.html', context=context)

    def post(self, request, pk):
        product = models.Products.objects.get(pk=pk)
        prod_edit_form = forms.EditProductForm(request.POST, request.FILES, instance=product)
        if prod_edit_form.is_valid():
            product = prod_edit_form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('ProductDetails', pk=product.id)


def delete_product(request, pk):
    obj = get_object_or_404(models.Products, pk=pk)
    if request.method == 'POST' or 'GET':
        obj.delete()
        return redirect('ListProducts')


class ProductDetails(View):
    def get(self, request, pk):
        product = models.Products.objects.get(pk=pk)
        comments = models.Comments.objects.filter(product=pk)
        context = {
            'comments': comments,
            'product': product
        }
        return render(request, 'product_details.html', context=context)


# profile
class MyProfile(View):
    def get(self, request, pk):
        my_profile = models.Accounts.objects.get(pk=pk)
        context = {
            'my_profile': my_profile
        }
        return render(request, 'my_profile.html', context=context)


class Profile(View):
    def get(self, request, pk):
        profile = models.Accounts.objects.get(pk=pk)
        context = {
            'profile': profile
        }
        return render(request, 'profile.html', context=context)


class EditProfile(View):
    def get(self, request, pk):
        profile = models.Accounts.objects.get(pk=pk)
        edit_profile_form = forms.EditProfileForm(instance=profile)
        context = {
            'edit_profile_form': edit_profile_form
        }
        return render(request, 'edit_profile.html', context=context)

    def post(self, request, pk):
        profile = models.Accounts.objects.get(pk=pk)
        edit_profile_form = forms.EditProfileForm(request.POST, instance=profile)
        if edit_profile_form.is_valid():
            user = edit_profile_form.save(commit=False)
            password = edit_profile_form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('MyProfile', pk=profile.id)
        else:
            context = {
                'edit_profile_form': edit_profile_form
            }
            return render(request, 'edit_profile.html', context=context)


# comment
class AddComment(LoginRequiredMixin, View):
    def get(self, request, pk):
        product = models.Products.objects.get(pk=pk)
        add_comment_form = forms.AddCommentForm()
        context = {
            'product': product,
            'add_comment_form': add_comment_form
        }
        return render(request, 'add_comment.html', context=context)

    def post(self, request, pk):
        product = models.Products.objects.get(pk=pk)
        add_comment_form = forms.AddCommentForm(request.POST)
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.account = request.user
            comment.product_id = product.id
            comment.save()
            return redirect('ProductDetails', pk=pk)
        else:
            context = {
                'add_comment_form': add_comment_form
            }
            return render(request, 'add_comment.html', context=context)


class EditComment(View):
    def get(self, request, pk):
        comment = models.Comments.objects.get(pk=pk)
        comment_edit_form = forms.EditCommentForm(instance=comment)
        context = {
            'comment_edit_form': comment_edit_form
        }
        return render(request, 'edit_comment.html', context=context)

    def post(self, request, pk):
        comment = models.Comments.objects.get(pk=pk)
        comment_edit_form = forms.EditCommentForm(request.POST, instance=comment)
        if comment_edit_form.is_valid():
            comment = comment_edit_form.save(commit=False)
            comment.account = request.user
            comment.product_id = comment.product_id
            comment.save()
            return redirect('ProductDetails', pk=pk)
        else:
            context = {
                'comment_edit_form': comment_edit_form
            }
            return render(request, 'edit_comment.html', context=context)


def delete_comment(request, pk):
    obj = get_object_or_404(models.Comments, pk=pk)
    if request.method == 'POST' or 'GET':
        obj.delete()
        print('function is working =======================')
        return redirect('ListProducts')


class ListCategories(View):
    def get(self, request):
        categories = models.Categories.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'list_categories.html', context=context)


class FilterCategories(View):
    def get(self, request, pk):
        products = models.Products.objects.filter(category=pk)
        context = {
            'products': products
        }
        print(products)
        return render(request, 'products.html', context=context)
