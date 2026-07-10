# DAX Measures

The model contains the following analytical measures.

```DAX
Total IPC Crimes =
SUM ( crime_data[Total_IPC_Crimes] )
```

```DAX
Total Murder =
SUM ( crime_data[Murder] )
```

```DAX
Total Rape =
SUM ( crime_data[Rape] )
```

```DAX
Total Robbery =
SUM ( crime_data[Theft] )
```

> **Verified issue:** the supplied `Total Robbery` measure sums the `Theft` column. Validate the likely correction `SUM(crime_data[Robbery])` in Power BI Desktop before using robbery results.

```DAX
Total Kidnap =
SUM ( crime_data[Kidnapping] )
```

```DAX
Total Theft =
SUM ( crime_data[Theft] )
```

```DAX
Total IPC (no state totals) =
CALCULATE (
    [Total IPC Crimes],
    crime_data[District] <> "ZZ TOTAL"
)
```

```DAX
% Murder =
DIVIDE ( [Total Murder], [Total IPC Crimes] )
```

```DAX
% Rape =
DIVIDE ( [Total Rape], [Total IPC Crimes] )
```

```DAX
% Robbery =
DIVIDE ( [Total Robbery], [Total IPC Crimes] )
```

```DAX
% Theft =
DIVIDE ( [Total Theft], [Total IPC Crimes] )
```

```DAX
% Kidnap =
DIVIDE ( [Total Kidnap], [Total IPC Crimes] )
```

```DAX
Total IPC (Prev Year) =
CALCULATE (
    [Total IPC Crimes],
    PREVIOUSYEAR ( 'Date'[Date] )
)
```

```DAX
YoY % Total IPC =
VAR Prev = [Total IPC (Prev Year)]
RETURN
    DIVIDE ( [Total IPC Crimes] - Prev, Prev )
```

```DAX
Total IPC (Rolling 3Y) =
VAR MaxYear = MAX ( 'Date'[Year] )
RETURN
    AVERAGEX (
        FILTER (
            ALL ( 'Date'[Year] ),
            'Date'[Year] >= MaxYear - 2
                && 'Date'[Year] <= MaxYear
        ),
        CALCULATE ( [Total IPC Crimes] )
    )
```

```DAX
District Share of State =
DIVIDE (
    [Total IPC Crimes],
    CALCULATE (
        [Total IPC Crimes],
        ALLEXCEPT ( crime_data, crime_data[State] ),
        crime_data[District] <> "ZZ TOTAL",
        KEEPFILTERS ( VALUES ( 'Date'[Year] ) )
    )
)
```

```DAX
State Avg (per district) =
VAR StateTotal =
    CALCULATE (
        [Total IPC Crimes],
        ALLEXCEPT ( crime_data, crime_data[State] ),
        crime_data[District] <> "ZZ TOTAL",
        KEEPFILTERS ( VALUES ( 'Date'[Year] ) )
    )
VAR DistrictCount =
    CALCULATE (
        DISTINCTCOUNT ( crime_data[District] ),
        ALLEXCEPT ( crime_data, crime_data[State] ),
        crime_data[District] <> "ZZ TOTAL",
        KEEPFILTERS ( VALUES ( 'Date'[Year] ) )
    )
RETURN
    DIVIDE ( StateTotal, DistrictCount )
```

```DAX
District – State Avg Gap =
[Total IPC Crimes] - [State Avg (per district)]
```
