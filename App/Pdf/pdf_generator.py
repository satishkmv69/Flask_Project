from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(resume):
    file_name = "resume.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)

    c.drawString(50, 800, resume.full_name)
    c.drawString(50, 780, resume.email)
    c.drawString(50, 760, resume.phone)

    c.drawString(50, 720, "Skills:")
    c.drawString(50, 700, resume.skills)

    c.drawString(50, 660, "Education:")
    c.drawString(50, 640, resume.education)

    c.drawString(50, 600, "Experience:")
    c.drawString(50, 580, resume.experience)

    c.save()
    return file_name
