ansible_snippet_generator
=========================

A small script to generate snipmate.vim snippets to be used in ansible playbooks

Requierements
-------------

- ansible sources: https://github.com/ansible/ansible / http://ansible.cc
- snipmate.vim: https://github.com/msanders/snipmate.vim

What does it do ?
-----------------

This scripts will parse the DOCUMENTATION strings of ansible module, and
generate snippets to be used with snipmate.vim. The snippets will use the module
name, and provides all the requireds parameters directly, and the optional
parameters in comment.

Output is done on STDOUT, you can redirect it to your
snipmate.vim/snippets/yaml.snippets if you wish.

Usage
-----

Installation:

- put the script in ansible/hacking (so it can find module_formatter.py)
- call passing the ansible/library folder, redirect output to a file

In vim:
- Edit a .yaml file
- type `play` and then <tab>, it will fill the start of the playbook
- the cursor will be placed on the next token, for playbook this is the hosts
  variable, you can then jump between tokens with <tab> and <S-tab>
- then you can add an action for a given module by typing the name of the module
  followed by <tab>

Example
-------

 TODO: link to asciicast.
