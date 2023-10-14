import fitz
import pandas as pd

def extract_company_summary_from_pdf(pdf_path):
    keywords = {
        'profit': None,
        'value': None,
        'Total assets': None,
        'liabilities': None,
        'net profit': None,
        'gross profit': None
    }

    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text = page.get_text()

        for keyword in keywords.keys():
            if keyword in text.lower():
                start_index = text.lower().index(keyword)
                value_start_index = start_index + len(keyword)
                value_end_index = value_start_index + 50  # Assuming value is within the next 50 characters
                keywords[keyword] = text[value_start_index:value_end_index].strip()

        if all(keywords.values()):
            break

    pdf_document.close()
    return keywords


if __name__ == "__main__":
    pdf_file_path = "path/to/your/annual_report.pdf"
    company_summary = extract_company_summary_from_pdf(pdf_file_path)

    df = pd.DataFrame(company_summary.items(), columns=['Metric', 'Value'])
    print(df)
