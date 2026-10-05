# Platform Model Card | بطاقة نماذج المنصة

## Purpose

A production-style portfolio project for unsupervised screening, review prioritisation, case management, and auditability across four UKCS field series.

## Per-field model stack

Each field has an independent RobustScaler, 500-tree Isolation Forest, PCA model retaining at least 95% variance, and statistical-consensus layer. Seventeen features combine log levels, log changes, and five cross-measure ratios.

## Severity policy

- **Critical:** all three methods flag the month.
- **High:** two methods agree.
- **Review:** one method flags.
- **Normal:** no method flags.

The risk score is an average percentile ranking. It is not an incident probability.

## Current output

- 240 field-months scored
- 4 critical cases
- 22 high cases
- 43 review cases
- 171 normal field-months
- 6 cross-field high/critical clusters

## Governance features

Deterministic run identity, source SHA-256, model artifacts per field, immutable generated case IDs, explicit statuses, reviewer assignment, notes, and an append-only audit table for workflow actions.

## Limitations and prohibited uses

- No verified labels; precision, recall, and incident-detection accuracy cannot be claimed.
- Cross-field clusters can reflect shared maintenance, reporting, weather, or legitimate operating conditions.
- Driver fields represent large scaled deviations, not causal explanations.
- This is not a control-room alarm system.
- Do not use for shutdown, safety, compliance, reserves, investment, or autonomous operational decisions.

## العربية

تطبق المنصة نماذج مستقلة لكل حقل وتحوّل الإشارات إلى حالات قابلة للإدارة والتدقيق. Critical يعني اتفاق الطرق الثلاث، لكنه لا يعني حادثاً مؤكداً أو احتمال فشل بنسبة محددة. المنصة لترتيب المراجعة البشرية وليست نظام إنذار أو قرار تشغيلي.

