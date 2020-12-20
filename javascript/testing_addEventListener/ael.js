window.onload = function() {var btn = document.getElementById("demo");
btn.addEventListener("click", showDate);
// // function change() {
// //     var x = document.getElementById('name');
// //     x.value = x.value.toUpperCase();
// // }
btn.removeEventListener("mouseover", showDate);

function showDate(){
    alert(Date());
}
}
