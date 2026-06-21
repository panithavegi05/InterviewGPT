function startVoiceInput(){


const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

if(!SpeechRecognition){

    alert(
        "Speech Recognition Not Supported"
    );

    return;
}

let recognition =
    new SpeechRecognition();

recognition.lang = "en-US";

recognition.start();

alert(
    "Speak Now..."
);

recognition.onresult = function(event){

    let transcript =
        event.results[0][0].transcript;

    document.getElementById(
        "answer"
    ).value = transcript;

    alert(
        "You said: " + transcript
    );
};

recognition.onerror = function(event){

    alert(
        "Error: " + event.error
    );
};


}

function submitAnswer(){


let answer =
    document.getElementById(
        "answer"
    ).value;

if(answer==""){

    alert(
        "Answer Required"
    );

}else{

    alert(
        "Answer Submitted"
    );

}


}
