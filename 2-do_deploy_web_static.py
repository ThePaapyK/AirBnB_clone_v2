#!/usr/bin/python3
"""deploy web_static folder to my servers"""
from datetime import datetime
from fabric.api import *


env.user = 'ubuntu'
env.hosts = ['3.94.185.28', '35.153.17.98']

def do_pack():
    """makes the web_static folder an archive"""

    time = datetime.now()
    archive = "web_static_{}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
    local('mkdir -p versions')
    item = local('tar -cvzf versions/{} web_static'.format(archive))
    if item is not None:
        return archive
    else:
        return None


def do_deploy(archive_path):
    """deploy the tgz item to my web servers"""

    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/{}'.format(archive.strip('.tgz'))
        symp = '/data/web_static/current'
        put('archive_path', '/tmp/')
        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -c {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} {}'.format(path, symp))
        return True
    except:
        return False
