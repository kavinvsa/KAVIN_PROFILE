const revealItems = document.querySelectorAll('.reveal');

const io = new IntersectionObserver((entries) => {
  entries.forEach((entry, index) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, index * 80);
      io.unobserve(entry.target);
    }
  });
}, { threshold: 0.18 });

revealItems.forEach((item) => io.observe(item));

document.getElementById('year').textContent = new Date().getFullYear();

const slider = document.querySelector('[data-slider]');

if (slider) {
  const track = slider.querySelector('.slider-track');
  const slides = Array.from(track.children);
  const prevBtn = slider.querySelector('[data-prev]');
  const nextBtn = slider.querySelector('[data-next]');
  let current = 0;
  let autoTimer;

  const goTo = (index) => {
    current = (index + slides.length) % slides.length;
    track.style.transform = `translateX(-${current * 100}%)`;
  };

  const startAuto = () => {
    autoTimer = setInterval(() => {
      goTo(current + 1);
    }, 3600);
  };

  const stopAuto = () => {
    clearInterval(autoTimer);
  };

  prevBtn.addEventListener('click', () => goTo(current - 1));
  nextBtn.addEventListener('click', () => goTo(current + 1));
  slider.addEventListener('mouseenter', stopAuto);
  slider.addEventListener('mouseleave', startAuto);

  goTo(0);
  startAuto();
}
