#!/usr/bin/python3
# fabfile - generates a .tgz archive from the contents of web_static folder
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """ create a tar gzipped archive of the directory web_static
    """
    siku = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(siku.year,
                                                         siku.month,
                                                         siku.day,
                                                         siku.hour,
                                                         siku.minute,
                                                         siku.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
