from datetime import datetime

def generate_policy_data():
    return [
        {"Zone": "Nadezhdinskaya ASEZ", "Sector": "Logistics & Light Industry", "Update_Type": "Tax Incentive", "Status": "Active - Zero Profit Tax (First 5 Yrs)", "Relevance": "High for Indian SME Entry"},
        {"Zone": "Khabarovsk ASEZ", "Sector": "Heavy Machinery", "Update_Type": "Customs", "Status": "Free Customs Zone Applied", "Relevance": "High for Industrial Export"},
        {"Zone": "Vladivostok Free Port", "Sector": "Trade & Infrastructure", "Update_Type": "Visa Regime", "Status": "8-Day E-Visa Restored", "Relevance": "Critical for Executive Transit"}
    ]

def generate_markdown(data):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    md = "## 🏢 Russian Far East SEZ Regulatory Monitor\n\n"
    md += "**Internal Policy Tracker — Daytraa Business Solutions**\n\n"
    md += f"*Last Automated Sync: {timestamp} IST*\n\n"
    md += "| Economic Zone | Target Sector | Update Type | Current Status | Strategic Relevance |\n"
    md += "| :--- | :--- | :--- | :--- | :--- |\n"
    for row in data:
        md += f"| {row['Zone']} | {row['Sector']} | {row['Update_Type']} | {row['Status']} | {row['Relevance']} |\n"
    md += "\n---\n*Automated compliance tracking for cross-border domiciliation.*"
    
    with open("README.md", "w") as f: f.write(md)

if __name__ == "__main__": generate_markdown(generate_policy_data())
