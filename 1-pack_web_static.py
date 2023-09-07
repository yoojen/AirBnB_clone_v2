#!/usr/bin/python3
"""
creates a .tgz archive from the contents - web_static
"""

from fabric.api import local
import os.path
from datetime import datetime


def do_pack():
    """This function does pcking al files to one tgz compressed file"""

    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return file_name
