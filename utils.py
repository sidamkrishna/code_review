import subprocess

def run_flake8(filepath):
    try:
        result = subprocess.run(["flake8", filepath], capture_output=True, text=True)
        return result.stdout if result.stdout else "No style issues found 🎉"
    except Exception as e:
        return f"Error running flake8: {e}"

def run_black(filepath):
    try:
        # Get diff without modifying
        result = subprocess.run(["black", "--diff", filepath], capture_output=True, text=True)
        diff = result.stdout if result.stdout else "No formatting changes needed 🎉"

        # Now apply formatting
        subprocess.run(["black", filepath], capture_output=True, text=True)
        with open(filepath, 'r') as f:
            formatted_code = f.read()
        return formatted_code, diff
    except Exception as e:
        return f"Error running black: {e}", ""

def run_radon(filepath):
    try:
        result = subprocess.run(["radon", "cc", filepath, "-s", "-a"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error running radon: {e}"
