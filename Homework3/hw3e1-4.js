#!/usr/bin/env node
var b = require('bonescript');

var spawn = require('child_process').spawn,
	setTMP101 = spawn('./setTMP101-1.sh');

var alert1 = 'P9_11';
var alert2 = 'P9_15';

b.pinMode(alert1, b.INPUT, 7, 'pulldown');
b.pinMode(alert2, b.INPUT, 7, 'pulldown');

b.attachInterrupt(alert1, true, b.CHANGE, printTemp1);
b.attachInterrupt(alert2, true, b.CHANGE, printTemp2);

///////////////////////////////////////////////////////////////////
// Setting TMP101-1 and TMP101-2 registers
///////////////////////////////////////////////////////////////////

setTMP101.stdout.on('data', function(data){
	console.log('Setting T-High and T-Low: ' + data);
});

setTMP101.stderr.on('data', function(data){
	console.log('Error: ' + data);
});

setTMP101.on('close', function(code){
	console.log('Process exited with code: ' + code);
});

///////////////////////////////////////////////////////////////////
// Alert Interruptions
//////////////////////////////////////////////////////////////////

function printTemp1(x){
	if(x.value===1){
		getTMP101_1 = spawn('./getTemp1.sh');
		
		getTMP101_1.stdout.on('data', function(data){
			//console.log('The temperature in TMP101-1 is: ' + data);
			console.log(' ' + data);
		});

		getTMP101_1.stderr.on('data', function(data){
			console.log('Error: ' + data);
		});

		getTMP101_1.on('close', function(code){
			console.log('Process exited with code: ' + code);
		});
	}
	//console.log('Int error: ' + x.err);
	//console.log(x.value);
}

function printTemp2(y){
	if(y.value===1){
		getTMP101_2 = spawn('./getTemp2.sh');

        	getTMP101_2.stdout.on('data', function(data){
                	//console.log('The temperature in TMP101-1 is: ' + data);
			console.log(' ' + data);
        	});     
        
        	getTMP101_2.stderr.on('data', function(data){
                	console.log('Error: ' + data);
        	});     
        
        	getTMP101_2.on('close', function(code){
                	console.log('Process exited with code: ' + code);
        	});
	}     
	//console.log('Int error: ' + y.err);
	//console.log(y.value);
}
