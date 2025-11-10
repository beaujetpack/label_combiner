import requests
from pypdf import PdfWriter, PdfReader
from pathlib import Path
import io
import time
import os
import sys

def download_and_combine_pdfs_from_txt(txt_file_path, output_filename="combined.pdf"):
    """
    Download PDFs from URLs in a text file and combine them into one PDF.
    
    Args:
        txt_file_path: Path to the text file with one URL per line
        output_filename: Name of the output combined PDF file
    """
    
    # Convert to Path object for easier manipulation
    output_path = Path(output_filename)
    
    # If file exists, find an available filename with a number
    if output_path.exists():
        counter = 1
        stem = output_path.stem
        suffix = output_path.suffix
        parent = output_path.parent
        
        while True:
            new_name = f"{stem}_{counter}{suffix}"
            new_path = parent / new_name
            if not new_path.exists():
                output_filename = new_path
                break
            counter += 1
        
        print(f"Output file exists, using: {output_filename}\n")
    
    # Read URLs from text file
    with open(txt_file_path, 'r') as f:
        pdf_urls = [line.strip() for line in f if line.strip()]
    
    print(f"Total URLs in file: {len(pdf_urls)}")
    
    # Remove duplicates while preserving order
    pdf_urls = list(dict.fromkeys(pdf_urls))
    print(f"After removing duplicates: {len(pdf_urls)} unique URLs")
    
    # Show first few URLs for verification
    print("\nFirst 3 URLs:")
    for url in pdf_urls[:3]:
        print(f"  {url}")
    
    print(f"\nStarting download and combination...\n")
    
    # Create a PDF writer object
    pdf_writer = PdfWriter()
    
    # Download and add each PDF
    for idx, url in enumerate(pdf_urls, 1):
        try:
            print(f"Downloading PDF {idx}/{len(pdf_urls)}: {url}")
            
            # Download the PDF
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Read the PDF from memory
            pdf_file = io.BytesIO(response.content)
            pdf_reader = PdfReader(pdf_file)
            
            # Add all pages from this PDF
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
            
            print(f"  ✓ Added {len(pdf_reader.pages)} pages")
            
            # Small delay to be respectful to servers
            time.sleep(0.5)
            
        except Exception as e:
            print(f"  ✗ Error processing {url}: {str(e)}")
            continue
    
    # Write the combined PDF
    with open(output_filename, 'wb') as output_file:
        pdf_writer.write(output_file)
    
    print(f"\n✓ Combined PDF saved as: {output_filename}")
    print(f"Total pages: {len(pdf_writer.pages)}")


if __name__ == "__main__":
    # Get the directory of the executable (or script)
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        SCRIPT_DIR = Path(sys.executable).parent
    else:
        # Running as Python script
        SCRIPT_DIR = Path(__file__).parent
    
    TXT_FILE_PATH = SCRIPT_DIR / "links.txt"
    OUTPUT_FILE = SCRIPT_DIR / "combined_orders.pdf"
    
    download_and_combine_pdfs_from_txt(TXT_FILE_PATH, OUTPUT_FILE)