# Quality Review Before Public Use

## 1. Correct the Robbery Measure

The supplied model contains:

```DAX
Total Robbery =
SUM ( crime_data[Theft] )
```

The likely intended formula is:

```DAX
Total Robbery =
SUM ( crime_data[Robbery] )
```

After correction, validate `% Robbery`, every robbery KPI card and every visual that references the measure.

## 2. Replace the Local Data-Source Path

The Power Query source refers to a hard-coded local Windows path. In Power BI Desktop:

1. Open **Transform data**.
2. Select the `crime_data` query.
3. Edit the **Source** step.
4. Select an authorised `crime_data.csv`.
5. Apply changes and refresh.

Do not publish screenshots that expose private local paths.

## 3. Confirm Aggregate Rows

Several measures exclude `District = "ZZ TOTAL"`. Confirm that these records are genuine state totals, are excluded from district calculations and are not double-counted in national visuals.

## 4. Review the State Funnel

The state funnel currently uses a count of non-null `Year` records. Confirm whether the intended value should instead be Total IPC Crimes, district count or another state-level KPI.

## 5. Review Relationship Direction

The `crime_data[Year]` to `Date[Year]` relationship uses bidirectional filtering. Prefer a single direction from the Date table unless bidirectional behaviour is specifically required and tested.

## 6. Standardise Labels

Consider renaming `DISTRICT WISE DIVE` to `District-Wise Analysis` for a more professional portfolio presentation.

## 7. Validate Source and Context

Before publishing numerical findings:

- identify the official dataset owner and licence,
- confirm whether values represent reported cases,
- document the collection and reporting period,
- record the refresh date and active filters,
- avoid causal claims based only on dashboard correlations, and
- confirm that no restricted or confidential information is present.
