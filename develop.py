import os


def get_ip():
    ip = os.popen("curl --max-time 60 --ipv4 icanhazip.com").read().strip()
    # os.popen("curl http://freedns.afraid.org/dynamic/update.php?VmRDMHhhbTVlTWFvQ1p1UWpSOXU6MTgwNDk4NjA=")
    return ip


def get_storage():
    return os.popen('df -h')
