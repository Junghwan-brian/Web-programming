// alert("im working");

// const what = "jung";
// console.log(what);
// const title = document.getElementById("title");
// title.innerHTML = "Hi!!!!!";
// title.style.color = "red";
// console.dir(title);

// title.addEventListener("click", handleclick);

// const age = prompt("how old are u");
// if (age > 18) {
//   console.log("you can drink");
// } else {
//   console.log("go back");
// }

// <<const basecolor = "rgb(255, 107, 129)";
// const othercolor = "#7f8c8d";

// function handleClick() {
//   const currentColor = title.style.color;
//   if (currentColor === basecolor) {
//     title.style.color = othercolor;
//   } else {
//     title.style.color = basecolor;
//   }
// }>>

const title = document.querySelector("#title");

const clicked_class = "clicked";
function handleClick() {
  //   const hasclass = title.classList.contains(clicked_class);
  //   if (!hasclass) {
  //     title.classList.add(clicked_class);
  //   } else {
  //     title.classList.remove(clicked_class);
  //   }
  title.classList.toggle(clicked_class);
}

function init() {
  //   title.style.color = basecolor;
  title.addEventListener("click", handleClick);
}

init();
