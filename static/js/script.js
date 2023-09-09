var count = 0;
let speech = new SpeechSynthesisUtterance();

document.querySelector("#speak-button").addEventListener("click", () => {
    count++;
    speech.text = document.getElementById("speak-text").innerText;

    speech.rate = 1;

    console.log(speech.text);
    console.log(count);

    if (count % 2 == 0) {
        window.speechSynthesis.cancel();
    } else {
        window.speechSynthesis.speak(speech);
    }
});
