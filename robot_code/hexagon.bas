symbol counter = b1

main:
	; Set Motor Speed Low
	output C.5 
	
	doStuff:
	for counter = 1 to 7
		
		gosub driveAndTurn
		
	next counter
	
	end


	
driveAndTurn:
	; Drive forward
	forward A
	forward B
	pause 2000
	
	; Turn right
	halt A
	halt B
	forward A
	pause 750
	halt A
	
	return