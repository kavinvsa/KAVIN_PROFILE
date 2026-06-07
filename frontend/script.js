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

const chatbotForm = document.getElementById('chatbotForm');
const chatbotInput = document.getElementById('chatbotInput');
const chatbotMessages = document.getElementById('chatbotMessages');
const chatbotToggle = document.getElementById('chatbotToggle');
const chatbotClose = document.getElementById('chatbotClose');
const chatbotPanel = document.getElementById('chatbotPanel');

const backendUrl = 'http://localhost:8000/chat';

function openChatbot() {
  if (!chatbotPanel || !chatbotToggle) {
    return;
  }

  chatbotPanel.hidden = false;
  chatbotToggle.setAttribute('aria-expanded', 'true');

  if (chatbotInput) {
    window.setTimeout(() => chatbotInput.focus(), 0);
  }
}

function closeChatbot() {
  if (!chatbotPanel || !chatbotToggle) {
    return;
  }

  chatbotPanel.hidden = true;
  chatbotToggle.setAttribute('aria-expanded', 'false');
}

function addChatMessage(text, role) {
  if (!chatbotMessages) {
    return;
  }

  const message = document.createElement('div');
  message.className = `chatbot-message ${role}`;
  message.textContent = text;
  chatbotMessages.appendChild(message);
  chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

if (chatbotForm && chatbotInput && chatbotMessages) {
  chatbotForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const question = chatbotInput.value.trim();
    if (!question) {
      return;
    }

    addChatMessage(question, 'user');
    chatbotInput.value = '';

    const typingMessage = document.createElement('div');
    typingMessage.className = 'chatbot-message bot';
    typingMessage.textContent = 'Thinking...';
    chatbotMessages.appendChild(typingMessage);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;

    try {
      const response = await fetch(backendUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }),
      });

      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }

      const data = await response.json();
      typingMessage.textContent = data.answer || 'No answer returned.';
    } catch (error) {
      typingMessage.textContent = 'Backend not available. Start the FastAPI server on port 8000, then try again.';
    }
  });
}

if (chatbotToggle && chatbotPanel) {
  chatbotToggle.addEventListener('click', () => {
    const isOpen = !chatbotPanel.hidden;
    if (isOpen) {
      closeChatbot();
    } else {
      openChatbot();
    }
  });
}

if (chatbotClose && chatbotPanel && chatbotToggle) {
  chatbotClose.addEventListener('click', () => {
    closeChatbot();
  });
}
