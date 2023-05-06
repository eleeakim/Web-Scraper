
import requests
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_LINE_SPACING

# Make a GET request to the URL
url = 'https://www.privatehealth.co.uk/abdominal-pain/specialists/'
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to get page. Status code: {response.status_code}")
    exit()

# Parse the HTML content using BeautifulSoup
doc = BeautifulSoup(response.text, 'html.parser')

# Find all elements with class "doc-details"
doc_details = doc.find_all(class_="doc-details")

# Create a new Word document
document = Document()

# Set the spacing of the paragraphs
style = document.styles['Normal']
paragraph_format = style.paragraph_format
paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
paragraph_format.space_after = Pt(2)

# Add the text content of each element to the document
for tag in doc_details:
    document.add_paragraph(tag.get_text().strip(), style='Normal')

# Save the document to a file
document.save('result1.docx')

print(f"{len(doc_details)} elements with class 'doc-details' found.")
