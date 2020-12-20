window.onload = function() {
    var slider = document.getElementById("img");
    pictures = ["http://www.sololearn.com/uploads/slider/1.jpg", "http://www.sololearn.com/uploads/slider/2.jpg", "http://www.sololearn.com/uploads/slider/3.jpg"];
    var prev = document.getElementById("prev");
    var next = document.getElementById("next");
    var num = 0;

    prev.addEventListener("click", prevf);
    next.addEventListener("click", nextf);

    function prevf(){
        num--;
        if (num < 0){
            num = pictures.length - 1;
        }
        slider.src = pictures[num];
    }

    function nextf(){
        var maxval = pictures.length;
        num++;
        if (num >= maxval){
            num = 0;
        }
        slider.src = pictures[num];
    }
}
