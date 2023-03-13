# YouTube Audio Downloader and Converter
## A fully functional personal project to extract audio of any YouTube video with a music-oriented usage.

In order for the code to work, you'll need to follow the insctructions below.

## 1. Install the following libraries with pip
* pytube 12.1.2
* numpy 1.24.2
* lameenc 1.4.2
* moviepy 1.0.3

## 2. Fixing moviepy error
1. Localize moviepy root folder, then enter to 'audio/fx/all' and open the '__ init __.py' file
2. Comment the code except for the import, then add the following imports:

* import moviepy.audio.fx as fx

* import moviepy.audio.fx as fx

* from moviepy.audio.fx.audio_fadein import audio_fadein

* from moviepy.audio.fx.audio_fadeout import audio_fadeout

* from moviepy.audio.fx.audio_left_right import audio_left_right

* from moviepy.audio.fx.audio_loop import audio_loop

* from moviepy.audio.fx.audio_normalize import audio_normalize

* from moviepy.audio.fx.volumex import volumex

<img src="https://cdn.discordapp.com/attachments/440939498738548737/1084858226618671114/image.png">

3. Then do the same but with video: 'video/fx/all', open the '__ init __.py', comment the code and add the following imports:

* import moviepy.video.fx as fx

* from moviepy.video.fx.accel_decel import accel_decel

* from moviepy.video.fx.blackwhite import blackwhite

* from moviepy.video.fx.blink import blink

* from moviepy.video.fx.colorx import colorx

* from moviepy.video.fx.crop import crop

* from moviepy.video.fx.even_size import even_size

* from moviepy.video.fx.fadein import fadein

* from moviepy.video.fx.fadeout import fadeout

* from moviepy.video.fx.freeze import freeze

* from moviepy.video.fx.freeze_region import freeze_region

* from moviepy.video.fx.gamma_corr import gamma_corr

* from moviepy.video.fx.headblur import headblur

* from moviepy.video.fx.invert_colors import invert_colors

* from moviepy.video.fx.loop import loop

* from moviepy.video.fx.lum_contrast import lum_contrast

* from moviepy.video.fx.make_loopable import make_loopable

* from moviepy.video.fx.margin import margin

* from moviepy.video.fx.mask_and import mask_and

* from moviepy.video.fx.mask_color import mask_color

* from moviepy.video.fx.mask_or import mask_or

* from moviepy.video.fx.mirror_x import mirror_x

* from moviepy.video.fx.mirror_y import mirror_y

* from moviepy.video.fx.painting import painting

* from moviepy.video.fx.resize import resize

* from moviepy.video.fx.rotate import rotate

* from moviepy.video.fx.scroll import scroll

* from moviepy.video.fx.speedx import speedx

* from moviepy.video.fx.supersample import supersample

* from moviepy.video.fx.time_mirror import time_mirror

* from moviepy.video.fx.time_symmetrize import time_symmetrize
