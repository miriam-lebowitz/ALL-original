
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

// Audio check trial that does not allow user to repeat
function audio_check_trial_2(sound) {

    // Retrieves audio file name without file path for the purpose of getting the duration from the dictionary
    var audioFileName = (sound.substring(1+sound.lastIndexOf("/")))
	
	// Audio instance is set
	var audio = new Audio(sound);

	// Timeline for active entry trial 
	var audio_check_trial_2 = {
		timeline: [
		{
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
			html: '<input id="username" autocomplete = "off" style="display:none" type="text" name="fakeusernameremembered"><p style="display:block;margin-left: auto;margin-right: auto;"> Type the English word you hear. </p><input name="first" type="text" style="display:block;margin-left: auto;margin-right: auto;" required autocomplete="off";/>'
		},
		{
			// Blank screen before image is displayed again
			type: 'image-keyboard-response',
			stimulus: '/static/elise/img/images/blank.png',
			choices: jsPsych.NO_KEYS,
			trial_duration: 500
		}, 
		{	
			// Instruction page allows user to continue when ready 
			type: 'instructions',
			pages: ["TAKE A BREAK IF YOU NEED TO (MAX 5 MINUTES)."]
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

