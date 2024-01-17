import argparse
import os

def get_file_paths(file_names_arg, target_file_type):
    """
    Get a list of file paths from a command-line argument, which could be a list of file names
    or a file containing a list of file names.

    Args:
        file_names_arg (str or list): Either a string filename or a list of file names.
        target_file_type (str): Type of the file to look for. Will throw error if all the target files don't follow this type.

    Returns:
        list: A list of target type file paths.
    """
    # If the file_names_arg is a filename, read the file and get a list of file names
    print("Reading file names...")
    more_than_one_file_arg = len(file_names_arg) > 1
    first_file = file_names_arg[0]
    first_file_exists = os.path.isfile(first_file)
    if not more_than_one_file_arg and first_file_exists:
        with open(first_file, 'r') as f:
            file_paths = [line.strip() for line in f.readlines()]
        print(f"Found {len(file_paths)} files in {first_file}")
    else:
        # Otherwise, assume it's already a list of file names
        if more_than_one_file_arg:
            print(f"Found {len(file_names_arg)} files (directly passed as arguments)")
        elif not first_file_exists:
            raise ValueError(f"File not found: {first_file}")
        file_paths = file_names_arg

    # Confirm that all file paths have the same ending
    mismatched_file_paths = [f for f in file_paths if not f".{target_file_type}" == f[-(len(target_file_type)+1):]]
    if not mismatched_file_paths == []:
        raise ValueError(f"Input files not of expected type: should be {target_file_type}: {mismatched_file_paths[0]} not of type {target_file_type}")
    
    # Check if file paths exist
    file_paths = [f for f in file_paths if os.path.isfile(f)]
    return file_paths

def main():
    parser = argparse.ArgumentParser(description='Process NPZ files and generate a heatmap.')
    parser.add_argument('-f', '--file-names', nargs='+', help='List of NPZ filenames or a file containing NPZ filenames')
    args = parser.parse_args()

    # Get NPZ file paths either from a list of filenames or a file containing filenames
    npz_file_paths = get_file_paths(args.file_names, "npz")
    
    print(npz_file_paths)

if __name__ == "__main__":
    main()
