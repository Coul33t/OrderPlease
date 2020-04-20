import os
import shutil
from pathlib import Path
from filetypes import FILETYPES, REVERSED_FILETYPES

class FileSorter:
    def __init__(self, path, debug_mode=False):
        self.path = Path(path)
        self.ftypes_number = {}
        self.debug_mode = debug_mode

    def gather_filetype(self):
        self.ftypes_number = {k:0 for k in FILETYPES.keys()}
        self.ftypes_number['others'] = 0
        
        for f in os.listdir(self.path):
            if os.path.isfile(self.path / f):
                is_other = True

                for k, v in REVERSED_FILETYPES.items():
                    if f.split('.')[-1].lower() in k.split(','):
                        self.ftypes_number[v] += 1
                        is_other = False

                if is_other:
                    self.ftypes_number['others'] += 0


        self.print_ftypes_numbers()

    def folder_creation(self):
        for k, v in self.ftypes_number.items():
            if v > 0:
                if not os.path.exists(self.path / k):
                    if self.debug_mode:
                        print(f'folder {self.path / k} would be created')
                    else:
                        os.mkdir(self.path / k)

    def sort_files(self):
        for f in os.listdir(self.path):
            if os.path.isfile(self.path / f):

                for k, v in REVERSED_FILETYPES.items():
                    if f.split('.')[-1].lower() in k.split(','):
                        if self.debug_mode:
                            print(f'Original: {self.path / f}')
                            print(f'Destination: {self.path / v / f}')
                        else:
                            shutil.move(self.path / f, self.path / v / f)

        # For other file types (everything that's not sorted at this point is of type " other ")
        for f in os.listdir(self.path):
            if os.path.isfile(self.path / f):
                if self.debug_mode:
                    print(f'Original: {self.path / f}')
                    print(f'Destination: {self.path / "others" / f}')
                else:
                    shutil.move(self.path / f, self.path / "others" / f)

    def sort_monotype_folder(self):
        extension_type = {k:0 for k in FILETYPES.keys()}

        # For each folder other than the one created
        for f in os.listdir(self.path):
            if (not os.path.isfile(self.path / f)) and (f not in FILETYPES.keys()):

                # For each file in this folder
                for file_in_folder in os.listdir(self.path / f):
                    if os.path.isfile(self.path / f / file_in_folder):

                        # Add filetype to the correct category
                        is_other = True

                        for k, v in REVERSED_FILETYPES.items():
                            if file_in_folder.split('.')[-1].lower() in k.split(','):
                                extension_type[v] += 1
                                is_other = False

                        if is_other:
                            extension_type['others'] += 0

                non_zero = 0

                for v in extension_type.values():
                    if v > 0:
                        non_zero += 1

                if non_zero == 1:
                    
                    category = ''
                    for k, v in extension_type.items():
                        if v > 0:
                            category = k
                            break

                    if self.debug_mode:
                        print(f'Original: {self.path / f}')
                        print(f'Destination: {self.path / category / f}')
                    else:
                        shutil.move(self.path / f, self.path / category / f)
                        print(f'Moved {self.path / f}\nto {self.path / category / f}')


                else:
                    print(f'Can\'t move {self.path / f}: multiple file types inside.')



    def print_ftypes_numbers(self):
        print(f'Current files in {self.path}: {sum(v for v in self.ftypes_number.values())}')
        print('------------------------------')

        for k, v in self.ftypes_number.items():
            print(f'{k}: {v}')

    def run(self):
        self.gather_filetype()
        self.folder_creation()
        self.sort_files()
        self.sort_monotype_folder()



if __name__ == '__main__':
    path = r'E:\Users\Quentin\Downloads'
    filesorter = FileSorter(path)
    filesorter.run()