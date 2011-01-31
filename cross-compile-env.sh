#!/bin/bash
# Alexandre Gauthier - 2011-2012
# Cross compile convenience script.
# If it doesn't work, just hack it.
# Mostly made for myself :)

if [ -z $TSGE_CROSS ] ; then
	if [ -d ./mingw32-env ] ; then
		export TSGE_CROSS=$(dirname $(readlink -f $0))/mingw32-env
		echo "Found cross compile root in $TSGE_CROSS"
	else
		echo "Can't find 'mingw32-env'. If you have it somewhere else,"
		echo "Please export the TSGE_CROSS environment variable."
		echo "It should point to your mingw32 cross compile root, which"
		echo "should contain directores like 'sys-win32' and 'pdcurses-win32.'"
		echo "Example:"
		echo '  $ export TSGE_CROSS=/home/bob/mingw32-env'
		exit 1
	fi
fi

if [ -z $TSGE_CROSS_PREFIX ] ; then
	export TSGE_CROSS_PREFIX=i586-mingw32msvc-
	echo "Note: You can export TSGE_CROSS_PREFIX to set your toolchain"
	echo "prefix. The default value is \"${TSGE_CROSS_PREFIX}\"."
fi

# note: I am pretty sure waf ignores some of these, but the documentation
# is... lacking. Better safe than sorry. Unless you source this script,
# it's not going to pollute your environment anyways.
export MINGW_ROOT=$TSGE_CROSS/sys-win32
export PDCURSES_ROOT=$TSGE_CROSS/pdcurses-win32
export PKG_CONFIG_SYSROOT_DIR=$MINGW_ROOT
export PKG_CONFIG_PATH=$MINGW_ROOT/lib/pkgconfig
export AR=${TSGE_CROSS_PREFIX}ar
export RANLIB=${TSGE_CROSS_PREFIX}ranlib
export CC=${TSGE_CROSS_PREFIX}gcc
export CPP=${TSGE_CROSS_PREFIX}g++
export CXX=${TSGE_CROSS_PREFIX}g++
export LINK_CC=${TSGE_CROSS_PREFIX}gcc
export LINK_CXX=${TSGE_CROSS_PREFIX}g++

./configure --cross-compile-win32 --with-pdcurses-dir=$PDCURSES_ROOT

