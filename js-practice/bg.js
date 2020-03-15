const body = document.querySelector("body");

const IMG_NUMBER = 5;

function paintImage(imgNumber) {
  const image = new Image();
  //   위의 코드는 const image = document.createElement("img") 와 같은 것이다.
  image.src = `images/${imgNumber + 1}.jpg`;
  image.classList.add("bgImage");
  body.appendChild(image);
}

function genRandom() {
  const number = Math.floor(Math.random() * IMG_NUMBER);
  // math라는 모듈에 random생성 기능이 있고 그냥 math.random을 하면 소수점이 너무 많이 나오므로
  // floor를 사용해서 소수점을 모두 버려준다. floor는 버림, ceil은 올림이다. *5는 이미지가 5개라
  // 해줬으며 기본은 0~1이다.
  return number;
}

function init() {
  const randomNumber = genRandom();
  paintImage(randomNumber);
}

init();
