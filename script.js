// ============ FOOTER INJECTION ============
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('footer-component').forEach(el => {
    const tpl = document.getElementById('footer-template');
    if (tpl) {
      el.replaceWith(tpl.content.cloneNode(true));
    }
  });
});

// ============ HAMBURGER MENU ============
function toggleMenu() {
  const menu = document.getElementById('mobileMenu');
  if (menu) {
    menu.classList.toggle('open');
  }
}

// ============ NAVBAR SCROLL ============
window.addEventListener('scroll', () => {
  const navbar = document.getElementById('navbar');
  if (navbar) {
    navbar.classList.toggle('scrolled', window.scrollY > 20);
  }
});

// ============ FORM SUBMISSION ============
function submitForm() {
  const fnameEl = document.getElementById('fname');
  const emailEl = document.getElementById('femail');
  const messageEl = document.getElementById('fmessage');
  
  if (!fnameEl || !emailEl || !messageEl) return;
  
  const fname = fnameEl.value.trim();
  const email = emailEl.value.trim();
  const message = messageEl.value.trim();
  
  if (!fname || !email || !message) {
    alert('Please fill in all required fields (Name, Email, Message).');
    return;
  }
  
  const toast = document.getElementById('toast');
  if (toast) {
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 3500);
  }
  
  // Reset form
  ['fname','lname','femail','fphone','fmessage'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.value = '';
  });
  
  const serviceEl = document.getElementById('fservice');
  if (serviceEl) serviceEl.selectedIndex = 0;
}

// ============ REVEAL ON SCROLL ============
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => { 
    if (e.isIntersecting) e.target.classList.add('visible'); 
  });
}, { threshold: 0.1 });

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.card, .srv-card, .ind-card, .testi-card, .why-item, .stat-card, .mv-card, .tl-item').forEach(el => {
    el.classList.add('reveal');
    revealObserver.observe(el);
  });
});

// ============ ACTIVE NAV HIGHLIGHT ============
function setActiveNav() {
  const path = window.location.pathname;
  let page = path.split("/").pop().replace(".html", "");
  if (!page || page === "") page = "index";
  if (page === "home") page = "index";
  
  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === page + '.html' || (page === 'index' && href === 'index.html')) {
      a.classList.add('active');
    } else {
      a.classList.remove('active');
    }
  });
}

document.addEventListener('DOMContentLoaded', setActiveNav);
