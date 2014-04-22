beep:
	halt A
	halt B
	forward A
	backward B
	sound B.2,(50,100)
	pause 1000
	goto beep2
beep2:
	halt A
	halt B
	backward A
	forward B
	sound B.2,(100,50,50,100)
	pause 1000
	goto beep