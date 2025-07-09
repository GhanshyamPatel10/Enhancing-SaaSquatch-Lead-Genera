 Smart Lead Validator & Enricher

A lightweight tool built in under 5 hours to enrich and validate company leads for outbound sales and marketing teams. Upload a CSV file with `Company Name` and `Website` columns, and get enriched leads with LinkedIn URLs, industry info, employee count, and emails.

 🔧 Features

* Upload CSV with company data
* Enrich leads using mock logic or replace with APIs (Clearbit, Hunter.io, etc.)
* Export enriched data to CSV

 🚀 Quick Start

1. Clone this repository

```bash
git clone https://github.com/yourusername/lead-enricher-tool.git
cd lead-enricher-tool
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
streamlit run app.py
```

4. Upload your input file (CSV with `Company Name`, `Website`)

 🧪 Example CSV

```csv
Company Name,Website
OpenAI,https://openai.com
SaaSquatch,https://www.saasquatchleads.com
```

### 📦 Dependencies

* streamlit
* pandas
* requests (for API integration)



 📄 One-Page Report (report.md)

 🔍 Tool: Smart Lead Validator & Enricher

 🔹 Objective

To improve the quality and readiness of B2B leads by enriching them with validated data in seconds—saving hours of manual research for sales and marketing teams.

 🔹 Problem Statement

Raw leads often lack key information like industry, email, or LinkedIn—making them unfit for direct outreach. Sales teams spend excessive time validating each lead.

 🔹 Our Solution

We built a tool that takes basic lead data (Company Name, Website) and enriches it with key business info like:

* Industry
* Employee count
* LinkedIn URL
* Contact Email

This information helps prioritize leads for outbound campaigns and ensures cleaner CRM pipelines.

 🔹 Approach

* Used Python with Streamlit for a rapid, interactive UI
* Mocked enrichment logic (can be replaced with Clearbit/Hunter APIs)
* Export feature built using Pandas

🔹 Value Added

* Saves 2–4 minutes per lead on manual research
* Creates a consistent lead format
* Exportable CSV makes it CRM-compatible

 🔹 Real-World Business Use

Perfect for:

* SDRs preparing prospect lists
* Growth marketers needing enriched data
* SalesOps managing CRM input hygiene

> Time Spent: 4.5 hours total
> Codebase: \~100 lines of Python

✅ Ready for API integration & CRM connection
