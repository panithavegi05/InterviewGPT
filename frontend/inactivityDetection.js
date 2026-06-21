let timer;

function resetTimer() {

    clearTimeout(timer);

    timer = setTimeout(
        async () => {

            await fetch(
                "http://127.0.0.1:8000/anti-cheat",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        event: "long_inactivity"
                    })
                }
            );

        },
        30000
    );
}

window.addEventListener(
    "mousemove",
    resetTimer
);

window.addEventListener(
    "keydown",
    resetTimer
);

resetTimer();