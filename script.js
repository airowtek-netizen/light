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
  ['fname', 'lname', 'femail', 'fphone', 'fmessage'].forEach(id => {
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

// ============ SEARCH FUNCTONALITY ============
document.addEventListener('DOMContentLoaded', () => {
  const searchIcon = document.getElementById('searchIcon');
  const searchOverlay = document.getElementById('searchOverlay');
  const closeSearch = document.getElementById('closeSearch');
  const searchInput = document.getElementById('searchInput');
  const searchResults = document.getElementById('searchResults');

  if (!searchIcon || !searchOverlay) return;

  const searchData = [
    { title: 'Photogrammetry', category: 'Services', url: 'services.html#photogrammetry' },
    { title: 'LiDAR Processing', category: 'Services', url: 'services.html#lidar' },
    { title: 'Orthophoto', category: 'Services', url: 'services.html#orthophoto' },
    { title: 'CAD / GIS', category: 'Services', url: 'services.html#cad-gis' },
    { title: 'Scan to BIM', category: 'Services', url: 'services.html#bim' },
    { title: 'Mobile Mapping', category: 'Services', url: 'services.html#mobile-mapping' },
    { title: 'Infrastructure', category: 'Industries', url: 'industries.html' },
    { title: 'Urban Planning', category: 'Industries', url: 'industries.html' },
    { title: 'Mining', category: 'Industries', url: 'industries.html' },
    { title: 'Agriculture', category: 'Industries', url: 'industries.html' },
    { title: 'Smart Cities', category: 'Industries', url: 'industries.html' },
    { title: 'Utilities', category: 'Industries', url: 'industries.html' }
  ];

  function openSearch(e) {
    e.preventDefault();
    searchOverlay.classList.add('active');
    searchInput.value = '';
    renderResults('');
    setTimeout(() => searchInput.focus(), 100);
  }

  function hideSearch() {
    searchOverlay.classList.remove('active');
  }

  function renderResults(query) {
    if (!query.trim()) {
      searchResults.innerHTML = '';
      return;
    }

    const q = query.toLowerCase();
    const filtered = searchData.filter(item =>
      item.title.toLowerCase().includes(q) ||
      item.category.toLowerCase().includes(q)
    );

    if (filtered.length === 0) {
      searchResults.innerHTML = '<div style="padding: 20px; color: var(--text-muted);">No results found.</div>';
      return;
    }

    searchResults.innerHTML = filtered.map(item => `
      <a href="${item.url}" class="search-result-item">
        <div class="search-result-title">${item.title}</div>
        <div class="search-result-category">${item.category}</div>
      </a>
    `).join('');
  }

  searchIcon.addEventListener('click', openSearch);
  closeSearch.addEventListener('click', hideSearch);
  searchOverlay.addEventListener('click', (e) => {
    if (e.target === searchOverlay) hideSearch();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && searchOverlay.classList.contains('active')) hideSearch();
  });

  searchInput.addEventListener('input', (e) => {
    renderResults(e.target.value);
  });
});

// Dynamic Hero Subtitle based on Video Time
document.addEventListener('DOMContentLoaded', () => {
  const video = document.getElementById('heroVideo');
  const subtitle = document.getElementById('dynamicSubtitle');

  if (video && subtitle) {
    const captions = [
      { start: 0, text: 'Infrastructure Monitoring & Asset Management' },
      { start: 3, text: 'Autonomous Aerial Surveys & Data Capture' },
      { start: 6, text: 'Urban Planning, 3D Modeling & Smart City Analytics' },
      { start: 9, text: 'Utility Grid Inspection & Right-of-Way Mapping' },
      { start: 12, text: 'Precision Agriculture & Crop Health Analysis' },
      { start: 15, text: 'Coastal Mapping, Bathymetry & Maritime Logistics' },
      { start: 18, text: 'Topographical Surveys & Volumetric Analysis' }
    ];

    let currentCaptionIndex = -1;

    video.addEventListener('timeupdate', () => {
      const time = video.currentTime;

      // Find the appropriate caption for the current time
      let newIndex = -1;
      for (let i = captions.length - 1; i >= 0; i--) {
        if (time >= captions[i].start) {
          newIndex = i;
          break;
        }
      }

      if (newIndex !== -1 && newIndex !== currentCaptionIndex) {
        currentCaptionIndex = newIndex;
        // Fade out
        subtitle.style.opacity = '0';
        setTimeout(() => {
          subtitle.textContent = captions[currentCaptionIndex].text;
          // Fade in
          subtitle.style.opacity = '1';
        }, 300); // Wait for fade out
      }
    });
  }
});
