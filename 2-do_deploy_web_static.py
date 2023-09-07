#!/usr/bin/python3
"""
  send new version of web static to the server
"""

from fabric.api import local, run, put
from os import path
from datetime import datetime


def do_pack():
    """This function does pcking al files to one tgz compressed file"""

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    if path.isdir("version") is False:
        local("mkdir versions")
    # change to tgz
    local("tar -cvzf {} web_static".format(file_name))
    return file_name if path.exists(file_name) else None


def do_deploy(archive_path):
    """This function does deploy archive file to server"""

    if archive_path is None or path.exists(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    filename = file.split(".")[0]
    upload_path = "/tmp/" + file
    if put(archive_path, upload_path).failed is True:
        return False
    if run('sudo mkdir -p /data/web_static/releases/' + filename + '/\
           ').failed is True:
        return False
    # uncompressing to other folader
    rz = run('sudo tar -xzf ' + upload_path + ' -C /data/web_static/releases/' + filename)
    if rz.failed is True:
        return False
    # deleting compressed file from server
    if run('sudo rm -rf ' + upload_path).failed is True:
        return False
    if run("mv /data/web_static/releases/" + filename + "/web_static/* /data/web_static/releases/" + filename + "/").failed is True:
        return False
    if run("sudo rm -rf data/web_static/releases/" + filename + " /web_static").failed is True:
        return False
    # deleting symbolic link
    if run("sudo rm -rf /data/web_static/current").failed is True:
        return False
    if run("sudo ln -s /data/web_static/releases/" + filename + "/ /web_static/current").failed is True:
        return False
    return True