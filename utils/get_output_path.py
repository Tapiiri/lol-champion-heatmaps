import os

def get_output_path(output_arg, default_filename="output", default_file_type="npz"):
    """
    Get the output path from a command-line argument, which could be a path to a file or a folder.

    Args:
        output_arg (str): Either a string path or a folder path.

    Returns:
        str: A string path.
    """
    # If the output_arg is a folder, append the default filename
    if os.path.isdir(output_arg):
        output_path = os.path.join(output_arg, default_filename)
    else:
        output_path = output_arg

    # Check if path has file type defined
    has_file_type = "." in output_path.split("/")[-1] if os.name == "posix" else "." in output_path.split("\\")[-1]

    if not has_file_type:
        output_path += f".{default_file_type}"
    elif not output_path[-len(default_file_type):] == default_file_type:
        raise ValueError(f"Output file not of expected type: should be {default_file_type}: {output_path} not of type {default_file_type}")
    
    return output_path