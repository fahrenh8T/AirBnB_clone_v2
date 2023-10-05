#!/usr/bin/python3
# Fabfile to delete out-of-date archives - func do_clean
# usage: fab -f 100-clean_web_static.py do_clean:number=2 -i my_ssh_private_key -u ubuntu > /dev/null 2>&1
import os
from fabric.api import *

env.hosts = ["52.3.220.183", "54.237.46.105"]


def do_clean(number=0):
    """ delete out-of-date archives.

        Args:
            namba (int): The number of archives to keep.

        If 0 or 1, keeps only the most recent archive.
        If 2, keeps the most and second-most recent archives,
        etc.
    """
    namba = 1 if int(namba) == 0 else int(namba)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(namba)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(namba)]
        [run("rm -rf ./{}".format(a)) for a in archives]
