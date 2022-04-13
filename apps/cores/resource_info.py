import importlib.util
import json
import os
import sys

import redis

from healthchecker.settings import CELERY_BROKER_URL


class Redis:
    name: str
    status: bool
    config: dict


class SystemHealthChecker:

    @staticmethod
    def get_os():
        return {
            "platform": sys.platform,
            "name": os.name,
            "uname": os.uname()
        }

    @staticmethod
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

    @staticmethod
    def get_python():
        result = {"version": sys.version,
                  "executable": sys.executable,
                  "python_path": sys.path,
                  "version_info": {'major': sys.version_info.major,
                                   'minor': sys.version_info.minor,
                                   'micro': sys.version_info.micro,
                                   'release_level': sys.version_info.releaselevel,
                                   'serial': sys.version_info.serial}}
        if importlib.util.find_spec('pkg_resources'):
            import pkg_resources
            packages = dict([(p.project_name, p.version) for p in pkg_resources.working_set])
            result['packages'] = packages

        return result

    def get_process(self):
        return {'argv': sys.argv,
                'cwd': os.getcwd(),
                'user': self.get_login(),
                'pid': os.getpid(),
                'environ': self.safe_dump(os.environ)}

    @staticmethod
    def safe_dump(dictionary):
        result = {}
        for key in dictionary.keys():
            if 'key' in key.lower() or 'token' in key.lower() or 'pass' in key.lower():
                # Try to avoid listing passwords and access tokens or keys in the output
                result[key] = "********"
            else:
                try:
                    json.dumps(dictionary[key])
                    result[key] = dictionary[key]
                except TypeError:
                    pass
        return result

    @staticmethod
    def get_redis() -> Redis:
        r = Redis()
        r.name = "Redis"
        conn_split = CELERY_BROKER_URL.split("//")[-1].split(":")
        conn_redis = redis.Redis(host=conn_split[0], port=conn_split[1])
        r.config = {"host": conn_split[0], "port": conn_split[1]}
        try:
            if conn_redis.ping():
                r.status = True
            else:
                r.status = False
        except redis.TimeoutError:
            r.status = False
        except redis.ConnectionError:
            r.status = False
        return r

    @staticmethod
    def get_celery():
        """
        :return:
        """


if __name__ == '__main__':
    c = SystemHealthChecker()
    print(c.get_redis().status)
