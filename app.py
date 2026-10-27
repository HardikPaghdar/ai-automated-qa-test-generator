"""Generate a structured QA checklist from user stories and acceptance criteria."""
import re

def generate_test_cases(story: str, acceptance_criteria: list[str]) -> dict:
    if not story.strip():
        raise ValueError("story must not be empty")
    if not acceptance_criteria or not any(item.strip() for item in acceptance_criteria):
        raise ValueError("at least one acceptance criterion is required")
    cases = []
    for index, criterion in enumerate((c.strip() for c in acceptance_criteria if c.strip()), 1):
        cases.append({"id": f"AC-{index:02d}", "title": f"Verify: {criterion[:90]}",
                      "type": "acceptance", "preconditions": [story.strip()],
                      "steps": [f"Set up the scenario described by: {criterion}",
                                "Perform the relevant user action",
                                "Observe the result and compare it with the criterion"],
                      "expected_result": criterion, "priority": "P1"})
        lowered = criterion.lower()
        if any(word in lowered for word in ("required", "must", "email", "password", "amount", "limit")):
            cases.append({"id": f"NEG-{index:02d}", "title": f"Negative validation for AC-{index:02d}",
                          "type": "negative", "preconditions": [story.strip()],
                          "steps": ["Submit a missing, malformed, or boundary value relevant to this criterion"],
                          "expected_result": "The input is rejected safely and a useful validation message is shown.",
                          "priority": "P1"})
    cases.append({"id":"REG-01", "title":"Check related flow for regression", "type":"regression",
                  "preconditions":[story.strip()], "steps":["Complete the main user journey","Check adjacent screens and persisted state"],
                  "expected_result":"The requested behavior works without breaking adjacent functionality.","priority":"P2"})
    return {"story": story.strip(), "test_case_count": len(cases), "test_cases": cases,
            "disclaimer":"Generated checklist is a starting point; QA should refine test data and expected results."}

def to_markdown(result: dict) -> str:
    lines = ["# QA Test Plan", "", f"**Story:** {result['story']}", "", f"**Cases:** {result['test_case_count']}", ""]
    for case in result["test_cases"]:
        lines += [f"## {case['id']} — {case['title']}", f"- Type: {case['type']} | Priority: {case['priority']}",
                  "- Steps: " + "; ".join(case["steps"]), "- Expected: " + case["expected_result"], ""]
    return "\n".join(lines)
