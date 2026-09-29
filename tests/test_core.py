import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_case(self):
        state = core.new_game()
        self.assertTrue(core.file_case(state, 1))
        self.assertFalse(core.file_case(state, 1))

    def test_02_room_capacity(self):
        state = core.new_game()
        core.schedule(state, 1)
        core.schedule(state, 2)
        result = core.schedule(state, 3)
        self.assertFalse(result)

    def test_03_fee_exact(self):
        state = core.new_game()
        self.assertEqual(core.fee(state, 1, 3), 2)

    def test_04_cancel_refunds_fee(self):
        state = core.new_game()
        state["fee_paid"] = 80
        core.cancel(state, 1)
        self.assertEqual(state["fee_paid"], 100)

    def test_05_no_assign_absent_judge(self):
        state = core.new_game()
        core.file_case(state, 1)
        result = core.assign(state, 1, "J2")
        self.assertFalse(result)

    def test_06_judge_fail_no_fee(self):
        state = core.new_game()
        core.file_case(state, 1)
        state["cases"][1]["failed"] = True
        before = state["fee_paid"]
        result = core.judge(state, 1)
        self.assertFalse(result)
        self.assertEqual(state["fee_paid"], before)

    def test_07_absence_once(self):
        state = core.new_game()
        core.file_case(state, 1)
        state["cases"][1]["score"] = 10
        core.absence(state, 1)
        self.assertEqual(state["cases"][1]["score"], 9)

    def test_08_load_preserves_case(self):
        state = core.new_game()
        state["case_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["case_id"], 4)


if __name__ == "__main__":
    unittest.main()
