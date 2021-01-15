
// Plays audio file 
async function playAudio(audio) {
	audio.play()
}

// Function used to set a timer and then call the audio file player
function audioAfterTime(audio, time) {
	return new Promise(resolve => {
		setTimeout(() => {
			playAudio(audio);
		}, time);
	});
}

// Runs a forced choice 2 trial with 2 images, a boolean determining which is correct and an associated sound file  
function forced_choice_trial_2(image1, image2, correct, sound) {
	
	// Determines the appropriate key and image to set for the correct value in the user interaction
	var corimage;
	var key;
	if (correct) {
		key = 76;
		corimage = image1;
	}
	else {
		key = 65;
		corimage = image2;
	}

    // Retrieves audio file name without file path for the purpose of getting the duration from the dictionary
    var audioFileName = (sound.substring(1+sound.lastIndexOf("/")))

	// Audio instance is set 
	var audio = new Audio(sound);


	// variable storing the timeline for the trial that will be output
	let forced_choice_trial_2 = {
		timeline: [{
			// Displays fixation cross
			type: 'html-keyboard-response',
			stimulus: '+',
			choices: jsPsych.NO_KEYS,
			trial_duration: 500
		}, {
			// Calls sound in 1 second so that it will play during the image display
			type: 'call-function',
			async: false,
			func: function() { audioAfterTime(audio, 1000) }
		},
		{
			// Displays image and asks user to select y for yes or n for no based on the sound that is played
			type: 'categorize-html',
			stimulus: "<img src='" +image1+"'style='margin-left: auto;margin-right: auto;'><img src='" + image2+"' style='margin-left: auto;margin-right: auto;'>",
			key_answer: key,
			choices: [76, 65],
			correct_text: "<img src='" +"/static/elise/img/images/greencheck.png'style='margin-left: auto;margin-right: auto;'>",
			incorrect_text: "<img src='" + "/static/elise/img/images/redx.png' style='margin-left: auto;margin-right: auto;'>",
			prompt: "<p>Left Image: press L			 Right Image: press A</p>",
			show_stim_with_feedback: true,
			feedback_duration: 1000
		},
		{
			// Blank screen to implement pause
			type: 'image-keyboard-response',
			stimulus: '/static/elise/img/images/blank.png',
			choices: jsPsych.NO_KEYS,
			trial_duration: 500
		}, {
			// Calls sound in 1 second so that it will play during the image display
			type: 'call-function',
			async: false,
			func: function() { audioAfterTime(audio, 1000) }
		},
		{
			// Displays correct image 
			type: 'image-keyboard-response',
			prompt: "<p>" + "" + "</p>",
			stimulus: corimage,
			choices: jsPsych.NO_KEYS,
			// Retrieves sound duration from the dictionary and adds it to the trial duration 
			trial_duration: 2000+1000*(parseFloat(durationDict[audioFileName]))
		}
			, {
			// Retrieves and separates relevant data from the appropriate timeline node
			type: 'call-function',
			async: false,
			func: function() {
				var current_node_id = jsPsych.currentTimelineNodeID();
				// Navigates from the end of the timeline to the node associated with the categorize image trial
				var valid_node_id = current_node_id.substring(0, current_node_id.length - 3) + "2.0";
				// Gets data from this node and prints it to the screen
				// TODO: this will be changed to a server ajax call later in process
				var data_from_current_node = jsPsych.data.getDataByTimelineNode(valid_node_id);
				console.log(data_from_current_node.csv())
				
			}
		}
		],
		timeline_variables: [{
			img: null
		}
		]
	}

	return forced_choice_trial_2
}

