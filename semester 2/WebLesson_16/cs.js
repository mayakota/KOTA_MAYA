function mouse()
{
    var x = document.getElementById("canvas");
    canvas=x.getContext("2d");

    window.addEventListener("mousemove", icon, false);

}

function icon(e) {
    canvas.clearRect(0, 0, 1000, 1000);
    var xPos = e.clientX;
    var yPos = e.clientY;
    var pic = new Image();
    pic.src = "http://r.ddmcdn.com/s_f/o_1/cx_633/cy_0/cw_1725/ch_1725/w_720/APL/uploads/2014/11/too-cute-doggone-it-video-playlist.jpg";
    canvas.drawImage(pic, xPos, yPos, 200, 200);

}

window.addEventListener("load", mouse, false);