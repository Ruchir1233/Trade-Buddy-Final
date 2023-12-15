from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import NewItemForm, EditItemForm
from .models import Category, Item,UserActivity
from django.template.loader import render_to_string
from django.shortcuts import render
from django.db.models import Q
from datetime import datetime, timezone
from .models import Item, Category  # Update 'models' import to match your app
from django.http import HttpResponse
from openpyxl import Workbook
from .models import UserActivity
from item.models import UserPreferences
import pandas as pd
from itertools import chain
from django.shortcuts import render
# from your_app.models import UserPreferences  # Import your UserPreferences model
import pandas as pd
def export_user_activity_to_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="user_activity_export.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.append(['User', 'Product Category', 'Price Range', 'Timestamp'])

    # Fetch UserActivity data and write to Excel
    user_activities = UserActivity.objects.all()
    for obj in user_activities:
        ws.append([obj.user.username, obj.product_category, obj.price_range, obj.timestamp])

    wb.save(response)
    return response

# def items(request):
    

#     # Load data into DataFrame (adjust file path accordingly)
#     file_path = r'C:\Users\pankt\OneDrive\Desktop\Manipal-Marketplace-main\generated_data.xlsx'
#     data = pd.read_excel(file_path)

#     # Grouping users by preferences (top 3 categories)
#     top_categories_per_user = data.groupby('Username')['Product Category'].apply(lambda x: x.value_counts().index[:3].tolist())

#     # Displaying Top 3 Categories per User
#     for user, top_categories in top_categories_per_user.items():
#         print(f"User: {user}, Top 3 Categories: {top_categories}")
#     for user, top_categories in top_categories_per_user.items():
#         user_preferences = UserPreferences(username=user, top_categories=','.join(top_categories))
#         user_preferences.save()
#     query = request.GET.get('query', '')
#     query = request.GET.get('query', '')
#     category_id = request.GET.get('category')
#     min_price = request.GET.get('min_price')
#     max_price = request.GET.get('max_price')

#     categories = Category.objects.all()
#     items = Item.objects.filter(is_sold=False)

#     if category_id is not None and category_id != '0':
#         items = items.filter(category_id=category_id)

#     if query:
#         items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

#     if min_price:
#         try:
#             min_price = float(min_price)
#             items = items.filter(price__gte=min_price)
#         except ValueError:
#             pass

#     if max_price:
#         try:
#             max_price = float(max_price)
#             items = items.filter(price__lte=max_price)
#         except ValueError:
#             pass

#     return render(request, 'item/items.html', {
#         'items': items,
#         'query': query,
#         'categories': categories,
#         'category_id': int(category_id) if category_id is not None else 0
#     })




# def items(request):
#     # Load data into DataFrame (adjust file path accordingly)
#     file_path = r'C:\Users\pankt\OneDrive\Desktop\Manipal-Marketplace-main\generated_data.xlsx'
#     data = pd.read_excel(file_path)

#     # Grouping users by preferences (top 3 categories)
#     top_categories_per_user = data.groupby('Username')['Product Category'].apply(lambda x: x.value_counts().index[:3].tolist())

#     # Save top categories per user to UserPreferences model
#     for user, top_categories in top_categories_per_user.items():
#         user_preferences = UserPreferences.objects.create(username=user, top_categories=','.join(top_categories))

#     query = request.GET.get('query', '')
#     category_id = request.GET.get('category')
#     min_price = request.GET.get('min_price')
#     max_price = request.GET.get('max_price')

#     categories = Category.objects.all()
#     items = Item.objects.filter(is_sold=False)

#     # Filtering items based on query parameters
#     if category_id is not None and category_id != '0':
#         items = items.filter(category_id=category_id)

#     if query:
#         items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

#     if min_price:
#         try:
#             min_price = float(min_price)
#             items = items.filter(price__gte=min_price)
#         except ValueError:
#             pass

#     if max_price:
#         try:
#             max_price = float(max_price)
#             items = items.filter(price__lte=max_price)
#         except ValueError:
#             pass

#     return render(request, 'item/items.html', {
#         'items': items,
#         'query': query,
#         'categories': categories,
#         'category_id': int(category_id) if category_id is not None else 0,
#         'top_categories_per_user': top_categories_per_user  # Pass top categories per user to the template
#     })

# def process_data():
#     print("running alwayzzz")
#     file_path = r'C:\Users\pankt\OneDrive\Desktop\Manipal-Marketplace-main\generated_data.xlsx'
#     data = pd.read_excel(file_path)

#     top_categories_per_user = data.groupby('Username')['Product Category'].apply(lambda x: x.value_counts().index[:3].tolist())

#     # Save top categories per user to UserPreferences model
#     for user, top_categories in top_categories_per_user.items():
#         UserPreferences.objects.create(username=user, top_categories=','.join(top_categories))
import openpyxl
from datetime import timedelta
from random import randint
# from your_app.models import UserActivity
#     return top_categories_per_user
def make_excel():
    # Fetch data from the database
    user_activities = UserActivity.objects.all()

    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "User Activity"

    # Add headers to the Excel file
    sheet.append(['User', 'Product Category', 'Price Range', 'Duration'])

    # Iterate through fetched data and populate the Excel file
    for activity in user_activities:
        # Generate a random duration between 30 seconds and 3 minutes
        random_duration = timedelta(seconds=randint(30, 180))

        # Add data to the Excel file
        sheet.append([
            activity.user.username,
            activity.product_category,
            activity.price_range,
            str(random_duration)
        ])

    # Save the Excel file
    workbook.save('user_activity.xlsx')
