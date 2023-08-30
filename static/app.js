const navbarBurger = document.querySelector(".navbar-burger");
const navbaMmenu = document.querySelector(".navbar-menu");
const categoryToggle = document.querySelector("#categoryToggle");
const categoryList = document.querySelector("#categoryList");
const notification = document.querySelector(".notification");
const notificationDelete = document.querySelector(".delete");

navbarBurger.addEventListener("click", () => {
  navbaMmenu.classList.toggle("is-active");
  navbarBurger.classList.toggle("is-active");
});

categoryToggle.addEventListener("click", () => {
  categoryList.classList.toggle("is-hidden");
});

notificationDelete.addEventListener("click", () => {
  notification.classList.toggle("is-hidden");
});