from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, DeleteView, DetailView, ListView
from . models import*
from deliveries.models import Stock, Delivery
from suppliers.models import Supplier
from .forms import*
from django.conf import settings
from django.db.models import Sum
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from sales.models import Sale 
import json
from products.models import Product

# Create your views here.

# class CreateExpenseCategory(PermissionRequiredMixin, CreateView):
#     permission_required = ['expense.add_expense_category']
#     raise_exception = True
#     permission_denied_message = "You dont have permission to add customers"
#     model = ExpenseCategory
#     template_name = 'expense/add_expense_category.html'
#     form_class = CreateExpenseCategoryForm

#     def get_context_data(self, **kwargs):

#         context = super().get_context_data(**kwargs)

#         category_list = ExpenseCategory.objects.all().order_by('-pk')[:10]

#         categorys = []
#         num = 0

#         for category in category_list:
#             num = num + 1

#             categorys.append({
#                 'num': num,
#                 'pk': category.pk,
#                 'name': category.name,
#             })

#         context['categorys'] = categorys

#         return context

#     def get_success_url(self):

#         messages.success(self.request, 'Success, new expense categories created', extra_tags='alert alert-success')

#         return reverse_lazy('expense:create-expesne-category')
    


# class CreateExpense(PermissionRequiredMixin, CreateView):
#     permission_required = ['expense.add_expense']
#     raise_exception = True
#     permission_denied_message = "You dont have permission to add customers"
#     model = Expense
#     template_name = 'expense/add_expense.html'
#     form_class = CreateExpenseForm

#     def get_context_data(self, **kwargs):

#         context = super().get_context_data(**kwargs)

#         expense_list = Expense.objects.all().order_by('-pk')[:10]
#         total_sum = sum([item.price_total_amount for item in expense_list])

#         expenses = []
#         num = 0

#         for expense in expense_list:
#             num = num + 1

#             expenses.append({
#                 'num': num,
#                 'pk': expense.pk,
#                 'name': expense.name,
#                 'staff': expense.staff,
#                 'batch' : expense.branch,
#                 'amount':expense.amount,
#                 'quantity': expense.quantity,
#                 'category': expense.category 
#             })

#         context['expenses'] = expenses
#         context['total_sum '] = total_sum 

#         return context

#     def get_success_url(self):

#         messages.success(self.request, 'Success, new expense created', extra_tags='alert alert-success')

#         return reverse_lazy('expense:add-expesne')



def CreateExpense(request):
    category = Product.objects.all().filter(status="SERVICE")
    expense = Expense.objects.all().filter(staff=request.user).order_by('-pk')[:10]
    total_sum = sum([item.price_total_amount for item in expense])
    context = {
        'category':category,
        'values': request.POST,
        'expense':expense,
        'total_sum':total_sum
    
        }
    if request.method == 'GET':
        return render(request, 'expense/add_expense.html', context=context)
    
        

    if request.method == 'POST':
        name = request.POST['name']
        if not name:
            messages.error(request, 'Name is required')
            return render(request, 'expense/add_expense.html')  
    if request.method == 'POST':
        amount = request.POST['amount']
        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expense/add_expense.html')
        
    if request.method == 'POST':
        description = request.POST['description']
        quantity = request.POST['quantity']
        branch = request.POST['branch']
        total_amount = int(amount) * int(quantity)
        

    if request.method == 'POST':
        if not quantity:
            messages.error(request, 'Quantity is required')
            return render(request, 'expense/add_expense.html')
        

        
        Expense.objects.create(quantity=quantity, staff=request.user, branch=branch, name=name, description=description, amount=amount,total_amount=total_amount)
        messages.success(request, 'Success, new expense created', extra_tags='alert alert-success')

    
        return redirect('expense:add-expesne')
    
class ExpenseReportsHome(PermissionRequiredMixin, FormView):
    permission_required = ["expense.view_expense"]
    raise_exception = True
    permission_denied_message = "You dont have permission to view sales"
    template_name = 'expense/expense_report.html'
    form_class = ExpenseFiltersForm

    def post(self, request, *args, **kwargs):

        context = super().get_context_data(**kwargs)

        form = self.form_class(data=request.POST)

        if form.is_valid():
            context['expense_list'] = Expense.objects.filter(
                created__gte=str(form.cleaned_data['date_from']) + " 00:00:00",
                created__lte=str(form.cleaned_data['date_to']) + " 23:59:59",
                branch=form.cleaned_data['branch']
            )

            context['sum'] = context['expense_list'].aggregate(Sum('total_amount'))

        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):

        context = super().get_context_data(**kwargs)

        if request.GET.get("date_from"):

            context['expense_list'] = Expense.objects.filter(
                datetime__gte=request.GET.get("date_from"),
                datetime__lte=request.GET.get("date_to"),
                branch=request.GET.get("branch")
            )
        else:
            context['expense_list'] = Expense.objects.all()

        context['sum'] = context['expense_list'].aggregate(Sum('total_amount'))

        return render(request, self.template_name, context=context)
    

@login_required(login_url="/accounts/login/")
def ListExpense(request):
    expenses = Expense.objects.all().order_by('-pk')[:10]
    total_sum = sum([item.price_total_amount for item in expenses])
   
    context = {
        "expenses":expenses,
        "total_sum":total_sum
        
    }
    return render(request, "expense/expense.html", context)




class ProfitLossReportsHome(PermissionRequiredMixin, FormView):
    permission_required = ["profit_loss.view_profit_loss"]
    raise_exception = True
    permission_denied_message = "You dont have permission to view sales"
    template_name = 'profit_loss/profit_loss.html'
    form_class =  ProfitLoassFiltersForm

    def post(self, request, *args, **kwargs):

        context = super().get_context_data(**kwargs)

        form = self.form_class(data=request.POST)

        if form.is_valid():

            context['sale_list'] = Sale.objects.filter(
                datetime__gte=str(form.cleaned_data['date_from']) + " 00:00:00",
                datetime__lte=str(form.cleaned_data['date_to']) + " 23:59:59",
                branch_id=form.cleaned_data['branch']
            )

            context['sum'] = context['sale_list'].aggregate(Sum('total'))

        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):

        context = super().get_context_data(**kwargs)

        if request.GET.get("date_from"):

            context['sale_list'] = Sale.objects.filter(
                datetime__gte=request.GET.get("date_from"),
                datetime__lte=request.GET.get("date_to"),
                branch_id=request.GET.get("branch")
            )
        else:
            context['sale_list'] = Sale.objects.all()

        context['sum'] = context['sale_list'].aggregate(Sum('total'))

        return render(request, self.template_name, context=context)
