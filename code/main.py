"""
AtithiAI - Hotel Management Assistant
"""

def atithi_ai_response(query):
    query = query.lower()

    if "check-in" in query:
        return "Check-in starts at 2:00 PM."
    elif "check-out" in query:
        return "Check-out is by 11:00 AM."
    elif "pet" in query:
        return "Pets are allowed as per hotel policy."
    elif "shuttle" in query:
        return "Our hotel provides shuttle service on request."
    else:
        return "Please contact the hotel staff for further assistance."

if __name__ == "__main__":
    print("Welcome to AtithiAI")
    while True:
        user = input("Guest: ")
        if user.lower() in ["exit", "quit"]:
            break
        print("AtithiAI:", atithi_ai_response(user))

