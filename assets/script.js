// ============================================
// RESUME AI - LANDING PAGE SCRIPTS
// ============================================

/**
 * Configuration
 */
const CONFIG = {
    appUrl: 'http://localhost:8501',
    enableAnalytics: false,
    enableTracking: true,
    scrollBehavior: 'smooth'
};

/**
 * Launch the Streamlit application
 */
function launchApp() {
    // Redirect to the Streamlit app
    // Update the URL below to match your deployment URL
    window.location.href = CONFIG.appUrl; // For local development
    
    // For production, use:
    // window.location.href = 'https://your-streamlit-deployment-url.com';
}

/**
 * Show the demo modal
 */
function showDemo() {
    const modal = document.getElementById('demoModal');
    modal.style.display = 'block';
}

/**
 * Close the modal
 */
function closeModal() {
    const modal = document.getElementById('demoModal');
    modal.style.display = 'none';
}

/**
 * Close modal when clicking outside of it
 */
window.addEventListener('click', function(event) {
    const modal = document.getElementById('demoModal');
    if (event.target === modal) {
        closeModal();
    }
});

/**
 * Smooth scroll behavior for navigation links
 */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        
        // Don't prevent default for the launch/demo buttons
        if (href === '#launch') {
            return;
        }
        
        e.preventDefault();
        
        if (href === '#' || href === '') {
            return;
        }
        
        const target = document.querySelector(href);
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

/**
 * Add animation on scroll for feature cards
 */
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all feature cards
document.querySelectorAll('.feature-card, .step, .benefit-item').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(card);
});

/**
 * Add active state to navigation links based on scroll position
 */
window.addEventListener('scroll', function() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links a');
    
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

/**
 * Initialize on page load
 */
document.addEventListener('DOMContentLoaded', function() {
    console.log('Resume AI Landing Page Loaded');
    
    // Add any additional initialization code here
    initializeEventListeners();
});

/**
 * Initialize event listeners
 */
function initializeEventListeners() {
    // Add mouseenter event for feature cards
    document.querySelectorAll('.feature-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
    });
}

/**
 * Track page analytics events (optional)
 * You can integrate with Google Analytics or other tracking services
 */
function trackEvent(eventName, eventData = {}) {
    console.log('Event tracked:', eventName, eventData);
    
    // Store event in localStorage for analytics
    try {
        const events = JSON.parse(localStorage.getItem('landing_events') || '[]');
        events.push({
            name: eventName,
            data: eventData,
            timestamp: new Date().toISOString()
        });
        localStorage.setItem('landing_events', JSON.stringify(events.slice(-100))); // Keep last 100 events
    } catch (e) {
        console.warn('Could not track event:', e);
    }
    
    // Example: Send to Google Analytics
    // if (typeof gtag !== 'undefined') {
    //     gtag('event', eventName, eventData);
    // }
}

// Track CTA clicks
document.querySelectorAll('.btn-primary').forEach(button => {
    button.addEventListener('click', function() {
        trackEvent('cta_clicked', {
            cta_text: this.textContent.trim()
        });
    });
});
