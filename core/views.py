from django.shortcuts import render, redirect

from item.models import Category, Item
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignupForm
import random
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })
from django.http import HttpResponse
from openpyxl import Workbook
from item.models import UserActivity
def contact(request):
    return render(request, 'core/contact.html')
from django.shortcuts import render
def export_user_activity_to_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="user_activity_export.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.append(['User', 'Product Category', 'Price Range', 'Timestamp'])

    # Fetch UserActivity data and write to Excel
    user_activities = UserActivity.objects.all()
    for obj in user_activities:
        timestamp_naive = obj.timestamp.replace(tzinfo=None) 
        ws.append([obj.user.username, obj.product_category, obj.price_range, timestamp_naive])

    wb.save(response)
    return response
def custom_404_view(request, exception):
    return render(request, 'core/404.html', status=404)
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            c_otp = random.randint(1000, 9999)
            message = f'Hi your OTP is {c_otp}.'
            subject = 'BlogSpot Registration.'
            from_email = settings.EMAIL_HOST_USER
        
            send_mail(subject, message, from_email,[form.cleaned_data['email']])
            request.session['form_data'] = form.cleaned_data
            request.session['stored_otp'] = c_otp
            return render(request, 'core/otp.html')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
def otp_verification(request):
    if request.method == 'POST':
        print("running")
        print(request.POST.get('hidden_field'))
        user_entered_otp = request.POST.get('otp')
        print(user_entered_otp)
        session_data = dict(request.session.items())
        stored_otp = session_data.get('stored_otp')
        print(stored_otp)
        if stored_otp==int(user_entered_otp):
            form_data = request.session.get('form_data')
            form = SignupForm(form_data)
            if form.is_valid():
                print("valid")
                form.save()
            return redirect('/login/')
        else:
            return render(request, 'core/otp.html', {'error_message': 'Incorrect OTP. Please try again.'})
