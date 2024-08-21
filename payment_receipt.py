from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

def generate_receipt(data):
    """Generates a PDF receipt document."""

    # Define document and styles
    doc = SimpleDocTemplate("receipt.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    styleN = styles["Normal"]
    styleH = styles["Heading1"]

    # Create content elements
    elements = []

    # Header
    elements.append(Paragraph("Your Company Name", styleH))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Receipt", styleH))

    # Transaction Details
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph(f"Transaction ID: {data['transaction_id']}", styleN))
    elements.append(Paragraph(f"Date: {data['date']}", styleN))
    elements.append(Paragraph(f"Customer Name: {data['customer_name']}", styleN))

    # Items Table
    items = [
        ["Item Name", "Quantity", "Price"],
    ]
    for item in data['items']:
        items.append([item['name'], item['quantity'], f"${item['price']:.2f}"])

    table = Table(items, style=[
        ('ALIGN', (1, 1), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOX', (0, 0), (-1, -1), 0.25, 'black'),
        ('GRID', (0, 0), (-1, -1), 0.25, 'black'),
    ])
    elements.append(table)

    # Total
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph(f"Total: ${data['total']:.2f}", styleN))

    # Build and save the document
    doc.build(elements)

# Example data
data = {
    "transaction_id": "12345",
    "date": "2023-11-10",
    "customer_name": "John Doe",
    "items": [
        {"name": "Product A", "quantity": 2, "price": 10.99},
        {"name": "Product B", "quantity": 1, "price": 19.99},
    ],
    "total": 31.97,
}

generate_receipt(data)