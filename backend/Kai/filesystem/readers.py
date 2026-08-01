from pathlib import Path
from pypdf import PdfReader


class FileReader:
    """
    Reads different file types.
    """

    def read(self, path: str):

        file = Path(path)

        if not file.exists():
            return None

        extension = file.suffix.lower()

        if extension == ".txt":
            return self.read_txt(file)

        if extension == ".md":
            return self.read_md(file)

        if extension == ".pdf":
            return self.read_pdf(file)

        return "Unsupported file type."

    def read_txt(self, file: Path):

        with open(file, "r", encoding="utf-8") as f:
            return f.read()

    def read_md(self, file: Path):

        with open(file, "r", encoding="utf-8") as f:
            return f.read()

    def read_pdf(self, file: Path):

        reader = PdfReader(str(file))

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text.strip()