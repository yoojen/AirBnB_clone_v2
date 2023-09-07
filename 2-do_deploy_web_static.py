#!/usr/bin/python3
""" put data to the server by using fabfile"""

from fabric.api import local, run, put, env
from os import path
from datetime import datetime

env.hosts = ["3.94.213.85", "34.227.93.137"]


def do_pack():
    local("mkdir -p version")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "version/web-static_{}.tgz".format(date)
    # change to tgz
    local("tar -cvzf {} web-static".format(file_name))
    return file_name if path.exists(file_name) else None


def do_deploy(archive_path):
    if archive_path is None or path.exists(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    filename = file.split(".")[0]
    upload_path = "/tmp/" + file
    if put(archive_path, upload_path).failed is True:
        return False
    if run('mkdir -p /data/web_static/releases/' +filename + '/').failed is True:
        return False
    #uncompressing to other folader
    if run('tar -xzf ' + upload_path + ' -C /data/web_static/releases/' + filename).failed is True:
        return False
    #deleting compressed file from server
    if run('rm -rf ' + upload_path).failed is True:
        return False
    if run("mv /data/web_static/releases/" + filename + "/web_static/* /data/web_static/releases/"+ filename +"/").failed is True:
        return False
    if run("rm -rf data/web_static/releases/" + filename + "/web_static").failed is True:
        return False
    # deleting symbolic link
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/" + filename + "/ /data/web_static/current").failed is True:
        return False
    return True
