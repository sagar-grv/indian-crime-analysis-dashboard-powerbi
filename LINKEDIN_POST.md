# LinkedIn Post Draft

I built an **Indian Crime Analysis Dashboard** in Microsoft Power BI to turn a multidimensional dataset into a clear national-to-local analytical journey.

### The problem

Crime records spread across years, states, districts and offence categories are difficult to investigate through static tables. A useful report should help the viewer move from the overall pattern to the exact local context that needs review.

### The approach

- **National Overview** establishes context through KPI cards, a yearly trend, map, state comparison and decomposition tree.
- **State Deep-Dive** explains category share and district contribution within a selected state.
- **District-Wise Analysis** compares a district with its state average and shows the size of the gap.

The semantic model contains **18 explicit DAX measures**, including totals, crime-category shares, previous-year comparison, year-over-year change, a rolling three-year average, district share and state-average comparisons.

### Evidence and quality assurance

The GitHub repository includes:

- Verified inventory of **3 report pages** and **24 visual containers**
- DAX and field documentation
- Data-lineage and expected CSV schema
- SHA-256 checksum for file integrity
- A reproducible technical-evidence report
- A transparent quality review

During verification, I found that the supplied `Total Robbery` measure sums the Theft column. I documented the defect and its likely correction rather than presenting unsupported robbery results. This was an important reminder that dashboard development also requires model testing and responsible communication.

### Skills applied

Power BI • Power Query • DAX • time intelligence • geographic analysis • data modelling • quality assurance • data storytelling

Repository: https://github.com/sagar-grv/indian-crime-analysis-dashboard-powerbi

Feedback from Power BI developers, data analysts and business-intelligence professionals is welcome.

#PowerBI #DataAnalytics #BusinessIntelligence #DataVisualization #DAX #PowerQuery #DataQuality #DashboardDesign #DataStorytelling #PortfolioProject #OpenToWork
