from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from adminapp.forms import ProductCategoryEditForm, ProductEditForm
from products.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.order_by('-is_active').all()

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'категории/создание'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('myadmin:categories'))
    else:
        category_form = ProductCategoryEditForm()

    content = {'title': title, 'update_form': category_form}

    return render(request, 'category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'категории/редактирование'

    edit_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('myadmin:categories'))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'категории/удаление'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('myadmin:categories'))

    content = {'title': title, 'category_to_delete': category}

    return render(request, 'category_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукты'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'админка/продукты/создание'

    if request.method == 'POST':
        products_form = ProductEditForm(request.POST, request.FILES)
        if products_form.is_valid():
            products_form.save()
            return HttpResponseRedirect(reverse('myadmin:categories'))
    else:
        products_form = ProductEditForm()

    content = {'title': title, 'update_form': products_form}

    return render(request, 'products_create.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    title = 'админка/продукты'

    product = Product.objects.get(pk=pk)

    content = {
        'title': title,
        'object': product
    }
    return render(request, 'products_read.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'админка/продукты/создание'

    edit_product = get_object_or_404(Product, pk=pk)
    print(edit_product.pk)
    if request.method == 'POST':
        products_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if products_form.is_valid():
            products_form.save()
            return HttpResponseRedirect(reverse('myadmin:products', kwargs={'pk': edit_product.category_id}))
    else:
        products_form = ProductEditForm(instance=edit_product)

    content = {'title': title, 'update_form': products_form}

    return render(request, 'products_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'админка/продукты/удаление'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('myadmin:products', kwargs={'pk': product.category_id}))

    content = {'title': title, 'product_to_delete': product}

    return render(request, 'products_delete.html', content)
