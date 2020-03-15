const texts = [
  {
    text: "시간을 지배할 줄 아는 사람은 인생을 지배할 줄 아는 사람이다.",
    who: "에센 바흐"
  },
  {
    text:
      "시간의 걸음걸이에는 세 가지가 있다. 미래는 주저하면서 다가오고, 현재는 화살처럼 날아가고, 과거는 영원히 정지하고 있다.",
    who: "F. 실러"
  },
  { text: "짧은 인생은 시간낭비에 의해 더욱 짧아진다.", who: "S. 존슨" },
  {
    text:
      "시간을 단축시키는 것은 활동이요, 시간을 견디지 못하게 하는 것은 안일 함이다.",
    who: "괴테"
  },
  {
    text:
      "미래를 신뢰하지 마라, 죽은 과거는 묻어버려라, 그리고 살아있는 현재에 행동하라.",
    who: "롱펠로"
  },
  {
    text:
      "오늘 하루를 헛되이 보냈다면 그것은 커다란 손실이다. 하루를 유익하게 보낸 사람은 하루의 보물을 파낸 것이다. 하루를 헛되이 보냄은 내 몸을 헛되이 소모하고 있다는 것을 기억해야 한다.",
    who: "앙리 프레데리크 아미엘"
  },
  { text: "계획이란 미래에 관한 현재의 결정이다.", who: "드래커" },
  { text: "시간을 선택하는 것은 시간을 절약하는 것이다.", who: "베이컨" },
  {
    text: "시간이 덜어주거나 부드럽게 해주지 않는 슬픔이란 하나도 없다.",
    who: "키케로"
  },
  {
    text:
      "가장 바쁜 사람이 가장 많은 시간을 갖는다. 부지런히 노력하는 사람이 결국 많은 대가를 얻는다.",
    who: "알렉산드리아 피네"
  },
  {
    text: "그대의 하루 하루를 그대의 마지막 날이라고 생각하라.",
    who: "호라티우스"
  },
  {
    text:
      "내가 헛되이 보낸 오늘 하루는 어제 죽어간 이들이 그토록 바라던 하루이다. 단 하루면 인간적인 모든 것을 멸망시킬 수 있고 다시 소생시킬 수도 있다.",
    who: "소포클레스"
  },
  {
    text:
      '변명 중에서도 가장 어리석고 못난 변명은 "시간이 없어서" 라는 변명이다.',
    who: "에디슨"
  },
  {
    text:
      "사람은 금전을 시간보다 중히 여기지만, 그로 인해 잃어버린 시간은 금전으론 살 수 없다.",
    who: "유태격언"
  },
  {
    text:
      "시간을 최악으로 사용하는 사람들은 시간이 부족하다고 늘 불평하는데 일인자이다.",
    who: "라 브뤼에르"
  },
  {
    text:
      "삼십 분이란 티끌과 같은 시간이라고 말하지 말고, 그 동안이라도 티끌과 같은 일을 처리하는 것이 현명한 방법이다.",
    who: "괴테"
  },
  {
    text:
      "세월은 누구에게나 공평하게 주어진 자본금이다. 이 자본을 잘 이용한 사람에겐 승리가 있다.",
    who: "아뷰난드"
  },
  {
    text: "승자는 시간을 관리하며 살고, 패자는 시간에 끌려 산다.",
    who: "J. 하비스"
  },
  {
    text:
      "오늘의 식사는 내일로 미루지 않으면서 오늘 할 일은 내일로 미루는 사람이 많다.",
    who: "C. 힐티"
  },
  {
    text:
      "우리는 일 년 후면 다 잊어버릴 슬픔을 간직하느라고 무엇과도 바꿀 수 없는 소중한 시간을 버리고 있습니다. 소심하게 굴기에 인생은 너무나 짧습니다.",
    who: "카네기"
  },
  {
    text: "전력을 다해서 시간에 대항하라.",
    who: "톨스토이"
  },
  {
    text: "하루의 가장 달콤한 순간은 새벽에 있다.",
    who: "윌콕스"
  }
];

const saying = document.querySelector(".js-saying");
const text = saying.querySelector(".js-saying-title");
const who = saying.querySelector(".js-who");

function paintText(textIndex) {
  text.innerText = texts[textIndex].text;
  who.innerText = texts[textIndex].who;
}

function getRandom() {
  const number = Math.floor(Math.random() * texts.length);
  return number;
}

function init() {
  const randomNumber = getRandom();
  paintText(randomNumber);
}

init();
