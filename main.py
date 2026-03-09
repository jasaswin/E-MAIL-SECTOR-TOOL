


import pandas as pd

from src.parser import extract_domain, detect_domain_type, extract_person
from src.scraper import fetch_website_data
from src.classifier import classify_sector, confidence_score


def process_email(email):

    domain = extract_domain(email)
    person = extract_person(email)
    domain_type = detect_domain_type(domain)

    title, text = fetch_website_data(domain)

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


def main():

    df = pd.read_csv("data/emails.csv")

    results = []

    for email in df["email"]:

        print(f"Processing: {email}")

        result = process_email(email)

        results.append(result)

    output_df = pd.DataFrame(results)

    output_df.to_excel("output.xlsx", index=False)

    print("\nAll emails processed successfully.")
    print("Output saved to output.xlsx")


if __name__ == "__main__":
    main()