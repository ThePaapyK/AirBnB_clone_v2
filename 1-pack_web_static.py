#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """
    try:
        time = datetime.now()
        archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
        local('mkdir -p versions')
        local('tar -cvzf versions/{} web_static'.format(archive))
        return ("versions/{}".format(archive))
    except Exception:
        return None
