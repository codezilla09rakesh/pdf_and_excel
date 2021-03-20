from django.core.files import File
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http import HttpResponse
import yfinance as yf

from share.models import H
import os
from django.conf import settings
from django.core.files.storage import default_storage
from io import StringIO, BytesIO
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import base64

# Create your views here.
#
def Home(request):
    msft = yf.Ticker("INFY.NS")
    hist = msft.history(period="1y")
    open = hist.Open
    close = hist.Close
    print(type(close), type(open))
    context = {'open':open, 'close':close}
    return render(request,'share/home.html', context)


def render_to_pdf():
    template_path = 'share/email.html'
    template = get_template(template_path)
    context = {'myvar': 'this is your template context'}
    html = template.render(context)
    # Create a Django response object, and specify content_type as pdf
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # template = get_template(template_path)
    # html = render_to_string(template_path, context)
    # rsf = H.objects.get(id=1).name
    # H.objects.create(name=html)
    # find the template and render it.
    result = BytesIO()
    # print(result.getbuffer())
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), dest=result)
    # ile_data = ContentFile(pdf.content)
    # print(ile_data)
    # H.objects.create(name=r)
    # # create a pdf
    # pdf = pisa.CreatePDF(
    #    html, dest=result)
    # # if error then show some funy view
    if not pdf.err:
        # return HttpResponse(result.getvalue(), content_type='application/pdf')
        return pdf
        # return result.getvalue()
    else:
        return HttpResponse('Errors')


def render_pdf_view(request):
    # template_path = 'share/email.html'
    # context = {'myvar': 'this is your template context'}
    # # Create a Django response object, and specify content_type as pdf
    # # find the template and render it.
    # template = get_template(template_path)
    # html = template.render(context)
    # result = BytesIO()
    # pdf = pisa.CreatePDF(
    #    html, dest=result)
    # pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result)
    # result = render_to_pdf()
    # content =result.getvalue()
    # file_data = ContentFile(content)
    # h=H.objects.get(id=11)
    # h.name.save("s", file_data)

    # r = H.objects.get(id=11).name
    # path = default_storage.save("path_to_file.pdf", file_data)
    # print(path)
    # print(default_storage.exists(path))
    # print(default_storage.size(path))
    # print(type(default_storage.open(path).read()))
    # r = BytesIO(default_storage.open(path).read())



    # create a pdf
    # pdf = pisa.CreatePDF(
    #     BytesIO(html.encode("ISO-8859-1")), dest=result,)
    # print("?///////////////////", pdf.content)
    # ile_data = ContentFile(pdf)
    # print(ile_data)
    # if error then show some funy view
    # if pdf.err:
    #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return HttpResponse(result.getValue(), content_type='application/pdf')
    # return HttpResponse("Hello")
    template_path = 'share/opt_in_employer.html'
    context = {'pagesize':'A5',
               'myvar': 'this is your template context'
               }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = render_to_string(template_path,context)

    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result)
    content =result.getvalue()
    file_data = ContentFile(content)

    # h=H.objects.get(id=11)
    # h.name.save("s23", file_data)
    # create a pdf
    # pisa_status = pisa.CreatePDF(
    #    html, dest=response, )
    # if error then show some funy view
    if pdf.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return HttpResponse(result.getvalue(), content_type='application/pdf')


def Nlp(request):

    return HttpResponse(">>>>>>>>>>>>>>>>>>>>>>>")
