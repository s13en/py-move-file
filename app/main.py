import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Please use valid command format"
            "mv <source_file> <destination_path>"
        )

    src_file, dest_path = parts[1], parts[2]

    if not os.path.exists(src_file):
        print("Error: File does not exist")
        return

    if dest_path.endswith("/"):
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        final_destination = os.path.join(dest_path, os.path.basename(src_file))

    else:
        destination_directory = os.path.dirname(dest_path)
        if destination_directory and not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        final_destination = dest_path

    os.rename(src_file, final_destination)
    print(f"File '{src_file}' successfully moved to '{final_destination}'")
