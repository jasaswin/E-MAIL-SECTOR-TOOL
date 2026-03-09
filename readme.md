
Project Title

Email → Company / Sector Identification Tool

Objective

To identify the company and industry sector associated with email domains using web scraping and search-based enrichment.

Technologies Used

Python

Flask

Selenium

BeautifulSoup

Pandas

ThreadPoolExecutor

HTML / CSS


System Architecture
Email CSV
   ↓
Domain Extraction
   ↓
Web Scraping
   ↓
Google Search Fallback
   ↓
Sector Classification
   ↓
Results Table
   ↓
Excel Export


Features

CSV upload interface

Bulk processing of emails

Web scraping for company detection

Google search fallback

Sector classification

Excel export

Parallel processing

How to Run
pip install -r requirements.txt
python app.py

Open:

http://127.0.0.1:5000