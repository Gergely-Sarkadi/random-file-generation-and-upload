import random
import string

def generate_random_text(length):
    """Generate random text with the given length"""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def create_dummy_files(number_of_files=1, file_size_in_kbytes=1, target='generated_files/'):
    """Generate the given number of files with random content"""
    for i in range(number_of_files):
        filename = f'{target}{i}_dummy_file.txt'
        with open(filename, 'w') as file:
            for _ in range(file_size_in_kbytes):
                content = generate_random_text(1024) # 1 Kb
                file.write(content)
    print(f'Created {number_of_files} new files in the \'{target}\' directory')

create_dummy_files()
