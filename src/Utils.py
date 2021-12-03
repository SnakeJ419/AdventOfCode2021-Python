
def get_file_as_array(file_path: str):
    with open(file_path, 'r') as file:
        line = file.readline()
        file_array = []
        while line:
            file_array.append(line)
            line = file.readline()
        file.close()
        return file_array
