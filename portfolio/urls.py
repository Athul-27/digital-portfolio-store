"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from portfolioApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login',views.login, name= 'login'),
    path('registration',views.registration),
    path('conCreReg',views.conCreReg),
    path('makeUpReg',views.makeUpReg),



    #Edit Customer
    path('editregistration/<int:id>',views.editregistration),
    path('editcust',views.editcust, name= 'editcust'),
    path('logout',views.logout, name= 'logout'),
    path('bill',views.bill),


    #status update
    path('update_status/<int:id>/', views.update_status, name='update_status'),
    path('reactivate_user/<int:id>/', views.reactivate_user, name='reactivate_user'),



    #edit photographer
    path('editphoto/<int:id>', views.editphoto, name='editphoto'),
    path('edit_photo',views.edit_photo, name= 'edit_photo'),


    #edit Content creator
    path('editconcre/<int:id>', views.editconcre, name='editconcre'),
    path('edit_concre',views.edit_concre, name= 'edit_concre'),


    #Edit makeup
    path('editmake/<int:id>', views.editmake, name='editmake'),
    path('edit_make',views.edit_make, name= 'edit_make'),

    
    #admin
    path('adminhome',views.adminhome),
    path('adminaddStaff',views.adminaddStaff),
    path('adminvPublic',views.adminvPublic, name= "adminportfolio"), 
    path('adminfeedback',views.adminfeedback),
    path('adminconcre',views.adminconcre, name= "adminconcre"), 
    path('adminmakeup',views.adminmakeup, name= "adminmakeup"),  
    path('adminphoto',views.adminphoto, name= "adminphoto"),  
    path('adminportfolio',views.adminportfolio),


    #portfolio action
    path('pReject',views.pReject),
    path('pApprove',views.pApprove),
    path('mReject',views.mReject),
    path('mApprove',views.mApprove),
    path('cReject',views.cReject),
    path('cApprove',views.cApprove),


    #public
    path('publichome',views.publichome),
    path('createPortfolio',views.createPortfolio),
    path('viewPPayments',views.viewPPayments),
    path('viewProgress',views.viewProgress),
    path('rejectPort',views.rejectPort),
    path('Userpay',views.Userpay),
    path('Usercardpay',views.Usercardpay),
    path('memberworks',views.memberworks, name='memberworks'),


    #Photo
    path('staffhome',views.Staffhome),
    path('photoWorks',views.photoWorks),
    path('photoPayments',views.photoPayments),    

    #Makeup
    path('makeuphome',views.makeuphome),
    path('makeupWorks',views.makeupWorks),
    path('makeupPayments',views.makeupPayments),

    #ContentCreator
    path('concrehome',views.concrehome),
    path('conWorks',views.conWorks),
    path('conPayments',views.conPayments),
    path('twentyfive',views.twentyfive),
    path('fifty',views.fifty),
    path('seventyfive',views.seventyfive),
    

    #Works
    path('memberworks', views.memberworks, name='memberworks'),
    #;;;;;
    path('photoworkss/<int:id>/', views.photoworkss, name='photoworkss'),
    path('contentworks/<int:id>/', views.contentworks, name="contentworks"),
    path('makeworks/<int:id>/', views.makeworks, name="makeworks"),
]
