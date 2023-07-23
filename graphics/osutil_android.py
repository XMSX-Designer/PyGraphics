from jnius import autoclass

class Display:
    """
    A class representing display information for Android devices and providing a static method to get the screen size.

    Methods:
        get_size(): Get the screen size as a tuple (width, height) in pixels.
    """

    InputMethodManager = autoclass("android.view.inputmethod.InputMethodManager")
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    Context = autoclass("android.content.Context")
    activity = PythonActivity.mActivity

    @staticmethod
    def get_size():
        """
        Get the screen size using JNI (Java Native Interface) to interact with Android methods.

        Returns:
            tuple: A tuple containing the screen width and height in pixels.
        """
        rootView = Display.activity.getWindow().getDecorView()
        rect = autoclass('android.graphics.Rect')()
        rootView.getWindowVisibleDisplayFrame(rect)
        return rect.right, rect.bottom - rect.top
