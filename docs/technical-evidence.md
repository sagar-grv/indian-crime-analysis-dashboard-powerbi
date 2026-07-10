# Technical Evidence and Verification

## Verification Method

The Power BI template was treated as a read-only package. Its internal `Report/Layout` metadata and `DataModelSchema` were inspected to verify page names, visual containers, visual types, model tables, fields, measures and date configuration. The template was not modified during this verification.

## File Integrity

- Intended repository path: `dashboard/Indian_Crime_Analysis_Dashboard.pbit`
- Size: `23,928` bytes
- SHA-256: `8d6fde4dfb120ca98f93dc4d4db8f661742f0bb06bb57f82decd5d781de12984`

## Report Inventory

| Page | Visual count | Visual types |
|---|---:|---|
| National Overview | 12 | `card` × 6, `lineChart` × 1, `decompositionTree` × 1, `clusteredBarChart` × 1, `map` × 1, `textbox` × 1, `actionButton` × 1 |
| State Deep-Dive | 6 | `funnel` × 1, `clusteredColumnChart` × 1, `multiRowCard` × 1, `table` × 1, `slicer` × 1, `textbox` × 1 |
| DISTRICT WISE DIVE | 6 | `card` × 2, `table` × 1, `line/stacked-column combo` × 1, `textbox` × 1, `slicer` × 1 |

**Total:** 3 pages and 24 visual containers.

## Referenced Fields

- `State`
- `District`
- `Year`
- `Murder`
- `Rape`
- `Robbery`
- `Theft`
- `Kidnapping`
- `Total_IPC_Crimes`

## Model Evidence

- Primary model table: `crime_data`
- Explicit DAX measures: **18**
- Calculated date table: `Date`
- Configured analysis period: **2001–2014**
- Source type: local CSV query inside a Power BI template
- Dataset rows: not embedded in the PBIT

## Verified Quality Finding

`Total Robbery` currently sums `crime_data[Theft]`. This is documented in `docs/quality-review.md` and should be corrected and validated before robbery values are presented.

## Interpretation Boundary

This document proves what is present in the Power BI artefact. It does not prove that the underlying source is complete, current or appropriate for policy decisions. Public presentation should identify the dataset owner, collection method, reporting definitions, licence, observation period and active filter context.
