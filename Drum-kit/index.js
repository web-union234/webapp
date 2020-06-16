var noOfDrumBtns = document.querySelectorAll(".drum").length;

for (var i = 0; i < noOfDrumBtns; i++) {

  document.querySelectorAll(".drum")[i].addEventListener("click", function() {

    var buttonInnerHTML = this.innerHTML;

    makeSound(buttonInnerHTML);

    buttonAnimation(buttonInnerHTML);

  });

}

document.addEventListener("keypress", function(event) {

  makeSound(event.key);
  var string=document.getElementById('write').innerHTML;
  string=string+event.key;
  document.getElementById('write').innerHTML=string;
  buttonAnimation(event.key);

});


function makeSound(key) {

  switch (key) {
    case "a":
      var dom1 = new Audio("sounds/tom-1.mp3");
      dom1.play();
      break;

    case "s":
      var dom2 = new Audio("sounds/tom-2.mp3");
      dom2.play();
      break;

    case "d":
      var dom3 = new Audio('sounds/tom-3.mp3');
      dom3.play();
      break;

    case "f":
      var dom4 = new Audio('sounds/tom-4.mp3');
      dom4.play();
      break;

    case "j":
      var dom5 = new Audio('sounds/snare.mp3');
      dom5.play();
      break;

    case "k":
      var dom6 = new Audio('sounds/crash.mp3');
      dom6.play();
      break;

    case "l":
      var dom7 = new Audio('sounds/kick-bass.mp3');
      dom7.play();
      break;


    default: console.log(key);

  }
}


function buttonAnimation(currentKey) {

  var activeButton = document.querySelector("." + currentKey);

  activeButton.classList.add("pressed");

  setTimeout(function() {
    activeButton.classList.remove("pressed");
  }, 100);

}
