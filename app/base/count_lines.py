import glob
from os import walk

exclude_folders = [
    'node_modules',
    'ios',
    'android',
    '__pycache__'
]

exclude_files = [
    'json',
    'txt',
    'traineddata',
    'lstmf',
    'yml',
    'md'
    'log',
    'env',
    'gitignore',
    'dockerignore'
]

# get all files in directory
dirr = '/home/viktor/Documents/personal-expenses-accounting/app/services/web_service/'
folders = glob.glob(dirr + '/**/', recursive=True)

# only project related directories
directories = []
for folder in folders:
    current_folder = folder.split('/')[-2]
    if current_folder not in exclude_folders:
        files = glob.glob(folder + '*')
        print(files)
        directories.append(folder)


# num_lines = sum(1 for line in open('myfile.txt'))
