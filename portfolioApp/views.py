from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage
# from django.shortcuts import render



def index(request):
    return render(request, "index.html")

#login view.py
def login(request):
    msg = ""
    if(request.POST):
        email = request.POST.get("txtEmail")
        pwd = request.POST.get("txtPassword")
        user = authenticate(username=email, password=pwd)
        if user is not None:
            request.session['email'] = email
            if user.is_active:
                if user.userType == 'Admin':
                    return HttpResponseRedirect("/adminhome")
                elif user.userType == 'Customer':
                    cust = Customer.objects.get(email=email)
                    request.session['id'] = cust.id
                    request.session['name'] = cust.name
                    return HttpResponseRedirect("/publichome")

                elif user.userType == 'Staff':
                    stf = Photo.objects.get(email=email)
                    request.session['id'] = stf.id
                    request.session['name'] = stf.name
                    return HttpResponseRedirect("/staffhome")
                elif user.userType == 'makeup':
                    stf = MakeUp.objects.get(email=email)
                    request.session['id'] = stf.id
                    request.session['name'] = stf.name
                    return HttpResponseRedirect("/makeuphome")
                elif user.userType == 'content':
                    stf = Content.objects.get(email=email)
                    request.session['id'] = stf.id
                    request.session['name'] = stf.name
                    return HttpResponseRedirect("/concrehome")
            else:
                msg = "You are not authenticated to login"
        else:
            msg = "User doesnt exist"
    return render(request, "login.html", {"msg": msg})


#Customer registration
def registration(request):
    msg = ""
    if(request.POST):
        name = request.POST['txtName']
        lname = request.POST['txtLname']
        dob = request.POST['dob']
        state = request.POST['state']
        district = request.POST['district']
        pin = request.POST['pin']
        houseno = request.POST['houseno']
        gender = request.POST['gender']
        address = request.POST['txtAddress']
        email = request.POST['txtEmail']
        contact = request.POST['txtContact']
        pwd = request.POST['txtPassword']

        try:
            user = CustomUser.objects.create_user(
                username=email, password=pwd, is_active=1, userType='Customer')
            user.save()
            c = Customer.objects.create(
                name=name, address=address, contact=contact, email=email, user=user, lname=lname, district=district, state=state, pin=pin, houseno=houseno, gender=gender, dob=dob)
            c.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Registration successfull."
    return render(request, "registration.html", {"msg": msg})




#customer edit
def editregistration(request,id):
    cust=Customer.objects.filter(id=id)
    return render(request,'editcust.html', { 'dtls': cust})

