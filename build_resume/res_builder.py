from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def cv_pdf(filename):
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
    elems.append(Paragraph("Roman Tkachenko", styles['Header']))
    elems.append(Paragraph("Data Engineer", styles['Bold']))
    elems.append(Paragraph("Kyiv, Ukraine | +380970757662 | romuchqq@gmail.com", styles['CustomNormal']))
    elems.append(Paragraph('<a href="https://www.linkedin.com/in/romuch/" color="blue"><u>LinkedIn</u></a>', styles['CustomNormal']))
    elems.append(Spacer(1, 2))

    # Summary
    elems.append(Paragraph("Summary", styles['SubHeader']))
    elems.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2))
    elems.append(Paragraph(
        "Data Engineer skilled in Python, PySpark and SQL with hands-on experience building end-to-end data pipelines on GCP. Comfortable orchestrating ETL/ELT flows with Apache Airflow and Docker, applying data-quality checks, and collaborating in distributed teams.",
        styles['CustomNormal']))

    # Experience (wrapped in KeepTogether)
    experience_block = [
        Spacer(1, 2),
        Paragraph("Experience", styles['SubHeader']),
        HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2),
        Paragraph("Python Scraper Developer", styles['Bold']),
        Paragraph("OnlineMinds - Remote (Copenhagen, Denmark)", styles['Small']),
        Paragraph("03/2023 - 07/2023", styles['Small']),
        Paragraph(
            "- Worked in a distributed team at a startup to build scalable data scraping pipelines.<br/>"
            "- Developed web scraping solutions using Scrapy and Python.<br/>"
            "- Automated data collection workflows and structured large volumes of data.<br/>"
            "- Collaborated on GitHub, followed version control best practices.<br/>"
            "- Contributed to team discussions and agile development cycles.",
            styles['CustomNormal'])
    ]
    elems.append(KeepTogether(experience_block))

    # Projects (each project block in KeepTogether)
    project_section = [Spacer(1, 2), Paragraph("Projects", styles['SubHeader']),
                      HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2)]
    elems.append(KeepTogether(project_section))

    de_homework_tasks = [
        Paragraph("DE-homework-tasks", styles['Bold']),
        Paragraph("05/2024 - 06/2024", styles['Small']),
        Paragraph(
            "- Built and orchestrated end-to-end data pipelines as part of a comprehensive data engineering project.<br/>"
            "- Developed ETL jobs to fetch, transform, and store sales data (JSON, Avro).<br/>"
            "- Set up a PostgreSQL demo DB with Docker, wrote SQL queries.<br/>"
            "- Installed and configured Apache Airflow, built DAGs to automate workflows.<br/>"
            "- Used GCP (BigQuery, GCS) and PySpark (local) for dual pipeline execution.<br/>"
            "- Configured PySpark in Jupyter Notebook for distributed data processing.<br/>"
            "- Integrated third-party data (user_profiles) for enrichment, applied data quality checks.<br/>"
            "- Delivered final project aligned with industry-grade data governance and orchestration practices.",
            styles['CustomNormal'])]
    elems.append(KeepTogether(de_homework_tasks))

    python_scraper_project = [
        Paragraph("Python-scraper-rental-property", styles['Bold']),
        Paragraph("2023", styles['Small']),
        Paragraph(
            "- Designed and implemented a scalable Python data scraping solution using GraphQL and multiprocessing.<br/>"
            "- Parsed and structured real estate listings from GraphQL APIs.<br/>"
            "- Used multiprocessing for parallel data collection and aggregation.<br/>"
            "- Output aggregated dataset into a structured JSON file for analysis.",
            styles['CustomNormal'])]
    elems.append(KeepTogether(python_scraper_project))

    telegram_bot_project = [
        Paragraph("Telegram-bot-purchase-discount", styles['Bold']),
        Paragraph("2023", styles['Small']),
        Paragraph(
            "- Automated buyer-seller interaction with two Telegram bots to generate and validate promo codes.<br/>"
            "- Ensured seamless transaction flow using Telegram Bot API and data validation logic.",
            styles['CustomNormal'])]
    elems.append(KeepTogether(telegram_bot_project))

    # Education
    education_block = [
        Spacer(1, 2),
        Paragraph("Education", styles['SubHeader']),
        HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2),
        Paragraph(
            "BSc – Kyiv National Economics University, 2019-2023<br/>"
            "Data Engineering Bootcamp – Robot_Dreams, 2024",
            styles['CustomNormal'])
    ]
    elems.append(KeepTogether(education_block))

    # Certifications (all certifications in one block)
    certifications_block = [
        Spacer(1, 2),
        Paragraph("Certifications", styles['SubHeader']),
        HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2),
                 Paragraph('<a href="https://lms.robotdreams.cc/certificate/2e480b21e02dff5e65889aed4cc36ae1" color="blue"><u>Data Engineering – Robot dreams (2024-06)</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://www.datacamp.com/statement-of-accomplishment/course/29e98329ec4d55f8134e17216d593728bed8a063?raw=1" color="blue"><u>Joining Data in SQL – DataCamp (2024-03)</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://www.datacamp.com/statement-of-accomplishment/course/61888063091274e09813f85e58fa306d00a3d421?raw=1" color="blue"><u>Intermediate SQL – DataCamp (2024-03)</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://www.datacamp.com/statement-of-accomplishment/course/72362fca72a0af004867bac211f53d9028404a77?raw=1" color="blue"><u>Introduction to SQL – DataCamp (2024-02)</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://www.datacamp.com/statement-of-accomplishment/course/59e9d6c335f78068a8ca8a740173fd59845fa142?raw=1" color="blue"><u>Foundations of PySpark – DataCamp (2024-02)</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://www.datacamp.com/statement-of-accomplishment/course/3f96604954f801d61b10936afd69763e2f6b86e9?raw=1" color="blue"><u>Feature Engineering with PySpark – DataCamp (2024-02)</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://www.datacamp.com/statement-of-accomplishment/course/7b61bf6901e2d8a08c94890eb3da4f1afa67e509?raw=1" color="blue"><u>Cleaning Data with PySpark – DataCamp (2024-02)</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://www.datacamp.com/statement-of-accomplishment/course/9a5e8e264009fc01f009e5be1aa1ef5fd15cf1c2?raw=1" color="blue"><u>Big Data Fundamentals with PySpark – DataCamp (2024-02)</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://www.datacamp.com/statement-of-accomplishment/course/a55ca6e12ab14f8f920f7d34e2a5a8eac115a1b5?raw=1" color="blue"><u>Understanding Data Engineering – DataCamp (2024-02)</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://stepik.org/cert/1793553?lang=en" color="blue"><u>Python Generation (advanced) – Stepik</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://stepik.org/cert/2141673?lang=en" color="blue"><u>Hadoop, Big Data – Stepik (2023-07)</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://stepik.org/cert/2617752?lang=en" color="blue"><u>FastAPI Python – Stepik (2024-10)</u></a>', styles['CustomNormal']),
         Paragraph('<a href="https://www.hackerrank.com/certificates/5f619d6f531f" color="blue"><u>SQL (Basic) – HackerRank</u></a>', styles['CustomNormal'])
    ]
    elems.append(KeepTogether(certifications_block))

    # Skills (all in one block)
    skills_block = [
        Spacer(1, 2),
        Paragraph("Skills", styles['SubHeader']),
        HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2),
        Paragraph(
            "<b>Core Data Engineering Skills:</b> Python, PySpark, SQL, NoSQL, Apache Airflow, ETL/ELT, Data Pipelines, Data Cleaning, Data Orchestration, FastAPI, Google BigQuery, Snowflake, Docker, GCP (Cloud Platform), Hadoop, Web Scraping, Multiprocessing.",
            styles['CustomNormal']),
        Paragraph(
            "<b>Tools & Technologies:</b> PostgreSQL, MySQL, MS SQL, Cassandra, HDFS, YARN, MapReduce, Apache Spark ML, Anaconda, GitHub, Selenium, Beautiful Soup, Scrapy, Postman, Linux, Bash, Telegram Bot API, Slack, ChatGPT.",
            styles['CustomNormal']),
        Paragraph(
            "<b>Programming & Other:</b> Object-Oriented Programming (OOP), Software Design, Automation, APIs.",
            styles['CustomNormal'])
    ]
    elems.append(KeepTogether(skills_block))

    # Languages
    languages_block = [
        Spacer(1, 2),
        Paragraph("Languages", styles['SubHeader']),
        HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=2),
        Paragraph("- Ukrainian – Native", styles['CustomNormal']),
        Paragraph("- English – Intermediate", styles['CustomNormal'])
    ]
    elems.append(KeepTogether(languages_block))

    doc.build(elems)

cv_pdf('roman_tkachenko_cv.pdf')
