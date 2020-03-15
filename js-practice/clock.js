const clockContainer = document.querySelector(".js-clock");
const clockTittle = clockContainer.querySelector(".js-title");
const clockList = document.querySelector(".js-clockList");

// function getTime() {
//   const date = new Date();
//   const month = date.getMonth();
//   const dates = date.getDate();
//   const minutes = date.getMinutes();
//   const hours = date.getHours();
//   const seconds = date.getSeconds();
//   clockTittle.innerText = `${hours < 10 ? `0${hours}` : hours} ${
//     minutes < 10 ? `0${minutes}` : minutes
//   } ${seconds < 10 ? `0${seconds}` : seconds}`;
// seconds 파트에서 ?는 if와 같은 의미를 지닌다. 즉, 초가 10보다 작다면? 0과 초를 같이 내보내서
// 03 과같은 형태로 출력되게 하며  :는 else를 의미하며 seconds만 출력되게한다.
// }

function appendElem(parent, ...elem) {
  for (let i = 0; i < elem.length; i++) {
    parent.appendChild(elem[i]);
  }
  return parent;
}

function paintClock(time, text) {
  const li = document.createElement("li");
  const h1 = document.createElement("h1");
  const span = document.createElement("span");
  h1.innerText = addZero(time);
  span.innerText = text;
  return appendElem(li, h1, span);
}

function getTime() {
  clockList.innerText = "";
  const date = new Date();
  const days = paintClock(date.getDate(), "days");
  const hours = paintClock(date.getHours(), "hours");
  const mins = paintClock(date.getMinutes(), "minutes");
  const seconds = paintClock(date.getSeconds(), "seconds");
  appendElem(clockList, days, hours, mins, seconds);
}

function addZero(val) {
  return val < 10 ? `0${val}` : val;
}

function init() {
  setInterval(getTime, 1000);
  // setinterval은 (함수,변화할시간) 의 형태를 가지며 위 같은 경우는 시간을 1초마다 변경해서
  // 보여주는 기능을 한다.
}

init();
