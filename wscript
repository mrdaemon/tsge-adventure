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

    # Register command line options
    buildopt = opt.add_option_group("Project build options")

    buildopt.add_option('--with-pdcurses-dir', action="store", default=False,
            help="Use pdcurses and specify where it is unpacked." \
            "(Mostly useful for Win32 and cross-compilation)")

    crossopt = opt.add_option_group("Cross Compile and Win32 Options")

    crossopt.add_option('--cross-compile-win32', action="store_true",
            default=False, help="Enable cross compilation for win32 x86")

def configure(conf):
    # Cross compilation helper
    if conf.options.cross_compile_win32:
        conf.env['DEST_OS'] = "win32"

    conf.load('compiler_c')
    conf.load('vala')

    # OS X Specific check, compilations flags
    # are nearly always wrong unless 'c_osx' is loaded.
    if sys.platform == 'darwin':
        print("Configuring for Mac OS X")
        conf.load('c_osx')

        # Explicitely load the darwin gcc modifier,
        # to work around what seems to be a bug in waf.
        from waflib.Tools import gcc
        gcc.gcc_modifier_darwin(conf)
    else:
        conf.load('c_config')

    # Use extra pdcurses directory? (mostly useful on windows
    # and for cross compiling, where it might be outside normal paths.
    if conf.options.with_pdcurses_dir:
        conf.env.append_unique('INCLUDES', conf.options.with_pdcurses_dir)
        conf.env.append_unique('LIBPATH', conf.options.with_pdcurses_dir)

    # Check for curses support
    conf.check(features="c", header_name='curses.h', mandatory=True)

    # only use pdcurses if asked to, try ncurses, and fail back to
    # plain old system curses (which is often ncurses in disguise
    # anyways)
    if conf.options.with_pdcurses_dir:
        conf.check_cc(lib='pdcurses', uselib_store="CURSES")
    else:
        try:
            conf.check_cc(lib='ncurses', uselib_store="CURSES")
        except conf.errors.ConfigurationError:
            conf.check_cc(lib='curses', uselib_store="CURSES")

    # This depencency is implicit since the vala tools
    # check for GObject, which depends on glibc.
    # But I might wish to check for a specific version eventually.
    conf.check_cfg(package='glib-2.0', uselib_store='GLIB',
        atleast_version='2.10.0', args='--cflags --libs')

def build(bld):
    bld.recurse('src')

