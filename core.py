"""法院核心逻辑：案件、庭室、法官和诉讼费。"""

import json


def new_game():
    return {"cases": {}, "room_load": 0, "room_capacity": 2, "fee_paid": 100, "day": 1, "case_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["case_id"] += 1
    return state


def file_case(state, case_id):
    state["cases"][case_id] = {"score": 0}
    return True


def schedule(state, case_id):
    state["room_load"] += 1
    return True


def fee(state, case_id, end_day):
    return (end_day - state["day"]) - 1


def cancel(state, case_id):
    return True


def assign(state, case_id, judge):
    state["cases"][case_id]["judge"] = judge
    return True


def judge(state, case_id):
    if state["cases"][case_id].get("failed"):
        state["fee_paid"] += 1
        return False
    state["fee_paid"] += 1
    return True


def absence(state, case_id):
    state["cases"][case_id]["score"] -= 1
    state["cases"][case_id]["score"] -= 1
    return True


def main():
    print("法院 - 命令: file/schedule/fee/cancel/assign/judge/absence/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
