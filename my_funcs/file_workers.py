#function that opens file by its path and reads it

def read_from_file(filepath):
    with open(filepath, "r") as f_o:
        return f_o.readlines()

