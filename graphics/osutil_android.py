
from jnius import autoclass

    
class display:
    InputMethodManager = autoclass("android.view.inputmethod.InputMethodManager")
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    Context = autoclass("android.content.Context")
    activity = PythonActivity.mActivity
    
    @staticmethod
    def getsize():
        rootView = display.activity.getWindow().getDecorView()
        rect=autoclass('android.graphics.Rect')()
        rootView.getWindowVisibleDisplayFrame(rect)
        return rect.right,rect.bottom-rect.top
        