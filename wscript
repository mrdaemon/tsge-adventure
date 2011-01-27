#!/usr/bin/env python

#import Options

NAME = "The Shittiest Game Ever - Adventure"
APPNAME = "tsge"
COPYRIGHT = "Copyright \xc2\xa9 2011-2012 Alexandre Gauthier"

VERSION = "0.1.0"
VERSION_MAJOR_MINOR =  ".".join(VERSION.split(".")[0:2])

top = '.'
out = 'build'

def options(opt):
    opt.tool_options('compiler_cc')
    opt.tool_options('gnu_dirs')

   #opt.add_option('--with-ncurses',
   #    help = "Instruct linker to link against ncurses instead of curses",
   #    action = 'store_true',
   #    default = False)


def configure(conf):
    conf.check_tool('compiler_cc vala gnu_dirs')

    conf.check_cfg(package='glib-2.0', uselib_store='GLIB',
            atleast_version='2.14.0', mandatory=True, args='--cflags --libs')
    conf.check_cfg(package='gobject-2.0', uselib_store='GOBJECT',
            atleast_version='2.14.0', mandatory=True, args='--cflags --libs')

    #conf.check_vala_deps()

    # Check for curses/ncurses library
    #CURSES_LIB = "ncurses" if Options.options.with_ncurses else "curses"

    conf.check_cc(header_name = 'curses.h', lib="curses",
        uselib_store='CURSES', msg = "Checking for (n)curses",
        mandatory = True)


    conf.define('PACKAGE', APPNAME)
    conf.define('PACKAGE_NAME', APPNAME)
    conf.define('PACKAGE_STRING', APPNAME + '-' + VERSION)
    conf.define('PACKAGE_VERSION', APPNAME + '-' + VERSION)

    conf.define('VERSION', VERSION)
    conf.define('VERSION_MAJOR_MINOR', VERSION_MAJOR_MINOR)


def build(bld):
    bld.add_subdirs('src')

