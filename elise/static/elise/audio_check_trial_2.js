
// Plays audio file 
async function playAudio(audio) {
	audio.play()
}

// Sets timer then calls audio play function
function audioAfterTime(audio, time) {
	return new Promise(resolve => {
		setTimeout(() => {
			playAudio(audio);
		}, time);
	});
}

// Returns the active entry trial timeline
function audio_check_trial_2() {
	
	// Image and sound for audio check
	// TODO: make these random
	var image1 = "/static/elise/img/images/pizza.png"
	var sound = "/static/elise/sound/Pizza.mp3"

    // Retrieves audio file name without file path for the purpose of getting the duration from the dictionary
    var audioFileName = (sound.substring(1+sound.lastIndexOf("/")))
	
	// Audio instance is set
	var audio = new Audio(sound);

	// Timeline for active entry trial 
	var audio_check_trial_2 = {
		timeline: [{
			// Displays fixation cross
			type: 'html-keyboard-response',
			stimulus: '+',
			choices: jsPsych.NO_KEYS,
			trial_duration: 500
		}, {
			// Calls audio to play during the second image display
			type: 'call-function',
			async: false,
			func: function() { audioAfterTime(audio, 1000) }
		},
		{
			// Survey input used to prompt user entry 
			type: 'survey-html-form',
			preamble: "",
			// HTML form for user to enter info. "username" form serves only to prevent chrome from autocompleting
			html: '<input id="username" autocomplete = "off" style="display:none" type="text" name="fakeusernameremembered"><p style="display:block;margin-left: auto;margin-right: auto;"> What is the item? </p><input name="first" type="text" style="display:block;margin-left: auto;margin-right: auto;" required autocomplete="off";/>'
		},
		{
			// Blank screen before image is displayed again
			type: 'image-keyboard-response',
			stimulus: '/static/elise/img/images/blank.png',
			choices: jsPsych.NO_KEYS,
			trial_duration: 500
		}, {
			// Calls audio to play during the second image display
			type: 'call-function',
			async: false,
			func: function() { audioAfterTime(audio, 1000) }
		},
		{
			// Displays image a second time
			// Adds sound duration to trial time
			type: 'image-keyboard-response',
			prompt: "<p>" + "pizza" + "</p>",
			stimulus: image1,
			choices: jsPsych.NO_KEYS,
			// Arbitrary trial time for correct image to be displayed
			trial_duration: 2000+1000*(1.4)
		},
		 {
				// Instruction page allows user to continue when ready 
				type: 'instructions',
				pages: ["Continue when ready"]
				,
				show_clickable_nav: true,
				allow_backward:false
				

			}
			
		]
		,
		timeline_variables: [{
			img: null
		}
		]
		
	}
	return audio_check_trial_2
}

