from flask import Flask, request, send_from_directory, render_template_string
from datetime import datetime
import csv, os

app = Flask(__name__, static_url_path="", static_folder=".")

# Serve your existing index.html
@app.get("/")
def home():
    return send_from_directory(".", "index.html")

# Handle contact form submissions
@app.post("/contact")
def contact():
    name = request.form.get("name","").strip()
    email = request.form.get("email","").strip()
    year = request.form.get("year","").strip()
    message = request.form.get("message","").strip()

    # Save to leads.csv (create if not exists)
    file_exists = os.path.isfile("leads.csv")
    with open("leads.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp","name","email","student_year","message"])
        writer.writerow([datetime.now().isoformat(timespec="seconds"), name, email, year, message])

    # Simple thank-you page
    return render_template_string("""
<!doctype html>
<meta charset="utf-8">
<title>Thanks!</title>
<style>
  body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; line-height:1.6; padding:2rem; }
  a { color:#2563eb; text-decoration:none; }
  a:hover { text-decoration:underline; }
  .box { max-width:600px; margin:auto; padding:1.5rem; border:1px solid #e5e7eb; border-radius:.6rem; }
  .btn { display:inline-block; margin-top:1rem; padding:.6rem .9rem; border:1px solid #2563eb; border-radius:.5rem; }
</style>
<div class="box">
  <h1>Thanks—your message was sent.</h1>
  <p>We’ll get back to you within 1–2 business days.</p>
  <a class="btn" href="/">← Back to site</a>
</div>
""")

if __name__ == "__main__":
    app.run(debug=True)
