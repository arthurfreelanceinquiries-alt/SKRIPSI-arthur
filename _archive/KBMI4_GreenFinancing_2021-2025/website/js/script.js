(function() {
    'use strict';

    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    const navLinks = document.querySelectorAll('.nav-link');
    const navbar = document.getElementById('navbar');
    const sections = document.querySelectorAll('section[id]');
    const revealElements = document.querySelectorAll('.reveal');
    const statValues = document.querySelectorAll('.stat-value[data-target]');
    const barItems = document.querySelectorAll('.bar-item[data-value]');
    const backToTop = document.getElementById('backToTop');
    const yearElements = document.querySelectorAll('[data-year]');

    let lastScrollY = window.scrollY;

    function initMobileMenu() {
        if (!navToggle || !navMenu) return;

        navToggle.addEventListener('click', () => {
            const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
            navToggle.setAttribute('aria-expanded', !isExpanded);
            navMenu.classList.toggle('open');
            document.body.style.overflow = isExpanded ? '' : 'hidden';
        });

        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navToggle.setAttribute('aria-expanded', 'false');
                navMenu.classList.remove('open');
                document.body.style.overflow = '';
            });
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navMenu.classList.contains('open')) {
                navToggle.setAttribute('aria-expanded', 'false');
                navMenu.classList.remove('open');
                document.body.style.overflow = '';
                navToggle.focus();
            }
        });
    }

    function updateActiveNavLink() {
        const scrollPos = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + sectionId) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    function handleNavbarScroll() {
        const currentScrollY = window.scrollY;

        if (currentScrollY > 50) {
            navbar.style.boxShadow = 'var(--shadow-md)';
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        } else {
            navbar.style.boxShadow = 'none';
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        }

        lastScrollY = currentScrollY;
    }

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    function initRevealAnimations() {
        revealElements.forEach(el => revealObserver.observe(el));
    }

    function animateCountUp(element) {
        const target = parseFloat(element.getAttribute('data-target'));
        const suffix = element.getAttribute('data-suffix') || '';
        const duration = 1800;
        const startTime = performance.now();
        const isDecimal = target % 1 !== 0;

        function updateCount(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easedProgress = 1 - Math.pow(1 - progress, 3);
            const current = target * easedProgress;

            if (isDecimal) {
                element.textContent = current.toFixed(1) + suffix;
            } else {
                element.textContent = Math.floor(current) + suffix;
            }

            if (progress < 1) {
                requestAnimationFrame(updateCount);
            } else {
                element.textContent = target + suffix;
            }
        }

        requestAnimationFrame(updateCount);
    }

    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCountUp(entry.target);
                statsObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5
    });

    function initStatAnimations() {
        statValues.forEach(el => statsObserver.observe(el));
    }

    function animateBars(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const barItem = entry.target;
                const value = parseFloat(barItem.getAttribute('data-value'));
                const isPositive = barItem.getAttribute('data-positive') === 'true';
                const bar = barItem.querySelector('.bar');

                const maxValue = 0.385;
                const widthPercent = (value / maxValue) * 100;

                setTimeout(() => {
                    bar.style.width = widthPercent + '%';
                }, 200);

                barObserver.unobserve(barItem);
            }
        });
    }

    const barObserver = new IntersectionObserver(animateBars, {
        threshold: 0.3
    });

    function initBarAnimations() {
        barItems.forEach(el => barObserver.observe(el));
    }

    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;

                const target = document.querySelector(targetId);
                if (target) {
                    e.preventDefault();
                    const offsetTop = target.offsetTop - 70;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                    target.focus({ preventScroll: true });
                }
            });
        });
    }

    function handleResize() {
        if (!navToggle || !navMenu) return;
        if (window.innerWidth >= 768 && navMenu.classList.contains('open')) {
            navToggle.setAttribute('aria-expanded', 'false');
            navMenu.classList.remove('open');
            document.body.style.overflow = '';
        }
    }

    function initBackToTop() {
        if (!backToTop) return;

        const toggleVisibility = () => {
            backToTop.classList.toggle('visible', window.scrollY > 400);
        };

        window.addEventListener('scroll', toggleVisibility, { passive: true });

        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        toggleVisibility();
    }

    function initDynamicYear() {
        if (!yearElements.length) return;
        const currentYear = String(new Date().getFullYear());
        yearElements.forEach(el => {
            el.textContent = currentYear;
        });
    }

    function init() {
        initMobileMenu();
        initRevealAnimations();
        initStatAnimations();
        initBarAnimations();
        initSmoothScroll();
        initBackToTop();
        initDynamicYear();

        window.addEventListener('scroll', () => {
            updateActiveNavLink();
            handleNavbarScroll();
        }, { passive: true });

        window.addEventListener('resize', handleResize);

        updateActiveNavLink();
        handleNavbarScroll();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();