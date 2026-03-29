import os
import pathlib
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyDekJaZCBMNPxgGagBaqdH08f52getRJ9w"

OUTPUT_FOLDER = r"Enter-your-output-folder-path"
# SETUP

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def clean_path(raw: str) -> str:
    raw = raw.strip()
    # Remove surrounding double quotes (Windows adds these for paths with spaces)
    if len(raw) >= 2 and raw[0] == '"' and raw[-1] == '"':
        raw = raw[1:-1]
    # Remove surrounding single quotes
    elif len(raw) >= 2 and raw[0] == "'" and raw[-1] == "'":
        raw = raw[1:-1]
    return raw.strip()

def extract_text(filepath: pathlib.Path) -> str:
    suffix = filepath.suffix.lower()

    if suffix == ".txt":
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    elif suffix == ".pdf":
        try:
            import pdfplumber
        except ImportError:
            raise ImportError(
                "pdfplumber is not installed. Run: pip install pdfplumber"
            )
        text = ""
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    else:
        raise ValueError(f"Unsupported file type: {suffix}")

def summarize_text(text: str, detail: str = "medium") -> str:
    detail_instructions = {
        "short":    "Write a concise summary in 3-5 sentences.",
        "medium":   "Write a clear summary in 2-3 paragraphs covering the main points.",
        "detailed": "Write a detailed summary with key points, important details, and conclusions.",
    }
    instruction = detail_instructions.get(detail, detail_instructions["medium"])

    # Gemini has a token limit — truncate very large documents
    max_chars = 30_000
    if len(text) > max_chars:
        print(f"  Warning: Document is large — using first {max_chars} characters.")
        text = text[:max_chars]

    prompt = f"""You are a professional document summarizer.

{instruction}

Document:
\"\"\"
{text}
\"\"\"

Summary:"""

    response = model.generate_content(prompt)
    return response.text.strip()

# MAIN

def main():
    print("=" * 55)
    print("       AI Document Summarizer - Powered by Gemini")
    print("=" * 55)

    # Step 1: Ask user to enter file paths
    files = []
    print("\nEnter the path to each file you want to summarize.")
    print("You can add multiple files one by one.")
    print("Tip: On Windows, right-click your file > 'Copy as path', then paste here.")
    print("Press Enter with no input when you are done.\n")

    while True:
        raw = input("  File path (or press Enter to finish): ")
        cleaned = clean_path(raw)

        if cleaned == "":
            if not files:
                print("\nNo files entered. Please run the script again and provide at least one file.")
                return
            break

        filepath = pathlib.Path(cleaned)

        if not filepath.exists():
            print(f"  File not found: {cleaned}")
            print(f"  Tip: On Windows, right-click the file and choose 'Copy as path', then paste.\n")
            continue

        if filepath.suffix.lower() not in [".pdf", ".txt"]:
            print(f"  Unsupported file type '{filepath.suffix}'. Only .pdf and .txt are supported.\n")
            continue

        files.append(filepath)
        print(f"  Added: {filepath.name}\n")

    # Step 2: Ask for summary detail level
    print("\nSummary detail level:")
    print("  [1] Short    (3-5 sentences)")
    print("  [2] Medium   (2-3 paragraphs)  <- default")
    print("  [3] Detailed (full breakdown)")
    choice = input("\nEnter 1, 2, or 3 (press Enter for default): ").strip()
    detail_map = {"1": "short", "2": "medium", "3": "detailed", "": "medium"}
    detail = detail_map.get(choice, "medium")

    # Step 3: Process each file
    print(f"\nSummarizing {len(files)} file(s)...\n")

    success_count = 0
    for filepath in files:
        print(f"--- Processing: {filepath.name}")

        try:
            print("    Extracting text...")
            text = extract_text(filepath)

            if not text.strip():
                print("    No text could be extracted. Skipping.\n")
                continue

            print("    Sending to Gemini AI...")
            summary = summarize_text(text, detail=detail)

            output_filename = filepath.stem + "_summary.txt"
            output_path = pathlib.Path(OUTPUT_FOLDER) / output_filename

            with open(output_path, "w", encoding="utf-8") as out:
                out.write(f"SUMMARY OF: {filepath.name}\n")
                out.write(f"Detail level: {detail.upper()}\n")
                out.write("=" * 50 + "\n\n")
                out.write(summary)
                out.write("\n")

            print(f"    Summary saved -> output/{output_filename}\n")
            success_count += 1

        except Exception as e:
            print(f"    Error: {e}\n")

    print("=" * 55)
    print(f"  Done! {success_count}/{len(files)} file(s) summarized.")
    print(f"  Check the '{OUTPUT_FOLDER}/' folder for your summaries.")
    print("=" * 55)


if __name__ == "__main__":
    main()
