from pathlib import Path
from pypdf import PdfReader


class FileReader:
    """
    Reads different file types.
    """
    
    def resolve_file(self, file: Path):

        if file.exists():
            return file

        extensions = [
            ".txt",
            ".md",
            ".pdf",
            ".json",
            ".csv",
            ".py"
        ]

        for ext in extensions:

            candidate = file.with_suffix(ext)

            if candidate.exists():
                return candidate

        return None

    def read(self, path: str):

        file = self.resolve_file(Path(path))

        if file is None:
            return None

        extension = file.suffix.lower()

        if extension in ("", ".txt"):
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