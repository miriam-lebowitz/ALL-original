
// Fisher-Yates shuffle algorithm https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
function shuffle(array) {
	var m = array.length, t, i;

	// While there remain elements to shuffle…
	while (m) {

		// Pick a remaining element…
		i = Math.floor(Math.random() * m--);

		// And swap it with the current element.
		t = array[m];
		array[m] = array[i];
		array[i] = t;
	}

	return array;
}

// Global for storing experiment sequence that is produced after reading in the experiment sequence
var trialData = " ";

// Takes info from CSV file and obtains experiment sequence that is encoded and returned as a 2D list
function processData(allText) {

	// Regex to split CSV format into 2D matrix 
	var allTextLines = allText.split(/\r\n|\n/);

	// Headers for each column that are stored as the first row in the matrix
	var headers = allTextLines[0].split(',');

	// Removes any blank headers 
	while (headers[headers.length - 1] == "") {
		headers.pop();
	}

	// Stores experiment lines 
	var lines = [];

	// Iterates through rows, each of which stores a list of experiment codes
	for (var i = 0; i < allTextLines.length; i++) {

		// splits comma separated experiment codes for current row
		var data = allTextLines[i].split(',');

		// Removes empty columns
		while (data[data.length - 1] == "") {
			data.pop();
		}

		// Checks to see that removing empty columns did not lead to an uneven row length. If this happens,
		// the CSV file is not properly formatted
		if (data.length == headers.length) {

			// Array storing the specific experiment codes from each string 
			var tarr = [];

			// Iterates through the experiment sequence for the current row
			for (var j = 0; j < data.length; j++) {

				// The experiment codes are stored in the format 'experimentnumberplurality' i.e. 12s means the 12th 
				// monster singular will be the stimulus
				var curr = data[j]

				// Pushes a tuple storing the monster number and plurality by splitting the string 
				tarr.push([curr.substring(0, curr.length - 1), curr.substring(curr.length - 1)]);
			}

			// Pushes to matrix
			lines.push(tarr);
		}
	}

	// Sets trialData global to the matrix generated by the method
	trialData = lines;
}

// Given an image number, outputs a string with the file name for that image
function imageFileName(imageNumber) {

	// Small images
	if (imageNumber < 12) {
		return "l" + (imageNumber + 1) + ".png";
	}

	// Large images
	else {
		return "h" + (imageNumber - 12 + 1) + ".png";
	}
}

function getPrompt(sound) {
	var underscorePrompt = soundToPrompt[sound];
	var prompt = underscorePrompt.replace("_", " ");
	return prompt;
}

// Given the determiner number, a boolean with true-> small, false-> big, a monster number and a boolean 
// with true->singular false->plural, outputs the file name for the associated sound file
function soundFileName(determiner, isSmall, monsterNumber, isSingular) {

	// Encodes determiner number
	var det = "det" + determiner + "_";
	var size;

	// Encodes size based on boolean value
	if (isSmall) {
		size = "small";
	}
	else {
		size = "big";
		monsterNumber = monsterNumber - 12;
	}
	var plurality;

	// Encodes plurality based on boolean value
	if (isSingular) {
		plurality = "s";
	}
	else {
		plurality = "p";
	}

	// Concatenates all encodings as they appear in the file name
	return det + size + monsterNumber + plurality + ".wav";
}

// dictionaries for big and small file names
var big = {};
var small = {};

function constructValues() {

	// Shuffles between the 4 determiners and randomly assigns them to the small and big plural and singular forms
	var dets = [1, 2, 3, 4]
	shuffle(dets)
	detSmallSing = dets[0]
	detSmallPlur = dets[1]
	detLargeSing = dets[2]
	detLargePlur = dets[3]

	// Constructs file dictionary for small monsters
	for (var i = 0; i < 12; i++) {
		// Retrieves image file
		var img = imageFileName(i)

		// Retrieves sounds for plural and singular with selected determiner
		var singSound = soundFileName(detSmallSing, true, i, true)
		var plurSound = soundFileName(detSmallPlur, true, i, false)
		// Adds current monster to dictionary in the structure 
		// [image file name, sub-dictionary storing plural sound file with key p and singular sound file with key s, sub-dictionary storing plural prompt string with key p and singular prompt string with key s]
		small[i] = [img, { "p": plurSound, "s": singSound }, { "p": soundToPrompt[plurSound], "s": soundToPrompt[singSound] }]
	}
	// Constructs file dictionary for large monsters
	for (var i = 12; i < 30; i++) {
		// Retrieves image file
		var img = imageFileName(i)

		// Retrieves sounds for plural and singular with selected determiner
		singSound = soundFileName(detLargeSing, false, i, true)
		plurSound = soundFileName(detLargePlur, false, i, false)
		
		// Adds current monster to dictionary in the structure 
		// [image file name, sub-dictionary storing plural sound file with key p and singular sound file with key s, sub-dictionary storing plural prompt string with key p and singular prompt string with key s]
		big[i - 12] = [img, { "p": plurSound, "s": singSound }, { "p": soundToPrompt[plurSound], "s": soundToPrompt[singSound] }]
	}
}



