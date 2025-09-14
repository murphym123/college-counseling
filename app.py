from flask import Flask, send_from_directory, request, redirect, url_for
from datetime import datetime
from pathlib import Path
import csv, os

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)

# Health check (optional: Render can ping this)
@app.get("/healthz")
def healthz():
    return "ok", 200

# Serve homepage
@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

# Serve static assets like CSS/JS/images
@app.get("/<path:filename>")
def assets(filename):
    return send_from_directory(BASE_DIR, filename)

# Thank-you page (served from a separate file)
@app.get("/thanks")
def thanks():
    return send_from_directory(BASE_DIR, "thankyou.html")

# Contact form handler
@app.post("/contact")
def contact():
    name = request.form.get("name","").strip()
    email = request.form.get("email","").strip()
    year = request.form.get("year","").strip()
    message = request.form.get("message","").strip()

    leads_path = BASE_DIR / "leads.csv"
    new_file = not leads_path.exists()
    with open(leads_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["timestamp","name","email","student_year","message"])
        w.writerow([datetime.now().isoformat(timespec="seconds"), name, email, year, message])

    # redirect to thank-you page after saving
    return redirect(url_for("thanks"))

if __name__ == "__main__":
    app.run()