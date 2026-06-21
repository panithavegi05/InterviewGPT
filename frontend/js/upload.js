async function uploadResume() {

    alert("Function Started");

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let role = document.getElementById("role").value;

    alert(name);

    let response = await fetch(
        "http://127.0.0.1:8000/candidate",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                email: email,
                role: role
            })
        }
    );

    alert("Fetch Completed");

    let data = await response.json();

    alert(data.message);
}