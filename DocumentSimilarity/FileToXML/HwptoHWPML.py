#-*-coding:utf8;-*-
import redis
import os
from Naked.toolshed.shell import muterun_js


# self == file_path
# hwp_path == path about 'node-hwp-main/lib/hwp.js'
# name == file_name
# path == file_path except file_name
def make_xml(self):
    # fn_ext[0] : directory except file_name
    # fn_ext[1] : file_name include extension
    # fn_ext[2] : extension
    fn_ext = os.path.split(self)
    file_name = fn_ext[1].split('.')
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('hwp_path', 'C:/Exception/node-hwp-main/lib/hwp.js')
    r.set('name', file_name[0])
    r.set('path', fn_ext[0] + '/')

    muterun_js('C:/Exception/node-hwp-main/testGet.js')
    print("Make .hwp to .xml")