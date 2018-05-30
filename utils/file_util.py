#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import json
import shutil


def copytree(src, dst, symlinks=False, ignore=None):
    try:
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)
    except:
        pass


def make_dirs(path):
    try:
        os.makedirs(path)
    except:
        pass


def save_dict_as_json_file(directory_path, filename, dict_data):
    file_path = os.path.join(directory_path, filename)
    with open(file_path, "w") as outfile:
        json.dump(dict_data, outfile)


def remove_file(file_path):
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
        except:
            pass
