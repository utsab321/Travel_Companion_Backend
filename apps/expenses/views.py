from django.shortcuts import render ,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Expenses
from .serializers import ExpenseSerializer
from trips.models import Trip
from django.contrib import messages
from .forms import ExpenseForm


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 🔒 Only return logged-in user's expenses
        return Expenses.objects.filter(paid_by=self.request.user.userprofile)

    def perform_create(self, serializer):
        # 🔥 Auto assign logged-in user
        serializer.save(paid_by=self.request.user.userprofile)

# Create your views here.
@login_required
def add_expense(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
   
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        
        if form.is_valid():
            expense=form.save(commit=False)
            expense.trip = trip
            expense.paid_by = request.user.userprofile
            expense.save()

            expense.split_among.set(trip.participants.all())

            messages.success(request,f"Expense '{expense.description}' of {expense.amount} added!")
            return redirect ('trip_detail', trip_id= trip.id)
        else:
            # Pre- fill The form nicely
            form = ExpenseForm(initial={
                'paid_by' : request.user.userprofile,

            })

            return render (request, 'expenses/add_expense.html',{
                'form' :form,
                'trip' :trip,
                'title': f"Add expense to {trip.title}",
            })