// Global storing the current instruction within the trial
var currentInstructionCounter = 0

// Plays the next instruction in the sequence for the trial
function playNextInstruction() {

	// Stores timeline object for the instruction 
	var instruction;

	// Checks for comp or prod trial, generates the instruction message timeline object for the appropriate trial
	if (comp) {
		if (compMessageSequence[currentInstructionCounter] == null) {
			instruction = {
				// Displays message with no user response
				type: 'image-keyboard-response',
				stimulus: '/static/elise/img/images/blank.png',
				choices: jsPsych.NO_KEYS,
				trial_duration: 0
			}
		}
		else {
			instruction = {
				type: 'instructions',
				pages: ["<div style='white-space: pre-wrap;'>" + compMessageSequence[currentInstructionCounter] + "</div>"]
				,
				show_clickable_nav: true,
				allow_backward:false
			}
		}
	}
	else {
		if (prodMessageSequence[currentInstructionCounter] == null) {
			instruction = {
				type: 'image-keyboard-response',
				stimulus: '/static/elise/img/images/blank.png',
				choices: jsPsych.NO_KEYS,
				trial_duration: 0
			}
		}
		else {
			instruction = {
				type: 'instructions',
				pages: ["<div style='white-space: pre-wrap;'>" + prodMessageSequence[currentInstructionCounter] + "</div>"]
				,
				show_clickable_nav: true,
				allow_backward:false
			}
		}
	}
	// Increments counter so next instruction is selected on the next call
	currentInstructionCounter++;
	return instruction;
}

// Function used to pause the trial when required
function sleep(milliseconds) {
	const date = Date.now();
	let currentDate = null;
	do {
		currentDate = Date.now();
	} while (currentDate - date < milliseconds);
}
// Function for grabbing parameters from URL
function getParamFromURL( name ) {
	name = name.replace(/[\[]/,"\\[").replace(/[\]]/,"\\]");
	var regexS = "[\?&]"+name+"=([^&#]*)";
	var regex = new RegExp( regexS );
	var results = regex.exec( window.location.href );
	if( results == null )
		return "";
	else
		return results[1];
}

// Files storing message sequence globals that will be assigned within the makeExp function. They are assigned within this function because it won't be called until the files have already been processed 
var prodMessageSequence;
var compMessageSequence;


