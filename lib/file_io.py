def write_file(file_name, file_content = 'This is a test content.'):
    with open(f"{file_name}.txt", mode="w" ) as any_file:
        any_file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a" ) as any_file:
        any_file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", "r" ) as any_file:
        return any_file.read()
