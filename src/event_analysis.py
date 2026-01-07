import json
from pathlib import Path
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "events_mock.json"
def load_events(path):
    """
    Load mock crypto event data from JSON file.
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
def analyze_event(event):
    """
    Analyze a single crypto security event.
    """
    impact = event.get("impact_24h", 0)
    risk = event.get("risk", "unknown")

    if impact <= -15:
        impact_level = "Severe market reaction"
    elif impact <= -5:
        impact_level = "Moderate market reaction"
    else:
        impact_level = "Low market reaction"

    return {
        "event": event.get("event"),
        "date": event.get("date"),
        "impact_24h": impact,
        "risk": risk,
        "impact_level": impact_level
    }
def display_results(analysis_results):
    """
    Display analyzed events in a readable format.
    """
    print("\nCrypto Security Event Impact Analysis\n")
    print("-" * 45)

    for result in analysis_results:
        print(f"Event: {result['event']}")
        print(f"Date: {result['date']}")
        print(f"24h Impact: {result['impact_24h']}%")
        print(f"Risk Level: {result['risk']}")
        print(f"Impact Assessment: {result['impact_level']}")
        print("-" * 45)
def main():
    events = load_events(DATA_PATH)
    analysis_results = []

    for event in events:
        analyzed_event = analyze_event(event)
        analysis_results.append(analyzed_event)

    display_results(analysis_results)
if __name__ == "__main__":
    main()
