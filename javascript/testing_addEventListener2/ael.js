window.onload = function() {
    var slider = document.getElementById("img");
    pictures = ["https://cdn.pixabay.com/photo/2020/02/13/19/19/winter-4846638_960_720.jpg", "https://cdn.pixabay.com/photo/2018/03/28/00/31/winter-3267925_960_720.jpg", "https://cdn.pixabay.com/photo/2020/12/03/05/23/lion-5799523_960_720.jpg"];
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
