function active_comprehension_trial(image1,image2, sound){
var active_comprehension_trial = {
  timeline: [{
      type: 'html-keyboard-response',
      stimulus: '+',
      choices: jsPsych.NO_KEYS,
      trial_duration: 500
    },
    {
      type: 'categorize-image',
      stimulus: jsPsych.timelineVariable('img'),
      key_answer: 71,
      choices: [71, 72],
      correct_text: "<p class='prompt'>Correct! </p>",
      incorrect_text: "<p class='prompt'>Incorrect. </p>",
      prompt: "<p>Is this correct?</p>",
      stimulus_duration: 2500,
      show_stim_with_feedback: true,
      feedback_duration: 1000

    },
    {
      type: 'image-keyboard-response',

      stimulus: 'blank.PNG',
      choices: jsPsych.NO_KEYS,
      trial_duration: 500
    },
    {
      type: 'image-keyboard-response',
      prompt: "<p>I am text associated with an image.</p>",
      stimulus: jsPsych.timelineVariable('img'),
      choices: jsPsych.NO_KEYS,
      trial_duration: 2000
    }

  ],
  timeline_variables: [{
      img: image1
    }
  ]
}
return active_comprehension_trial
}

