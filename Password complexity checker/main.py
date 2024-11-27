import re

# Function to check password strength
def check_password_strength(password):
    # Initialize variables for password strength criteria
    length_criteria = len(password) >= 8
    upper_criteria = bool(re.search(r'[A-Z]', password))
    lower_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    # Initialize the strength score
    strength_score = 0
    
    # Check each criteria and increase the strength score
    if length_criteria:
        strength_score += 1
    if upper_criteria:
        strength_score += 1
    if lower_criteria:
        strength_score += 1
    if digit_criteria:
        strength_score += 1
    if special_char_criteria:
        strength_score += 1

    # Provide feedback based on the strength score
    if strength_score == 5:
        return "Strong password!"
    elif 3 <= strength_score < 5:
        return "Moderate password."
    else:
        return "Weak password. Try including more uppercase letters, numbers, or special characters."

# Main program
if _name_ == "_main_":
    # Get the user's input
    user_password = input("Enter the password to check: ")
    
    # Assess the password strength
    feedback = check_password_strength(user_password)
    
    # Print the result
    print(feedback)