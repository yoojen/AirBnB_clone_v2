#!/usr/bin/python3
""" put data to the server by using fabfile"""
import os.path
from fabric.api import env
from fabric.api import put,run

env.hosts = ["3.94.213.85", "34.227.93.137"]

def do_deploy(archive_path):
    """Distributes an archive to a web server.
        returns true or false
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    filename = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(filename)).failed is True:
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
    if run("mkdir -p /data/web_static/releases/{}/".
           format(filename)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, filename)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(filename, filename)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(filename)).failed is True:
        return False
    return True
