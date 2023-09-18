"use strict";

const btnNav = document.querySelector(".btn-mobile-nav");
const container = document.querySelector(".container");

btnNav.addEventListener("click", function () {
  container.classList.toggle("nav-open");
});
