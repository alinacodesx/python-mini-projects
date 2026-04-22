import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters chahiye")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Ek uppercase letter add karo")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Ek lowercase letter add karo")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Ek number add karo")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Ek special character add karo (!@#$ etc.)")

    levels = {5: "🟢 Strong", 4: "🟡 Medium", 3: "🟠 Weak", }
    strength = levels.get(score, "🔴 Very Weak")

    print(f"\nPassword: {'*' * len(password)}")
    print(f"Strength: {strength} ({score}/5)")
    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print(" ", f)

password = input("Enter password: ")
check_password_strength(password)
