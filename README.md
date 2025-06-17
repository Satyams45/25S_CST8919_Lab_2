#  CST8919 Lab 2: Web App with Threat Detection using Azure Monitor and KQL

## Overview
This project is a simple Python Flask-based web app deployed to Azure App Service. The app logs login attempts, and Azure Monitor is used to detect brute-force attacks through diagnostic logs. A custom KQL query and an Azure Monitor alert rule notify security teams via email when suspicious login behavior occurs.

---

## Deployment & Features

### Features Implemented
- Python Flask app with `/login` route that logs both **successful** and **failed** login attempts.
- Deployed on **Azure App Service (Linux)**.
- Connected to a **Log Analytics Workspace**.
- Diagnostic logs (`AppServiceConsoleLogs`, `AppServiceHTTPLogs`) enabled.
- Custom **KQL query** used to find failed logins.
- **Alert rule** configured to trigger email notifications on brute-force behavior (≥5 failed logins in 5 minutes).

---

## Application Details

### `/login` Route
- Accepts `POST` requests with `username` and `password` in JSON format.
- Logs "SUCCESSFUL LOGIN" or "FAILED LOGIN" using `logging` module.

### Sample Request (`test-app.http`)
```http
### Successful Login
POST https://Lab-2-app.azurewebsites.net/login
Content-Type: application/json

{
  "username": "admin",
  "password": "password123"
}

### Failed Login
POST https://Lab-2-app.azurewebsites.net/login
Content-Type: application/json

{
  "username": "admin",
  "password": "wrongpassword"
}
```

### Log Query with KQL
 KQL Query Used
```
AppServiceConsoleLogs
| where TimeGenerated > ago(30m)
| where Message has "FAILED LOGIN"
| summarize Count = count() by bin(TimeGenerated, 5m)

```
## Alert Rule Configuration
| Setting                     | Value                         |
| --------------------------- | ----------------------------- |
| **Scope**                   | Log Analytics Workspace       |
| **Condition**               | Custom log search (KQL above) |
| **Threshold**               | Greater than `5` results      |
| **Evaluation frequency**    | Every `1 minute`              |
| **Aggregation granularity** | `5 minutes`                   |
| **Action Group**            | Sends email notification      |
| **Severity**                | `2` (High) or `3` (Medium)    |

## Demo Video
🎬 Watch Demo Here: YouTube Demo

### How to Test the App
  1. Clone the repository:
```
git clone https://github.com/satyams45/25S-cst8919-lab2.git
cd cst8919-lab2-threat-detection
```
  2. Run app locally:

```
pip install -r requirements.txt
python app.py
```
  3. Use test-app.http with REST Client extension in VS Code to simulate login attempts.

## What I Learned
  - Kusto Query Language (KQL) is a powerful tool for querying and analyzing logs.

  - Learned how to connect diagnostic logs from Azure App Service to Log Analytics Workspace.

  - Discovered how to set up alert rules in Azure Monitor for real-time security monitoring.

  - Improved skills in detecting suspicious activity via logs.

## Challenges Faced
  - Diagnosing why some logs didn't appear in Log Analytics right away (due to log propagation delay).

  - Making sure the app logs both console and structured messages that Azure Monitor could ingest.

  - Creating a correct alert rule condition with the right query threshold.

## Future Improvements
  - Add IP logging and rate-limiting in the app to better detect brute-force and location-based attacks.

  - Integrate with Microsoft Sentinel or other SIEM for better incident response workflows.

  - Use Application Insights for enhanced telemetry and request tracing.

  - Implement real user authentication with hashed credentials instead of hardcoded logic.


