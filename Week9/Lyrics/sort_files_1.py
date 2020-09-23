import shutil
import os

def main():
    print("Starting directory is: {}".format(os.getcwd()))
    # Change to desired directory
    os.chdir('FilesToSort/')
    os.mkdir('xlsx')
    os.mkdir('xls')
    os.mkdir('txt')
    os.mkdir('png')
    os.mkdir('jpg')
    os.mkdir('gif')
    os.mkdir('docx')
    os.mkdir('doc')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        elif filename.endswith('xlsx'):
            shutil.move(filename, 'xlsx/' + filename)
        elif filename.endswith('txt'):
            shutil.move(filename, 'txt/' + filename)
        elif filename.endswith('png'):
            shutil.move(filename, 'png/' + filename)
        elif filename.endswith('jpg'):
            shutil.move(filename, 'jpg/' + filename)
        elif filename.endswith('gif'):
            shutil.move(filename, 'gif/' + filename)
        elif filename.endswith('docx'):
            shutil.move(filename, 'docx/' + filename)
        elif filename.endswith('doc'):
            shutil.move(filename, 'doc/' + filename)
        elif filename.endswith('xls'):
            shutil.move(filename, 'xls/' + filename)
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))


main()