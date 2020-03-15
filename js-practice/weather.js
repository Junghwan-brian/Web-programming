const API_KEY = "07d2854df955137d2b9c1e587779386d";
const COORDS = "coords";
const weather = document.querySelector(".js-weather");

function getWeather(lat, lgt) {
  fetch(
    `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lgt}&appid=${API_KEY}&units=metric`
    // fetch를 활용해서 웹사이트의 api url을 통해 정보를 불러온다.
    // API_KEY는 공짜 api를 쓰기 때문에 많이 쓰지 않는 다는 것을 알려준다
    // units=metric은 섭씨온도로 나타내준다.
  )
    .then(function(response) {
      return response.json();
      // then은 이전의 호출이 끝나면 시행되게 해준다
    })
    .then(function(json) {
      // console.log(json);
      const country = json.sys.country;

      const temperature = json.main.temp;
      const place = json.name;
      weather.innerText = `  ${country} ${place} ${temperature}º`;
    });
}

function saveCoords(coordsObj) {
  localStorage.setItem(COORDS, JSON.stringify(coordsObj));
}

function handleGeoSuccess(position) {
  // console.log(position);
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
  const coordsObj = {
    latitude,
    longitude
    // latitude,longtitude는 객체지만 각각 이름과 key가 같기 때문에 위와 같이 작성할 수 있다.
  };
  saveCoords(coordsObj);
  getWeather(latitude, longitude);
}

function handleGeoError() {
  console.log("Can't access geo location");
}

function askForCoords() {
  navigator.geolocation.getCurrentPosition(handleGeoSuccess, handleGeoError);
}

function loadCoords() {
  const loadedCoords = localStorage.getItem(COORDS);
  if (loadedCoords === null) {
    askForCoords();
  } else {
    const parseCoords = JSON.parse(loadedCoords);
    // console.log(parseCoords);
    getWeather(parseCoords.latitude, parseCoords.longitude);
  }
}

function init() {
  loadCoords();
}

init();
