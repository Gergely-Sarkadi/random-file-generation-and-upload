import random
import string
import time

def generate_random_text(length):
    """Generate random text with the given length"""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def create_dummy_files(number_of_files=10000, file_size_in_kbytes=1, target_directory='generated_files/'):
    """Generate the given number of files with the given size with random content"""
    start = time.time()
    for i in range(number_of_files):
        filename = f'{target_directory}{i}_dummy_file.txt'
        with open(filename, 'w') as file:
            for _ in range(file_size_in_kbytes):
                content = generate_random_text(1024) # 1 KiB data
                file.write(content)
    end = time.time()
    print(f'Created {number_of_files} new files with the size of {file_size_in_kbytes} KiB in the \'{target_directory}\' directory in {end - start} seconds.')

create_dummy_files()
