
from flask import Flask, render_template, request, send_file
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

from src.parser import extract_domain, detect_domain_type, extract_person
from src.scraper import fetch_website_data
from src.classifier import classify_sector, confidence_score

app = Flask(__name__)


def process_email(email):

    domain = extract_domain(email)
    person = extract_person(email)
    domain_type = detect_domain_type(domain)

    try:
        title, text = fetch_website_data(domain)
    except Exception:
        title, text = None, None

    if not title:
        company = "Unknown"
        sector = "Unknown"
        confidence = "Low"
    else:
        company = title
        sector, _ = classify_sector(text)
        confidence = confidence_score(domain, company, sector)

    return {
        "Email": email,
        "Domain": domain,
        "Domain Type": domain_type,
        "Person": person,
        "Company": company,
        "Sector": sector,
        "Confidence": confidence
    }


@app.route("/", methods=["GET", "POST"])
def index():

    results = None
    download_ready = False

    if request.method == "POST":

        file = request.files.get("csv_file")

        if file and file.filename.endswith(".csv"):

            df = pd.read_csv(file)

            # Parallel processing
            with ThreadPoolExecutor(max_workers=3) as executor:
                results = list(executor.map(process_email, df["email"]))

            # Save Excel
            output_df = pd.DataFrame(results)
            output_df.to_excel("output.xlsx", index=False)

            download_ready = True

    return render_template(
        "index.html",
        results=results,
        download_ready=download_ready
    )


#  Download Excel route (must be OUTSIDE index)
@app.route("/download")
def download_excel():

    return send_file(
        "output.xlsx",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)