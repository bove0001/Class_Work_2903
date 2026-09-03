spam_prediction = 0.55
if spam_prediction > 0.85:
    classification = "BLOCKED SPAM"
elif spam_prediction > 0.5:
    classification = "HUMAN REVIEW REQUIRED"
else: classification = "APPROVED"



print(f"Spam prediction: {classification} ({spam_prediction})")



