import requests
from django.shortcuts import render
from django.http import HttpResponse
from fpdf import FPDF
import os

import re

def home(request):
    api_key = "" #Sign in to NewsAPI and Enter the API key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url).json()

    # Fetch top 4 headlines for the banner
    top_headlines = response.get('articles', [])[:8]

    # Define categories with valid slugs
    categories = [
        {"name": "Business", "slug": "business"},
        {"name": "Entertainment", "slug": "entertainment"},
        {"name": "Health", "slug": "health"},
        {"name": "Science", "slug": "science"},
        {"name": "Sports", "slug": "sports"},
        {"name": "Technology", "slug": "technology"},
    ]
    
    # Debugging: Print categories to check slugs
    print(categories)

    return render(request, "home.html", {
        "top_headlines": top_headlines,
        "categories": categories,
    })



def category_news(request, category):
    api_key = "b03cd05b424946719bdd9a8b1a92eb8c"
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}"
    response = requests.get(url).json()
    
    return render(request, "category.html", {
        "category": category,
        "articles": response.get('articles', [])[:12],  # Top 10 articles
    })


def generate_pdf(request):
    title = request.GET.get('title', 'Untitled')
    description = request.GET.get('description', 'No description available.')
    image_url = request.GET.get('image', '')
    url = request.GET.get('url', '')

    # Helper function to clean text
    def clean_text(text):
        # Replace unsupported characters with plain equivalents
        text = re.sub(r'[‘’]', "'", text)  # Replace curly quotes
        text = re.sub(r'[“”]', '"', text)  # Replace curly double quotes
        text = re.sub(r'[—–]', '-', text)  # Replace long dashes
        text = re.sub(r'[…]', '...', text)  # Replace ellipsis with three dots
        return text

    # Clean inputs
    title = clean_text(title)
    description = clean_text(description)

    class PDF(FPDF):
        def header(self):
            self.set_font('Helvetica', 'B', 16)  # Using Helvetica (default)
            self.cell(0, 10, 'InfoSphere', border=False, ln=True, align='C')
            self.ln(10)

    pdf = PDF()

    # Add a page
    pdf.add_page()

    # Set font for title
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 10, title, ln=True)
    pdf.ln(10)

    # Set font for description
    pdf.set_font('Helvetica', '', 12)
    
    # Add description to PDF
    pdf.multi_cell(0, 10, description)
    pdf.ln(10)

    # Check if image URL is valid, and add it if it is
    if image_url:
        try:
            pdf.image(image_url, x=10, y=pdf.get_y(), w=100)  # Resize image as needed
            pdf.ln(60)  # Adjust space after image
        except Exception as e:
            pdf.cell(0, 10, f'Image could not be loaded: {str(e)}', ln=True)

    # Add URL
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('Helvetica', 'I', 12)
    pdf.cell(0, 10, url, ln=True, link=url)
    pdf.set_text_color(0, 0, 0)

    # Generate the PDF as binary content
    pdf_content = pdf.output(dest='S')  # Already a bytearray

    # Prepare the response
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{title[:50]}.pdf"'

    return response
