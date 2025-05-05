# Employee Performance Evaluation Expert System

def evaluate_performance(punctuality, task_completion, teamwork):
    # Rule 1: All high
    if punctuality == "high" and task_completion == "high" and teamwork == "high":
        return "Excellent"
    # Rule 2: All medium or high
    elif punctuality in ["medium", "high"] and task_completion in ["medium", "high"] and teamwork in ["medium", "high"]:
        return "Good"
    # Rule 3: Any low
    elif punctuality == "low" or task_completion == "low" or teamwork == "low":
        return "Needs Improvement"
    else:
        return "Invalid input"

# Input from user
print("Please enter performance levels (high / medium / low):")
punctuality = input("Punctuality: ").lower()
task_completion = input("Task Completion: ").lower()
teamwork = input("Teamwork: ").lower()

# Evaluation
result = evaluate_performance(punctuality, task_completion, teamwork)
print("\nPerformance Evaluation Result:", result)




def evaluate_score(punctuality, task_completion, teamwork):
    scores = {
        "high": 3,
        "medium": 2,
        "low": 1
    }

    total = (
        scores.get(punctuality, 0) * 0.3 +   # 30% weight
        scores.get(task_completion, 0) * 0.5 +  # 50% weight
        scores.get(teamwork, 0) * 0.2        # 20% weight
    )

    if total >= 2.5:
        return "Excellent"
    elif total >= 1.8:
        return "Good"
    else:
        return "Needs Improvement"

# Inputs
punctuality = input("Punctuality (high/medium/low): ").lower()
task_completion = input("Task Completion (high/medium/low): ").lower()
teamwork = input("Teamwork (high/medium/low): ").lower()

# Result
result = evaluate_score(punctuality, task_completion, teamwork)
print("Evaluation:", result)

