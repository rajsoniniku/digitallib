"""
Validation and Error Handling utilities.
Satisfies Non-Functional Requirements: Reliability and Usability.
"""

def validate_menu_choice(choice_str: str, max_option: int) -> int:
    """Validates if user input is an integer within valid menu bounds."""
    if not choice_str.strip().isdigit():
        return -1
    val = int(choice_str)
    if 1 <= val <= max_option:
        return val
    return -1

def sanitize_string(input_str: str) -> str:
    """Sanitizes user text inputs."""
    return input_str.strip().title()
