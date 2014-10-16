#!/usr/bin/env node

var b = require('bonescript');

// Declaring variables
var OUTA = 'P9_37'; //analog in
var OUTB = 'P9_39'; //analog in

//while(0<10){
	// Setting pinout
	b.analogRead(OUTA, printStatusA);
	b.analogRead(OUTB, printStatusB);

//while(1===1){
	function printStatusA(x){
		console.log('x.value = ' + x.value);
		console.log('x.err = ' + x.err);
	}

	function printStatusB(y){
		console.log('y.value = ' + y.value);
		console.log('y.err = ' + y.err);
	}
//}
