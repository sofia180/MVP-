# Crypto Event Impact MVP

## Overview
This project is a lightweight, event-driven MVP designed to analyze how security-related events influence crypto projects and market behavior.  
The goal of this MVP is not to provide real-time analytics, but to demonstrate **product thinking, event classification, and impact assessment logic** in the context of crypto and fintech.

---

## Problem Statement
Security incidents such as hacks and smart contract exploits often trigger sharp market reactions and increase project risk.  
However, these events are frequently analyzed in an unstructured or reactive manner, making it difficult for teams and analysts to quickly assess their potential impact.

---

## Solution
This MVP introduces a structured approach to analyzing security-related events by:
- classifying incidents,
- estimating short-term market impact,
- assigning qualitative risk levels.

The project focuses on **clarity, explainability, and decision-support**, rather than complex predictive models.

---

## Key Features
- Event-driven analysis focused on security incidents  
- Impact estimation based on 24h market reaction (mock data)  
- Risk level classification (low / medium / high)  
- Clean, minimal MVP architecture suitable for rapid validation  

---

## MVP Scope
**Included:**
- Security-related crypto events (e.g. hacks, exploits)
- Event metadata (date, type)
- Simplified impact metrics
- Qualitative risk evaluation logic

**Not Included (by design):**
- Live market data
- Real token prices or APIs
- Investment recommendations
- Production-grade analytics

This scope reflects a **true MVP**, built to validate assumptions and demonstrate product reasoning.

---

## Tech Stack
- Python
- JSON (mock event data)
- Minimal file-based architecture

---

## Project Structure
crypto-event-impact-mvp/
│
├── data/
│ └── events_mock.json
│
├── src/
│ └── event_analysis.py
│
└── README.md

---

## Metrics & Evaluation Logic
The MVP evaluates events using simplified criteria:
- Percentage price impact within 24 hours
- Predefined thresholds for impact severity
- Qualitative risk labeling for fast interpretation

This approach prioritizes **interpretability over complexity**, which is critical at the MVP stage.

---

## Use Case
- Early-stage crypto teams validating risk awareness tools
- Analysts exploring event-driven market behavior
- Product managers testing MVP concepts in fintech and Web3

---

## Disclaimer
This project uses **mock data** and simplified logic for demonstration and educational purposes only.  
It does **not** represent real investment advice, real market data, or production systems.

---

## Why This MVP Matters
- Demonstrates event-driven and analytical thinking
- Shows understanding of crypto-specific risks
- Emphasizes product scope definition and MVP discipline
- Designed to be extensible without exposing sensitive logic

---

## Future Improvements
- Additional event categories (regulatory, listings, governance)
- Scoring model (0–100 risk index)
- Visualization layer
- Data source abstraction

## Licence
This project use MIT license
