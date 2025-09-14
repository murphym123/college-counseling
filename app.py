from flask import Flask, send_from_directory, request, render_template_string
from datetime import datetime
from pathlib import Path
import csv, os

BASE_DIR = Path(__file__).resolve().parent  # absolute path to this folder
app = Flask(__name__)

# ---- Root + static files (served from the repo folder) ----
@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.get("/<path:filename>")
def assets(filename):
    # serves styles.css, script.js, images, etc.
    return send_from_directory(BASE_DIR, filename)

# ---- Contact form ----
@app.post("/contact")
def contact():
    name = request.form.get("name","").strip()
    email = request.form.get("email","").strip()
    year = request.form.get("year","").strip()
    message = request.form.get("message","").strip()

    file_exists = (BASE_DIR / "leads.csv").exists()
    with open(BASE_DIR / "leads.csv", "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not file_exists:
            w.writerow(["timestamp","name","email","student_year","message"])
        from datetime import datetime
        w.writerow([datetime.now().isoformat(timespec="seconds"), name, email, year, message])

    return render_template_string("""
    <!doctype html><meta charset="utf-8"><title>Thanks!</title>
    <style>
      body { font-family: system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif; line-height:1.6; padding:2rem; }
      a { color:#2563eb; text-decoration:none; } a:hover{ text-decoration:underline; }
      .box{ max-width:600px; margin:auto; padding:1.5rem; border:1px solid #e5e7eb; border-radius:.6rem; }
      .btn{ display:inline-block; margin-top:1rem; padding:.6rem .9rem; border:1px
