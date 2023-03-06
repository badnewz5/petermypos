from django.urls import path
from expesne import views

app_name = 'expense'

urlpatterns = [
    path('expense/', views.ListExpense, name='expesne'),
    path('add_expense/', views.CreateExpense, name='add-expesne'),
    path('expense-report', views.ExpenseReportsHome.as_view(), name="expense-report"),
    path('profit-loss-report', views.ProfitLossReportsHome.as_view(), name="profit-loss-report"),

]
