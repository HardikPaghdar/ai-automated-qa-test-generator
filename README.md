# AI Automated QA Test Generator

A requirements-to-checklist prototype that converts a user story and acceptance criteria into a structured set of acceptance, negative-validation, and regression test cases.

## Features
- Validates required input.
- Produces stable test case IDs and structured steps.
- Adds a negative validation case for criteria that mention common required/boundary fields.
- Exports the plan as Markdown.
- Ships with a sample password-reset story and regression tests.

## Quick start
Requires Python 3.10+.

```bash
python - <<'PY'
import json
from app import generate_test_cases, to_markdown
sample = json.load(open("examples/story.json", encoding="utf-8"))
result = generate_test_cases(sample["story"], sample["acceptance_criteria"])
print(to_markdown(result))
PY
```

## Tests
`python -m unittest discover -s tests -v`

## Scope and limitations
The generator uses deterministic templates; it does not call an LLM, execute the application, or guarantee complete test coverage. Review generated steps and expected results, especially for security, payments, and edge cases. A sensible extension is an optional LLM adapter with schema validation and human approval before exporting to Jira or a test management system.

## Explore more

- [AI Meeting Intelligence Assistant](https://github.com/HardikPaghdar/ai-meeting-intelligence-assistant) — extracts action candidates from text transcripts.
- [Multi-Agent Software Engineer](https://github.com/HardikPaghdar/multi-agent-software-engineer) — human-supervised task planning.
- [More projects on my portfolio](https://hardikpaghdar.netlify.app/).
