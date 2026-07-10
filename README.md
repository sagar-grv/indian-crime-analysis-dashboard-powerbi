# Indian Crime Analysis Dashboard | Power BI

> National-to-district analysis of reported IPC crime indicators across 2001–2014.

[![Power BI](https://img.shields.io/badge/Microsoft-Power%20BI-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Portfolio Project](https://img.shields.io/badge/Project-Portfolio-blue)](https://github.com/sagar-grv/indian-crime-analysis-dashboard-powerbi)
[![Verification](https://img.shields.io/badge/Report-Verified-success)](docs/technical-evidence.md)

## Why This Project Exists

Crime records spread across years, states, districts and offence categories are difficult to explore through static tables. This report converts that complexity into a deliberate analytical sequence that moves from the national picture to the local exception.

## Analytical Story

The report uses a **national-to-local drill-down** narrative:

1. **Establish the national picture** — KPI cards, a yearly trend, map, state comparison and decomposition tree identify where deeper investigation is required.
2. **Explain the state context** — the state page compares category shares and district contributions within a selected state.
3. **Test district-level deviation** — the district page compares a district with its state average and exposes the size of the gap.

The model includes 18 explicit DAX measures covering totals, category shares, previous-year comparison, year-over-year change, a rolling three-year average, district share and state-average comparisons. A formula defect found during verification is documented transparently in [`docs/quality-review.md`](docs/quality-review.md); the original PBIT is preserved as supplied rather than silently altered without Power BI Desktop validation.

## Verified Project Evidence

The supplied Power BI artefact was inspected in read-only mode by parsing its internal `Report/Layout` metadata and `DataModelSchema`. This verifies the project structure independently of screenshots.

| Evidence | Verified value |
|---|---:|
| Power BI pages | **3** |
| Visual containers | **24** |
| Explicit DAX measures | **18** |
| Configured period | **2001–2014** |
| Dashboard file size | **23,928 bytes** |
| SHA-256 | `8d6fde4dfb120ca98f93dc4d4db8f661742f0bb06bb57f82decd5d781de12984` |

### Page and Visual Inventory

| Report page | Visuals | Verified visual types |
|---|---:|---|
| National Overview | 12 | `card` × 6, `lineChart` × 1, `decompositionTree` × 1, `clusteredBarChart` × 1, `map` × 1, `textbox` × 1, `actionButton` × 1 |
| State Deep-Dive | 6 | `funnel` × 1, `clusteredColumnChart` × 1, `multiRowCard` × 1, `table` × 1, `slicer` × 1, `textbox` × 1 |
| DISTRICT WISE DIVE | 6 | `card` × 2, `table` × 1, `line/stacked-column combo` × 1, `textbox` × 1, `slicer` × 1 |

Full proof is available in [`docs/technical-evidence.md`](docs/technical-evidence.md) and [`evidence/report-inventory.json`](evidence/report-inventory.json).

## Data Fields Referenced by the Report

`State`, `District`, `Year`, `Murder`, `Rape`, `Robbery`, `Theft`, `Kidnapping`, `Total_IPC_Crimes`

## Transparent Quality Finding

The supplied model defines:

```DAX
Total Robbery = SUM ( crime_data[Theft] )
```

The likely intended calculation is:

```DAX
Total Robbery = SUM ( crime_data[Robbery] )
```

This finding affects robbery KPIs and percentage calculations and must be corrected and validated in Power BI Desktop before numerical findings are published.

## Data Lineage

This is a Power BI template with a local CSV query. Dataset rows are not embedded in the PBIT; a schema template, data dictionary and source-review checklist are supplied for reproducibility. The official dataset owner, licence and collection method must be added before the data itself is redistributed.

## Skills Demonstrated

Power BI • Power Query • DAX • time intelligence • geographic analysis • data modelling • quality assurance • responsible data storytelling

## Repository Structure

```text
.
├── dashboard/          # Original Power BI template when reconstructed
├── data/               # Expected schema, not the underlying dataset
├── docs/               # Story, DAX, data dictionary, evidence and quality review
├── evidence/           # Machine-readable inventory and checksum
├── screenshots/        # Power BI exports after validation
├── LINKEDIN_POST.md
├── LICENSE
└── README.md
```

## How to Review

1. Read `docs/quality-review.md` before interpreting the report.
2. Download `dashboard/Indian_Crime_Analysis_Dashboard.pbit` when present.
3. Open it with Power BI Desktop and reconnect an authorised CSV source.
4. Correct and validate the robbery measure.
5. Confirm treatment of `ZZ TOTAL` rows and relationship direction.
6. Verify the artefact against `evidence/SHA256SUMS.txt`.

## Interpretation Boundary

The dashboard supports descriptive exploration; it does not establish causes, public-safety effectiveness or individual risk. Reported-case counts depend on source definitions, reporting practices, coverage and data quality. Numerical conclusions are intentionally not fabricated where the source dataset is absent or an identified measure requires correction.

## Author

**Sagar Gurav**  
AI/ML and Data Analytics Student
