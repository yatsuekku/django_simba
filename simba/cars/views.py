from django.shortcuts import render
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hehe.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response,initialFontName='Times-Roman')

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Pchnij w tą waśń rum i ósm skrzyń fig.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

# Create your views here.