// Generates an experiment timeline 
function makeExp() {
	
	// Sequences for messages. 
	prodMessageSequence = [openingmessagep, overviewmessage, audiocheckmessage1, audiocheckmessage2, audiocheckmessage, audiocheckmessage3, passivemessage1
		, passivemessage, passivemessage2, activeprodmessage1, activeprodmessage, "", activeprodmessage2
		, passivemessage, activeprodmessage, passivemessage, activeprodmessage, audiocheckmessage
		, passivemessage, activeprodmessage, passivemessage, activeprodmessage, passivemessage, activeprodmessage, audiocheckmessage
		, passivemessage, activeprodmessage, passivemessage, activeprodmessage, passivemessage, activeprodmessage, audiocheckmessage
		, passivemessage, activeprodmessage, passivemessage, activeprodmessage, passivemessage, activeprodmessage, audiocheckmessage
		, forcedchoicemessage2pic, audiocheckmessage
		, forcedchoicemessage4pic, audiocheckmessage, , audiocheckmessage, audiocheckmessage, audiocheckmessage
		, grammaticalityjudgment, audiocheckmessage, audiocheckmessage, audiocheckmessage, audiocheckmessage
		, prodtest1, prodtest2, audiocheckmessage, prodtestmessage
		, audiocheckmessage, prodtestmessage, audiocheckmessage, prodtestmessage, audiocheckmessage
		, endmessagep]
	for (var i = 0; i < prodMessageSequence.length; i++) {
		if (prodMessageSequence[i] == ""){
		prodMessageSequence[i] = null;
		}
	}
	compMessageSequence = [openingmessagec, overviewmessage, audiocheckmessage1, audiocheckmessage2, audiocheckmessage, audiocheckmessage3, passivemessage1
		, passivemessage, passivemessage2, activecompmessage1bcd, activecompmessage11, activecompmessage, activecompmessage2
		, passivemessage, activecompmessage, passivemessage, activecompmessage, audiocheckmessage
		, passivemessage, activecompmessage, passivemessage, activecompmessage, passivemessage, activecompmessage, audiocheckmessage
		, passivemessage, activecompmessage, passivemessage, activecompmessage, passivemessage, activecompmessage, audiocheckmessage
		, passivemessage, activecompmessage, passivemessage, activecompmessage, passivemessage, activecompmessage, audiocheckmessage
		, forcedchoicemessage2pic, audiocheckmessage
		, forcedchoicemessage4pic, audiocheckmessage, FC4message, audiocheckmessage, FC4message
		, audiocheckmessage, FC4message, audiocheckmessage
		, grammaticalityjudgment, audiocheckmessage, grammaticalityjudgmentmessage, audiocheckmessage, grammaticalityjudgmentmessage
		, audiocheckmessage, grammaticalityjudgmentmessage, audiocheckmessage
		, prodtest1, prodtest2, audiocheckmessage, prodtestmessage
		, audiocheckmessage, prodtestmessage, audiocheckmessage, prodtestmessage, audiocheckmessage
		, endmessagec]
	for (var i = 1; i < compMessageSequence.length; i++) {
		if (compMessageSequence[i] == ""){
		compMessageSequence[i] = null;
		}
	}
	

	// Obtains value 'cond' from URL which encodes whether the experiment will be production 'p'/NA or comprehension 'c'
	// Obtains value 'subjectnr' from URL
	// example: http://localhost:8000/elise6.html?subjectnr=11111&?cond=c
	// example: https://talk.psych.wisc.edu/test/elise7/?subjectnr=11113&?cond=p
	const queryString = window.location.search;
	const urlParams = new URLSearchParams(queryString);
	cond = getParamFromURL('cond');
	subjectnr =getParamFromURL('subjectnr');
	console.log(subjectnr)
	console.log(cond)
	if (cond == 'c') {
		comp = true;
	} else {
		comp = false;
		cond = 'p'
	}
	console.log(comp)

	// Constructs dictionary of appropriate sound and image files
	constructValues()

	// Obtains big and small values from the dictionary storing their data
	var bigValues = Object.values(big);
	var smallValues = Object.values(small);
	
	// Obtains the specific image and sound files and prompt text for each of the big and small data files
	var bigImages = [];
	for (var i = 0; i < bigValues.length; i++) {
		bigImages.push(bigValues[i][0]);
	}
	var smallImages = [];
	for (var i = 0; i < smallValues.length; i++) {
		smallImages.push(smallValues[i][0]);
	}
	var bigSounds = [];
	for (var i = 0; i < bigValues.length; i++) {
		bigSounds.push(bigValues[i][1]);
	}
	var smallSounds = [];
	for (var i = 0; i < smallValues.length; i++) {
		smallSounds.push(smallValues[i][1]);
	}

	// Shuffles the big and small images and sounds
	shuffle(bigImages);
	shuffle(smallImages);
	shuffle(bigSounds);
	shuffle(smallSounds);
	
	// Concatenates images such that 0-17 are big, 18-29 small
	var allImages = bigImages.concat(smallImages);
	var allSounds = bigSounds.concat(smallSounds);
	
	// Adds participant monster selections to data array
	for(var i = 0; i < 12;i++){
		participant_data_array.push([i,allImages[i],allSounds[i]["s"],allSounds[i]["p"],"big","training"])
	}
	for(var i = 12; i < 18;i++){
		participant_data_array.push([i,allImages[i],allSounds[i]["s"],allSounds[i]["p"],"big","testing"])
	}
	// Adds participant monster selections to data array
	for(var i = 18; i < 24;i++){
		participant_data_array.push([i,allImages[i],allSounds[i]["s"],allSounds[i]["p"],"small","training"])
	}
	for(var i = 24; i < 30;i++){
		participant_data_array.push([i,allImages[i],allSounds[i]["s"],allSounds[i]["p"],"small","testing"])
	}
	console.log(participant_data_array)
	// Shuffles the row sequences in trial data 
	shuffle(trialData);
	console.log(trialData)

	// Stores experiment timeline object
	var experiments = []


	experiments.push(playNextInstruction())
	experiments.push(playNextInstruction())
	experiments.push(playNextInstruction())
	experiments.push(audio_check_trial_1("/static/elise/sound/airplane_w.mp3"))
	experiments.push(playNextInstruction())
	experiments.push(playNextInstruction())
	experiments.push(audio_check_trial_2("/static/elise/sound/candle_w.mp3"))
	experiments.push(playNextInstruction())
	experiments.push(playNextInstruction())
	experiments.push(playNextInstruction())

	// Current row
	curr = trialData[0];
	console.log(curr)
	// Stores experiment block for this row
	block = [];

	// Shuffles the row itself
	shuffle(curr);
	

	//[first 6 passive trials]
	// Iterates through the row, obtaining trial objects
	for (var j = 0; j < curr.length; j++) {

		// Obtains monster number and plurality from the parsed data
		var monsterIndex = parseInt(curr[j][0]);
		var singOrPlural = curr[j][1];
		var isPlural = false;

		if (singOrPlural == 'p'){
			isPlural = true;
		}



		// Calls functions to obtain trial objects and pushes them to the timeline
		// this part of the experiment contains passive comprehension trials
		experiments.push(passive_comprehension_trial("/static/elise/img/images/" + allImages[monsterIndex],
			"/static/elise/sound/combinedsounds/" + allSounds[monsterIndex][singOrPlural], getPrompt(allSounds[monsterIndex][singOrPlural]),isPlural, monsterIndex));

	}

	experiments.push(playNextInstruction())
	experiments.push(playNextInstruction())
	if (comp) {
		experiments.push(active_comprehension_trial("/static/elise/img/images/pear.png", "/static/elise/img/images/apple.png", false, "/static/elise/sound/apple_w.mp3", "apple", false, "-"))
		experiments.push(active_comprehension_trial("/static/elise/img/images/apple.png", "/static/elise/img/images/apple.png", true, "/static/elise/sound/apple_w.mp3", "apple", false, "-"))
	} // if practice trial for production  is desired:
	//else {
		//experiments.push(active_production_trial("/static/elise/img/images/apple.png", "/static/elise/sound/apple_w.mp3", "apple", false, "-"))
	//}
	experiments.push(playNextInstruction())
	experiments.push(playNextInstruction())


	// Current row
	curr = trialData[0];

	// Shuffles the row sequence once again
	shuffle(curr);

	// Creates a list of 3 random indexes to decide which of the active trials will be mismatches
	// These will only be used for active comprehension blocks
	// The third mismatchtrial chosen will be a plurality mismatch instead of a noun mismatch
	var index_list = []
	for (var k = 0; k < 6; k++) {
		index_list.push(k);
	}
	var mismatches = []
	var pluralMismatch = []
	var randind = 0;
	var randchoice = 0;
	randind = (Math.floor(Math.random() * 6))
	randchoice = (index_list.splice(randind, 1)[0])
	mismatches.push(randchoice);
	randind = (Math.floor(Math.random() * 5))
	randchoice = (index_list.splice(randind, 1)[0])
	mismatches.push(randchoice);
	randind = (Math.floor(Math.random() * 4))
	randchoice = (index_list.splice(randind, 1)[0])
	pluralMismatch.push(randchoice);
	mismatches = new Set(mismatches);
	pluralMismatch = new Set(pluralMismatch);
	// Comprehension trial
	if (comp) {

		// Same process as passive trial but generates active comprehension trial 
		for (var j = 0; j < curr.length; j++) {
			var monsterIndex = parseInt(curr[j][0]);
			var singOrPlural = curr[j][1];
			var isPlural = false;
			var firstImage = allImages[monsterIndex];
			var secondImage = allImages[monsterIndex];
			var correct = true;

			// If target audio is plural, set images as plural
			if (singOrPlural == 'p'){
				isPlural = true;
				firstImage = firstImage.substring(0,firstImage.length-4)+"p.png";
				secondImage = secondImage.substring(0,secondImage.length-4)+"p.png";
			}

			// This is where a mismatched image will be chosen for 3 random indices 
			// It's chosen 0-11 if that's what the monster itself is (big neighborhood, trained)
			// It's chosen 18-23 if that's what the monster itself is (small neighborhood, trained)
			// For the single pluralMismatch it's simply the monster itself with opposite plurality
			if (mismatches.has(j)) {
				correct = false;
				if (monsterIndex < 12) {
					randMonster = Math.floor(Math.random() * 12);
					if (randMonster == monsterIndex && randMonster < 11) {
						randMonster++;
					}
					else if (randMonster == monsterIndex) {
						randMonster = 0;
					}
				} else {
					randMonster = Math.floor(Math.random() * 6 + 18);
					if (randMonster == monsterIndex && randMonster < 23) {
						randMonster++;
					}
					else if (randMonster == monsterIndex) {
						randMonster = 18;
					}
				}
				firstImage = allImages[randMonster];
				if(isPlural){
					firstImage = firstImage.substring(0,firstImage.length-4)+"p.png";
				}
			} else if (pluralMismatch.has(j)){
				correct = false;
				if(isPlural){
					firstImage = allImages[monsterIndex];
				} else{
					firstImage = firstImage.substring(0,firstImage.length-4)+"p.png";
				}
			}

			experiments.push(active_comprehension_trial(
				"/static/elise/img/images/" + firstImage,
				"/static/elise/img/images/" + secondImage,
				correct,
				"/static/elise/sound/combinedsounds/" + allSounds[monsterIndex][singOrPlural],
				getPrompt(allSounds[monsterIndex][singOrPlural]),isPlural,monsterIndex));

		}
	}
	// Production trial 
	else {
		for (var j = 0; j < curr.length; j++) {
			var monsterIndex = parseInt(curr[j][0]);
			var singOrPlural = curr[j][1];
			var isPlural = false;

			if (singOrPlural == 'p'){
				isPlural = true;
			}

			experiments.push(active_production_trial("/static/elise/img/images/" + allImages[monsterIndex],
				"/static/elise/sound/combinedsounds/" + allSounds[monsterIndex][singOrPlural], getPrompt(allSounds[monsterIndex][singOrPlural]),isPlural,monsterIndex));
		}
	}
	experiments.push(playNextInstruction())

	// Pushes block of experiments to matrix
	//experiments = experiments.concat(block);

	// Iterates through the rows in the trial data matrix
	// Starts at index 1 to account for initial trials that have already been added
	for (var i = 1; i < trialData.length; i++) {
		// Current row
		curr = trialData[i];
		console.log(curr)

		// Stores experiment block for this row
		block = [];

		// Shuffles the row itself
		shuffle(curr);

		//Passivemessage
		experiments.push(playNextInstruction())

		//[round of 6 passive trials]
		// Iterates through the row, obtaining trial objects
		for (var j = 0; j < curr.length; j++) {

			// Obtains monster number and plurality from the parsed data
			var monsterIndex = parseInt(curr[j][0]);
			var singOrPlural = curr[j][1];

			var isPlural = false;

			if (singOrPlural == 'p'){
				isPlural = true;
			}

			// Calls functions to obtain trial objects and pushes them to the timeline
			// this part of the experiment contains passive comprehension trials
			experiments.push(passive_comprehension_trial("/static/elise/img/images/" + allImages[monsterIndex],
				"/static/elise/sound/combinedsounds/" + allSounds[monsterIndex][singOrPlural], getPrompt(allSounds[monsterIndex][singOrPlural]),isPlural, monsterIndex));
		}


		// Shuffles the row sequence once again
		shuffle(curr);

		// Creates a list of 3 random indexes to decide which of the active trials will be mismatches
		// These will only be used for active comprehension blocks
		index_list = []
		for (var j = 0; j < 6; j++) {
			index_list.push(j);
		}
		let mismatches = []
		let randind = (Math.floor(Math.random() * 6))
		let randchoice = (index_list.splice(randind, 1)[0])
		mismatches.push(randchoice);
		randind = (Math.floor(Math.random() * 5))
		randchoice = (index_list.splice(randind, 1)[0])
		mismatches.push(randchoice);
		randind = (Math.floor(Math.random() * 4))
		randchoice = (index_list.splice(randind, 1)[0])
		mismatches.push(randchoice);
		console.log(mismatches)
		mismatches = new Set(mismatches);

		//Activecompmessage		activeprodmessage
		experiments.push(playNextInstruction())

		//[round of 6 active comp trials]	[round of 6 active prod trials]
		// Comprehension trial
		if (comp) {

			// Same process as passive trial but generates active comprehension trial 
			for (var j = 0; j < curr.length; j++) {
				var monsterIndex = parseInt(curr[j][0]);
				var singOrPlural = curr[j][1];
				var isPlural = false;
				var firstImage = allImages[monsterIndex];
				var secondImage = allImages[monsterIndex];
				var correct = true;

				// If target audio is plural, set images as plural
				if (singOrPlural == 'p'){
					isPlural = true;
					firstImage = firstImage.substring(0,firstImage.length-4)+"p.png";
					secondImage = secondImage.substring(0,secondImage.length-4)+"p.png";
				}

				// This is where a mismatched image will be chosen for 3 random indices 
				// It's chosen 0-11 if that's what the monster itself is (big neighborhood, trained)
				// It's chosen 18-23 if that's what the monster itself is (small neighborhood, trained)
				// For the single pluralMismatch it's simply the monster itself with opposite plurality
				if (mismatches.has(j)) {
					correct = false;
					if (monsterIndex < 12) {
						randMonster = Math.floor(Math.random() * 12);
						if (randMonster == monsterIndex && randMonster < 11) {
							randMonster++;
						}
						else if (randMonster == monsterIndex) {
							randMonster = 0;
						}
					} else {
						randMonster = Math.floor(Math.random() * 6 + 18);
						if (randMonster == monsterIndex && randMonster < 23) {
							randMonster++;
						}
						else if (randMonster == monsterIndex) {
							randMonster = 18;
						}
					}
					firstImage = allImages[randMonster];
					if(isPlural){
						firstImage = firstImage.substring(0,firstImage.length-4)+"p.png";
					}
				} else if (pluralMismatch.has(j)){
					correct = false;
					if(isPlural){
						firstImage = allImages[monsterIndex];
					} else{
						firstImage = firstImage.substring(0,firstImage.length-4)+"p.png";
					}
				}

				experiments.push(active_comprehension_trial(
					"/static/elise/img/images/" + firstImage,
					"/static/elise/img/images/" + secondImage,
					correct,
					"/static/elise/sound/combinedsounds/" + allSounds[monsterIndex][singOrPlural],
					getPrompt(allSounds[monsterIndex][singOrPlural]),isPlural,monsterIndex));
			}

		}
		// Production trial 
		else {
			for (var j = 0; j < curr.length; j++) {
				var monsterIndex = parseInt(curr[j][0]);
				var singOrPlural = curr[j][1];

				var isPlural = false;

				if (singOrPlural == 'p'){
					isPlural = true;
				}

				experiments.push(active_production_trial("/static/elise/img/images/" + allImages[monsterIndex],
					"/static/elise/sound/combinedsounds/" + allSounds[monsterIndex][singOrPlural], getPrompt(allSounds[monsterIndex][singOrPlural]),isPlural,monsterIndex));
			}
		}

		if ((i + 1) % 3 == 0) {
			experiments.push(playNextInstruction())
			console.log(i)
			if (i == 2) {
				experiments.push(audio_check_trial_2("/static/elise/sound/wallet_w.mp3"))
			} else if (i == 5) {
				experiments.push(audio_check_trial_2("/static/elise/sound/feather_w.mp3"))
			} else if (i == 8) {
				experiments.push(audio_check_trial_2("/static/elise/sound/onion_w.mp3"))
			} else {
				experiments.push(audio_check_trial_2("/static/elise/sound/towel_w.mp3"))
			}
			
		}
	}
	experiments.push(playNextInstruction())
	experiments.push(playNextInstruction())
	// Returns matrix of experiment timelines
	return experiments;
}