const targetSentence = document.getElementById("target-sentence").textContent.trim();
const typingInput = document.getElementById("typing-input");
const restartButton = document.getElementById("restart-button");
const typingResults = document.getElementById("typing-results");

let startTime = null;
let correctionCount = 0;
typingInput.addEventListener("paste", function (event) {
    event.preventDefault();
    alert("Please type the sentence manually.");
});
typingInput.addEventListener("keydown", function (event) {
    if (startTime === null) {
        startTime = performance.now();
        console.log("Timer started");
    }

    if (event.key === "Backspace") {
        correctionCount++;
        console.log("Corrections:", correctionCount);
    }
});
typingInput.addEventListener("input", function () {
    if (typingInput.value === targetSentence && startTime !== null) {
        const endTime = performance.now();

        const totalTime = (endTime - startTime) / 1000;
        const typingSpeed = targetSentence.length / totalTime;
	const typingData = {
        totalTime: totalTime.toFixed(2),
        typingSpeed: typingSpeed.toFixed(2),
        corrections: correctionCount
};
        typingResults.innerHTML = `
            Total time: ${totalTime.toFixed(2)} seconds<br>
            Typing speed: ${typingSpeed.toFixed(2)} characters/second<br>
            Corrections: ${correctionCount}
        `;

        console.log("Typing completed");
        console.log("Total time:", totalTime.toFixed(2));
        console.log("Typing speed:", typingSpeed.toFixed(2));
        console.log("Corrections:", correctionCount);
	fetch("/collect-typing", {
   	 method: "POST",
    	headers: {
        "Content-Type": "application/json"
    },
        body: JSON.stringify(typingData)
		})
	.then(response => response.json())
	.then(data => {
    	console.log("Typing data sent:", data);
})
.catch(error => {
    console.error("Error sending typing data:", error);
});         
   }
});
restartButton.addEventListener("click", function () {
    typingInput.value = "";
    typingResults.textContent = "";
    startTime = null;
    correctionCount = 0;

    console.log("Experiment restarted");
    typingInput.focus();
});
