from datetime import datetime

# ANSI color codes
COLORS = {
    "reset": "\033[0m",       # Reset color
    "info": "\033[94m",       # Blue
    "success": "\033[92m",    # Green
    "warning": "\033[93m",    # Yellow
    "danger": "\033[91m",     # Red
    "bold": "\033[1m",        # Bold text
    "time": "\033[90m"        # Gray (for timestamp)
}

def log(message: str, level: str = "info") -> None:
    """
    Prints a colored and styled log message based on the specified level.

    Args:
        message (str): The log message to print.
        level (str): The log level ('info', 'success', 'warning', 'danger').
    """
    level = level.lower()
    color = COLORS.get(level, COLORS["reset"])
    time_color = COLORS["time"]
    reset_color = COLORS["reset"]
    current_time = datetime.now().strftime('%H:%M:%S')
    
    print(
        f"{time_color}[{current_time}]{reset_color} "
        f"{color}{COLORS['bold']}{level.upper()}{reset_color}: {message}"
    )


