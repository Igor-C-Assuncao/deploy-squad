import subprocess

def run_linter(file_path: str) -> str:
    """
    Executes Ruff static analysis on the specified file to detect code style violations and potential bugs.
    """
    try:
        result = subprocess.run(
            ["ruff", "check", file_path], 
            capture_output=True, 
            text=True, 
            check=False
        )
        return result.stdout if result.stdout else "No linting issues found."
    except Exception as e:
        return f"Failed to execute linter execution: {str(e)}"

def get_git_diff(repo_path: str) -> str:
    """
    Retrieves the current uncommitted git modifications to evaluate new code changes.
    """
    try:
        result = subprocess.run(
            ["git", "diff", "HEAD"], 
            cwd=repo_path, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout if result.stdout else "No changes detected in Git repository."
    except Exception as e:
        return f"Failed to read git diff: {str(e)}"