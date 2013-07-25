#!/usr/bin/env python2

from ansible.utils.module_docs import get_docstring
import os
import sys

# add play by default
print "snippet play"
print "	- hosts: ${1:group}"
print "	  user: ${2:root}"
print "	  tasks:"
print 

libpath = os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir, 'library'
    ))

fname_list = []

for d in os.listdir(libpath):
    for f in os.listdir(os.path.join(libpath, d)):
        fname_list.append(os.path.join(libpath, d, f))

for fname in fname_list: 
    if os.path.isdir(fname):
        continue

    doc, examples = get_docstring(fname)
    if doc != None:
        print "snippet %s" % (doc['module'])
        print "	- name: ${1:task_description}"
        print "	  %s:" % (doc['module']),
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
