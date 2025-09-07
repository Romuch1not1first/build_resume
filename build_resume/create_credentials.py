import json

# Example credentials template
example_credentials = {
    "personal_info": {
        "name": "Your Name",
        "title": "Your Job Title",
        "location": "Your Location",
        "phone": "Your Phone Number",
        "email": "your.email@example.com",
        "linkedin": "https://www.linkedin.com/in/yourprofile/"
    },
    "summary": "Your professional summary here...",
    "experience": [
        {
            "title": "Job Title",
            "company": "Company Name - Location",
            "period": "MM/YYYY - MM/YYYY",
            "description": [
                "First bullet point of your responsibilities.",
                "Second bullet point of your responsibilities.",
                "Third bullet point of your responsibilities."
            ]
        }
    ],
    "projects": [
        {
            "name": "Project Name",
            "period": "YYYY",
            "description": [
                "First bullet point describing the project.",
                "Second bullet point describing the project.",
                "Third bullet point describing the project."
            ]
        }
    ],
    "education": [
        "Degree – University Name, YYYY-YYYY",
        "Additional Education – Institution, YYYY"
    ],
    "certifications": [
        {
            "name": "Certification Name (YYYY-MM)",
            "url": "https://example.com/certificate-link"
        }
    ],
    "skills": {
        "core_data_engineering": "Your core skills here...",
        "tools_technologies": "Your tools and technologies here...",
        "programming_other": "Your programming and other skills here..."
    },
    "languages": [
        "Language 1 – Proficiency Level",
        "Language 2 – Proficiency Level"
    ]
}

