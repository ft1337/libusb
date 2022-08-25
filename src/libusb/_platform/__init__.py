# Copyright (c) 2016-2022 Adam Karpierz
# Licensed under the zlib/libpng License
# https://opensource.org/licenses/Zlib

import sys
import os
import platform

is_windows = (bool(platform.win32_ver()[0])
              or (sys.platform in ("win32", "cygwin"))
              or (sys.platform == "cli" and os.name in ("nt", "ce"))
              or (os.name == "java"
                  and "windows" in platform.java_ver()[3][0].lower()))
is_linux   = sys.platform.startswith("linux")
is_macos   = (sys.platform == "darwin")
is_android = False
is_posix   = (os.name == "posix")
is_32bit   = (sys.maxsize <= 2**32)

def defined(varname, __getframe=sys._getframe):
    frame = __getframe(1)
    return varname in frame.f_locals or varname in frame.f_globals

del sys, os, platform

if is_windows:
    from ._windows import DLL_PATH, DLL, dlclose, CFUNC
    from ._windows import timeval
elif is_linux:
    from ._linux   import DLL_PATH, DLL, dlclose, CFUNC
    from ._linux   import timeval
elif is_macos:
    from ._macos   import DLL_PATH, DLL, dlclose, CFUNC
    from ._macos   import timeval
else:
    raise ImportError("unsupported platform")
