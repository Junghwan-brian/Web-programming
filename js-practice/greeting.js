const form = document.querySelector(".js-form"),
  input = form.querySelector("input"),
  greeting = document.querySelector(".js-greetings");
//   1) document.querySelector looks for an element in ALL the document
// 2) form.querySelector looks for an element inside the FORM element

const USER_LS = "currentUser",
  SHOWING_CN = "showing";

function saveName(text) {
  localStorage.setItem(USER_LS, text);
}

function paintGreeting(text) {
  form.classList.remove(SHOWING_CN);
  greeting.classList.add(SHOWING_CN);
  greeting.innerText = `Hello ${text}`;
}

function handleSubmit(event) {
  event.preventDefault();
  const currentValue = input.value;
  //   console.log(currentValue);
  paintGreeting(currentValue);
  saveName(currentValue);
}

function askforName() {
  form.classList.add(SHOWING_CN);
  form.addEventListener("submit", handleSubmit);
}

function loadName() {
  const currentUser = localStorage.getItem(USER_LS);
  if (currentUser === null) {
    askforName();
  } else {
    paintGreeting(currentUser);
  }
}

function init() {
  loadName();
}

init();
