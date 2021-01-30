from __future__ import print_function
import os
import hipmetastrip
import shutil


def do(kwargs):
    if not kwargs.get('success', False):
        return
    basedir = os.path.dirname(kwargs['file'])
    backupdir = os.path.join(basedir, 'backup')
    skip_backup = False
    if not os.path.exists(backupdir):
        try:
            os.makedirs(backupdir)
        except:
            skip_backup = True
    if not skip_backup:
        shutil.copy2(kwargs['file'], os.path.join(backupdir, os.path.basename(kwargs['file'] + '.orig')))
    try:
        hipmetastrip.clean_file(kwargs['file'], kwargs['file'])
    except RuntimeError as e:
        print('failed to strip metadata from hip: %s' % repr(e))


if hou.licenseCategory() == hou.licenseCategoryType.Commercial:
    do(kwargs)
