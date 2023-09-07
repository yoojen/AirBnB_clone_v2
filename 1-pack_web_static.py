#!/usr/bin/python3
"""
creates a .tgz archive from the contents - web_static
"""

from fabric.api import local
from os import path
from datetime import datetime


def do_pack():
    """This function does pcking al files to one tgz compressed file"""

    local("mkdir -p version")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "version/web_static_{}.tgz".format(date)
    # change to tgz
    local("tar -cvzf {} web_static".format(file_name))
    return file_name if path.exists(file_name) else None
