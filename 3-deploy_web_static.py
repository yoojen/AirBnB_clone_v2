#!/usr/bin/python3
#creates a .tgz archive from the contents - web_static
"""
creates a .tgz archive from the contents - web_static
"""
from fabric.api import run, put, env, local
import os.path
from datetime import datetime

env.hosts = ["3.94.213.85", "34.227.93.137"]

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

def do_deploy(archive_path):
    """This function does deployment of tgz compressed file
     All goes on the server to be accessed via domain name
    """
    
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    filename = file.split(".")[0]
    upload_path = "/tmp/" + file
    if put(archive_path, upload_path).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/" + filename + '/').failed is True:
        return False
    # uncompressing to other folader
    if run("tar -xzf " + upload_path + " -C /data/web_static/releases/" + filename).failed is True:
        return False
    # deleting compressed file from server
    if run('rm ' + upload_path).failed is True:
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
  
def deploy():
    """create full deploy by calling previous created functions
      this makes it easier to read codes
    """
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
