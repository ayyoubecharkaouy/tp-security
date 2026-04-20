const btn = document.getElementById("btn");

btn.addEventListener("click", () => {
    const text = document.getElementById("text").value;
    const hash = document.getElementById("hash").value;
    const result = document.getElementById("result");
    const xhr = new XMLHttpRequest();

    xhr.open("POST", "http://localhost:8000/compare", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = () => {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            result.innerHTML = response.message;
            result.style.color = response.match ? "green" : "red";
        } else {
            result.innerHTML = "Erreur lors de la comparaison!";
            result.style.color = "red";
        }
    };

    xhr.send(JSON.stringify({ text, hash }));
});
