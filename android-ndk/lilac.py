#!/usr/bin/env python3

from lilaclib import *

depends = ["ncurses5-compat-libs"]
build_prefix = 'extra-x86_64'
post_build = aur_post_build
pre_build = aur_pre_build

if __name__ == '__main__':
  single_main(build_prefix)
