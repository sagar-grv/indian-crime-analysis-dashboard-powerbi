# Data Dictionary

## `crime_data`

| Field | Type | Description |
|---|---|---|
| `State` | Text | Indian state or union territory |
| `District` | Text | District name; source may include aggregate rows such as `ZZ TOTAL` |
| `Year` | Whole number | Reporting year |
| `Murder` | Whole number | Reported murder cases |
| `Rape` | Whole number | Reported rape cases |
| `Robbery` | Whole number | Reported robbery cases |
| `Theft` | Whole number | Reported theft cases |
| `Kidnapping` | Whole number | Reported kidnapping/abduction cases; renamed from `Kidnapping_Abduction` in Power Query |
| `Total_IPC_Crimes` | Whole number | Total reported IPC crime cases |

## `Date`

| Field | Type | Description |
|---|---|---|
| `Date` | Date | Calculated daily date covering 1 January 2001 through 31 December 2014 |
| `Year` | Whole number | Calendar year used to relate the date table to `crime_data[Year]` |

## Power Query Transformations

- Promotes the first CSV row to headers.
- Assigns text and whole-number data types.
- Renames `Kidnapping_Abduction` to `Kidnapping`.
- Standardises selected state/union-territory names, including Andaman & Nicobar Islands and Dadra & Nagar Haveli.
