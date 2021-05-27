import os
import sys
import resource


def get_login():
    # Based on https://github.com/gitpython-developers/GitPython/pull/43/
    # Fix for 'Inappopropirate ioctl for device' on posix systems.
    if os.name == "posix":
        import pwd
        username = pwd.getpwuid(os.geteuid()).pw_name
    else:
        username = os.environ.get('USER', os.environ.get('USERNAME', 'UNKNOWN'))
        if username == 'UNKNOWN' and hasattr(os, 'getlogin'):
            username = os.getlogin()
    return username


def get_curr_mem_usg():
    with open('/proc/self/status') as f:
        print(f.readlines())
        # usage = f.read().split('VmRSS:')[1].split('\n')[0][:-3]
        # print(int(usage.strip()) / 1024)

    with open('/proc/meminfo') as mem:
        mem_info = mem.readlines()
        info = dict()
        for item in mem_info:
            key, value = item.split(":")
            info.update({key: value})

        print(info)

        total_mem = round(int(int(info['MemTotal'].split()[0]) / 1024) / 1024, 2)
        total_available = round(int(int(info['MemAvailable'].split()[0]) / 1024) / 1024, 2)

        print(f"Total memory {total_mem} GB - total available {total_available} GB")

    # print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


if __name__ == '__main__':
    get_curr_mem_usg()
