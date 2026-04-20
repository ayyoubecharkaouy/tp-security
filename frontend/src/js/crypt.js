const btn = document.getElementById("btn");

btn.addEventListener("click", () => {
  const text = document.getElementById("text").value;
  const result = document.getElementById("result");
  const xhr = new XMLHttpRequest();

  xhr.open("POST", "http://localhost:8000/crypt", true);
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onload = () => {
    if (xhr.status === 200) {
      const response = JSON.parse(xhr.responseText);
      result.innerHTML = " Texte crypte : " + response.new_text;
      result.innerHTML += "<br>";
      result.innerHTML += " Cle de cryptage : " + response.key;
    } else {
      result.innerHTML = "Erreur lors du cryptage!";
    }
  };

  xhr.send(JSON.stringify({ text }));
});
