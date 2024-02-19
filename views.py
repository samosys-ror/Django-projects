# This class show the home page 
class HomeView(TemplateView):
    template_name = "home/index.html"
    
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Login function starts
def login(request):
    if request.method ==  'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect ('home')
        else:
            messages.error(request,"Invalid email or password.")
    form = AuthenticationForm()            
    return render (request,"home/login.html",{"form":form})

# Login function ends 


# Logout function starts 

def logout_request(request):
    logout(request)
    return redirect('login')

# Logout function ends 


# Order list function starts
def order_list(request):
    id = request.GET.get("id")
    if id:
        try:
            order = Order.objects.get(id=id)
            course_name = str(order.course_name)
            topic = str(order.topic)
            payment_method = int(order.payment_method)   
            created_at = order.created_at.strftime("%Y-%m-%d %I:%M %p")
            data = {
                "course_name": course_name,
                "topic": topic,
                "transaction_id": order.transaction_id,
                "first_name": order.first_name,
                "last_name": order.last_name,
                "email": order.email,
                "phone": order.phone,
                "country": order.country,
                "state": order.state,
                "city": order.city,
                "timezone": order.timezone,
                "postcode": order.postcode,
                "company_name": order.company_name,
                "coaching_topic": order.coaching_topic,
                "purchase_status": order.purchase_status,
                "payment_method": payment_method,
                "subtotal_price": order.subtotal_price,
                "tax_price": order.tax_price,
                "total_price": order.total_price,
                "created_at": created_at,
            }
            return JsonResponse({'data': data})
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Invalid id'}) 
    form = OrderForm()
    orders = Order.objects.all()
    context = {"orders":orders,"form":form}
    return render (request,"order/order_list.html",context) 

# Order list function ends


# Order create function starts

def order_create(request):
    if request.method == "POST":  
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'order added successfully'})
        else:
            return JsonResponse({'error': 'Invalid data'}) 
    else:
        return JsonResponse({'error': 'Invalid request'})    

# Order create function ends

# Order update function starts
def order_update(request):
    if request.method == "POST":
        id = request.POST.get('id')
        if id :
            try:
                order_obj = Order.objects.get(id=id)
                form = OrderForm(request.POST,instance=order_obj)
                if form.is_valid():
                    form.save()
                    return JsonResponse({'message': 'Order updated successfully'})
                else:
                    return JsonResponse({'error': 'Invalid data'})  
            except Course.DoesNotExist:
                return JsonResponse({'error': 'Invalid id'}) 
        else: 
            return JsonResponse({'error': 'Invalid id'})
    else:    
        return JsonResponse({'error': 'Invalid request'})        

# Order update function ends


# Order delete function starts

def order_delete(request):
    if request.method == "POST":
        id = request.POST.get('id')
        if id:
            try:
                brand_obj = Order.objects.get(id=id)
                brand_obj.delete()
                return JsonResponse({'message': 'Order deleted successfully'})
            except Course.DoesNotExist:
                return JsonResponse({'error': 'Invalid id'}) 
        else: 
            return JsonResponse({'error': 'Invalid id'})
    else:    
        return JsonResponse({'error': 'Invalid request'})
          
# Order delete function ends
