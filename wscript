#!/usr/bin/env python
# encoding: utf-8
# Alexandre Gauthier, 2011

import sys

APPNAME = "tsge-adventure"
VERSION = "0.1.0"

top = '.'
out = 'build'

def options(opt):
    opt.load('compiler_c')
    opt.load('vala')

def configure(conf):
    conf.load('compiler_c')
    conf.load('vala')

    # Let's spare our windows friends some pain by setting
    # then straight right away.
    if sys.platform == 'win32':
        print("Windows does not have (n)curses. Sorry.")
        print("If you really want to, cygwin's your best bet.")
        conf.fatal("Platform unsupported.")

    if sys.platform == 'darwin':
        print("Configuring for Mac OS X")
        conf.load('c_osx')
        # Explicitely load the darwin gcc modifier
        # because my LINKERFLAGS are full of linuxisms and I have no
        # no fucking clue why. It has been driving me insane.
        from waflib.Tools import gcc
        gcc.gcc_modifier_darwin(conf)
    else:
        conf.load('c_config')

    try:
        conf.check_cc(header_name='ncurses.h', lib=['ncurses'],
            uselib_store='NCURSES')
    except conf.errors.ConfigurationError:
        print("OH GOD WHERE IS NCURSES")
        print("Hold on, hold on, let's try grandpa curses.")
        conf.check_cc(header_name='curses.h', lib=['curses'],
            uselib_store='NCURSES', mandatory=True)

    conf.check_cfg(package='glib-2.0', uselib_store='GLIB',
        atleast_version='2.10.0', args='--cflags --libs')

def build(bld):
    bld.recurse('src')



