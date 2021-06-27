import os


class Develop:
    def getIp(self):
        ip = os.popen("curl --max-time 60 --ipv4 icanhazip.com").read().strip()
        os.popen("curl http://freedns.afraid.org/dynamic/update.php?VmRDMHhhbTVlTWFvQ1p1UWpSOXU6MTgwNDk4NjA=")
        return ip

    def getStorage(self):
        return os.popen('df -h')
