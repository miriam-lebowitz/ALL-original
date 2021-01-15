// This code converts the message text from txt files to strings, allowing them to easily be placed into trial objects within the sequence

// Variables that store strings containing messages
var activecompmessage11;
var activecompmessage1bcd;
var activecompmessage2;
var activecompmessage3;
var activeprodmessage;
var activeprodmessage1;
var activeprodmessage2;
var endmessagec;
var endmessagep;
var forcedchoicemessage2pic;
var forcedchoicemessage4pic;
var grammaticalityjudgment;
var openingmessagec;
var openingmessagep;
var passivemessage;
var passivemessage1;
var passivemessage2;
var prodtest1;
var prodtest2;
var prodtestmessage;
var vocabtestmessage1;
var vocabtestmessage2;

// Makes ajax calls for each individual text file
// If message files and names are changed, they will need to have their ajax calls edited/added here 
function processMessages() {
	 
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/activecompmessage11.txt",
		dataType : "text",
		success : function(data) {
			activecompmessage11 = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/activecompmessage1bcd.txt",
		dataType : "text",
		success : function(data) {
			activecompmessage1bcd = data;
			
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/activecompmessage2.txt",
		dataType : "text",
		success : function(data) {
			activecompmessage2 = data;
	
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/activecompmessage3.txt",
		dataType : "text",
		success : function(data) {
			activecompmessage3 = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/activeprodmessage.txt",
		dataType : "text",
		success : function(data) {
			activeprodmessage = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/activeprodmessage1.txt",
		dataType : "text",
		success : function(data) {
			activeprodmessage1 = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/activeprodmessage2.txt",
		dataType : "text",
		success : function(data) {
			activeprodmessage2 = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/endmessagec.txt",
		dataType : "text",
		success : function(data) {
			endmessagec = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/endmessagep.txt",
		dataType : "text",
		success : function(data) {
			endmessagep = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/forcedchoicemessage2pic.txt",
		dataType : "text",
		success : function(data) {
			forcedchoicemessage2pic = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/forcedchoicemessage4pic.txt",
		dataType : "text",
		success : function(data) {
			forcedchoicemessage4pic = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/grammaticalityjudgment.txt",
		dataType : "text",
		success : function(data) {
			grammaticalityjudgment = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/openingmessagec.txt",
		dataType : "text",
		success : function(data) {
			openingmessagec = data;
			console.log(openingmessagec);
		}
	});
	
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/openingmessagep.txt",
		dataType : "text",
		success : function(data) {
			openingmessagep = data;
		}
	});$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/passivemessage.txt",
		dataType : "text",
		success : function(data) {
			passivemessage = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/passivemessage1.txt",
		dataType : "text",
		success : function(data) {
			passivemessage1 = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/passivemessage2.txt",
		dataType : "text",
		success : function(data) {
			passivemessage2 = data;
		}
	});
	
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/prodtest1.txt",
		dataType : "text",
		success : function(data) {
			prodtest1 = data;
		}
	});$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/prodtest2.txt",
		dataType : "text",
		success : function(data) {
			prodtest2 = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/prodtestmessage.txt",
		dataType : "text",
		success : function(data) {
			prodtestmessage = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/vocabtestmessage1.txt",
		dataType : "text",
		success : function(data) {
			vocabtestmessage1 = data;
		}
	});
	$.ajax({
		type : "GET",
		url : "/static/elise/Instructions/vocabtestmessage2.txt",
		dataType : "text",
		success : function(data) {
			vocabtestmessage2 = data;
			
		}
	});
	
	}
	
	
	
	