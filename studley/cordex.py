from pypdf import PdfWriter, PdfReader

def get_codex_sequence(input_seq):

    first_half = input_seq[:len(input_seq)//2]
    second_half = input_seq[len(input_seq)//2:]
    second_half.reverse()
    res = []

    for i in range(len(input_seq)//4):
        res.append(second_half.pop(0))
        res.append(first_half.pop(0))
        res.append(first_half.pop(0))
        res.append(second_half.pop(0))

    return res

def reorder_pdfs(codex_sequence: list):
    PAGES_PER_CODEX = len(codex_sequence)
    pdf_writer = PdfWriter()

    with open("Programming Languages - Principles and Paradigms.pdf", "rb") as f:
        input_pdf = PdfReader(f)
        total_number_pages = len(input_pdf.pages)

        for codex_number in range(total_number_pages//PAGES_PER_CODEX):
            for page_number in codex_sequence:
                pdf_writer.add_page(input_pdf.pages[page_number+codex_number*PAGES_PER_CODEX])

        with open("output_test.pdf", "wb") as writef:
            pdf_writer.write(writef)

if __name__ == "__main__":
    input_seq = [i for i in range(16)]
    res = get_codex_sequence(input_seq)
    reorder_pdfs(res)
    print(res)
    