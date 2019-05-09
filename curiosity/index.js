(async () => {
    let ws = await connect('test', 9000, (msg) => {
        console.log('back', msg);
    });
    ws.send({ 'action': 'echo', 'msg': 'hi' });
})();