const features = {
    language: navigator.language,
    cpuCores: navigator.hardwareConcurrency,
    screenResolution: screen.width + "x" + screen.height,
    colorDepth: screen.colorDepth,
    windowSize: window.innerWidth + "x" + window.innerHeight,
    timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone,
    referrer: document.referrer || "None"
};

console.log("Active features:", features);

const outputElement = document.getElementById("feature-output");

outputElement.innerHTML = `
    Language: ${features.language}<br>
    CPU cores: ${features.cpuCores}<br>
    Screen resolution: ${features.screenResolution}<br>
    Color depth: ${features.colorDepth}<br>
    Window size: ${features.windowSize}<br>
    Time zone: ${features.timeZone}<br>
    Referrer: ${features.referrer}
`;

async function generateFingerprint() {
    const fingerprintString =
        features.language + "|" +
        features.cpuCores + "|" +
        features.screenResolution + "|" +
        features.colorDepth + "|" +
        features.timeZone;

    console.log("Fingerprint source:", fingerprintString);

    const encodedData = new TextEncoder().encode(fingerprintString);

    const hashBuffer = await crypto.subtle.digest(
        "SHA-256",
        encodedData
    );

    const hashArray = Array.from(new Uint8Array(hashBuffer));

    const fingerprintHash = hashArray
        .map(byte => byte.toString(16).padStart(2, "0"))
        .join("");

    console.log("Fingerprint:", fingerprintHash);

    document.getElementById("fingerprint-output").textContent =
        fingerprintHash;

    fetch("/collect-fingerprint", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            fingerprint: fingerprintHash
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Fingerprint sent:", data);
    })
    .catch(error => {
        console.error("Error sending fingerprint:", error);
    });
}

generateFingerprint();
