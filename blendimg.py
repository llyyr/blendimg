#!/usr/bin/env python3.10
import argparse
from PIL import Image

p = argparse.ArgumentParser()
p.add_argument('bright', type=str, help='Image to use as bright/front layer.')
p.add_argument('dark', type=str, help='Image to use as dark/back layer.')
p.add_argument('output', type=str, help='Filename for output.')
p.add_argument('-b', dest='BRIGHT_LUM', type=int, default=0,
                    help='Increase the brightness of bright/front layer.\
                            Negative value accepted.')
p.add_argument('-d', dest='DARK_LUM', type=int, default=0,
                    help='Decrease the brightness of dark/back layer.\
                            Negative value accepted.')

def converge(c1, c2):
    c1 = max(0, c1 - args.DARK_LUM)
    c2 = min(c2 + args.BRIGHT_LUM, 255)
    A = min(255 + c1 - c2, 255)
    C = round(255 * c1 / A) if A != 0 else 0
    return C, A

if __name__ == '__main__':
    args = p.parse_args()

    bright = Image.open(args.bright, 'r').convert('LA').split()[0]
    dark = Image.open(args.dark, 'r').convert('LA').split()[0]
    assert dark.size == bright.size, 'Images have different dimensions'

    out = Image.new('LA', dark.size)
    out.putdata(list(map(converge, dark.getdata(), bright.getdata())))
    out.save(args.output, 'PNG')
