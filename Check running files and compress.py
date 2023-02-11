import subprocess
import gzip

def check_and_compress_files(file_name, directory):
    # Use lsof to check if the file is running in the specified directory
    output = subprocess.run(["lsof", "-a", "-d", "/var/log", file_name], stdout=subprocess.PIPE)
    
    files = output.stdout.decode("utf-8")
    if files:
        print(f"{file_name} is currently running in {directory}, cannot compress.")
    else:
        # Open the file for reading
        with open(file_name, 'rb') as f_in:
            # Open a gzip file for writing
            with gzip.open(file_name + '.gz', 'wb') as f_out:
                # Compress the file
                f_out.writelines(f_in)
                print(f"{file_name} has been compressed and saved as {file_name}.gz")

check_and_compress_files("my_file.txt", "/var/log")
