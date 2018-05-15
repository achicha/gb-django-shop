from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from adminapp.forms import ProductCategoryEditForm, ProductEditForm
from products.models import ProductCategory, Product

class ProductCategoryView(UserPassesTestMixin, ListView):
    model = ProductCategory
    template_name = 'categories.html'
    success_url = reverse_lazy('myadmin:categories')
    fields = ('__all__')

    def test_func(self):
        """if user passed that test, then let allow him to use admin panel"""
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/категории'
        return context

    def get_queryset(self):
        # show only active categories
        query_set = self.model.objects.filter(is_active=1)
        return query_set

# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     title = 'админка/категории'
#
#     categories_list = ProductCategory.objects.order_by('-is_active').all()
#
#     content = {
#         'title': title,
#         'objects': categories_list
#     }
#
#     return render(request, 'categories.html', content)

class ProductCategoryCreateView(UserPassesTestMixin, CreateView):
    model = ProductCategory
    template_name = 'category_update.html'
    success_url = reverse_lazy('myadmin:categories')
    fields = ('__all__')

    def test_func(self):
        """if user passed that test, then let allow him to use admin panel"""
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/создание'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     title = 'категории/создание'
#
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('myadmin:categories'))
#     else:
#         category_form = ProductCategoryEditForm()
#
#     content = {'title': title, 'update_form': category_form}
#
#     return render(request, 'category_update.html', content)

class ProductCategoryUpdateView(UserPassesTestMixin, UpdateView):
    model = ProductCategory
    template_name = 'category_update.html'
    success_url = reverse_lazy('myadmin:categories')
    fields = ('__all__')

    def test_func(self):
        """if user passed that test, then let allow him to use admin panel"""
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = 'категории/редактирование'
#
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('myadmin:categories'))
#     else:
#         edit_form = ProductCategoryEditForm(instance=edit_category)
#
#     content = {'title': title, 'update_form': edit_form}
#
#     return render(request, 'category_update.html', content)

class ProductCategoryDeleteView(UserPassesTestMixin, DeleteView):
    model = ProductCategory
    template_name = 'category_delete.html'
    success_url = reverse_lazy('myadmin:categories')
    fields = ('__all__')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        """if user passed that test, then let allow him to use admin panel"""
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/удаление'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     title = 'категории/удаление'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('myadmin:categories'))
#
#     content = {'title': title, 'category_to_delete': category}
#
#     return render(request, 'category_delete.html', content)

class ProductView(UserPassesTestMixin, ListView):
    model = Product
    template_name = 'products_base.html'
    success_url = reverse_lazy('myadmin:products')
    paginate_by = 2
    fields = ('__all__')

    def test_func(self):
        """if user passed that test, then let allow him to use admin panel"""
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # add title to context manager
        context['title'] = 'админка/продукты'

        # paginate by page
        list_products = Product.objects.filter(category=self.kwargs.get('pk'), is_active=1)
        paginator = Paginator(list_products, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
        context['current_page'] = file_exams

        return context

    def get_queryset(self):
        # show only products from our category
        query_set = self.model.objects.filter(category=self.kwargs.get('pk'), is_active=1)
        return query_set

# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk):
#     title = 'админка/продукты'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     content = {
#         'title': title,
#         'category': category,
#         'objects': products_list,
#     }
#
#     return render(request, 'products_base.html', content)

class ProductCreateView(UserPassesTestMixin, CreateView):
    model = Product
    template_name = 'products_update.html'
    success_url = reverse_lazy('myadmin:products', kwargs={'pk': model.objects.last().category_id})
    fields = ('__all__')

    def test_func(self):
        """if user passed that test, then let allow him to use admin panel"""
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/продукты/создание'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     title = 'админка/продукты/создание'
#
#     if request.method == 'POST':
#         products_form = ProductEditForm(request.POST, request.FILES)
#         if products_form.is_valid():
#             products_form.save()
#             return HttpResponseRedirect(reverse('myadmin:categories'))
#     else:
#         products_form = ProductEditForm()
#
#     content = {'title': title, 'update_form': products_form}
#
#     return render(request, 'products_create.html', content)

class ProductDetailView(UserPassesTestMixin, DetailView):
    model = Product
    template_name = 'products_read.html'
    success_url = reverse_lazy('myadmin:products', kwargs={'pk': model.objects.last().category_id})
    fields = ('__all__')

    def test_func(self):
        """if user passed that test, then let allow him to use admin panel"""
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/продукты/описание'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     title = 'админка/продукты'
#
#     product = Product.objects.get(pk=pk)
#
#     content = {
#         'title': title,
#         'object': product
#     }
#     return render(request, 'products_read.html', content)

class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'products_update.html'
    success_url = reverse_lazy('myadmin:products', kwargs={'pk': model.objects.last().category_id})
    fields = ('__all__')

    def test_func(self):
        """if user passed that test, then let allow him to use admin panel"""
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/продукты/редактирование'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     title = 'админка/продукты/создание'
#
#     edit_product = get_object_or_404(Product, pk=pk)
#     print(edit_product.pk)
#     if request.method == 'POST':
#         products_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#         if products_form.is_valid():
#             products_form.save()
#             return HttpResponseRedirect(reverse('myadmin:products', kwargs={'pk': edit_product.category_id}))
#     else:
#         products_form = ProductEditForm(instance=edit_product)
#
#     content = {'title': title, 'update_form': products_form}
#
#     return render(request, 'products_update.html', content)

class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'products_delete.html'
    success_url = reverse_lazy('myadmin:categories')
    fields = ('__all__')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        """if user passed that test, then let allow him to use admin panel"""
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админки/продукты/удаление'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'админка/продукты/удаление'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('myadmin:products', kwargs={'pk': product.category_id}))
#
#     content = {'title': title, 'product_to_delete': product}
#
#     return render(request, 'products_delete.html', content)
