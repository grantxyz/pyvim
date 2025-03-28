import os
import sys
import binascii

def show_help():
    print("\nCommands:")
    print("  <pyvim> path/to/file             - Open file in edit mode")
    print("  <pyvim> path/to/file -see        - View file contents")
    print("  <pyvim> path/to/file -hex        - View file in hexadecimal")
    print("  <pyvim> path/to/file -size       - Show file size")
    print("  <pyvim> path/to/file -lines      - Count lines in file")
    print("  <pyvim> path/to/file -words      - Count words in file")
    print("  <pyvim> path/to/file -chars      - Count characters in file")
    print("  <pyvim> path/to/file -exists     - Check if file exists")
    print("  help                              - Show this help menu")
    print("  exit, quit                        - Exit Pyvim")

def edit_file(path):
    if not os.path.exists(path):
        print("File not found. Creating a new file...")
    with open(path, 'a+') as f:
        while True:
            line = input()
            if line == ':q':
                break
            f.write(line + '\n')

def view_file(path):
    if not os.path.exists(path):
        print("File not found.")
        return
    with open(path, 'r') as f:
        print(f.read())

def view_hex(path):
    if not os.path.exists(path):
        print("File not found.")
        return
    with open(path, 'rb') as f:
        print(binascii.hexlify(f.read()).decode())

def file_size(path):
    if not os.path.exists(path):
        print("File not found.")
        return
    print(f"Size: {os.path.getsize(path)} bytes")

def count_lines(path):
    if not os.path.exists(path):
        print("File not found.")
        return
    with open(path, 'r') as f:
        print(f"Lines: {len(f.readlines())}")

def count_words(path):
    if not os.path.exists(path):
        print("File not found.")
        return
    with open(path, 'r') as f:
        print(f"Words: {len(f.read().split())}")

def count_chars(path):
    if not os.path.exists(path):
        print("File not found.")
        return
    with open(path, 'r') as f:
        print(f"Characters: {len(f.read())}")

def file_exists(path):
    print("Exists: Yes" if os.path.exists(path) else "Exists: No")

def main():
    while True:
        command = input("<pyvim> ")
        if command in ["exit", "quit"]:
            break
        elif command == "help":
            show_help()
        else:
            parts = command.split()
            if len(parts) < 1:
                continue
            path = parts[0]
            flag = parts[1] if len(parts) > 1 else ""

            if flag == "-see":
                view_file(path)
            elif flag == "-hex":
                view_hex(path)
            elif flag == "-size":
                file_size(path)
            elif flag == "-lines":
                count_lines(path)
            elif flag == "-words":
                count_words(path)
            elif flag == "-chars":
                count_chars(path)
            elif flag == "-exists":
                file_exists(path)
            else:
                edit_file(path)

if __name__ == "__main__":
    main()
