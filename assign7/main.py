from typing import List, Dict, Set
from functools import reduce


def total_time_per_user(logs: List[Dict[str, str | float]]) -> Dict[str, float]:
    return reduce(
        lambda acc, log: (
            acc.__setitem__(
                str(log["user"]),
                acc.get(str(log["user"]), 0.0) + float(log["duration"])
            ) or acc
        ),
        logs,
        {}
    )


def most_active_users(logs: List[Dict[str, str | float]], k: int) -> List[str]:
    totals = total_time_per_user(logs)
    return [
        user
        for user, _ in sorted(
            totals.items(),
            key=lambda item: item[1],
            reverse=True
        )[:k]
    ]


def unique_actions(logs: List[Dict[str, str | float]]) -> Set[str]:
    return {str(log["action"]) for log in logs}


def print_complexity(operation: str, time_complexity: str, space_complexity: str) -> None:
    print(f"\nComplexity of {operation}:")
    print(f"Time Complexity: {time_complexity}")
    print(f"Space Complexity: {space_complexity}")


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    logs: List[Dict[str, str | float]] = []

    print("=== Activity Log Analyzer ===")

    while True:
        print("\nEnter activity log details:")

        user = input("Enter user roll number (e.g. CSB24067): ").strip()
        action = input("Enter action (e.g. YouTube, Chrome, WhatsApp): ").strip()
        duration = read_float("Enter duration: ")

        logs.append({
            "user": user,
            "action": action,
            "duration": duration
        })

        choice = input("Do you want to add another log? (yes/no): ").strip().lower()
        if choice != "yes":
            break

    print("\nAll Logs:")
    for log in logs:
        print(log)
    print_complexity("displaying all logs", "O(n)", "O(1) auxiliary")

    totals = total_time_per_user(logs)
    print("\nTotal time per user:")
    print(totals)
    print_complexity("total_time_per_user", "O(n)", "O(u)")

    k = read_int("\nEnter value of k for most active users: ")
    top_users = most_active_users(logs, k)
    print("\nMost active users:")
    print(top_users)
    print_complexity("most_active_users", "O(n + u log u)", "O(u)")

    actions = unique_actions(logs)
    print("\nUnique actions:")
    print(actions)
    print_complexity("unique_actions", "O(n)", "O(a)")
