// Theme toggle
(function() {
  const toggle = document.getElementById('theme-toggle');
  const html = document.documentElement;

  function getPreferred() {
    const stored = localStorage.getItem('theme');
    if (stored) return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function apply(theme) {
    html.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }

  apply(getPreferred());

  if (toggle) {
    toggle.addEventListener('click', function() {
      const current = html.getAttribute('data-theme');
      apply(current === 'dark' ? 'light' : 'dark');
    });
  }
})();

// Mobile nav toggle
(function() {
  const btn = document.getElementById('nav-toggle');
  const nav = document.getElementById('main-nav');
  if (btn && nav) {
    btn.addEventListener('click', function() {
      nav.classList.toggle('open');
    });
  }
})();

// ToC active link tracking
(function() {
  const tocLinks = document.querySelectorAll('.toc-wrapper nav a');
  if (!tocLinks.length) return;

  const headings = [];
  tocLinks.forEach(function(link) {
    const id = link.getAttribute('href').replace('#', '');
    const el = document.getElementById(id);
    if (el) headings.push({ el: el, link: link });
  });

  function updateActive() {
    let active = headings[0];
    for (var i = 0; i < headings.length; i++) {
      if (headings[i].el.getBoundingClientRect().top <= 100) {
        active = headings[i];
      }
    }
    tocLinks.forEach(function(l) { l.classList.remove('active'); });
    if (active) active.link.classList.add('active');
  }

  window.addEventListener('scroll', updateActive, { passive: true });
  updateActive();
})();