# Roman's actual credentials
roman_credentials = {
    "personal_info": {
        "name": "Roman Tkachenko",
        "title": "Data Engineer",
        "location": "Kyiv, Ukraine",
        "phone": "+380970757662",
        "email": "romuchqq@gmail.com",
        "linkedin": "https://www.linkedin.com/in/romuch/"
    },
    "summary": "Data Engineer skilled in Python, PySpark and SQL with hands-on experience building end-to-end data pipelines on GCP. Comfortable orchestrating ETL/ELT flows with Apache Airflow and Docker, applying data-quality checks, and collaborating in distributed teams.",
    "experience": [
        {
            "title": "Python Scraper Developer",
            "company": "OnlineMinds - Remote (Copenhagen, Denmark)",
            "period": "03/2023 - 07/2023",
            "description": [
                "Worked in a distributed team at a startup to build scalable data scraping pipelines.",
                "Developed web scraping solutions using Scrapy and Python.",
                "Automated data collection workflows and structured large volumes of data.",
                "Collaborated on GitHub, followed version control best practices.",
                "Contributed to team discussions and agile development cycles."
            ]
        }
    ],
    "projects": [
        {
            "name": "DE-homework-tasks",
            "period": "05/2024 - 06/2024",
            "description": [
                "Built and orchestrated end-to-end data pipelines as part of a comprehensive data engineering project.",
                "Developed ETL jobs to fetch, transform, and store sales data (JSON, Avro).",
                "Set up a PostgreSQL demo DB with Docker, wrote SQL queries.",
                "Installed and configured Apache Airflow, built DAGs to automate workflows.",
                "Used GCP (BigQuery, GCS) and PySpark (local) for dual pipeline execution.",
                "Configured PySpark in Jupyter Notebook for distributed data processing.",
                "Integrated third-party data (user_profiles) for enrichment, applied data quality checks.",
                "Delivered final project aligned with industry-grade data governance and orchestration practices."
            ]
        },
        {
            "name": "Python-scraper-rental-property",
            "period": "2023",
            "description": [
                "Designed and implemented a scalable Python data scraping solution using GraphQL and multiprocessing.",
                "Parsed and structured real estate listings from GraphQL APIs.",
                "Used multiprocessing for parallel data collection and aggregation.",
                "Output aggregated dataset into a structured JSON file for analysis."
            ]
        },
        {
            "name": "Telegram-bot-purchase-discount",
            "period": "2023",
            "description": [
                "Automated buyer-seller interaction with two Telegram bots to generate and validate promo codes.",
                "Ensured seamless transaction flow using Telegram Bot API and data validation logic."
            ]
        }
    ],
    "education": [
        "BSc – Kyiv National Economics University, 2019-2023",
        "Data Engineering Bootcamp – Robot_Dreams, 2024"
    ],
    "certifications": [
        {
            "name": "Data Engineering – Robot dreams (2024-06)",
            "url": "https://lms.robotdreams.cc/certificate/2e480b21e02dff5e65889aed4cc36ae1"
        },
        {
            "name": "Joining Data in SQL – DataCamp (2024-03)",
            "url": "https://www.datacamp.com/statement-of-accomplishment/course/29e98329ec4d55f8134e17216d593728bed8a063?raw=1"
        },
        {
            "name": "Intermediate SQL – DataCamp (2024-03)",
            "url": "https://www.datacamp.com/statement-of-accomplishment/course/61888063091274e09813f85e58fa306d00a3d421?raw=1"
        },
        {
            "name": "Introduction to SQL – DataCamp (2024-02)",
            "url": "https://www.datacamp.com/statement-of-accomplishment/course/72362fca72a0af004867bac211f53d9028404a77?raw=1"
        },
        {
            "name": "Foundations of PySpark – DataCamp (2024-02)",
            "url": "https://www.datacamp.com/statement-of-accomplishment/course/59e9d6c335f78068a8ca8a740173fd59845fa142?raw=1"
        },
        {
            "name": "Feature Engineering with PySpark – DataCamp (2024-02)",
            "url": "https://www.datacamp.com/statement-of-accomplishment/course/3f96604954f801d61b10936afd69763e2f6b86e9?raw=1"
        },
        {
            "name": "Cleaning Data with PySpark – DataCamp (2024-02)",
            "url": "https://www.datacamp.com/statement-of-accomplishment/course/7b61bf6901d8a08c94890eb3da4f1afa67e509?raw=1"
        },
        {
            "name": "Big Data Fundamentals with PySpark – DataCamp (2024-02)",
            "url": "https://www.datacamp.com/statement-of-accomplishment/course/9a5e8e264009fc01f009e5be1aa1ef5fd15cf1b5?raw=1"
        },
        {
            "name": "Understanding Data Engineering – DataCamp (2024-02)",
            "url": "https://www.datacamp.com/statement-of-accomplishment/course/a55ca6e12ab14f8f920f7d34e2a5a8eac115a1b5?raw=1"
        },
        {
            "name": "Python Generation (advanced) – Stepik",
            "url": "https://stepik.org/cert/1793553?lang=en"
        },
        {
            "name": "Hadoop, Big Data – Stepik (2023-07)",
            "url": "https://stepik.org/cert/2141673?lang=en"
        },
        {
            "name": "FastAPI Python – Stepik (2024-10)",
            "url": "https://stepik.org/cert/2617752?lang=en"
        },
        {
            "name": "SQL (Basic) – HackerRank",
            "url": "https://www.hackerrank.com/certificates/5f619d6f531f"
        }
    ],
    "skills": {
        "core_data_engineering": "Python, PySpark, SQL, NoSQL, Apache Airflow, ETL/ELT, Data Pipelines, Data Cleaning, Data Orchestration, FastAPI, Google BigQuery, Snowflake, Docker, GCP (Cloud Platform), Hadoop, Web Scraping, Multiprocessing.",
        "tools_technologies": "PostgreSQL, MySQL, MS SQL, Cassandra, HDFS, YARN, MapReduce, Apache Spark ML, Anaconda, GitHub, Selenium, Beautiful Soup, Scrapy, Postman, Linux, Bash, Telegram Bot API, Slack, ChatGPT.",
        "programming_other": "Object-Oriented Programming (OOP), Software Design, Automation, APIs."
    },
    "languages": [
        "Ukrainian – Native",
        "English – Intermediate"
    ]
}

# Write example credentials file
with open('credentials.example.json', 'w', encoding='utf-8') as f:
    json.dump(example_credentials, f, indent=2, ensure_ascii=False)

# Write Roman's credentials file
with open('credentials.json', 'w', encoding='utf-8') as f:
    json.dump(roman_credentials, f, indent=2, ensure_ascii=False)

print("Created credentials.example.json and credentials.json files successfully!")
