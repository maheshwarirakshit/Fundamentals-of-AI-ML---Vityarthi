# Fundamentals-of-AI-ML---Vityarthi
# 📄 AI Document Summarizer

An AI-powered Python automation tool that automatically summarizes PDF and TXT documents using Google Gemini. Drop your files in, run the script, and get clean, readable summaries saved instantly.

---

## 🚀 What It Does

- Accepts `.pdf` and `.txt` files as input
- Extracts text automatically from any document
- Sends the content to **Google Gemini AI** for intelligent summarization
- Lets you choose your summary detail level: **Short**, **Medium**, or **Detailed**
- Saves each summary as a `.txt` file in the `output/` folder
- Batch processes multiple files in one run

---

## 📁 Project Structure

```
ai-document-summarizer/
│
├── input/               # Place your PDF or TXT files here
├── output/              # Summaries are saved here automatically
├── summarizer.py        # Main script
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-document-summarizer.git
cd ai-document-summarizer
```

### 2. Install Dependencies

Make sure you have Python 3.8 or higher installed. Then run:

```bash
pip install -r requirements.txt
```

### 3. Get a Free Gemini API Key

1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the key

### 4. Add Your API Key

Open `AI-Document-Summarizer.py` and replace the placeholder on line 9:

```python
GEMINI_API_KEY = "AIzaSyDekJaZCBMNPxgGagBaqdH08f52getRJ9w"
```

with your actual key:

```python
GEMINI_API_KEY = "AIzaSyDekJaZCBMNPxgGagBaqdH08f52getRJ9w"
```

---

## ▶️ How to Use

### Step 1 — Add your files

Copy any `.pdf` or `.txt` files into the `input/` folder.

### Step 2 — Run the script

```bash
python AI-Document-Summarizer.py
```

### Step 3 — Choose summary length

```
Summary detail level:
  [1] Short    (3–5 sentences)
  [2] Medium   (2–3 paragraphs)  ← default
  [3] Detailed (full breakdown)

Enter 1, 2, or 3 (press Enter for default):
```

### Step 4 — Get your summaries

Summaries are saved in the `output/` folder as `filename_summary.txt`.

---

## 🧪 Example

**Input:** `input/research_paper.pdf`

**Run:** `python summarizer.py` → choose `2` for Medium

**Output:** `output/research_paper_summary.txt`

```
SUMMARY OF: research_paper.pdf
Detail level: MEDIUM
==================================================

This paper investigates the impact of urban green spaces on mental health
outcomes in densely populated cities. The researchers conducted a 12-month
longitudinal study across five cities, surveying over 3,000 participants...
```

---

## 📦 Dependencies

| Library | Purpose |
|---|---|
| `google-generativeai` | Connects to Google Gemini AI API |
| `pdfplumber` | Extracts text from PDF files |

---

## ⚠️ Limitations

- Very large documents (over ~30,000 characters) are trimmed before summarization
- Scanned PDFs (image-based) cannot be read without OCR — only text-based PDFs are supported
- Requires an active internet connection to call the Gemini API

---

## 🛠️ Built With

- Python 3
- [Google Gemini API](https://ai.google.dev/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)


#Rakshit Maheshwari

#25BCE10162

#VIT Bhopal University
