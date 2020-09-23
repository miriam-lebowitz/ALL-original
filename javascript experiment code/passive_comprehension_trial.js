// JavaScript Document
function passive_comprehension_trial(image, sound) {
  var passive_comprehension_trial = {
    timeline: [{
        type: 'html-keyboard-response',
        stimulus: '+',
        choices: jsPsych.NO_KEYS,
        trial_duration: 500
      },
      {
        type: 'image-keyboard-response',

        stimulus: jsPsych.timelineVariable('img'),
        choices: jsPsych.NO_KEYS,
        trial_duration: 2500
      },
      {
        type: 'image-keyboard-response',

        stimulus: 'blank.PNG',
        choices: jsPsych.NO_KEYS,
        trial_duration: 500
      },
      {
        type: 'image-keyboard-response',
        prompt: '<p>I am text associated with an image<\p>',
        stimulus: jsPsych.timelineVariable('img'),
        choices: jsPsych.NO_KEYS,
        trial_duration: 2000
      }

    ],
    timeline_variables: [{
      img: image
    }]
  }
  return passive_comprehension_trial
}
