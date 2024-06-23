import fitz  # Import the PyMuPDF library for reading PDF files
import os    # Import the os library for file system operations

def search_keywords_in_pdf(pdf_path, keywords):
    """
    Searches for specified keywords in a single PDF file.

    Args:
        pdf_path (str): Path to the PDF file.
        keywords (list of str): List of keywords to search for.

    Returns:
        list of tuples: Each tuple contains (file_path, page_number, keyword).
    """
    results = []
    try:
        document = fitz.open(pdf_path)  # Open the PDF file
        for page_num in range(len(document)):  # Iterate through each page in the PDF
            page = document[page_num]
            text = page.get_text()  # Extract the text content of the page
            for keyword in keywords:
                if keyword.lower() in text.lower():  # Case-insensitive search for the keyword
                    results.append((pdf_path, page_num + 1, keyword))  # Append the result if keyword is found
        document.close()  # Close the document
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")  # Print an error message if the PDF can't be read
    return results

def search_keywords_in_pdfs(pdf_folder, keywords, output_file):
    """
    Searches for specified keywords in all PDF files within a folder and its subfolders.

    Args:
        pdf_folder (str): Path to the folder containing PDF files.
        keywords (list of str): List of keywords to search for.
        output_file (str): Path to the output text file where results will be written.

    Returns:
        None
    """
    results = []
    for root, _, files in os.walk(pdf_folder):  # Walk through the folder and its subfolders
        for file in files:
            if file.lower().endswith('.pdf'):  # Check if the file is a PDF
                pdf_path = os.path.join(root, file)  # Get the full path of the PDF file
                results.extend(search_keywords_in_pdf(pdf_path, keywords))  # Search for keywords in the PDF file
    
    with open(output_file, 'w') as f:  # Open the output file in write mode
        for result in results:
            f.write(f"File: {result[0]}, Page: {result[1]}, Keyword: {result[2]}\n")  # Write the results to the file

if __name__ == "__main__":
    # Define the path to the folder containing PDF files
    pdf_folder = "path/to/your/pdf/folder"
    
    # Define the list of keywords to search for
    keywords = ["keyword1", "keyword2", "keyword3"]
    
    # Define the path to the output text file
    output_file = "search_results.txt"
    
    # Call the function to search for keywords in PDFs and write the results to the output file
    search_keywords_in_pdfs(pdf_folder, keywords, output_file)
    
    # Print a message indicating that the results have been written to the output file
    print(f"Results written to {output_file}")
