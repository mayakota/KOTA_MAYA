function drag() {
    mantis = document.getElementById("dog");
    leftbox = document.getElementById("leftBox")

    mantis.addEventListener("dragstart", startDrag, false);
    mantis.addEventListener("dragend", endDrag, false);

    leftbox.addEventListener("dragenter", dragEnter, false);
    leftbox.addEventListener("dragleave", dragLeave, false);
    leftbox.addEventListener("dragover", function (e) {e.preventDefault()}, false);
    leftbox.addEventListener("drop", drop, false);

}

function startDrag(e) {
    var pic = <img id = "dog" src = "http://r.ddmcdn.com/s_f/o_1/cx_633/cy_0/cw_1725/ch_1725/w_720/APL/uploads/2014/11/too-cute-doggone-it-video-playlist.jpg" >;
    e.dataTransfer.setData("Picture", pic);
}

function dragEnter(e) {
    e.preventDefault();
    leftbox.style.background = "purple";
}

function drop(e) {
    e.preventDefault();
    leftBox.innerHTML = e.dataTransfer.getData("Picture");
}

function endDrag(e) {
    pic = e.target;
    pic.style.visibility = "hidden"








}
