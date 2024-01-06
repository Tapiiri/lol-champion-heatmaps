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
    first_file = file_names_arg[0]
    if len(file_names_arg) == 1 and os.path.isfile(first_file) and not f"{target_file_type}" in first_file:
        with open(first_file, 'r') as f:
            file_paths = [line.strip() for line in f.readlines()]
    else:
        # Otherwise, assume it's already a list of file names
        file_paths = file_names_arg

    # Confirm that all file paths have the same ending
    if not all([f".{target_file_type}" == file_paths[-(len(target_file_type)+1):] for file_paths in file_paths]):
        raise ValueError(f"Input files not of expected type: should be {target_file_type}")
    
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
