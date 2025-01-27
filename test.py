import os


def human_read_format(size):
    sizes = ['Б', 'КБ', 'МБ', 'ГБ']
    n = size
    i = 0
    while n // 1024:
        i += 1
        n //= 1024
    return str(round(size / 1024 ** i)) + sizes[i]


def get_files_sizes():
    return '\n'.join([i + ' ' + human_read_format(os.path.getsize(i)) for i in os.listdir() if os.path.isfile(i)])
