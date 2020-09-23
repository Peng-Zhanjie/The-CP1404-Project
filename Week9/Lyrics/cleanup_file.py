import shutil
import os


def Old():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Old')
    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # TODO: Use exception handling to avoid the crash (just pass)
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue
        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)

def Sunday():
    os.chdir('Lyrics/Sunday')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # TODO: Use exception handling to avoid the crash (just pass)
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue
        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)


def Special():
    os.chdir('Lyrics/Special')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # TODO: Use exception handling to avoid the crash (just pass)
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue
        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)



def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace("_", " ")
    filename=filename.replace("TXT","txt")
    new_name = filename
    situation = 0
    change = 1
    for char in filename:
        if situation + 1 == len(filename):
            situation += 1
        else:
            if (char.isspace() is False) and (
                    filename[situation + 1].isalpha() == True and filename[situation + 1].isupper() == True):
                new_name = new_name[:situation + change] + " " + new_name[situation + change:]
                change += 1
            situation += 1
    new_name=new_name.title()
    new_name=new_name.replace("Txt","txt")
    new_name=new_name.replace(" ","_")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        # TODO: add a loop to rename the files
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename,new_name))
            filename_fullpath =directory_name.strip(".\\") + "\\" +filename
            new_name_fullpath = directory_name.strip(".\\") + "\\" + new_name
            filename_fullpath = os.path.join(os.getcwd(),filename_fullpath)
            new_name_fullpath = os.path.join(os.getcwd(),new_name_fullpath)
            os.rename(filename_fullpath,new_name_fullpath)



demo_walk()
