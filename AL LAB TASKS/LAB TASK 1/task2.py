
def check_scholarship(score, documents, attendance, interview):
    if score >= 70 and documents and attendance >= 75 and interview >= 60:
        return "PASS", "All conditions are satisfied"
    
    reasons = []

    if score < 70:
        reasons.append("Score is below 70")
    if not documents:
        reasons.append("Documents are incomplete")
    if attendance < 75:
        reasons.append("Attendance is below 75%")
    if interview < 60:
        reasons.append("Interview score is below 60")

    return "FAIL", ", ".join(reasons)


tests = [
    ("T1", 82, True, 90, 75, "PASS"),
    ("T2", 85, True, 74, 80, "FAIL"),
    ("T3", 78, True, 80, 59, "FAIL"),
    ("T4", 70, True, 75, 60, "PASS")
]

for name, score, documents, attendance, interview, expected in tests:
    result, reason = check_scholarship(score, documents, attendance, interview)

    print("\nTest:", name)
    print("Input:", score, documents, attendance, interview)
    print("Expected Result:", expected)
    print("Actual Result:", result)
    print("Reason:", reason)
