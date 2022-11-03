function setupWS() {
    let loc = window.location, new_uri;
    new_uri = loc.protocol === "https:" ? "wss:" : "ws:";
    new_uri += "//" + loc.host + "/ws/";
    ws = new WebSocket(new_uri)
}

window.onload = setupWS