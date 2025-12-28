import os
import shutil

def organize_files_by_substring(path, substring):
    files = os.listdir(path)
    
    for file in files:
        # Skip directories
        if os.path.isdir(os.path.join(path, file)):
            continue
        
        # Check if the substring is present in the file name
        if substring in file:
            # Create directory if it doesn't exist
            if not os.path.exists(os.path.join(path, substring)):
                os.makedirs(os.path.join(path, substring))
            
            # Move the file to the corresponding directory
            shutil.move(os.path.join(path, file), os.path.join(path, substring, file))
            
# Example usage:
path = input("Enter path: ")
substring = input("Enter substring to organize files: ")
organize_files_by_substring(path, substring)
print("Files organized successfully!")
