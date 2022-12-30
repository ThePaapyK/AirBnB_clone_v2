#!/usr/bin/python3
"""full deployment to web servers"""
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['3.94.185.28', '35.153.17.98']

def deploy():
    """calls two functions to fully deploy
    the web_static folder
    """
    try:
        archive_name = do_pack()
        val = do_deploy(archive_name)
        return val
    except Exception:
        return False
