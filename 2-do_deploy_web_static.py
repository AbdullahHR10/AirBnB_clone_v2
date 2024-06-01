#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""


from fabric.api import env, put, run
import os


env.hosts = ['3.89.160.4', '34.232.66.125']


def do_deploy(archive_path):
    """Fabric script that distributes an archive to your web servers
    using the function do_deploy."""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_file = archive_path.split("/")[-1]
        archive_name = archive_path.split(".")[0]
        release_dir = f"/data/web_static/releases/{archive_name}/"
        run(f"mkdir -p {release_dir}")
        run(f"tar -xzf /tmp/{archive_file} -C {release_dir}")
        run(f"rm /tmp/{archive_file}")
        run(f"mv {release_dir}web_static/* {release_dir}")
        run(f"rm -rf {release_dir}web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {release_dir} /data/web_static/current")
        return True
    except Exception as e:
        return False
