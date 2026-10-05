# UKCS Multi-Field Anomaly Monitoring and Case Management Platform

**Project 3 — Level 3 (Advanced)**

A production-style energy-data portfolio platform that scores 240 field-months across four BP-operated UKCS fields, compares three anomaly-detection approaches, creates review cases, identifies cross-field clusters, preserves an audit trail, and serves the workflow through FastAPI and Streamlit.
## Author

**Dr Khaldoun Shaker**  
Petroleum & Reservoir Engineer | Energy Data Analytics  
Edinburgh, United Kingdom  

Built as an independent professional portfolio project to apply my petroleum
and reservoir engineering experience to energy-data problems using Python,
SQL and machine learning. I reviewed the engineering assumptions, analytical
workflow, results and limitations.

© 2026 Khaldoun Shaker. All rights reserved.
## Headline result

- 4 fields × 60 months = 240 scored field-months
- 4 critical cases: all three methods agree
- 22 high cases: two methods agree
- 43 review cases: one method flags
- 171 normal field-months
- 6 cross-field high/critical clusters

![Portfolio risk heatmap](outputs/charts/01_portfolio_risk_heatmap.png)

## Platform capabilities

- Strict multi-field data-quality gate
- Independent scaler, Isolation Forest, and PCA artifacts per field
- Statistical-consensus safeguard and percentile risk score
- Critical/high/review/normal policy
- Deterministic case IDs and run identity
- SQLite case registry with assignment, notes, status, and audit log
- Cross-field cluster detection
- FastAPI read/write case-management interface
- Streamlit monitoring dashboard
- Docker, Compose, Makefile, CI, tests, and bilingual documentation

## Fields

Schiehallion, Clair Ridge, Loyal, and Alligin.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_pipeline.py
python -m unittest discover -s tests -v
python run_api.py
```

Open API docs at `http://localhost:8000/docs`.

In another terminal:

```bash
streamlit run dashboard.py
```

Open the dashboard at `http://localhost:8501`.

Docker alternative:

```bash
docker compose up --build
```

## Structure

```text
.
├── config/settings.yaml
├── data/raw and data/processed
├── docs/ARCHITECTURE.md, API.md, CASE_WORKFLOW.md
├── models/                       # 12 artifacts, metadata, SQLite registry
├── outputs/charts and outputs/tables
├── src/                          # data, features, detection, registry, API
├── tests/
├── dashboard.py
├── Dockerfile and docker-compose.yml
├── run_pipeline.py and run_api.py
└── requirements.txt
```

## Responsible use

This is not a control-room alarm or autonomous decision system. It has no verified incident labels and cannot claim diagnostic accuracy. Cases and cross-field clusters prioritise human investigation only.

---

## الملخص العربي

هذا هو **المشروع الثالث – المستوى الثالث المتقدم**. توسع من حقل واحد إلى أربعة حقول، ويحوّل نتائج Isolation Forest وPCA والقواعد الإحصائية إلى حالات مراجعة فعلية لها رقم وحالة ومسؤول وملاحظة وسجل تدقيق.

تتضمن المنصة Dashboard وAPI وقاعدة SQLite ونماذج محفوظة وDocker وCI واختبارات. اكتشفت 69 حالة للمراجعة وستة أشهر مشتركة بين أكثر من حقل، لكنها لا تعتبرها أعطالاً مؤكدة؛ بل ترتبها للمراجعة الهندسية البشرية.

