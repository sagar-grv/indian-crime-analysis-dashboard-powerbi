# Complete the Power BI Template Upload

The final source file should appear here with the exact name:

```text
Indian_Crime_Analysis_Dashboard.pbit
```

## Verified Integrity Values

- Expected size: `23928` bytes
- Expected SHA-256: `8d6fde4dfb120ca98f93dc4d4db8f661742f0bb06bb57f82decd5d781de12984`

## Method 1 — Run the Existing GitHub Workflow

1. Open the repository’s **Actions** tab.
2. Select **Reconstruct Power BI dashboard**.
3. Enable workflows if GitHub displays an enablement notice.
4. Select **Run workflow** on the `main` branch.
5. Confirm that a bot commit named `Add checksum-verified Power BI dashboard artifact` appears.
6. Confirm that this folder then contains `Indian_Crime_Analysis_Dashboard.pbit`.

The reconstruction script validates chunk count, encoded length, compressed size, final file size and SHA-256. It stops with an error rather than committing a mismatched file.

## Method 2 — Upload the Original PBIT Manually

1. Download and extract the prepared crime-dashboard package from the ChatGPT conversation.
2. Open this repository on GitHub.
3. Select **Add file → Upload files**.
4. Upload only `Indian_Crime_Analysis_Dashboard.pbit` into this folder.
5. Commit the file to `main`.
6. Verify the local file before upload:

```powershell
Get-FileHash .\Indian_Crime_Analysis_Dashboard.pbit -Algorithm SHA256
```

The reported hash must match the expected value above.

## Required Quality Correction

After opening the validated PBIT, correct the current robbery measure before using or publishing robbery-related values:

```DAX
Total Robbery =
SUM ( crime_data[Robbery] )
```

Then refresh and validate dependent visuals and `% Robbery`.
