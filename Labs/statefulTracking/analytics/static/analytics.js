function getCookie(name) {
    const cookies = document.cookie.split("; ");

    for (const cookie of cookies) {
        const [key, value] = cookie.split("=");

        if (key === name) {
            return value;
        }
    }

    return null;
}


function generateId() {
    return Math.random().toString(36).substring(2, 12);
}


let analyticsId = getCookie("analytics_id");

if (!analyticsId) {
    analyticsId = generateId();

    document.cookie =
        "analytics_id=" + analyticsId +
        "; Max-Age=86400; Path=/";
}


// Information about the current publisher page
const publisher = window.location.hostname;
const page = window.location.pathname;


// Send the activity to the analytics server
const url =
    "http://analytics.test:9100/collect" +
    "?id=" + encodeURIComponent(analyticsId) +
    "&publisher=" + encodeURIComponent(publisher) +
    "&page=" + encodeURIComponent(page);

fetch(url, {
    mode: "no-cors"
});

console.log("Analytics ID:", analyticsId);
console.log("Analytics event sent:", publisher, page);
