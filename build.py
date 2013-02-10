#!/usr/bin/env python

import glob
import time


def readfile(fn):
  with open(fn, 'Ur') as f:
    return f.read()


def build():
  c = '\n\n'.join(map(readfile, glob.glob('code/*')))
  n = time.strftime('%Y-%m-%d-%H%M%S')
  m = readfile('main.js').replace('@@BUILDDATE@@', n)
  m = m.split('@@INJECTHERE@@')
  m.insert(1, c)
  t = '\n\n'.join(m)

  with open('total-conversion-build.user.js', 'w') as f:
    f.write(t)

if __name__ == "__main__":
  build()

# vim: ai si ts=4 sw=4 sts=4 et
