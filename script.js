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
document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  
  if (hamburger && mobileMenu) {
    // Toggle menu on hamburger click
    hamburger.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = mobileMenu.classList.toggle('open');
      hamburger.classList.toggle('active', isOpen);
      document.body.classList.toggle('menu-open', isOpen);
    });

    // Close menu when a mobile menu link is clicked
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        hamburger.classList.remove('active');
        document.body.classList.remove('menu-open');
      });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (mobileMenu.classList.contains('open') &&
          !mobileMenu.contains(e.target) &&
          !hamburger.contains(e.target)) {
        mobileMenu.classList.remove('open');
        hamburger.classList.remove('active');
        document.body.classList.remove('menu-open');
      }
    });

    // Close menu on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileMenu.classList.contains('open')) {
        mobileMenu.classList.remove('open');
        hamburger.classList.remove('active');
        document.body.classList.remove('menu-open');
      }
    });
  }
});

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
