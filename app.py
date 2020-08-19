import os
from os import fdopen, remove, walk
import glob
from tempfile import mkstemp
import shutil
from shutil import move, copymode


def get_categories_paths(blog_path):
    category_paths = []
    for (blogpath, categories, hidden_files) in walk(blog_path):
        break

    for category in categories:
        category_path = f"{blog_path}/{category}"
        category_paths.append(category_path)
    return category_paths


def sort_and_move_image_file(blog_path):
    category_paths = get_categories_paths(blog_path)
    for category_folder in category_paths:
        jpg_file_list = glob.glob(f"{category_folder}/*.jpg")
        jpeg_file_list = glob.glob(f"{category_folder}/*.jpeg")
        png_file_list = glob.glob(f"{category_folder}/*.png")

        image_list = jpg_file_list + jpeg_file_list + png_file_list
        image_dest = f"{category_folder}/images"

        for item in image_list:
            shutil.move(item, image_dest)
            print(f"moved image of {item} to {image_dest}")


def get_markdown_paths(blog_path):
    all_markdown_files = []
    category_paths = get_categories_paths(blog_path)
    for category_folder in category_paths:
        markdown_file_list = glob.glob(f"{category_folder}/*.md")
        all_markdown_files += markdown_file_list
    print(all_markdown_files)
    return all_markdown_files


# source: https://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
def replace_img_notation(blog_path):
    markdown_file_list = get_markdown_paths(blog_path)
    for markdown_file_path in markdown_file_list:
        # Create temp file
        fh, abs_path = mkstemp()
        with fdopen(fh, "w") as new_file:
            with open(markdown_file_path) as old_file:
                for line in old_file:
                    if "images/" in line:
                        new_file.write(line)
                    elif "http" in line:
                        new_file.write(line)
                    else:
                        pattern = "]("
                        substitute_pattern = "](images/"
                        new_file.write(line.replace(pattern, substitute_pattern))
        # Copy the file permissions from the old file to the new file
        copymode(markdown_file_path, abs_path)
        # Remove original file
        remove(markdown_file_path)
        # Move new file
        move(abs_path, markdown_file_path)


BLOG_PATH = "/Users/noopy/noopy/content/blog"
sort_and_move_image_file(BLOG_PATH)
replace_img_notation(BLOG_PATH)
