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
    opt.add_option('--with-pdcurses-dir', action="store", default=False,
        help="Use pdcurses and specify where it is unpacked." \
        "(Mostly useful for Win32 and cross-compilation)")

def configure(conf):
    conf.load('compiler_c')
    conf.load('vala')

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

    # Use extra pdcurses directory? (mostly useful on windows
    # and for cross compiling.
    if conf.options.with_pdcurses_dir:
        conf.env.append_unique('INCLUDES', conf.options.with_pdcurses_dir)
        conf.env.append_unique('LIBPATH', conf.options.with_pdcurses_dir)

    conf.check(features="c", header_name='curses.h', mandatory=True)

    if conf.options.with_pdcurses_dir:
        conf.check_cc(lib='pdcurses', uselib_store="CURSES")
    else:
        try:
            conf.check_cc(lib='ncurses', uselib_store="CURSES")
        except conf.errors.ConfigurationError:
            conf.check_cc(lib='curses', uselib_store="CURSES")

    conf.check_cfg(package='glib-2.0', uselib_store='GLIB',
        atleast_version='2.10.0', args='--cflags --libs')

def build(bld):
    bld.recurse('src')



