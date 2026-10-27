import unittest
from app import generate_test_cases, to_markdown

class TestGeneratorTests(unittest.TestCase):
    def test_builds_cases_for_each_criterion(self):
        result = generate_test_cases("As a user, I can sign in.", ["Email is required", "Valid credentials open dashboard"])
        self.assertGreaterEqual(result["test_case_count"], 3)
        self.assertTrue(any(case["type"] == "negative" for case in result["test_cases"]))
    def test_rejects_missing_story(self):
        with self.assertRaises(ValueError): generate_test_cases("", ["criterion"])
    def test_markdown_export(self):
        result = generate_test_cases("As a buyer, I can search.", ["Results show matching products"])
        self.assertIn("QA Test Plan", to_markdown(result))
        self.assertIn("AC-01", to_markdown(result))

if __name__ == "__main__": unittest.main()
