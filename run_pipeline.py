from pathlib import Path
from src.pipeline import run

if __name__ == "__main__":
    result=run(Path(__file__).resolve().parent)
    print(f"Run ID: {result['run_id']}")
    print(f"Scored months: {result['total_scored_months']}")
    print(f"Cases: {result['total_cases']} (critical={result['critical_cases']}, high={result['high_cases']}, review={result['review_cases']})")
    print(f"Cross-field clusters: {result['cross_field_clusters']}")

