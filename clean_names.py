import os
import datetime

def get_creation_date(file_path):
    creation_time = os.path.getctime(file_path)
    return datetime.datetime.fromtimestamp(creation_time)

def get_modified_date(file_path):
    modified_time = os.path.getmtime(file_path)
    return datetime.datetime.fromtimestamp(modified_time)

def rename_wav_files(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".wav"):
            file_path = os.path.join(directory, filename)
            modified_date = get_modified_date(file_path)

            # Format the new filename
            new_filename = "{:%Y%m%d--%H%M}___{}".format(modified_date, filename)
            new_filepath = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(file_path, new_filepath)
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    target_directory = "."
    rename_wav_files(target_directory)
