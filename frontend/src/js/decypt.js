const btn = document.getElementById("btn");

btn.addEventListener("click", () => {
    const text = document.getElementById("text").value;
    const key = document.getElementById("key").value;
    const result = document.getElementById("result");
    const xhr = new XMLHttpRequest();

    xhr.open("POST", "http://localhost:8000/decrypt", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = () => {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            result.innerHTML = response.text;
        } else {
            result.innerHTML = "Erreur lors du décryptage!";
        }
    };

    xhr.send(JSON.stringify({ text, key }));
});
