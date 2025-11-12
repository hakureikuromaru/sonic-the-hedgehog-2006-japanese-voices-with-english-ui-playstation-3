import os
import shutil
'''
The files within the subdirectories in the event directory have two sets of files: The English files that start with "E" and
the Japanese files that start with "J" (Or "e" and "j" respectively in a few cases). The first portion of code here replaces
the "J" in each file to "E" (or "j" to "e"), so that the PS3 system on English detects the Japanese files as English, and the
actual English files are automatically removed, as no more than one file of the same name can exist in the same path.
'''
def rename_uppercase_files(event_directory, old_letter, new_letter):
    try:
        # Iterate through all files in the directory
        for dirpath, dirnames, filenames in os.walk(event_directory):
            for filename in filenames:
                # Check if the filename starts with the old_letter
                if filename.startswith(old_letter):
                    # Construct new filename by replacing first letter
                    new_filename = new_letter + filename[1:]
                    # Create full directory paths
                    old_file = os.path.join(dirpath, filename)
                    new_file = os.path.join(dirpath, new_filename)
                    # Rename the file
                    os.rename(old_file, new_file)
                    print(f"Renamed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def rename_lowercase_files(event_directory, old_letter_low, new_letter_low):
    try:
        # Iterate through all files in the directory
        for dirpath, dirnames, filenames in os.walk(event_directory):
            for filename in filenames:
                # Check if the filename starts with the old_letter_low
                if filename.startswith(old_letter_low):
                    # Construct new filename by replacing first letter
                    new_filename_low = new_letter_low + filename[1:]
                    # Create full directory paths
                    old_file = os.path.join(dirpath, filename)
                    new_file = os.path.join(dirpath, new_filename_low)
                    # Rename the file
                    os.rename(old_file, new_file)
                    print(f"Renamed: {filename} -> {new_filename_low}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Variables
event_directory = "event"  # Directory path
old_letter = "J" # Uppercase letter to match at start
new_letter = "E" # Uppercase letter to replace with
old_letter_low = "j" #Lowercase letter to match at start
new_letter_low= "e" #Lowercase etter to replace with
rename_uppercase_files(event_directory, old_letter, new_letter)
rename_lowercase_files(event_directory, old_letter_low, new_letter_low)

'''
The other half of this software, followed by this message, calls the "os" module, as the previous half did, to read
the "sound" directory, and then the directory in "sound", "j", so that the code can call the shutil module to move the files
in "j" to "e", the other directory in "sound". By default, "j" contains the Japanese voice files, and "e" is the directory that
the PS3 system detects when its locale is set to English.
'''

def move_files(source_dir, destination_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Get list of files in source directory
    try:
        files = os.listdir(source_dir)

        #  Move each file
        for file_name in files:
            source_path = os.path.join(source_dir, file_name)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.move(source_path, destination_path)
            print(f"Moved '{file_name}' to '{destination_dir}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

#Variables
source_dir = "sound/voice/j"  #Japanese voices directory
destination_dir = "sound/voice/e" #Directory that the game uses when PS3 locale is set to English
move_files(source_dir, destination_dir) #Execute file movement

print("File update complete!")