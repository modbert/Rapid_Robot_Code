main:
	forward A ; go forwards
	forward B
	; test bumpers
	; to see if hit
	if pinC.3 = 1 then doRight
	if pinC.1 = 1 then doLeft
	goto main
	
doLeft:
	gosub goBack
	forward A ; turn for 0.32s
	backward B
	pause 320
	goto main
	
doRight:
	gosub goBack
	backward A ; turn for 0.32s
	forward B
	pause 320
	goto main
	
goBack:
	backward A ; reverse for 0.5s
	backward B
	pause 500
	
	forward B
	'IndianaJones
	tune B.2, 3,($C4,$7C,$75,$77,$7C,$C0,$7C,$32,$7C,$74,$B5,$3C,$37,$7C,$79,$7B,$7C,$C5,$3C,$39,$7C,$7B,$C0,$C2,$C4);,$34);,$7C,$75);,$77,$7C,$80,$3C,$02,$7C,$44,$85,$37,$7C,$77,$04,$7C,$02,$7C,$77,$04,$7C,$02,$7C,$77,$05,$7C,$04,$7C,$42,$80)

	let w0 = timer ; seed w0 with timer value   
	random w0 ; put random value into w0 
	let w1 = w0 / 10
	pause w1
	return