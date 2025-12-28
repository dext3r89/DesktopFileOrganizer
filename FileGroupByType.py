import os
import shutil

def organize_files_by_type(path):
    files = os.listdir(path)
    file_types = set()  # Set to store unique file extensions
    
    # Extract file extensions and add them to the set
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            file_types.add(os.path.splitext(file)[1][1:].upper())  # Extract extension and convert to uppercase
    
    # Prompt the user to choose a file type
    print("Choose a file type to organize:")
    for idx, file_type in enumerate(file_types, start=1):
        print(f"{idx}. {file_type}")
    
    choice = int(input("Enter your choice (1-" + str(len(file_types)) + "): "))
    
    # Check if the choice is within valid range
    if 1 <= choice <= len(file_types):
        selected_type = list(file_types)[choice - 1]
        
        # Create directory for selected file type if it doesn't exist
        if not os.path.exists(os.path.join(path, selected_type)):
            os.makedirs(os.path.join(path, selected_type))
        
        # Move files of selected type to corresponding directory
        for file in files:
            if os.path.isfile(os.path.join(path, file)):
                file_ext = os.path.splitext(file)[1][1:].upper()
                if file_ext == selected_type:
                    shutil.move(os.path.join(path, file), os.path.join(path, selected_type, file))
        
        print(f"Files of type '{selected_type}' organized successfully!")
    else:
        print("Invalid choice!")

# Example usage:
path = input("Enter path to directory: ")
organize_files_by_type(path)