const toDoForm = document.querySelector(".js-toDoForm"),
  toDoInput = toDoForm.querySelector("input"),
  toDoList = document.querySelector(".js-toDoList");

const TODOS_LS = "toDos";

let toDos = [];

function deleteToDo(event) {
  const btn = event.target;
  const li = btn.parentNode;
  toDoList.removeChild(li);
  const cleanToDos = toDos.filter(function(toDo) {
    return toDo.id !== parseInt(li.id);
    // li의 id가 문자열로 되어있어서 정수값으로 바꿔줬다.
  });
  // filter는 toDos에있는 배열값중 fiterFuntion의 함수에 참인값만 filterFuntion으로 가서 return된다.
  // 그리고 true인 값들로만 이루어진 배열을 만든다.
  toDos = cleanToDos;
  // toDos를 cleanToDos로 바꿔줬다
  saveToDos();
}

function saveToDos() {
  localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
  // JSON.stringify는 object를 문자열(string)으로 바꿔준다.
}

function paintToDo(text) {
  const li = document.createElement("li");
  //   createElement는 html의 요소를 만드는 역할을 한다.
  const delBtn = document.createElement("button");
  // delBtn.classList.add("far", "fa-times-circle");

  const span = document.createElement("span");
  const newId = toDos.length + 1;
  // toDos.length는 toDos에 몇개의 요소가 있는지 알려준다.
  span.innerText = text;
  delBtn.innerHTML = "✔";

  delBtn.addEventListener("click", deleteToDo);
  li.appendChild(span);
  li.appendChild(delBtn);
  // delBtn.appendChild(check);
  //   appendChild는 span과 delBtn을 리스트에 넣는 역할을 한다.
  li.id = newId;
  toDoList.appendChild(li);
  const toDoObj = {
    text: text,
    id: newId
  };
  toDos.push(toDoObj);
  // push는 ()안의 것(toDoObj)을 .앞에있는 배열(toDos)에 추가해주는 것이다.
  saveToDos();
}

function handlesubmit(event) {
  event.preventDefault();
  //   preventDefault는 여기서 입력창에 입력후 엔터를 눌러도 그 이벤트가 사라지며 새로고침되지 않고
  //   유지될 수 있도록 막는다. 원래 디폴트 값은 그 값이 날아가며 새로고침되는것이다.
  const currentValue = toDoInput.value;
  paintToDo(currentValue);
  toDoInput.value = "";
  //   위의 명령은 엔터를 치면 입력창의 입력한 값이 없어지게 한다
}

function loadToDos() {
  const loadedToDos = localStorage.getItem(TODOS_LS);
  if (loadedToDos !== null) {
    const parsedToDos = JSON.parse(loadedToDos);
    // 여기서 JSON.parse는 문자열을 자바스크립트 오브젝트로 변환시켜준다
    parsedToDos.forEach(function(toDo) {
      console.log(toDo.text);
      paintToDo(toDo.text);
    });
    // forEach는 배열에 담겨있는 것들 각각에 한번씩 함수를 실행시켜 주는 것.
    // 위의경우에는 function을 forEach안에서 만들어서 사용했고 function을 따로 만들어서
    // 사용할 수도 있다.
  }
}

function init() {
  loadToDos();

  toDoForm.addEventListener("submit", handlesubmit);
}

init();
