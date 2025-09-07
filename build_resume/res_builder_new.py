from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import json
import os

def load_credentials():
    """Load credentials from JSON file"""
    credentials_file = 'credentials.json'
    if not os.path.exists(credentials_file):
        print(f"Error: {credentials_file} not found!")
        print("Please copy credentials.example.json to credentials.json and fill in your information.")
        return None
    
    with open(credentials_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def cv_pdf(filename, credentials):
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=20, bottomMargin=20)
    styles = getSampleStyleSheet()

    # Custom styles
    styles.add(ParagraphStyle(name='Header', fontSize=20, leading=26, fontName='Helvetica-Bold', spaceAfter=0))
    styles.add(ParagraphStyle(name='SubHeader', fontSize=13, leading=20, fontName='Helvetica-Bold', spaceAfter=0))
    styles.add(ParagraphStyle(name='Bold', fontSize=12, leading=20, fontName='Helvetica-Bold', spaceAfter=0))
    styles.add(ParagraphStyle(name='CustomNormal', fontSize=10, leading=16, fontName='Helvetica', spaceAfter=0))
    styles.add(ParagraphStyle(name='Small', fontSize=10, leading=15, fontName='Helvetica', spaceAfter=0))

    elems = []

    # Header
    personal_info = credentials['personal_info']
    elems.append(Paragraph(personal_info['name'], styles['Header']))
    elems.append(Paragraph(personal_info['title'], styles['Bold']))
    elems.append(Paragraph(f"{personal_info['location']} | {personal_info['phone']} | {personal_info['email']}", styles['CustomNormal']))
    elems.append(Paragraph(f'<a href="{personal_info["linkedin"]}" color="blue"><u>LinkedIn</u></a>', styles['CustomNormal']))
    elems.append(Spacer(1, 2))

    # Summary
    elems.append(Paragraph("Summary", styles['SubHeader']))
    elems.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2))
    elems.append(Paragraph(credentials['summary'], styles['CustomNormal']))

    # Experience (wrapped in KeepTogether)
    if credentials['experience']:
        experience_block = [
            Spacer(1, 2),
            Paragraph("Experience", styles['SubHeader']),
            HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2)
        ]
        
        for exp in credentials['experience']:
            experience_block.extend([
                Paragraph(exp['title'], styles['Bold']),
                Paragraph(exp['company'], styles['Small']),
                Paragraph(exp['period'], styles['Small']),
                Paragraph("<br/>".join([f"- {desc}" for desc in exp['description']]), styles['CustomNormal'])
            ])
        
        elems.append(KeepTogether(experience_block))

    # Projects (each project block in KeepTogether)
    if credentials['projects']:
        project_section = [Spacer(1, 2), Paragraph("Projects", styles['SubHeader']),
                          HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2)]
        elems.append(KeepTogether(project_section))

        for project in credentials['projects']:
            project_block = [
                Paragraph(project['name'], styles['Bold']),
                Paragraph(project['period'], styles['Small']),
                Paragraph("<br/>".join([f"- {desc}" for desc in project['description']]), styles['CustomNormal'])
            ]
            elems.append(KeepTogether(project_block))

    # Education
    if credentials['education']:
        education_block = [
            Spacer(1, 2),
            Paragraph("Education", styles['SubHeader']),
            HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2),
            Paragraph("<br/>".join(credentials['education']), styles['CustomNormal'])
        ]
        elems.append(KeepTogether(education_block))

    # Certifications (all certifications in one block)
    if credentials['certifications']:
        certifications_block = [
            Spacer(1, 2),
            Paragraph("Certifications", styles['SubHeader']),
            HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2)
        ]
        
        for cert in credentials['certifications']:
            certifications_block.append(
                Paragraph(f'<a href="{cert["url"]}" color="blue"><u>{cert["name"]}</u></a>', styles['CustomNormal'])
            )
        
        elems.append(KeepTogether(certifications_block))

    # Skills (all in one block)
    if credentials['skills']:
        skills_block = [
            Spacer(1, 2),
            Paragraph("Skills", styles['SubHeader']),
            HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2),
            Paragraph(f"<b>Core Data Engineering Skills:</b> {credentials['skills']['core_data_engineering']}", styles['CustomNormal']),
            Paragraph(f"<b>Tools & Technologies:</b> {credentials['skills']['tools_technologies']}", styles['CustomNormal']),
            Paragraph(f"<b>Programming & Other:</b> {credentials['skills']['programming_other']}", styles['CustomNormal'])
        ]
        elems.append(KeepTogether(skills_block))

    # Languages
    if credentials['languages']:
        languages_block = [
            Spacer(1, 2),
            Paragraph("Languages", styles['SubHeader']),
            HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2),
            Paragraph("<br/>".join([f"- {lang}" for lang in credentials['languages']]), styles['CustomNormal'])
        ]
        elems.append(KeepTogether(languages_block))

    doc.build(elems)

def main():
    # Load credentials
    credentials = load_credentials()
    if credentials is None:
        return
    
    # Generate PDF
    output_filename = f"{credentials['personal_info']['name'].lower().replace(' ', '_')}_cv.pdf"
    cv_pdf(output_filename, credentials)
    print(f"Resume generated successfully: {output_filename}")

if __name__ == "__main__":
    main()
