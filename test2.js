#!/usr/bin/env node

var toby = require('bonescript');

// Declaring LED variables
var LED1 = 'P9_11'; // WORKS!
var LED2 = 'P9_13'; // WORKS!
var LED3 = 'P9_15'; //WORKS!
var LED4 = 'P9_17';

// Declaring Button variables
var button1 = 'P9_23'; //WORKS!
var button2 = 'P9_24'; //WORKS!
var button3 = 'P9_27'; //WORKS!
var button4 = 'P9_30';

// Setting pinout
// Buttons
toby.pinMode(button1, toby.INPUT, 7, 'pulldown');
toby.pinMode(button2, toby.INPUT, 7, 'pulldown');
toby.pinMode(button3, toby.INPUT, 7, 'pulldown');
toby.pinMode(button4, toby.INPUT, 7, 'pulldown');

//LEDs
toby.pinMode(LED1, toby.OUTPUT);
toby.pinMode(LED2, toby.OUTPUT);
toby.pinMode(LED3, toby.OUTPUT);
toby.pinMode(LED4, toby.OUTPUT);

// Defining interrupts
toby.attachInterrupt(button1, true, toby.CHANGE, blink1);
toby.attachInterrupt(button2, true, toby.CHANGE, blink2);
toby.attachInterrupt(button3, true, toby.CHANGE, blink3);
toby.attachInterrupt(button4, true, toby.CHANGE, blink4);

function blink1(x){
	if(+x.value===1){
		toby.digitalWrite(LED1,toby.HIGH);
	}else{
		toby.digitalWrite(LED1,toby.LOW);
	}
}

function blink2(y){
	if(+y.value===1){
		toby.digitalWrite(LED2, toby.HIGH);
	}else{
		toby.digitalWrite(LED2, toby.LOW);
	}
}

function blink3(z){
	if(+z.value===1){
		toby.digitalWrite(LED3, toby.HIGH);
	}else{
		toby.digitalWrite(LED3, toby.LOW);
	}
}

function blink4(a){
	if(+a.value===1){
		toby.digitalWrite(LED4, toby.HIGH);
	}else{
		toby.digitalWrite(LED4, toby.LOW);
	}
}
