function shapes()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    var g = canvas.createLinearGradient(10, 10, 700, 520);
    g.addColorStop(0, "purple");
    g.addColorStop(0.3, "white");
    g.addColorStop(0.7, "yellow");
    canvas.fillStyle = g;
    canvas.beginPath();
    canvas.moveTo(200, 0);
    canvas.lineTo(170. 130);
    c

}
