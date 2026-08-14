/**
 * main.js
 * Presidential School Website Main JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {

    // --- 1. Language Switching System ---
    function switchLanguage(lang) {
        // Save to sessionStorage
        sessionStorage.setItem('lang', lang);
        
        // Update all elements with both data-uz and data-en attributes
        document.querySelectorAll('[data-uz][data-en]').forEach(el => {
            const translation = el.getAttribute(`data-${lang}`);
            if (translation) {
                el.textContent = translation;
            }
        });
        
        // Update language dropdown display text
        const display = document.getElementById('langDisplay');
        if (display) {
            display.textContent = lang === 'uz' ? "O'zbek" : 'English';
        }
    }

    // Initialize language from sessionStorage or default to 'uz'
    const currentLang = sessionStorage.getItem('lang') || 'uz';
    switchLanguage(currentLang);

    // --- 6. Language Dropdown ---
    const langDropdownEl = document.querySelector('.lang-dropdown');
    const langToggleBtn = document.getElementById('langToggle');
    const langOptions = document.getElementById('langOptions');
    
    if (langToggleBtn && langOptions && langDropdownEl) {
        langToggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            langOptions.classList.toggle('show');
            langDropdownEl.classList.toggle('open');
        });
        
        langOptions.querySelectorAll('[data-lang]').forEach(option => {
            option.addEventListener('click', (e) => {
                e.stopPropagation();
                const lang = option.getAttribute('data-lang');
                if (lang) {
                    // Update active state
                    langOptions.querySelectorAll('.lang-option').forEach(o => o.classList.remove('active'));
                    option.classList.add('active');
                    
                    switchLanguage(lang);
                    langOptions.classList.remove('show');
                    langDropdownEl.classList.remove('open');
                }
            });
        });
    }

    // --- 2. Partners Carousel ---
    const track = document.querySelector('.carousel-track');
    const prevBtn = document.querySelector('.carousel-arrow.prev');
    const nextBtn = document.querySelector('.carousel-arrow.next');
    
    if (track) {
        const items = Array.from(track.children);
        // Assuming cards are 200px wide with a 32px gap
        const itemWidth = 232; 
        let currentIndex = 0;
        let autoPlayInterval;
        
        const getVisibleCount = () => {
            const containerWidth = track.parentElement.offsetWidth;
            return Math.floor(containerWidth / itemWidth) || 1;
        };

        const updateCarousel = () => {
            track.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
            track.style.transition = 'transform 0.5s ease-in-out';
        };
        
        const moveNext = () => {
            const visibleCount = getVisibleCount();
            if (currentIndex >= items.length - visibleCount) {
                currentIndex = 0; // Jump back to start
            } else {
                currentIndex++;
            }
            updateCarousel();
        };

        const movePrev = () => {
            const visibleCount = getVisibleCount();
            if (currentIndex <= 0) {
                currentIndex = Math.max(0, items.length - visibleCount); // Jump to end
            } else {
                currentIndex--;
            }
            updateCarousel();
        };

        if (nextBtn) nextBtn.addEventListener('click', moveNext);
        if (prevBtn) prevBtn.addEventListener('click', movePrev);

        // Auto-play
        const startAutoPlay = () => {
            autoPlayInterval = setInterval(moveNext, 3000);
        };

        const stopAutoPlay = () => {
            clearInterval(autoPlayInterval);
        };

        // Pause on hover
        track.parentElement.addEventListener('mouseenter', stopAutoPlay);
        track.parentElement.addEventListener('mouseleave', startAutoPlay);
        
        startAutoPlay();
        
        // Handle resize
        window.addEventListener('resize', () => {
            const visibleCount = getVisibleCount();
            if (currentIndex > items.length - visibleCount) {
                currentIndex = Math.max(0, items.length - visibleCount);
                updateCarousel();
            }
        });
    }

    // --- 3. Mobile Menu ---
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const mobileNav = document.querySelector('.mobile-nav');
    
    if (mobileToggle && mobileNav) {
        const toggleMenu = (e) => {
            if (e) e.stopPropagation();
            mobileToggle.classList.toggle('active');
            mobileNav.classList.toggle('active');
            
            // Prevent body scroll when open
            if (mobileNav.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        };

        mobileToggle.addEventListener('click', toggleMenu);

        // Close when clicking a nav link
        mobileNav.querySelectorAll('a:not(.mobile-dropdown-toggle)').forEach(link => {
            link.addEventListener('click', () => {
                if (mobileNav.classList.contains('active')) toggleMenu();
            });
        });

        // Mobile dropdown accordions
        mobileNav.querySelectorAll('.mobile-dropdown-toggle').forEach(toggle => {
            toggle.addEventListener('click', (e) => {
                e.preventDefault();
                const menu = toggle.nextElementSibling;
                if (menu && menu.classList.contains('mobile-dropdown-menu')) {
                    const isOpen = menu.classList.contains('show');
                    
                    // Optional: Close other open menus in mobile nav
                    mobileNav.querySelectorAll('.mobile-dropdown-menu.show').forEach(m => m.classList.remove('show'));
                    mobileNav.querySelectorAll('.mobile-dropdown-toggle.active').forEach(t => t.classList.remove('active'));
                    
                    if (!isOpen) {
                        menu.classList.add('show');
                        toggle.classList.add('active'); // For chevron rotation via CSS
                    }
                }
            });
        });
    }

    // --- 4. Desktop Dropdown Menus ---
    const desktopDropdowns = document.querySelectorAll('.nav-dropdown');
    
    desktopDropdowns.forEach(dropdown => {
        let leaveTimeout;
        
        dropdown.addEventListener('mouseenter', () => {
            clearTimeout(leaveTimeout);
            dropdown.classList.add('open');
        });
        
        dropdown.addEventListener('mouseleave', () => {
            leaveTimeout = setTimeout(() => {
                dropdown.classList.remove('open');
            }, 200);
        });
        
        // Touch support (click toggle)
        const link = dropdown.querySelector('a');
        if (link) {
            link.addEventListener('click', (e) => {
                // If the device doesn't support hover, treat it as a click toggle
                if (window.matchMedia('(hover: none)').matches) {
                    e.preventDefault();
                    dropdown.classList.toggle('open');
                }
            });
        }
    });

    // --- 5. Scroll Effects ---
    const header = document.querySelector('.main-header');
    
    if (header) {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        };
        
        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll(); // Check initial scroll position
    }

    // Global click handler to close things when clicking outside
    document.addEventListener('click', (e) => {
        // Close language dropdown
        if (langOptions && langOptions.classList.contains('show') && !e.target.closest('.lang-dropdown')) {
            langOptions.classList.remove('show');
            if (langDropdownEl) langDropdownEl.classList.remove('open');
        }
        
        // Close mobile menu
        if (mobileNav && mobileNav.classList.contains('active') && !e.target.closest('.mobile-nav') && !e.target.closest('.mobile-menu-toggle')) {
            mobileToggle.classList.remove('active');
            mobileNav.classList.remove('active');
            document.body.style.overflow = '';
        }
    });
});
