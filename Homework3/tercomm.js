#!/usr/bin/env node

var b = require('bonescript')
var spawn = require('child_process').spawn,
	//ls = spawn('ls',['-lh','/usr']);
	ls = spawn('./readTMP101.sh');

ls.stdout.on('data', function (data){
	console.log('\n' + data); //Returns the command
});

ls.stderr.on('data', function(data){
	console.log('Error!:' + data); //Error with the command
});

ls.on('close', function(code){
	console.log('Exited with code ' + code); //When command exists
});
