document.addEventListener(
    "visibilitychange",
    async () => {

        if (document.hidden) {

            await fetch(
                "http://127.0.0.1:8000/anti-cheat",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        event: "tab_switch"
                    })
                }
            );
        }
    }
);