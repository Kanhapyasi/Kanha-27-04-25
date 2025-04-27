[2_xmLdRBD.csv](https://github.com/user-attachments/files/19928635/2_xmLdRBD.csv)# Kanha-27-04-25

## Some ideas of improving the solution

### 1. Better Handling of Missing Data
Right now, the repo doesn't properly handle missing business hours or missing timezone entries — it mostly assumes things will be there.
It would be cleaner if default values like 24/7 open and America/Chicago timezone were handled more gracefully either at the time of data ingestion into the DB itself, or at query time with fallback logic. Ideally, this should not be patched later when fetching.

### 2. Poll Interpolation Needs More Thought
The current logic does a rough assumption: if the last status is "active," it remains "active" until the next status flip.
A better approach would be to divide the gap between two polls proportionally.
If there’s a 2-hour gap between polls, don’t blindly assign everything to the last seen status — maybe split based on timestamps, or if missing too much, mark the gap as unknown and exclude it from strict uptime/downtime calculations.

### 3. Heavy Dependency on Pandas, No Optimization
In the repo, it loads the full dataset into memory using Pandas every time a report is triggered.
This is fine for the size of the current dataset (few thousand rows), but once you get millions of rows (hourly polls × hundreds of stores × days), it will crash.
Instead, SQL queries should be tightened — load only what you need for that report (for the last hour, last day, last week) using timestamp filters directly in SQL, not in Python.

### 4. No Background Processing for Reports
The current /trigger_report API waits until the whole report is generated.
It’s not scalable. If the report takes 5 minutes to generate, your API will timeout.
The right way is to use a background worker (like Celery with Redis or even just Python’s ThreadPoolExecutor) to do report generation, while the API just returns a report_id immediately.


### 5. Assumption that Data is Static
The current code assumes the input CSVs won't change during runtime.
The system requirement says data will update every hour, so realistically, you should plan for re-ingesting or updating DB tables incrementally rather than wiping everything and reloading CSVs every time.


##OUTPUT
https://github.com/Kanhapyasi/Kanha-27-04-25/blob/main/media/reports/2_xmLdRBD.csv

[store_id,last_one_hour uptime,last_one_hour downtime,last_one_hour unit,last_one_day uptime,last_one_day downtime,last_one_day unit,last_one_week uptime,last_one_week downtime,last_one_week unit
d7564e8c-0edb-4e6f-aa64-c72b701e3c57,0,60,minutes,0,0,hours,0,126,hours
Uploading 2_xmLdRBD.csv…]()
