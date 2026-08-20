import os


def move_file(command: str) -> None:
    _, source_file, destination = command.split()

    destination_file = destination

    if destination.endswith("/"):
        destination_file = destination + os.path.basename(source_file)

    destination_dir = os.path.dirname(destination_file)

    if destination_dir:
        curren_path = ""
        for part in destination_dir.split("/"):
            curren_path = os.path.join(curren_path,
                                       part) if curren_path else part

            if not os.path.exists(curren_path):
                os.mkdir(curren_path)

    with open(source_file, "r") as file_in, open(destination_file,
                                                 "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source_file)
