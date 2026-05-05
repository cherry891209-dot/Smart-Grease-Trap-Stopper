const demo = document.querySelector(".sink-demo");
const stopper = document.querySelector(".stopper");

if (demo && stopper) {
  stopper.addEventListener("click", () => {
    demo.classList.toggle("is-active");
  });
}

const header = document.querySelector(".site-header");

window.addEventListener("scroll", () => {
  if (!header) return;
  header.classList.toggle("is-scrolled", window.scrollY > 24);
});
