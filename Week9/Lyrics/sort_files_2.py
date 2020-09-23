import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    # Change to desired directory
    category = []
    doc = input("What category would you like to sort doc files into?")
    if doc not in category: category.append(doc)
    docx = input("What category would you like to sort docx files into?")
    if docx not in category: category.append(docx)
    png = input("What category would you like to sort png files into?")
    if png not in category: category.append(png)
    gif = input("What category would you like to sort gif files into?")
    if gif not in category: category.append(gif)
    txt = input("What category would you like to sort txt files into?")
    if txt not in category: category.append(txt)
    xls = input("What category would you like to sort xls files into?")
    if xls not in category: category.append(xls)
    xlsx = input("What category would you like to sort xlsx files into?")
    if xlsx not in category: category.append(xlsx)
    jpg = input("What category would you like to sort jpg files into?")
    if jpg not in category: category.append(jpg)

    os.chdir('FilesToSort/')
    for item in category:
        os.mkdir(item)
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        elif filename.endswith('xlsx'):
            shutil.move(filename, '{}/'.format(xlsx) + filename)
        elif filename.endswith('txt'):
            shutil.move(filename, '{}/'.format(txt) + filename)
        elif filename.endswith('png'):
            shutil.move(filename, '{}/'.format(png) + filename)
        elif filename.endswith('jpg'):
            shutil.move(filename, '{}/'.format(jpg) + filename)
        elif filename.endswith('gif'):
            shutil.move(filename, '{}/'.format(gif) + filename)
        elif filename.endswith('docx'):
            shutil.move(filename, '{}/'.format(docx) + filename)
        elif filename.endswith('doc'):
            shutil.move(filename, '{}/'.format(doc) + filename)
        elif filename.endswith('xls'):
            shutil.move(filename, '{}/'.format(xls) + filename)
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))


main()
