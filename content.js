/**
 * Tableau d'exemples de sélecteurs
 */
let bets = [
  '[data-automation-locator="betPlace.dozen-1st12"]',
  '[data-automation-locator="betPlace.dozen-2nd12"]',
  '[data-automation-locator="betPlace.dozen-3rd12"]',
];
let play;
let lastNubers = null; // a ajouter

/**
 * FUNCTIONS
 */
function nGame() {
  play = getTemps();
  console.log("Nouveau jeux!!!");
  console.log(play);
  if (play) {
    console.log(getNumbers());
  }
}
function clickOnRoulette(selector) {
  let element = document.querySelector(selector);
  if (element) {
    console.log("Clique sur :", selector, element);

    // 1) Mousedown
    const mouseDownEvent = new MouseEvent("mousedown", {
      bubbles: true,
      cancelable: true,
      view: window,
    });
    element.dispatchEvent(mouseDownEvent);

    // 2) Mouseup
    const mouseUpEvent = new MouseEvent("mouseup", {
      bubbles: true,
      cancelable: true,
      view: window,
    });
    element.dispatchEvent(mouseUpEvent);

    // 3) Click
    const clickEvent = new MouseEvent("click", {
      bubbles: true,
      cancelable: true,
      view: window,
    });
    element.dispatchEvent(clickEvent);
  } else {
    console.warn("Élément non trouvé :", selector);
  }
}
function getTemps() {
  // On recherche la div avec la classe .timer-wrapper et l'attribut data-automation-locator="element.Timer"
  return document.querySelector(
    '.timer-wrapper[data-automation-locator="element.Timer"]'
  )
    ? true
    : false;
}
function getNumbers() {
  const parent = document.querySelector(".game-area__history-line--UnnO5");
  if (!parent) return null;
  const firstChild = parent.firstElementChild;
  if (!firstChild) return null;
  const valueElement = firstChild.querySelector(
    ".roulette-history-item__value-text--siwxW"
  );
  if (!valueElement) return null;
  return valueElement.textContent.trim();
}
/**
 * OBSERVERS
 */
{
  const targetNode = document.body;
  const config = { childList: true, subtree: true };
  let lastState = null; // inconnu au début
  function callback(mutationsList, observer) {
    for (const mutation of mutationsList) {
      if (mutation.type === "childList") {
        const timerElement = document.querySelector(
          '.timer-wrapper[data-automation-locator="element.Timer"]'
        );
        const currentState = !!timerElement;
        if (currentState !== lastState) {
          lastState = currentState;
          nGame();
        }
      }
    }
  }
  const observer = new MutationObserver(callback);
  observer.observe(targetNode, config);
}
// Tests
document.addEventListener("keydown", (event) => {
  // Se déclenche uniquement si l'utilisateur n'appuie pas sur la touche meta
  if (event.metaKey) return;

  switch (event.key) {
    case "1":
      console.log("aaaaa");
      clickOnRoulette(bets[0]);
      break;
    case "2":
      clickOnRoulette(bets[1]);
      break;
    case "3":
      clickOnRoulette(bets[2]);
      break;
    // Vous pouvez ajouter d'autres cas si besoin ("2", "3", etc.)
    default:
      break;
  }
});
