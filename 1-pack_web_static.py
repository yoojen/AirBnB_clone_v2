#!/usr/bin/python3
"""
creates a .tgz archive from the contents - web_static
"""

from fabric.api import local
from os import path
from datetime import datetime


def do_pack():
    """This function does pcking al files to one tgz compressed file"""

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    if path.exists("versions") is False:
        local("mkdir versions")
    # change to tgz
    local("tar -cvzf {} web_static".format(file_name))
    return file_name if path.exists(file_name) else None
