import unittest
# Import your clean functions from your quiz engine core file
from search_engine.quiz_question import get_quiz_questions, evaluate_answer

class TestQuizEngine(unittest.TestCase):

    def test_quiz_questions_structure(self):
        """Validates that the question collection matches the expected dictionary format."""
        questions = get_quiz_questions()
        
        # Test total number of questions populated
        self.assertEqual(len(questions), 2)
        
        # Test schema constraints for Question 1
        q1 = questions[0]
        self.assertEqual(q1["id"], 1)
        self.assertEqual(q1["correct_key"], "b")
        self.assertIn("a", q1["options"])

    def test_evaluate_correct_answer_exact_match(self):
        """Verifies that an exact lowercase match returns True."""
        self.assertTrue(evaluate_answer(correct_key="b", user_choice="b"))

    def test_evaluate_correct_answer_case_insensitivity(self):
        """Ensures that user string variations in casing (e.g., 'B') result in accurate matches."""
        self.assertTrue(evaluate_answer(correct_key="b", user_choice="B"))
        self.assertTrue(evaluate_answer(correct_key="a", user_choice="A"))

    def test_evaluate_correct_answer_with_whitespace(self):
        """Defends against user typos containing spaces by ensuring .strip() cleans the string."""
        self.assertTrue(evaluate_answer(correct_key="b", user_choice=" b  "))
        self.assertTrue(evaluate_answer(correct_key="a", user_choice="  A\n"))

    def test_evaluate_incorrect_answer(self):
        """Verifies that alternative valid option letters cleanly evaluate to False."""
        self.assertFalse(evaluate_answer(correct_key="b", user_choice="a"))
        self.assertFalse(evaluate_answer(correct_key="a", user_choice="c"))

    def test_invalid_cli_choice_handling(self):
        """Tests milestone B6 constraint: weird, erratic inputs return False gracefully without crashes."""
        self.assertFalse(evaluate_answer(correct_key="b", user_choice="xyz"))
        self.assertFalse(evaluate_answer(correct_key="b", user_choice="123"))
        self.assertFalse(evaluate_answer(correct_key="b", user_choice=""))

if __name__ == "__main__":
    unittest.main()
