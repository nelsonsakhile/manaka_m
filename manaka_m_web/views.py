from calendar import c
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.http import FileResponse
import io
from reportlab.lib.units import inch

# For Report Lab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
# End for report lab

# Create your views here.

def index(request):
	queryset = ClintsRegister.objects.all()
	form = ClintsRegisterForm(request.POST or None)
	title = 'Nothing'
	total_clients =  ClintsRegister.objects.count()

	context = {
	'title': title,
	'queryset': queryset,
	'form': form,
	'total_clients': total_clients,
	}
	return render(request, "index.html", context)



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('list_invoice')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('list_invoice')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')

def list_invoice(request):
    title = 'list of Invoices'
    queryset = ClintsRegister.objects.all()
    context = {
        'title': title,
        'queryset': queryset,
    }

    
    return render(request, 'list_invoice.html', context)



def download_invoice(request, pk):

    buffer = io.BytesIO()

    c = canvas.Canvas(buffer, pagesize=letter, bottomup=1)
    queryset = ClintsRegister.objects.get(id=pk)
    invoice_file_name = f'{str(queryset.name)}_{str(queryset.invoice_type)}.pdf'
    
    # Watermark
    watermark = 'E-INVOICE-trans.png'
    c.drawImage(watermark, -10, -100, width=640, height=1000)

    #Type invoice or reciept
    c.setFont('Helvetica-Bold', 12, leading=None)
    my_type = str(queryset.invoice_type)
    c.drawCentredString(300, 610, my_type )
    

    # Invoice Date
    c.setFont('Helvetica', 12, leading=None)
    c.drawCentredString(425, 610, "Date:")
    c.setFont('Helvetica', 12, leading=None)
    c.drawString(489, 611, str(queryset.invoice_date) )

    # Invoice Number
    c.drawCentredString(415, 630, str(queryset.invoice_type) + ':')
    c.setFont('Helvetica', 12, leading=None)
    invoice_number_string = str('0000'+ str(queryset.invoice_number))
    c.drawRightString(550, 630, invoice_number_string)

    # Customer name
    c.setFont('Helvetica', 12, leading=None)
    c.drawString(58, 630, "To:")
    c.setFont('Helvetica', 12, leading=None)
    c.drawCentredString(150, 630, str(queryset.name) )

    # Phone Number
    c.setFont('Helvetica', 12, leading=None)
    c.drawString(58, 610, "Phone: ")
    c.setFont('Helvetica', 12, leading=None)
    c.drawCentredString(150, 610, str(queryset.phone_number) )

    # Logo
    logo = 'bx-logo.png'
    c.drawImage(logo, 400, 660, width=150, height=100)


    # drawing Horizontal line
    c.line(58, 590, 550, 590) 

    # Table Header
    c.setFont('Helvetica-Bold', 12, leading=None)
    c.drawCentredString(130, 480, 'ITEMS')     
    c.drawCentredString(250, 480, 'QUANTITY')     
    c.drawCentredString(360, 480, 'UNIT PRICE')     
    c.drawCentredString(480, 480, 'LINE TOTAL')  

    # Items Listing
    c.setFont('Helvetica', 12, leading=None)
    c.drawCentredString(130, 450, str(queryset.line_one) )
    c.drawCentredString(250, 450, str(queryset.line_one_quantity) )
    c.drawCentredString(360, 450, str(queryset.line_one_unit_price) )
    c.drawCentredString(480, 450, str(queryset.line_one_total_price) )

    if queryset.line_two != '':
        c.setFont('Helvetica', 12, leading=None)
        c.drawCentredString(130, 420, str(queryset.line_two) )
        c.drawCentredString(250, 420, str(queryset.line_two_quantity) )
        c.drawCentredString(360, 420, str(queryset.line_two_unit_price) )
        c.drawCentredString(480, 420, str(queryset.line_two_total_price) )

    if queryset.line_three != '':
        c.setFont('Helvetica', 12, leading=None)
        c.drawCentredString(130, 390, str(queryset.line_three) )
        c.drawCentredString(250, 390, str(queryset.line_three_quantity) )
        c.drawCentredString(360, 390, str(queryset.line_three_unit_price) )
        c.drawCentredString(480, 390, str(queryset.line_three_total_price) )

    if queryset.line_four != '':
        c.setFont('Helvetica', 12, leading=None)
        c.drawCentredString(130, 360, str(queryset.line_four) )
        c.drawCentredString(250, 360, str(queryset.line_four_quantity) )
        c.drawCentredString(360, 360, str(queryset.line_four_unit_price) )
        c.drawCentredString(480, 360, str(queryset.line_four_total_price) )

    if queryset.line_five != '':
        c.setFont('Helvetica', 12, leading=None)
        c.drawCentredString(130, 330, str(queryset.line_five) )
        c.drawCentredString(250, 330, str(queryset.line_five_quantity) )
        c.drawCentredString(360, 330, str(queryset.line_five_unit_price) )
        c.drawCentredString(480, 330, str(queryset.line_five_total_price) )
    
    # drawing Vertical lines
    c.line(190, 260, 190, 460)
    c.line(305, 260, 305, 460)
    c.line(420, 260, 420, 460)

    # TOTAL
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawString(420, 140, "TOTAL:")
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawRightString(550, 140, 'R'+str(queryset.total) )

    # Deposit
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawString(420, 120, "DEPOSIT:")
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawRightString(550, 120, 'R' + str(queryset.deposit) )

    # amount due
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawString(420, 100, "AMOUNT DUE:")
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawRightString(550, 100, 'R' + str(queryset.amount_due) )

    # SIGN
    c.setFont('Helvetica-Bold', 10, leading=None)
    c.drawString(58, 140, 'Banking details')
    c.drawString(58, 120, 'Account Number: 1443722020')
    c.drawString(58, 100, 'Bank          : Capitec Bank')

    
    #DLTC text
    c.setFont('Helvetica-Bold', 12, leading=None)
    c.drawCentredString(300, 210, 'NB: Payment does not include DLTC booking payments')
    

    # Watermark
    top = 'top_design.png'
    c.drawImage(top, -3, 770, width=620, height=30)
    bottom = 'bottom_desgin.png'
    c.drawImage(bottom, 0, -1, width=620, height=50)

    c.showPage()
    c.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename= invoice_file_name)



def add_invoice(request):
    
    form = ClintsRegisterForm(request.POST or None)
    total_invoices = ClintsRegister.objects.count()
    queryset = ClintsRegister.objects.order_by('-invoice_date')[:7]
    
    if form.is_valid():
        form.save()
        return redirect("/list_invoice")
    context = {
        "form" : form,
        "title": "New Invoice",
        'total_invoices': total_invoices,
        'queryset' : queryset,
    }

    return render(request, "new_invoice.html", context)


def update_invoice(request, pk):
    queryset = ClintsRegister.objects.get(id=pk)
    form = ClintsRegisterUpdateForm(instance = queryset)
    if request.method == 'POST':
        form = ClintsRegisterUpdateForm(request.POST, instance=queryset)
        
        if form.is_valid():
            form.save()
            return redirect("/list_invoice")

    context = {
        "form" : form,
    }

    return render(request, "new_invoice.html", context)



def delete_invoice(request, pk):
    queryset = ClintsRegister.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect("/list_invoice")
    return render(request, "delete_invoice.html")