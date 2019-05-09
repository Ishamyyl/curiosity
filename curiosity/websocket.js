class WebSocketBridge {
    constructor(url, port, cb, protocols) {
        url = `ws://127.0.0.1:${port}/${url}`;
        this.socket = new WebSocket(url, protocols);
        this.socket.onmessage = (event) => {
            console.log(event);
            cb(JSON.parse(event.data));
        };
    }
    send(msg) {
        this.socket.send(JSON.stringify(msg));
    }
}

function connect(url, port, cb, protocols) {
    return new Promise((resolve, reject) => {
        s = new WebSocketBridge(url, port, cb, protocols);
        s.socket.onopen = () => {
            resolve(s);
        }
        s.socket.onerror = (err) => {
            reject(err);
        }
    });
}