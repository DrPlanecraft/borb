from borb.pdf import Alignment
from borb.pdf import ChunkOfText
from borb.pdf import Document
from borb.pdf import PDF
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from tests.test_case import TestCase


class TestAddChunkOfTextUsingAlignment(TestCase):
    def test_add_chunkoftext(self):
        pdf = Document()
        page = Page()
        pdf.add_page(page)
        layout = SingleColumnLayout(page)
        layout.add(
            self.get_test_header(
                test_description="This test adds a ChunkOfText to the PDF."
            )
        )
        layout.add(ChunkOfText("Lorem Ipsum Dolor"))
        with open(self.get_first_output_file(), "wb") as fh:
            PDF.dumps(fh, pdf)
        self.compare_visually_to_ground_truth(self.get_first_output_file())
        self.check_pdf_using_validator(self.get_first_output_file())

    def test_add_chunkoftext_align_left_top(self):
        pdf = Document()
        page = Page()
        pdf.add_page(page)
        layout = SingleColumnLayout(page)
        layout.add(
            self.get_test_header(
                test_description="This test adds a ChunkOfText to the PDF with horizontal alignment LEFT and vertical alignment TOP."
            )
        )
        layout.add(
            ChunkOfText(
                "Lorem Ipsum Dolor",
                horizontal_alignment=Alignment.LEFT,
                vertical_alignment=Alignment.TOP,
            )
        )
        with open(self.get_second_output_file(), "wb") as fh:
            PDF.dumps(fh, pdf)
        self.compare_visually_to_ground_truth(self.get_second_output_file())
        self.check_pdf_using_validator(self.get_second_output_file())

    def test_add_chunkoftext_align_left_middle(self):
        pdf = Document()
        page = Page()
        pdf.add_page(page)
        layout = SingleColumnLayout(page)
        layout.add(
            self.get_test_header(
                test_description="This test adds a ChunkOfText to the PDF with horizontal alignment LEFT and vertical alignment MIDDLE."
            )
        )
        layout.add(
            ChunkOfText(
                "Lorem Ipsum Dolor",
                horizontal_alignment=Alignment.LEFT,
                vertical_alignment=Alignment.MIDDLE,
            )
        )
        with open(self.get_third_output_file(), "wb") as fh:
            PDF.dumps(fh, pdf)
        self.compare_visually_to_ground_truth(self.get_third_output_file())
        self.check_pdf_using_validator(self.get_third_output_file())

    def test_add_chunkoftext_align_left_bottom(self):
        pdf = Document()
        page = Page()
        pdf.add_page(page)
        layout = SingleColumnLayout(page)
        layout.add(
            self.get_test_header(
                test_description="This test adds a ChunkOfText to the PDF with horizontal alignment LEFT and vertical alignment BOTTOM."
            )
        )
        layout.add(
            ChunkOfText(
                "Lorem Ipsum Dolor",
                horizontal_alignment=Alignment.LEFT,
                vertical_alignment=Alignment.BOTTOM,
            )
        )
        with open(self.get_fourth_output_file(), "wb") as fh:
            PDF.dumps(fh, pdf)
        self.compare_visually_to_ground_truth(self.get_fourth_output_file())
        self.check_pdf_using_validator(self.get_fourth_output_file())

    def test_add_chunkoftext_align_centered_top(self):
        pdf = Document()
        page = Page()
        pdf.add_page(page)
        layout = SingleColumnLayout(page)
        layout.add(
            self.get_test_header(
                test_description="This test adds a ChunkOfText to the PDF with horizontal alignment CENTERED and vertical alignment TOP."
            )
        )
        layout.add(
            ChunkOfText(
                "Lorem Ipsum Dolor",
                horizontal_alignment=Alignment.CENTERED,
                vertical_alignment=Alignment.TOP,
            )
        )
        with open(self.get_fifth_output_file(), "wb") as fh:
            PDF.dumps(fh, pdf)
        self.compare_visually_to_ground_truth(self.get_fifth_output_file())
        self.check_pdf_using_validator(self.get_fifth_output_file())

    def test_add_chunkoftext_align_centered_middle(self):
        pdf = Document()
        page = Page()
        pdf.add_page(page)
        layout = SingleColumnLayout(page)
        layout.add(
            self.get_test_header(
                test_description="This test adds a ChunkOfText to the PDF with horizontal alignment CENTERED and vertical alignment MIDDLE."
            )
        )
        layout.add(
            ChunkOfText(
                "Lorem Ipsum Dolor",
                horizontal_alignment=Alignment.CENTERED,
                vertical_alignment=Alignment.MIDDLE,
            )
        )
        with open(self.get_sixth_output_file(), "wb") as fh:
            PDF.dumps(fh, pdf)
        self.compare_visually_to_ground_truth(self.get_sixth_output_file())
        self.check_pdf_using_validator(self.get_sixth_output_file())

    def test_add_chunkoftext_align_centered_bottom(self):
        pdf = Document()
        page = Page()
        pdf.add_page(page)
        layout = SingleColumnLayout(page)
        layout.add(
            self.get_test_header(
                test_description="This test adds a ChunkOfText to the PDF with horizontal alignment CENTERED and vertical alignment BOTTOM."
            )
        )
        layout.add(
            ChunkOfText(
                "Lorem Ipsum Dolor",
                horizontal_alignment=Alignment.CENTERED,
                vertical_alignment=Alignment.BOTTOM,
            )
        )
        with open(self.get_seventh_output_file(), "wb") as fh:
            PDF.dumps(fh, pdf)
        self.compare_visually_to_ground_truth(self.get_seventh_output_file())
        self.check_pdf_using_validator(self.get_seventh_output_file())

    def test_add_chunkoftext_align_right_top(self):
        pdf = Document()
        page = Page()
        pdf.add_page(page)
        layout = SingleColumnLayout(page)
        layout.add(
            self.get_test_header(
                test_description="This test adds a ChunkOfText to the PDF with horizontal alignment RIGHT and vertical alignment TOP."
            )
        )
        layout.add(
            ChunkOfText(
                "Lorem Ipsum Dolor",
                horizontal_alignment=Alignment.RIGHT,
                vertical_alignment=Alignment.TOP,
            )
        )
        with open(self.get_eight_output_file(), "wb") as fh:
            PDF.dumps(fh, pdf)
        self.compare_visually_to_ground_truth(self.get_eight_output_file())
        self.check_pdf_using_validator(self.get_eight_output_file())

    def test_add_chunkoftext_align_right_middle(self):
        pdf = Document()
        page = Page()
        pdf.add_page(page)
        layout = SingleColumnLayout(page)
        layout.add(
            self.get_test_header(
                test_description="This test adds a ChunkOfText to the PDF with horizontal alignment RIGHT and vertical alignment MIDDLE."
            )
        )
        layout.add(
            ChunkOfText(
                "Lorem Ipsum Dolor",
                horizontal_alignment=Alignment.RIGHT,
                vertical_alignment=Alignment.MIDDLE,
            )
        )
        with open(self.get_nineth_output_file(), "wb") as fh:
            PDF.dumps(fh, pdf)
        self.compare_visually_to_ground_truth(self.get_nineth_output_file())
        self.check_pdf_using_validator(self.get_nineth_output_file())

    def test_add_chunkoftext_align_right_bottom(self):
        pdf = Document()
        page = Page()
        pdf.add_page(page)
        layout = SingleColumnLayout(page)
        layout.add(
            self.get_test_header(
                test_description="This test adds a ChunkOfText to the PDF with horizontal alignment RIGHT and vertical alignment BOTTOM."
            )
        )
        layout.add(
            ChunkOfText(
                "Lorem Ipsum Dolor",
                horizontal_alignment=Alignment.RIGHT,
                vertical_alignment=Alignment.BOTTOM,
            )
        )
        with open(self.get_tenth_output_file(), "wb") as fh:
            PDF.dumps(fh, pdf)
        self.compare_visually_to_ground_truth(self.get_tenth_output_file())
        self.check_pdf_using_validator(self.get_tenth_output_file())
