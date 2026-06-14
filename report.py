from scanner import scan_directory

folder = input("Folder to scan: ")

results = scan_directory(folder)

with open("report.txt", "w") as report:

    report.write("FILE INSPECTOR REPORT\n")
    report.write("=" * 50 + "\n\n")

    for item in results:

        report.write(
            f"{item['file']} -> {item['type']}\n"
        )

print("Report saved as report.txt")
