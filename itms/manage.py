#!/usr/bin/env python
import os
import sys
#from os.path import abspath,dirname
#project_dir = abspath(dirname(dirname(__file__)))
#sys.path.insert(0,project_dir)
#sys.path.insert(0,'/home/wuwenzhong/imediapro-itms2/itms')
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "itms.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