def process_data():
    make_excel()
    print("running always")
    file_path = r'C:\Users\pankt\OneDrive\Desktop\TradeBuddy\user_activity.xlsx'
    data = pd.read_excel(file_path)

    top_categories_per_user = data.groupby('User')['Product Category'].apply(lambda x: x.value_counts().index[:3].tolist())

    # Update or create top categories per user in UserPreferences model
    for user, top_categories in top_categories_per_user.items():
        try:
            user_pref = UserPreferences.objects.get(username=user)
            user_pref.top_categories = ','.join(top_categories)
            user_pref.save()
        except UserPreferences.DoesNotExist:
            UserPreferences.objects.create(username=user, top_categories=','.join(top_categories))
    # print(top_categories_per_user)
    return top_categories_per_user



# View function for rendering
def items(request):
    top_categories_per_user = process_data() 
    print(type(top_categories_per_user)) # Call the function to process data
    filter_applied = False

    query = request.GET.get('query', '')
    category_id = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    # Filtering items based on query parameters
    if category_id is not None and category_id != '0':
        items = items.filter(category_id=category_id)
        filter_applied = True

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
        filter_applied = True

    if min_price:
        try:
            min_price = float(min_price)
            items = items.filter(price__gte=min_price)
            filter_applied = True
        except ValueError:
            pass

    if max_price:
        try:
            max_price = float(max_price)
            items = items.filter(price__lte=max_price)
            filter_applied = True
        except ValueError:
            pass

    # items1 = Item.objects.filter(category__name__in=top_categories_per_userss)
    print(top_categories_per_user)

    current_user1 = request.user.username
    if current_user1 in top_categories_per_user:
        top_categories_for_user = top_categories_per_user[current_user1]
        print(f"Top categories for user {current_user1}: {top_categories_for_user}")
        items1 = Item.objects.filter(category__name__in=top_categories_for_user)
        all_items = Item.objects.filter(is_sold=False)
        remaining_items = all_items.exclude(id__in=items1)
        merged_items = list(chain(items1,remaining_items))
    else:
        print(f"No top categories found for user {current_user1}")
        
        
    top_categories_per_user_exists = top_categories_per_user.any()
    return render(request, 'item/items.html', {
        'filter_applied': filter_applied,
        'items1': items1,
        'merged_items':merged_items,
        'items': items,
        'query': query,
        'remaining_items': remaining_items,
        'categories': categories,
        'category_id': int(category_id) if category_id is not None else 0,
        'top_categories_per_user': top_categories_per_user,  # Pass top categories per user to the template
        'top_categories_per_user_exists': top_categories_per_user_exists
    })
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    if request.user.is_authenticated:
        print(type(item.category.name))
        
        activity = UserActivity.objects.create(
            user=request.user,
            product_category=item.category.name,  # Replace with actual category data
            price_range=item.price,    # Replace with actual price range data
            # timestamp_start=timezone.now()
        )
        activity.save()
        
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Item, UserActivity
import time

# def detail(request, pk):
#     print("start")
#     item = get_object_or_404(Item, pk=pk)
#     related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    
#     timestamp_start = None
    
#     if request.user.is_authenticated:
#         timestamp_start = timezone.now()
        
#     context = {
#         'item': item,
#         'related_items': related_items
#     }

#     if request.user.is_authenticated:
#         # Introduce a delay to simulate user interaction
#         time.sleep(1)  # Sleep for 1 second
#         print("runningmcbxhrj")
#         return record_user_activity(request, item, timestamp_start, context)
#     else:
#         return render(request, 'item/detail.html', context)

# def record_user_activity(request, item, timestamp_start, context):
#     print("startsis")
#     timestamp_end = timezone.now()
#     duration = timestamp_end - timestamp_start

#     activity = UserActivity.objects.create(
#         user=request.user,
#         product_category=item.category.name,
#         price_range=item.price,
#         timestamp_start=timestamp_start,
#         timestamp_end=timestamp_end,
#         duration=duration
#     )
#     print("Runninf")
#     activity.save()

#     return render(request, 'item/detail.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        # request.FILES -> to get the files that user uploads
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            user_email = request.user.email
    
            user_emails=[]
            user_emails.append(user_email)
            print(user_emails)
            message = 'Hi your OTP is'
            subject = 'BlogSpot Registration.'
            from_email = settings.EMAIL_HOST_USER
            print(request.session.get('email'))
            # send_mail(subject, message, from_email,user_emails)
            email_context = {
                'item_name': item.name,
                'item_description': item.description,
                'item_price': item.price,
                'site_url':('/www.tradebuddy.com'),
                'item_image':" https://127.0.0.1:8000/media/item_images/p4_GV0H5kV.jpg"  # Your website URL
                # You might need to adjust these variables based on your Item model fields
            }
            html_message = render_to_string('item/mailtemplate.html', email_context)
            send_mail(subject, '', from_email,user_emails, html_message=html_message)
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
@login_required
def activate_ad(request, pk):
    ad = get_object_or_404(Item, pk=pk)
    ad.keepactive = True
    ad.save()
    print("runiing")
    return redirect(request.META.get('HTTP_REFERER'))

def deactivate_ad(request, pk):
    ad = get_object_or_404(Item, pk=pk)
    ad.keepactive = False
    ad.save()
    return redirect(request.META.get('HTTP_REFERER'))