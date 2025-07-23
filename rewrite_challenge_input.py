import json
import os

def rewrite_challenge_input_json(new_json_bytes, target_path=None):
    """
    Overwrite the challenge1b_input.json file with the contents of a newly uploaded JSON file.
    Args:
        new_json_bytes (bytes): The bytes of the uploaded JSON file.
        target_path (str, optional): The path to the challenge1b_input.json file. If None, defaults to Collections/challenge1b_input.json.
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        # Parse the uploaded JSON
        new_data = json.loads(new_json_bytes.decode("utf-8"))
        # Determine the target path
        if target_path is None:
            base_dir = os.path.dirname(__file__)
            target_path = os.path.join(base_dir, "Collections", "challenge1b_input.json")
        # Write the new data to the file
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(new_data, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error rewriting challenge1b_input.json: {e}")
        return False