def editcust(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        name = request.POST.get('txtName')
        lname = request.POST.get('txtLname')
        dob = request.POST.get('dob')
        state = request.POST.get('state')
        district = request.POST.get('district')
        pin = request.POST.get('pin')
        houseno = request.POST.get('houseno')
        gender = request.POST.get('gender')
        address = request.POST.get('txtAddress')
        email = request.POST.get('txtEmail')
        contact = request.POST.get('txtContact')
        pwd = request.POST.get('txtPassword')

        try:
            # Retrieve the existing customer object by ID
            c = Customer.objects.get(id=id)
            # Update the attributes
            c.name = name
            c.lname = lname
            c.dob = dob
            c.state = state
            c.district = district
            c.pin = pin
            c.houseno = houseno
            c.gender = gender
            c.address = address
            c.email = email
            c.contact = contact
            c.password = pwd
            # Save the updated object
            c.save()
            msg = "Update successful."
            # Redirect to adminvpublic.html after successful update
            return redirect('adminvPublic')
        except Customer.DoesNotExist:
            msg = "Customer does not exist."
        except Exception as e:
            msg = f"Error updating customer: {str(e)}"
    else:
        msg = "Invalid request method."

    # Render registration.html with a message
    return render(request, "adminvPublic.html", {"msg": msg})





#photographer edit
def editphoto(request,id):
    photo=Photo.objects.filter(id=id)
    return render(request,'editphoto.html', { 'photo': photo})

def edit_photo(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        name = request.POST.get('txtName')
        lname = request.POST.get('txtLname')
        dob = request.POST.get('dob')
        state = request.POST.get('state')
        district = request.POST.get('district')
        pin = request.POST.get('pin')
        houseno = request.POST.get('houseno')
        gender = request.POST.get('gender')
        address = request.POST.get('txtAddress')
        email = request.POST.get('txtEmail')
        contact = request.POST.get('txtContact')
        pwd = request.POST.get('txtPassword')

        try:
            # Retrieve the existing customer object by ID
            p = Photo.objects.get(id=id)
            # Update the attributes
            p.name = name
            p.lname = lname
            p.dob = dob
            p.state = state
            p.district = district
            p.pin = pin
            p.houseno = houseno
            p.gender = gender
            p.address = address
            p.email = email
            p.contact = contact
            p.password = pwd
            # Save the updated object
            p.save()
            msg = "Update successful."
            # Redirect to adminphoto.html after successful update
            return redirect('adminphoto')
        except Photo.DoesNotExist:
            msg = "Photographer does not exist."
        except Exception as e:
            msg = f"Error updating Photographer: {str(e)}"
    else:
        msg = "Invalid request method."

    # Render registration.html with a message
    return render(request, "adminphoto.html", {"msg": msg})





#content creator edit
def editconcre(request,id):
    con=Content.objects.filter(id=id)
    return render(request,'editconcre.html', { 'concre': con})

def edit_concre(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        name = request.POST.get('txtName')
        lname = request.POST.get('txtLname')
        dob = request.POST.get('dob')
        state = request.POST.get('state')
        district = request.POST.get('district')
        pin = request.POST.get('pin')
        houseno = request.POST.get('houseno')
        gender = request.POST.get('gender')
        address = request.POST.get('txtAddress')
        email = request.POST.get('txtEmail')
        contact = request.POST.get('txtContact')
        pwd = request.POST.get('txtPassword')

        try:
            # Retrieve the existing content creator object by ID
            c = Content.objects.get(id=id)
            # Update the attributes
            c.name = name
            c.lname = lname
            c.dob = dob
            c.state = state
            c.district = district
            c.pin = pin
            c.houseno = houseno
            c.gender = gender
            c.address = address
            c.email = email
            c.contact = contact
            c.password = pwd
            # Save the updated object
            c.save()
            msg = "Update successful."
            # Redirect to adminconcre.html after successful update
            return redirect('adminconcre')
        except Content.DoesNotExist:
            msg = "content creator does not exist."
        except Exception as e:
            msg = f"Error updating content creator: {str(e)}"
    else:
        msg = "Invalid request method."

    # Render registration.html with a message
    return render(request, "adminconcre.html", {"msg": msg})





#Makeup Artists edit
def makeUpReg(request):
    msg = ""
    if(request.POST):
        name = request.POST['txtName']
        lname = request.POST['txtLname']
        dob = request.POST['dob']
        state = request.POST['state']
        district = request.POST['district']
        pin = request.POST['pin']
        houseno = request.POST['houseno']
        gender = request.POST['gender']
        address = request.POST['txtAddress']
        email = request.POST['txtEmail']
        contact = request.POST['txtContact']
        pwd = request.POST['txtPassword']

        try:
            user = CustomUser.objects.create_user(
                username=email, password=pwd, is_active=1, userType='makeup')
            user.save()
            c = MakeUp.objects.create(
                name=name, address=address, contact=contact, email=email, user=user, lname=lname, district=district, state=state, pin=pin, houseno=houseno, gender=gender, dob=dob)
            c.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Registration successfull."
    return render(request, "makeUpReg.html", {"msg": msg})

def editmake(request,id):
    con=MakeUp.objects.filter(id=id)
    return render(request,'editmake.html', { 'make': con})

def edit_make(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        name = request.POST.get('txtName')
        lname = request.POST.get('txtLname')
        dob = request.POST.get('dob')
        state = request.POST.get('state')
        district = request.POST.get('district')
        pin = request.POST.get('pin')
        houseno = request.POST.get('houseno')
        gender = request.POST.get('gender')
        address = request.POST.get('txtAddress')
        email = request.POST.get('txtEmail')
        contact = request.POST.get('txtContact')
        pwd = request.POST.get('txtPassword')

        try:
            # Retrieve the existing content creator object by ID
            c = MakeUp.objects.get(id=id)
            # Update the attributes
            c.name = name
            c.lname = lname
            c.dob = dob
            c.state = state
            c.district = district
            c.pin = pin
            c.houseno = houseno
            c.gender = gender
            c.address = address
            c.email = email
            c.contact = contact
            c.password = pwd
            # Save the updated object
            c.save()
            msg = "Update successful."
            # Redirect to adminmakeup.html after successful update
            return redirect('adminmakeup')
        except MakeUp.DoesNotExist:
            msg = "Makeup Artists does not exist."
        except Exception as e:
            msg = f"Error updating Makeup Artists: {str(e)}"
    else:
        msg = "Invalid request method."

    # Render registration.html with a message
    return render(request, "adminmakeup.html", {"msg": msg})











def conCreReg(request):
    msg = ""
    if(request.POST):
        name = request.POST['txtName']
        lname = request.POST['txtLname']
        dob = request.POST['dob']
        state = request.POST['state']
        district = request.POST['district']
        pin = request.POST['pin']
        houseno = request.POST['houseno']
        gender = request.POST['gender']
        address = request.POST['txtAddress']
        email = request.POST['txtEmail']
        contact = request.POST['txtContact']
        pwd = request.POST['txtPassword']

        try:
            user = CustomUser.objects.create_user(
                username=email, password=pwd, is_active=1, userType='content')
            user.save()
            c = Content.objects.create(
                name=name, address=address, contact=contact, email=email, user=user, lname=lname, district=district, state=state, pin=pin, houseno=houseno, gender=gender, dob=dob)
            c.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Registration successfull."
    return render(request, "conCreReg.html", {"msg": msg})


'''COMMON INTERFACE'''

'''ADMIN INTERFACE'''


def adminhome(request):
    # Count the number of instances for each model
    num_customers = Customer.objects.count()
    num_content_creators = Content.objects.count()
    num_makeup_professionals = MakeUp.objects.count()
    num_photos = Photo.objects.count()
    num_portfolios =  Portfolio.objects.count()
    num_feedbacks = Feedback.objects.count()

    return render(request, "adminhome.html", {
        'num_customers': num_customers,
        'num_content_creators': num_content_creators,
        'num_makeup_professionals': num_makeup_professionals,
        'num_photos': num_photos,
        'num_portfolios': num_portfolios,
        'num_feedbacks': num_feedbacks,
    })

def adminaddStaff(request):
    msg = ""
    data = Photo.objects.all()
    if request.POST:
        name = request.POST.get('txtName')
        lname = request.POST.get('txtLname')
        contact = request.POST.get('txtContact')
        email = request.POST.get('txtEmail')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        houseno = request.POST.get('houseno')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('txtAddress')
        pwd = request.POST.get('txtPassword')

        try:
            user = CustomUser.objects.create_user(
                username=email, password=pwd, is_active=True, userType='Staff')
            user.save()
            c = Photo.objects.create(
                name=name, lname=lname, contact=contact, email=email, district=district, state=state, pin=pin, houseno=houseno, gender=gender, dob=dob, address=address, user=user)
            c.save()
            msg = "Registration successful."
        except Exception as e:
            msg = "Sorry, registration error: " + str(e)

    return render(request, "adminaddStaff.html", {"msg": msg, "data": data})




def adminvPublic(request):
    cust=Customer.objects.all()
    return render(request, "adminvPublic.html",{"cust":cust})

def adminfeedback(request):
    # Query Feedback objects and prefetch related Portfolio objects
    data = Feedback.objects.all().prefetch_related('customer__portfolio_set')

    return render(request, "adminfeedback.html", {"data": data})

def adminconcre(request):
    concreact=Content.objects.filter(user__is_active=True)
    concredeact=Content.objects.filter(user__is_active=False)   
    return render(request, "adminconcre.html",{"concredeact":concredeact,"concreact":concreact})

def adminphoto(request):
    photoact=Photo.objects.filter(user__is_active=True)
    photodeact=Photo.objects.filter(user__is_active=False)
    return render(request, "adminphoto.html",{"photodeact":photodeact,"photoact":photoact})

def adminportfolio(request):
    portfolios = Portfolio.objects.all()
    current_date = datetime.now().date()
    current_time = datetime.now().time()
    
    # Render the HTML template with the context data
    return render(request, "adminportfolio.html", {"portfolio": portfolios, "current_date": current_date, "current_time": current_time})

def adminmakeup(request):
    dataa=MakeUp.objects.filter(user__is_active=True)
    datar=MakeUp.objects.filter(user__is_active=False)   
    return render(request, "adminmakeup.html",{"datar":datar,"dataa":dataa})

def pReject(request):
    id = request.GET.get('id')
    p = CustomUser.objects.get(id=id)
    p.is_active = False
    p.save()
    return redirect("/adminphoto")

def pApprove(request):
    id = request.GET.get('id')
    p = CustomUser.objects.get(id=id)
    p.is_active = True
    p.save()
    return redirect("/adminphoto")

def mReject(request):
    id = request.GET.get('id')
    p = CustomUser.objects.get(id=id)
    p.is_active = False
    p.save()
    return redirect("/adminmakeup")

def mApprove(request):
    id = request.GET.get('id')
    p = CustomUser.objects.get(id=id)
    p.is_active = True
    p.save()
    return redirect("/adminmakeup")

def cReject(request):
    id = request.GET.get('id')
    p = CustomUser.objects.get(id=id)
    p.is_active = False
    p.save()
    return redirect("/adminconcre")

def cApprove(request):
    id = request.GET.get('id')
    p = CustomUser.objects.get(id=id)
    p.is_active = True
    p.save()
    return redirect("/adminconcre")


'''ADMIN INTERFACE'''
'''PUBLIC INTERFACE'''


def publichome(request):
    return render(request, "publichome.html")



def createPortfolio(request):
    photo  = Photo.objects.all()
    content  = Content.objects.all()
    makeup  = MakeUp.objects.all()
    uid = request.session["id"]
    u = Customer.objects.get(id=uid)

    if request.POST:
        name = request.POST['name']
        ldate = request.POST['ldate'] #last date for portfolio submission
        photoid = request.POST['photoid']
        makeupid = request.POST['makeupid']
        concreid = request.POST['concreid']
        desc = request.POST['desc']
        p_title = request.POST['p_title']
        email = request.POST['email']
        contact = request.POST['contact']
        pic = request.FILES.get('pic')
        bio = request.POST['bio']

        ph = Photo.objects.get(id=photoid)
        make = MakeUp.objects.get(id=makeupid)
        con = Content.objects.get(id=concreid)

        fs=FileSystemStorage()
        filename=fs.save(pic.name,pic)

        p = Portfolio.objects.create(name=name,progress="0",status="requested",l_date=ldate,desc=desc,userid=u,photo=ph,makeup=make,concre=con,p_title=p_title,email=email,contact=contact,pic=pic,bio=bio)
        p.save()

    return render(request, "createPortfolio.html",{"photo":photo, "content":content,"makeup":makeup})




def viewPPayments(request):
    id = request.session['id']
    data = Payment.objects.filter(customer__id=id)
    return render(request,"viewPPayments.html",{"data":data})

def viewProgress(request):
    id = request.session['id']
    u = Customer.objects.get(id=id)

    ports = Portfolio.objects.filter(userid=u)

    if request.POST:
        feed = request.POST['feed']
        pid = request.POST['pid']
        p = Portfolio.objects.get(id=pid)
        p.status = "Done"
        p.save()
        f = Feedback.objects.create(feed=feed,customer=u)
        f.save()
    return render(request,"viewProgress.html",{"ports":ports})

def rejectPort(request):
    id = request.GET.get('id')
    p = Portfolio.objects.get(id=id)

    if request.POST:
        reason = request.POST['reason']
        p.progress = "75"
        p.status = "Rejected"
        p.reason = reason
        p.save()
        return redirect("/viewProgress")
    return render(request,"rejectPort.html")


def Userpay(request):
    # Retrieve data from request
    id = request.GET.get('id')
    uid = request.session['id']
    u = Customer.objects.get(id=uid)
    cards = Card.objects.filter(customer__id=uid)
    p = Portfolio.objects.get(id=id)
    tot = int(p.price)

    if request.method == 'POST':
        cnumber = request.POST.get('cnumber')
        expiry = request.POST.get('expiry')
        photoamt = 0.1 * tot
        amt = tot - photoamt
        makeamt = 0.1 * amt
        conamt = amt - makeamt
        
        # Check if the card already exists
        existing_card = Card.objects.filter(card_no=cnumber, customer=u).first()

        if existing_card:
            card = existing_card
        else:
            # Create a new card entry
            card = Card.objects.create(card_no=cnumber, Name=u.name, exp_date=expiry, customer=u)
        
        # Create payment entry
        pay = Payment.objects.create(totamt=tot, conamt=conamt, photoamt=photoamt, makeupamt=makeamt, customer=p.userid, content=p.concre, makeup=p.makeup, photo=p.photo)
        
        # Update portfolio status
        p.status = "Paid"
        p.save()
        
        return redirect("/viewProgress")
    
    return render(request, "Userpay.html", {"p": p, "cards": cards})


def Usercardpay(request):
    # Retrieve data from request
    id = request.GET.get('id')
    cnum = request.GET.get('cnum')
    exp = request.GET.get('exp')
    uid = request.session['id']
    u = Customer.objects.get(id=uid)
    cards = Card.objects.filter(customer__id=uid)
    p = Portfolio.objects.get(id=id)
    tot = int(p.price)

    if request.method == 'POST':
        cnumber = request.POST.get('cnumber')
        expiry = request.POST.get('expiry')
        photoamt = 0.1 * tot
        amt = tot - photoamt
        makeamt = 0.1 * amt
        conamt = amt - makeamt

        # Check if the card already exists
        existing_card = Card.objects.filter(card_no=cnumber, customer=u).first()

        if existing_card:
            card = existing_card
        else:
            # Create a new card entry
            card = Card.objects.create(card_no=cnumber, Name=u.name, exp_date=expiry, customer=u)
        
        # Create payment entry
        pay = Payment.objects.create(totamt=tot, conamt=conamt, photoamt=photoamt, makeupamt=makeamt, customer=p.userid, content=p.concre, makeup=p.makeup, photo=p.photo)
        
        # Update portfolio status
        p.status = "Paid"
        p.save()
        
        return redirect("/viewProgress")
    
    return render(request, "Usercardpay.html", {"p": p, "cards": cards, "cnum": cnum, "exp": exp})


'''PUBLIC INTERFACE'''

'''Photo INTERFACE'''


def Staffhome(request):
    return render(request, "staffhome.html")

def photoWorks(request):
    id  = request.session['id']
    u = Photo.objects.get(id=id)
    p = Portfolio.objects.filter(photo=u)
    return render(request, "staffWorks.html",{"ports":p})

def photoPayments(request):
    id = request.session["id"]
    u = Photo.objects.get(id=id)
    data = Payment.objects.filter(photo=u)
    return render(request, "staffPayments.html",{"data":data})
'''Photo INTERFACE'''

'''ContentCreator INTERFACE'''

def concrehome(request):
    return render(request, "concrehome.html")

def conWorks(request):
    uid  = request.session["id"]
    u = Content.objects.get(id=uid)
    ports = Portfolio.objects.filter(concre=uid)
    if request.POST:
        price= request.POST["price"]
        file = request.FILES["file"]
        id = request.POST["id"]
        p = Portfolio.objects.get(id=id)
        p.price = price
        p.file = file
        p.progress = "100"
        p.status = "Complete"
        p.save()
    return render(request, "conWorks.html",{"ports": ports})

def conPayments(request):
    id = request.session["id"]
    u = Content.objects.get(id=id)
    data = Payment.objects.filter(content=u)
    return render(request, "conPayments.html",{"data": data})

def twentyfive(request):
    id=request.GET.get('id')
    p = Portfolio.objects.get(id=id)
    p.progress = "25"
    p.save()
    return redirect("/conWorks")

def fifty(request):
    id=request.GET.get('id')
    p = Portfolio.objects.get(id=id)
    p.progress = "50"
    p.save()
    return redirect("/conWorks")

def seventyfive(request):
    id=request.GET.get('id')
    p = Portfolio.objects.get(id=id)
    p.progress = "75"
    p.status = "Almost"
    p.save()
    return redirect("/conWorks")
'''ContentCreator Interface'''


'''Makeup Interface'''

def makeuphome(request):
    return render(request, "makeuphome.html")

def makeupWorks(request):
    id  = request.session['id']
    u = MakeUp.objects.get(id=id)
    p = Portfolio.objects.filter(makeup=u)
    return render(request,"makeupWorks.html",{"ports":p})

def makeupPayments(request):
    id = request.session["id"]
    u = MakeUp.objects.get(id=id)
    data = Payment.objects.filter(makeup=u)
    return render(request,"makeupPayments.html",{"data":data})

'''Makeup Interface'''
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request, "index.html")

def bill(request):
    return render(request, "bill.html")


def update_status(request, id):
    try:
        # Retrieve the customer object with the given id
        customer = Customer.objects.get(id=id)
        # Deactivate the user associated with the customer
        customer.status = False
        customer.save()
        return redirect('/adminvPublic')  # Redirect to the desired URL after updating
    except Customer.DoesNotExist:
        # Handle the case where the customer with the given id does not exist
        # You may want to render an error page or redirect to a different URL
        return redirect('/error-page')



def reactivate_user(request, id):
    try:
        # Retrieve the customer object with the given id
        customer = Customer.objects.get(id=id)
        # Reactivate the user associated with the customer
        customer.status = True
        customer.save()
        return redirect('/adminvPublic')  # Redirect to the desired URL after updating
    except Customer.DoesNotExist:
        # Handle the case where the customer with the given id does not exist
        # You may want to render an error page or redirect to a different URL
        return redirect('/error-page')




#Members and thier pre works

#ALL
def memberworks(request):
    con = Content.objects.all()
    pho = Photo.objects.all()
    make = MakeUp.objects.all()
    return render(request, "memberworks.html", { 'contents':con,'photo':pho,'makeup':make})


def photoworkss(request, id):
    # Query portfolios and payments for the specific photographer
    portfolios = Portfolio.objects.filter(photo_id=id)
    payments = Payment.objects.filter(photo_id=id)
    # Pass the queried data to the template
    return render(request, "photoworks.html", {'portfolios': portfolios, 'payments': payments})

def makeworks(request, id):
    # Query portfolios and payments for the specific photographer
    portfolios = Portfolio.objects.filter(makeup_id=id)
    payments = Payment.objects.filter(makeup_id=id)
    # Pass the queried data to the template
    return render(request, "makeworks.html", {'portfolios': portfolios, 'payments': payments})

def contentworks(request, id):
    # Query portfolios and payments for the specific photographer
    portfolios = Portfolio.objects.filter(concre_id=id)
    payments = Payment.objects.filter(content_id=id)
    # Pass the queried data to the template
    return render(request, "contentworks.html", {'portfolios': portfolios, 'payments': payments})


