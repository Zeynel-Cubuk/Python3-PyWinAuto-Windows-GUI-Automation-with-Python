import time
import warnings
from pywinauto import Application

warnings.simplefilter("ignore")

#path = r"C:\Users\Red\AppData\Roaming\Spotify\Spotify.exe"
path = "notepad.exe"
app = Application(backend="uia").start(cmd_line=path).connect(title="Adsız - Not Defteri",timeout=20)
time.sleep(2)
#app.AdsızNotDefteri.print_control_identifiers()

textEditor = app.AdsızNotDefteri.child_window(auto_id="15", control_type="Edit").wrapper_object()
textEditor.type_keys("Test!!")
folder = app.AdsızNotDefteri.child_window(title="Dosya", control_type="MenuItem").wrapper_object()
folder.click_input()
#app.AdsızNotDefteri.print_control_identifiers()

time.sleep(2)

save = app.AdsızNotDefteri.child_window(title="Kaydet	Ctrl+S", auto_id="3", control_type="MenuItem").wrapper_object()
save.click_input()
#app.AdsızNotDefteri.print_control_identifiers()

time.sleep(2)

filename = app.AdsızNotDefteri.child_window(title="Dosya adı:", auto_id="1001", control_type="Edit").wrapper_object()
filename.type_keys("test.txt")
#app.AdsızNotDefteri.print_control_identifiers()

time.sleep(2)

saveBtn = app.AdsızNotDefteri.child_window(title="Kaydet", auto_id="1", control_type="Button").wrapper_object()
saveBtn.click_input()

time.sleep(2)



