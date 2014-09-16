#!/usr/bin/env node
var b = require('bonescript');
///////////////////////////////////////////
// Declaring variables
//////////////////////////////////////////

var rowSize = 8;
var colSize = 8;
var panel = new Array(8);
var curr_row = 4;
var curr_col = 4;
var rows, cols;
var up = 'P9_23';
var down = 'P9_24';
var left = 'P9_27';
var right = 'P9_30';
var clear = 'P9_21';

// Setting up a second direction for the array
for(rows = 0; rows < 8; rows++){
	panel[rows] = new Array(8);
}

/////////////////////////////////////////
// Setting pinout / inputs
////////////////////////////////////////

b.pinMode(up, b.INPUT, 7, 'pulldown');
b.pinMode(down, b.INPUT, 7, 'pulldown');
b.pinMode(left, b.INPUT, 7, 'pulldown');
b.pinMode(right, b.INPUT, 7, 'pulldown');
b.pinMode(clear, b.INPUT, 7, 'pulldown');

/////////////////////////////////////////
// Defining interrupts
////////////////////////////////////////
b.attachInterrupt(up, true, b.CHANGE, sketchUp);
b.attachInterrupt(down, true, b.CHANGE, sketchDown);
b.attachInterrupt(left, true, b.CHANGE, sketchLeft);
b.attachInterrupt(right, true, b.CHANGE, sketchRight);
b.attachInterrupt(clear, true, b.CHANGE, clearSketch);

///////////////////////////////////////
// Clearing game array
//////////////////////////////////////
for(rows=0;rows<rowSize;rows++){
	for(cols=0;cols<colSize;cols++){
		panel[rows][cols] = ' '; // use o for testing
	}
}

///////////////////////////////////////
// The game itself
//////////////////////////////////////

for (rows = 0; rows < 8; rows++){
	console.log(panel[rows].toString());
}
console.log('\n');

// Sketch Up Function
function sketchUp(w){
	if(w.value===1){
		if(curr_row<=0){
			curr_row = 0;
			panel[curr_row][curr_col] = 'x';
		}else{
			curr_row--;
			panel[curr_row][curr_col] = 'x';
		}
		for(rows = 0; rows < 8; rows++){
			console.log(panel[rows].toString());
		}
		console.log('\n');
	}
}

// Sketch Left Function
function sketchLeft(a){
	if(a.value===1){
		if(curr_col<=0){
			curr_col = 0;
			panel[curr_row][curr_col] = 'x';
		}else{
			curr_col--;
			panel[curr_row][curr_col] = 'x';
		}
		for(rows = 0; rows < 8; rows++){
			console.log(panel[rows].toString());
		}
		console.log('\n');
	}
}

// Sketch Down Function
function sketchDown(s){
	if(s.value===1){
		if(curr_row>=7){
			curr_row = 7;
			panel[curr_row][curr_col] = 'x';
		}else{
			curr_row++;
			panel[curr_row][curr_col] = 'x';
		}
		for(rows = 0; rows < 8; rows++){
			console.log(panel[rows].toString());
		}
		console.log('\n');
	}
}

// Sketch Right Function
function sketchRight(d){
	if(d.value===1){
		if(curr_col>=7){
			curr_col = 7;
			panel[curr_row][curr_col] = 'x';
		}else{
			curr_col++;
			panel[curr_row][curr_col] = 'x';
		}
		for(rows = 0; rows < 8; rows++){
			console.log(panel[rows].toString());
		}
		console.log('\n');
	}
}

function clearSketch(c){
	if(c.value===1){
		for(rows = 0; rows < rowSize; rows++){
			for(cols = 0; cols < colSize; cols++){
				panel[rows][cols] = ' ';
			}
		}
		for(rows = 0; rows < 8; rows++){
			console.log(panel[rows].toString());
		}
		console.log('\n');
	}
}


