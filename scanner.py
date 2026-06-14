import os
from signatures import SIGNATURES


def identify_file(filepath):
    try:
        with open(filepath, "rb") as f:
            header = f.read(16)

        for sig, filetype in SIGNATURES.items():
            if header.startswith(sig):
                return filetype

        return "Unknown"

    except Exception as e:
        return f"Error: {e}"


def scan_directory(folder):
    results = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)

            detected_type = identify_file(path)

            results.append({
                "file": path,
                "type": detected_type
            })

    return results
