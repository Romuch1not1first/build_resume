# Resume Builder

A Python application that generates a professional PDF resume using ReportLab library.

## Features

- Clean, professional resume layout
- Structured sections: Header, Summary, Experience, Projects, Education, Certifications, Skills, and Languages
- Clickable links for LinkedIn and certifications
- Responsive design optimized for A4 page size
- Custom styling with proper spacing and typography

## Requirements

- Python 3.6+
- ReportLab library

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd build_resume
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Simply run the script to generate the PDF resume:

```bash
python res_builder.py
```

This will create a file named `roman_tkachenko_cv.pdf` in the current directory.

## Customization

To customize the resume for your own use:

1. Edit the `res_builder.py` file
2. Modify the personal information in the header section (lines 20-23)
3. Update the experience, projects, education, and other sections as needed
4. Run the script to generate your personalized resume

## Project Structure

- `res_builder.py` - Main script that generates the PDF resume
- `roman_tkachenko_cv.pdf` - Generated PDF resume (example output)
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Dependencies

- reportlab - For PDF generation and formatting

## License

This project is open source and available under the MIT License.
