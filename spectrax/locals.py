import platform as _p

# Determine the platform the code is running on (Linux, Windows, etc.)
PLATFORM = _p.system()

# Initialize the OSUTIL variable based on the platform
if PLATFORM in ["Linux", "Linux2"]:
    import spectrax.osutil_android
    OSUTIL = spectrax.osutil_android
    print("This software does not support Linux, only Android.")
elif PLATFORM in ["Windows"]:
    import spectrax.osutil_windows
    OSUTIL = spectrax.osutil_windows
else:
    OSUTIL = None

# Get the window size from the OSUTIL (if available)
if OSUTIL:
    WINDOW_SIZE = OSUTIL.display.getsize()
else:
    WINDOW_SIZE = None

# Define constants for movie options
MOVIE_NO_AUDIO = "no-audio"
MOVIE_ALLOW_AUDIO = "allow-audio"
MOVIE_HIGH_DEF = "hd"
MOVIE_STANDARD_DEF = "sd"
MOVIE_LOW_DEF = "ld"

# Define constants for supported graphics backends
class Backends:
    """
    Constants representing supported graphics backends.

    Attributes:
        PYGAME (str): Pygame backend.
        PIL (str): PIL (Pillow) backend.
        CV2 (str): OpenCV backend.
    """
    PYGAME = "pygame"
    PIL = "pil"
    CV2 = "cv2"
