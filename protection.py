import PyPDF2
import sys
def create_password_protected_pdf(input_pdf_path, output_pdf_path, password):
    # Open the original PDF file
    try:
        with open(input_pdf_path, 'rb') as input_file:
            reader = PyPDF2.PdfReader(input_file)
            writer = PyPDF2.PdfWriter()

            # Add all pages to the writer
            for page_num in range(len(reader.pages)):
                writer.add_page(reader.pages[page_num])

            # Encrypt the PDF with the provided password
            writer.encrypt(password)

            # Write the encrypted PDF to a new file
            with open(output_pdf_path, 'wb') as output_file:
                writer.write(output_file)

            print(f"Password-protected PDF created: {output_pdf_path}")
    except FileNotFoundError:
        print(f"Error: The file {input_pdf_path} was not found.")
    except PyPDF2.utils_PdfReadError:
        print(f"Error: The file {input_pdf_path} is not a valid PDF.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python protection.py <input_pdf_path> <output_pdf_path> <password>")
        sys.exit(1)

    input_pdf_path = sys.argv[1]
    output_pdf_path = sys.argv[2]
    password = sys.argv[3]

    create_password_protected_pdf(input_pdf_path, output_pdf_path, password)

if __name__ == "__main__":
    main()