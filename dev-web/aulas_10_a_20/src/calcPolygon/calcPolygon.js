function calcPolygon() {
    var numSides = parseInt(document.getElementById('numSides').value);
    var sideLength = parseFloat(document.getElementById('sideLength').value);

    if (isNaN(numSides) || isNaN(sideLength)) {
        document.getElementById('polygonResult').innerHTML = "Valor inválido. Tente novamente.";
        return;
    }

    var result = "";

    switch (numSides) {
        case 3:
            var perimeter = numSides * sideLength;
            result = "TRIÂNGULO - Perímetro: " + perimeter.toFixed(2) + " cm";
            break;
        case 4:
            var area = sideLength * sideLength;
            result = "QUADRADO - Área: " + area.toFixed(2) + " cm²";
            break;
        case 5:
            result = "PENTÁGONO";
            break;
        default:
            result = "Número de lados inválido. Digite 3, 4 ou 5.";
            break;
    }

    document.getElementById('polygonResult').innerHTML = result;
}
