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


def sort_and_move_image_file(category_folder):
    jpg_file_list = glob.glob(f"{category_folder}/*.jpg")
    jpeg_file_list = glob.glob(f"{category_folder}/*.jpeg")
    png_file_list = glob.glob(f"{category_folder}/*.png")

    image_list = jpg_file_list + jpeg_file_list + png_file_list
    image_dest = f"{category_folder}/images"

    for item in image_list:
        shutil.move(item, image_dest)
        print(f"moved image of {item} to {image_dest}")


def move_images(blog_path):
    category_paths = get_categories_paths(blog_path)
    for item in category_paths:
        sort_and_move_image_file(item)


blog_path = "/Users/noopy/noopy/content/blog"
