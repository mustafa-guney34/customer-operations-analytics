
# Customer Operations Analytics


## Executive Summary

This analysis shows that customer satisfaction (NPS) is primarily driven by work type rather than operational delays. Repair appointments score significantly lower than installations, explaining temporary weekly dips in NPS.

While lateness does not directly reduce NPS when controlling for work type, it substantially increases the probability that customers are not at home. This highlights that operational improvements should focus on preventing window crossings and managing work type mix, rather than only reducing delay size.



## Project Overview

This project analyzes operational performance and customer satisfaction
using service appointment data.

The goal is to understand:

1. What drives customer satisfaction (NPS)?
2. How often are experts late?
3. What are the operational side effects of lateness?

The analysis combines operational data, expert characteristics,
and customer feedback to generate actionable business insights.

---

## Business Context

In customer operations environments, operational execution
directly impacts customer experience.

This project explores:

- Weekly NPS trends
- Differences between work types (installation vs repair)
- The impact of lateness on customer satisfaction
- The operational consequences of late arrivals

The analysis is structured to separate:

- Data loading
- Feature engineering
- Analytical modules
- Regression validation

---

## Data Description

The dataset consists of three sources:

- **Service Appointments**  
  Appointment timing, work type, service territory, and customer presence.

- **Experts**  
  Years in service and skill level of technicians.

- **NPS Responses**  
  Customer satisfaction scores submitted after appointments.

Total volume:
- 18,425 service appointments
- 3,145 NPS responses (~17% response rate)
- 207 experts

---

## Methodology

The analysis follows a structured, business-first approach:

### 1. Data Architecture
All data sources are merged into a single analytical dataset
using a modular data loader.

### 2. Feature Engineering
Key operational metrics are derived:
- Lateness flag
- Delay in minutes
- Execution week
- Customer not at home indicator

### 3. Descriptive Analysis
Segment-level comparisons were performed to identify differences in:
- NPS by work type
- Weekly NPS trends
- Lateness rates
- Operational impact

### 4. Model Validation
Regression models were used to validate whether:
- Work type remains a significant driver of NPS
- Lateness significantly increases no-show probability

---

## Key Insights

### 1. NPS is primarily driven by work type

- Repair appointments score ~3 points lower on average than installations.
- The temporary dip in weekly NPS is explained by a higher share of repair work.
- Regression analysis confirms that work type remains highly significant
  even when controlling for experience and skill level.

### 2. Lateness is a structural operational issue

- Approximately 17–18% of all appointments are late.
- Lateness rates are relatively consistent across work types.

### 3. Lateness does not significantly reduce NPS directly

- Once controlling for work type, lateness has no statistically significant
  direct impact on NPS.
- This suggests customer satisfaction is more sensitive to work type than timing deviations.

### 4. Lateness strongly increases customer no-show risk

- When appointments are on time, ~15% of customers are not at home.
- When appointments are late, this increases to ~41%.
- Logistic regression confirms this relationship is highly significant.

---

## Strategic Implications

- Interpret NPS always in the context of work type mix.
- Focus operational improvements on preventing window crossings.
- Prioritize coaching and planning support for less experienced experts.
- Consider real-time tracking or automated communication to reduce no-show risk.

---

## Project Structure

customer-operations-analytics/

- data/
  - serviceappointments.csv
  - experts.csv
  - nps.csv

- src/
  - data_loader.py
  - feature_engineering.py
  - analysis_nps.py
  - analysis_lateness.py
  - regression_models.py

- main.py
- README.md

The architecture separates:

- Data loading
- Feature engineering
- Analytical logic
- Model validation
- Business-facing output

---

## How to Run

From the project root:

python3 main.py

The script will:

- Load and merge datasets
- Prepare analytical features
- Generate key insights
- Validate findings via regression models

---

## Tech Stack

- Python  
- Pandas  
- Statsmodels  
- Modular project structure  

