import argparse
import os

def get_npz_file_paths(file_names_arg):
    """
    Get a list of NPZ file paths from a command-line argument, which could be a list of file names
    or a file containing a list of file names.

    Args:
        file_names_arg (str or list): Either a string filename or a list of file names.

    Returns:
        list: A list of NPZ file paths.
    """
    # If the file_names_arg is a filename, read the file and get a list of file names
    first_file = file_names_arg[0]
    if len(file_names_arg) == 1 and os.path.isfile(first_file) and not ".npz" in first_file:
        with open(first_file, 'r') as f:
            file_paths = [line.strip() for line in f.readlines()]
    else:
        # Otherwise, assume it's already a list of file names
        file_paths = file_names_arg
    
    # Check if file paths exist
    file_paths = [f for f in file_paths if os.path.isfile(f)]
    return file_paths

def main():
    parser = argparse.ArgumentParser(description='Process NPZ files and generate a heatmap.')
    parser.add_argument('-f', '--file-names', nargs='+', help='List of NPZ filenames or a file containing NPZ filenames')
    args = parser.parse_args()

    # Get NPZ file paths either from a list of filenames or a file containing filenames
    npz_file_paths = get_npz_file_paths(args.file_names)
    
    print(npz_file_paths)

if __name__ == "__main__":
    main()
