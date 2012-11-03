#!/usr/bin/env python2

from module_formatter import get_docstring
import os
import sys

# add play by default
print "snippet play"
print "	- hosts: ${1:group}"
print "	  user: ${2:root}"
print "	  tasks:"
print 

list = os.listdir(sys.argv[1])
os.chdir(sys.argv[1])

for m in list:
    if os.path.isdir(m):
        continue

    doc = get_docstring(m)
    if doc != None:
        print "snippet %s" % (doc['module'])
        print "	- name: ${1:task_description}"
        print "	  action: %s" % (doc['module']),
        if 'options' in doc:
            count = 1
            for o in doc['options']:
                if 'required' in doc['options'][o] and doc['options'][o]['required']:
                    count += 1
                    if 'default' in doc['options'][o] and doc['options'][o]['default']:
                        value = "${%d:%s}" % (count, doc['options'][o]['default'])
                    else:
                        value = "${%d}" % (count)
                    print "%s=%s" % (o, value),
            print "#",
            for o in doc['options']:
                if not 'required' in doc['options'][o] or doc['options'][o]['required'] == False:
                    count += 1
                    if 'default' in doc['options'][o] and doc['options'][o]['default']:
                        value = "${%d:%s}" % (count, doc['options'][o]['default'])
                    else:
                        value = "${%d}" % (count)
                    print "%s=%s" % (o, value),
            print
    print
