blendimg
=====

Blend two grayscale images by converging alpha channel

### Requirements
* python3
* PIL

### Usage
```blendimg.py 31451163_p0.jpg 18455721_p0.jpg out.png -d 80```

```
usage: blendimg.py [-h] [-b BRIGHT_LUM] [-d DARK_LUM] bright dark output

positional arguments:
  bright         Image to use as bright/front layer.
  dark           Image to use as dark/back layer.
  output         Filename for output.

options:
  -h, --help     show this help message and exit
  -b BRIGHT_LUM  Increase the brightness of bright/front layer. Negative value accepted.
  -d DARK_LUM    Decrease the brightness of dark/back layer. Negative value accepted.
```

### Screenshots

![Screenshot](https://raw.githubusercontent.com/llyyr/blendimg/master/out.png)

### Sources
* https://pixiv.net/i/31451163
* https://pixiv.net/i/18455721
