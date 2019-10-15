# trial in progress

import os
import shutil

def extract_extensions(fileType):
    if fileType == "audio":
        file_name = "audio_formats.txt"
    elif fileType == "video":
        file_name = "video_formats.txt"
    elif fileType == "text_file":
        file_name = "text_file_formats.txt"
    elif fileType == "3d_image":
        file_name = "3d_image_formats.txt"
    # add other file types here
    file = open(file_name, "r")
    ex_list = []
    for line in file:
        line_read = line
        splited_line = line_read.split("\t")
        first_element = splited_line[0]
        splited_first_element = first_element.split(".")
        extension = splited_first_element[1]
        ex_list.append(extension)
        ex_list.append(extension.lower())
    file.close()
    #print(ex_list)
    return ex_list

# function creates folder if does not exist and handle the error
def create_folder(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except OSError:
        print("Error: Creating directory. " + folder_path)
    except FileNotFoundError:
        print("folder path is not founded ")


def destination_class(file_type, source_folder):
    if file_type == "audio":
        destination = source_folder + "Audios"
        create_folder(destination)
        return destination
    if file_type == "video":
        destination = source_folder + "Videos"
        create_folder(destination)
        return destination
    if file_type == "text_file":
        destination = source_folder + "Text_files"
        create_folder(destination)
        return destination
    if file_type == "3d_image":
        destination = source_folder + "3D_Images"
        create_folder(destination)
        return destination
    if file_type == "compressed":
        destination = source_folder + "Compressed"
        create_folder(destination)
        return destination
    if file_type == "executable":
        destination = source_folder + "Executables"
        create_folder(destination)
        return destination
    if file_type == "presentation":
        destination = source_folder + "Presentations"
        create_folder(destination)
    if file_type == "spreadsheet":
        destination = source_folder + "Spreadsheets"
        create_folder(destination)
        return destination
    if file_type == "internet_related":
        destination = source_folder + "Internet_Related"
        create_folder(destination)
        return destination
    if file_type == "mix":
        destination = source_folder + "Arranged"
        create_folder(destination)
        return destination


def move_to_destination(destination, root_folder, root_folder_list, extensions):
    for file in root_folder_list:
        if extensions == "none":
            file_path = root_folder + file
            shutil.move(file_path, destination)
            print("File moved to " + destination + " successfully...")

        else:
            for extension in extensions:
                if file.endswith("." + extension):
                    file_path = root_folder + file
                    shutil.move(file_path, destination)
                    print("File moved to " + destination + " successfully...")


# extension like: "mp4", "mp3"...
def classifying_type(classification_type, root_folder):
    try:
        root_folder_list = os.listdir(root_folder)  # put all the files in list
    except OSError:
        print("Error: Creating directory. " + root_folder)
    except FileNotFoundError:
        print("folder path is not founded ")
    video_extensions_extracted = extract_extensions("video")
    audio_extensions_extracted = extract_extensions("audio")
    text_file_extensions_extracted = extract_extensions("text_file")
    three_d_image_extensions_extracted = extract_extensions("3d_image")

    # add other extracts here

    video_extensions = video_extensions_extracted
    audio_extensions = audio_extensions_extracted
    text_file_extensions = text_file_extensions_extracted
    three_d_image_extensions = three_d_image_extensions_extracted

    # add other file_extensions here

    mix_extensions = "none"

    if classification_type == "video_classification":
        extensions = video_extensions
        file_type = "video"
    if classification_type == "audio_classification":
        extensions = audio_extensions
        file_type = "audio"
    if classification_type == "text_file_classification":
        extensions = text_file_extensions
        file_type = "text_file"
    if classification_type == "3d_image_classification":
        extensions = three_d_image_extensions
        file_type = "3d_image"
    if classification_type == "mix_classification":
        extensions = mix_extensions
        file_type = "mix"
    # add here the other extensions list types

    destination = destination_class(file_type, root_folder)
    move_to_destination(destination, root_folder, root_folder_list, extensions)


def user_classify_dir_prompt():
    # inputed_root_folder = input("Enter the working folder path to be classified (example:'C:/Users/John/Downloads/)': ")
    print("Do you like to classify the current directory folder path (Y/N): ")
    current_dir_classify = input()
    if current_dir_classify == "y" or current_dir_classify == "Y":
        user_root_folder = "./"
    elif current_dir_classify == "n" or current_dir_classify == "N":
        user_root_folder = input("Enter the working folder path to be classified (example:'C:/Users/John/Downloads/)':")
        try:
            if not os.path.exists(user_root_folder):
                print("Sorry.The entered folder path does not exist")
            else:
                user_root_folder = user_root_folder
        except OSError:
            print(
                "Error: creating or accessing directory. " + user_root_folder + ". " + "Please check whether the enterd folder path exist.")
        except FileNotFoundError:
            print("folder path is not founded ")
    else:
        print("Invalid input")

    return user_root_folder


def classify(function_root_folder):
    # copy files by there extension (by filtering )
    root_folder = function_root_folder

    classifying_type("video_classification", root_folder)
    classifying_type("audio_classification", root_folder)
    classifying_type("text_file_classification", root_folder)
    classifying_type("3d_image_classification", root_folder)
    classifying_type("mix_classification", root_folder)


def main():
    # choosing target root folder by the user to be classified


    user_dir = user_classify_dir_prompt()

    # classification process " the essential function "
    classify(user_dir)

    #
    # if __name__ == '__main__':
main()


