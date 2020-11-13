import ui
import bSettings
import bMore
import bPlay

#Button actions
def play(Sender):
	bPlay.vp.present()
	bPlay.location_start()
def more(sender):
	bMore.vm.present()
def setting(sender):
	bSettings.vs.present()
	
#Settings
	


#Main View
v = ui.load_view()
v.present()
#intro()