
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
console.log(document.getElementsByTagName("form")[0])
// Returns the active entry trial timeline
function active_production_trial(image1, sound, prompt) {

	// Saves current folder in server for ease of path determination
	var loc = window.location.protocol + "//" + window.location.host + "/" + window.location.pathname + window.location.search;

	// Audio instance is set
	var audio = new Audio(sound);

	// Adds the duration of the audio to the image displays within the timeline
	audio.addEventListener("loadeddata", function() {
		active_production_trial['timeline'][4]['stimulus_duration'] += 1000 * this.duration;

	});

	// Timeline for active entry trial 
	var active_production_trial = {
		timeline: [{
			// Displays fixation cross
			type: 'html-keyboard-response',
			stimulus: '+',
			choices: jsPsych.NO_KEYS,
			trial_duration: 500
		},
		{
			// Survey input used to prompt user entry 
			type: 'survey-html-form',
			preamble: "<img src='" + loc + image1 + "' style='display:block;margin-left: auto;margin-right: auto;'>",
			// TODO: Make button wait for input 
			html: '<p style="display:block;margin-left: auto;margin-right: auto;"> What is the name of this alien? click continue after typing </p><input name="first" type="text" style="display:block;margin-left: auto;margin-right: auto;" required/>'
		},
		{
			// Blank screen before image is displayed again
			type: 'image-keyboard-response',
			stimulus: loc + '/lcnl javascript experiments/blank.png',
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
			type: 'image-keyboard-response',
			prompt: "<p>" + prompt + "</p>",
			stimulus: image1,
			choices: jsPsych.NO_KEYS,
			trial_duration: 2000
		}
			, {
			// Calls sound in 1 second so that it will play during the image display
			type: 'call-function',
			async: false,
			func: function() {
				var current_node_id = jsPsych.currentTimelineNodeID();

				var valid_node_id = current_node_id.substring(0, current_node_id.length - 3) + "1.0";
				console.log(valid_node_id);
				var data_from_current_node = jsPsych.data.getDataByTimelineNode(valid_node_id);
				console.log(data_from_current_node.csv());

			}
		}
		],
		timeline_variables: [{
			img: image1
		}
		]
	}
	return active_production_trial
}

