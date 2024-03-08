function calcAverage() {
    var nota1 = parseFloat(document.getElementById("nota1").value);
    var nota2 = parseFloat(document.getElementById("nota2").value);

    var media = (nota1 + nota2) / 2;

    var resultado = document.getElementById("mediaSemestral");
    resultado.innerHTML = "Média Semestral: " + media.toFixed(2);

    if (media >= 6.0) {
        resultado.innerHTML += "<br>PARABÉNS! Você foi aprovado!";
    }
}