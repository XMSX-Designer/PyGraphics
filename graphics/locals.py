import platform as _p

PLATFORM=_p.system()

if PLATFORM in ["Linux","Linux2"]:
    import graphics.osutil_android
    OSUTIL=graphics.osutil_android
    print("this sofware does not support linux, only android")
elif PLATFORM in ["Windows"]:
    import graphics.osutil_windows
    OSUTIL=graphics.osutil_windows
    
else:
    OSUTIL=None

WINDOW_SIZE=OSUTIL.display.getsize()

MOVIE_NO_AUDIO="no-audio"
MOVIE_ALLOW_AUDIO="allow-audio"
MOVIE_HIGH_DEF="hd"
MOVIE_STANDARD_DEF="sd"
MOVIE_LOW_DEF="ld"
class backends:
    PYGAME="pygame"
    PIL="pil"
    CV2="cv2"
