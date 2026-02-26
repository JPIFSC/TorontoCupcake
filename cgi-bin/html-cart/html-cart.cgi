<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-TCFWH7NT');</script>
    <!-- End Google Tag Manager -->

    <!-- Meta Tags for SEO SMO -->
    <meta name="description" content="Review your order and purchase delicious cupcakes from Toronto Cupcake. Enjoy a seamless ordering experience for the sweetest treats in town.">
    <meta name="keywords" content="cupcakes, gourmet cupcakes, bakery, Toronto, Toronto Cupcake, cupcake delivery">
    <!-- Open Graph Meta Tags (OG) for Social Media Optimization -->
    <meta property="og:title" content="Toronto Cupcake - Gourmet Cupcakes Delivered to Your Doorstep">
    <meta property="og:description" content="Toronto Cupcake offers freshly baked gourmet cupcakes daily.">
    <meta property="og:image" content="https://www.torontocupcake.com/images/default-image.jpg">
    <meta property="og:url" content="https://www.torontocupcake.com">
    <meta property="og:type" content="website">

    <!-- Meta for twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Toronto Cupcake - The Sweetest Bakery in Town">
    <meta name="twitter:description" content="Enjoy a selection of gourmet cupcakes at Toronto Cupcake.">
    <meta name="twitter:image" content="https://www.torontocupcake.com/images/default-image.jpg">
    <meta name="author" content="Toronto Cupcake">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Toronto Cupcake | Your Shopping Cart</title>
    <link rel="stylesheet" href="../../css/torontocupcake.css">
    <!-- <link rel="stylesheet" href="../../css/torontocupcake.css"> -->
    <link rel="shortcut icon" href="../../favicon.ico" />
    <link rel="canonical" href="../../index.html" />
    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/smoothness/jquery-ui.css">
    <!-- Organization Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Toronto Cupcake",
      "url": "https://www.torontocupcake.com",
      "logo": "https://www.torontocupcake.com/images/logo.png",
      "sameAs": ["https://www.instagram.com/torontocupcake"],
      "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+1-877-334-9468",
        "contactType": "Customer Service"
      }
    }
    </script>
<style>
    /* Table styles for cart display */
    .cart-table  {
        width: 100%;
        border-collapse: collapse;
    }
    .cart-table th, .cart-table td {
        border: 1px solid #ddd;
        padding: 8px;
    }
    .header-row {
        background-color: #8C1822;
        color: #ffffff;
        font-weight: bold;
    }
    .footer-row {
        background-color: #f4f4f4;
        font-weight: bold;
    }
    .total-item-row {
        font-weight: normal;
        background-color: #fff;
    }
    .cart-divider {
        border: 0;
        border-top: 2px solid #8C1822;
    }
    
    /* Datepicker styles */
    .ui-datepicker {
        background: white;
        border: 1px solid #ccc;
        padding: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    .ui-datepicker-calendar td a {
        color: black !important;
        text-decoration: none;
    }
    .ui-datepicker-unselectable .ui-state-disabled {
        color: #ccc !important;
    }
    .ui-datepicker-prev, .ui-datepicker-next {
        cursor: pointer;
        color: #333;
    }
    .ui-datepicker-title {
        color: #333;
    }
    
    /* Form layout */
    .form-section {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }
    .form-column {
        flex: 1;
        min-width: 300px;
    }
    .form-label {
        display: block;
        margin-bottom: 5px;
        font-weight: bold;
    }
    .form-input, .floating-input, #pickup-time {
        width: 100%;
        padding: 10px;
        font-size: 1rem;
        border: 2px solid #888;
        border-radius: 8px;
        outline: none;
        box-sizing: border-box;
        transition: border-color 0.3s;
    }
    .form-input:focus, .floating-input:focus, #pickup-time:focus {
        border-color: #8C1822;
    }
    .form-subheading {
        font-size: 1.2rem;
        margin-bottom: 15px;
        color: #333;
    }

    /* Important section styling */
    .important-section {
        margin-top: 20px;
        padding: 15px;
        background-color: #fefefe;
        border: 1px solid #ccc;
        border-radius: 8px;
    }
    
    /* Floating label for inputs */
    .floating-label {
        position: absolute;
        top: 10px;
        left: 12px;
        color: #888;
        font-size: 1rem;
        pointer-events: none;
        background-color: white;
        padding: 0 4px;
        border-radius: 4px;
        transition: 0.2s ease all;
    }
    .floating-input:focus ~ .floating-label,
    .floating-input:not(:placeholder-shown) ~ .floating-label,
    #pickup-time:focus ~ .floating-label,
    #pickup-time:not(:placeholder-shown) ~ .floating-label {
        top: -8px;
        left: 8px;
        font-size: 0.85rem;
        color: #333;
    }

    .form-input:focus ~ .inline-label,
    .form-input:not(:placeholder-shown) ~ .inline-label {
        top: -1.1em;
        font-size: 0.85rem;
        color: #333;
    }

    /* Delivery time section styling */
    #delivery-time-section {
        position: relative;
        border: 2px solid #888;
        border-radius: 8px;
        padding: 20px;
        box-sizing: border-box;
        transition: border-color 0.3s;
        margin-top: 15px;
    }
    #delivery-time-section:focus-within {
        border-color: #8C1822;
    }
    /* Updated styling for Delivery Time section */
    /* Delivery Time Container Styling */
    .delivery-time-container {
        background-color: #fefefe; /* Matching other input backgrounds */
        border: 2px solid #888;
        border-radius: 8px;
        padding: 15px;
        box-sizing: border-box;
        margin-top: 15px;
    }

    /* Align the "Delivery Times" label with the border */
    #delivery-time-header {
        position: absolute;
        top: -10px;
        left: 12px;
        padding: 0 4px;
        background-color: #fefefe; /* Background to blend with the container */
        font-size: 1rem;
        color: #888;
    }

    /* Full-width styling for Pickup Time input to match label */
    #pickup-time {
        width: 100%; /* Ensures input spans full width */
        padding: 10px;
        font-size: 1rem;
        border: 2px solid #888;
        border-radius: 8px;
        box-sizing: border-box;
    }

    /* Floating label for pickup time input */
    #pickup-time ~ .floating-label {
        left: 12px;
        color: #888;
        top: 8px;
        font-size: 1rem;
        transition: 0.2s ease all;
    }

    /* Adjust floating label when input is focused or contains text */
    #pickup-time:focus ~ .floating-label,
    #pickup-time:not(:placeholder-shown) ~ .floating-label {
        top: -10px;
        font-size: 0.85rem;
        color: #333;
    }

    /* Radio options styling for alignment */
    .radio-options {
        display: flex;
        flex-direction: column;
        gap: 5px;
        font-size: 0.95rem;
        color: #333;
    }
    .radio-options label {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .radio-options input[type="radio"] {
        transform: scale(1.1);
    }
    /* Additional Delivery or Pickup Date styling */
    .input-container {
        position: relative;
        margin-top: 20px;
        width: 100%;
        max-width: 100%;
    }

    /* Inline label for "Delivery or Pickup Date" */
    .input-container .inline-label {
        position: absolute;
        top: -0.6em;
        left: 12px;
        padding: 0 4px;
        font-size: 1rem;
        color: #888;
        background-color: white;
        border-radius: 4px;
        transition: 0.2s ease all;
        white-space: nowrap;
        pointer-events: none;
    }

    /* Adjust label position when input is focused or contains text */
    .input-container .floating-input:focus ~ .inline-label,
    .input-container .floating-input:not(:placeholder-shown) ~ .inline-label {
        top: -1.1em;
        left: 8px;
        font-size: 0.85rem;
        color: #333;
    }

    /* Instructions styling below date picker */
    .form-instructions {
        font-size: 0.85rem;
        color: #666;
        margin-top: 5px;
    }

    /* Radio buttons group styling */
    .radio-group {
    display: flex;
    gap: 15px;
    margin-top: 10px;
    font-size: 1rem;
    color: #333;
    flex-wrap: wrap; /* This allows wrapping to a new line */
    }
    /* Notification container */
    .notification {
        background-color: #D95A4E;
        color: #ffffff; /* White text */
        padding: 15px;
        margin: 15px 0;
        border-radius: 8px; /* Rounded corners */
        font-size: 1rem;
        line-height: 1.4;
        display: block;
        justify-content: space-between;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
        max-width: 100%; /* Responsive width */
    }

    /* Icon or close button styling within notification, if needed */
    .notification .icon,
    .notification .close-btn {
        margin-left: 10px;
        cursor: pointer;
        color: #ffffff;
        font-size: 1.2rem;
    }

    /* Ensure the text wraps on smaller screens */
    @media (max-width: 768px) {
        .notification {
            font-size: 0.9rem;
            padding: 10px;
        }
    }
    .notification p {
        display: block;
        margin: 0; /* Reset margin if thereâs unwanted spacing */
    }
    .notification, .notification p {
        color: #ffffff !important; /* Ensure text is white */
    }
    /* Ensure form-row uses flexbox for better alignment */
    .form-row {
        display: flex;
        flex-direction: column;
        position: relative;
        margin-bottom: 20px;
    }

    /* Adjust label styling for inline alignment */
    .inline-label {
        position: absolute;
        top: -8px; /* Adjust as necessary to align with the border */
        left: 12px; /* Aligns with input padding */
        font-size: 0.85rem;
        color: #888;
        background-color: white;
        padding: 0 4px;
        pointer-events: none;
        transition: 0.2s ease all;
        z-index: 1;
    }

    /* Adjust input styling to have consistent padding */
    .form-input {
        padding: 16px 10px 10px; /* Adjusted top padding for label space */
        font-size: 1rem;
        border: 2px solid #888;
        border-radius: 8px;
        width: 100%;
        box-sizing: border-box;
        outline: none;
        transition: border-color 0.3s;
    }

    /* Hover and focus state for better UI feedback */
    .form-input:focus {
        border-color: #8C1822;
    }

    /* Adjust floating behavior of label when input is focused */
    .form-input:focus ~ .inline-label,
    .form-input:not(:placeholder-shown) ~ .inline-label {
        top: -8px;
        left: 12px;
        font-size: 0.75rem;
        color: #333;
        background-color: white;
        padding: 0 4px;
    }

    .icon-delete {
        width: 24px;
        height: 24px;
        cursor: pointer;
        transition: transform 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease;
    }

    /* Hover effect with shadow */
    .icon-delete:hover {
        transform: scale(1.1);        /* Slightly enlarges the icon */
        opacity: 0.8;                 /* Reduces opacity for a soft effect */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); /* Adds shadow on hover */
    }
    .price-column, .amount-column {
        text-align: right;
        font-family: Tahoma, monospace; /* Monospace for number alignment */
        padding-right: 10px;
    }
    .price-column:hover, .amount-column:hover {
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2); /* Subtle shadow on hover */
    }
    .table-wrapper {
        display: flex;
        justify-content: flex-end; /* Aligns to the right on large screens */
        padding: 10px;
        box-sizing: border-box;
        width: 100%;
    }

    .totals-table {
    width: 100%;
    max-width: 500px;
    font-family: Tahoma, Arial, sans-serif;
    font-size: 1.1rem;
    border-collapse: collapse;
    margin: auto;
}
.totals-table th, .totals-table td {
    padding: 8px;
    text-align: right;
    border-bottom: 1px solid #ddd;
}

.totals-table th {
    background-color: #8C1822;
    color: #ffffff;
    font-weight: bold;
    text-align: right;
}

.totals-table td {
    font-family: Tahoma, monospace;
}

.totals-table .item-column {
    width: 200px; /* Increase this if necessary */
    text-align: left;
    padding-left: 10px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
    .totals-table caption {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip: rect(1px, 1px, 1px, 1px); /* Screen reader only */
}
.totals-table .amount-column,
.totals-table .price-column {
    min-width: 80px; /* Minimum width to prevent wrapping */
    text-align: right;
    padding-right: 10px;
}

    /* Responsive Design: Center table on smaller screens */
    @media (max-width: 768px) {
        .table-wrapper {
            justify-content: center; /* Center-aligns on mobile */
            padding: 0;
        }
        .totals-table {
            max-width: 100%; /* Full width on mobile */
            margin: auto;
        }
    }
    .actions-container {
        display: flex;
        justify-content: space-between; /* Distribute buttons evenly */
        gap: 10px; /* Space between buttons */
        margin-top: 20px; /* Space above the buttons */
    }

    .actions-container form {
        flex: 1; /* Makes each button take up equal space */
    }
    
</style>
</head>

<body>
    <a href="html-cart.cgi?action=display_cart&amp;page=cupcakes.html#main-content" class="skip-link">Skip to main content</a>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TCFWH7NT" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->

    <header class="masthead" role="banner">
        <div class="logo-container">
            <img src="../../images/transparent-TO-logo.png" alt="Toronto Cupcake Logo" class="logo">
            <img src="../../images/transparent-TO-logo.png" alt="Toronto Cupcake Logo" class="logo" aria-hidden="true">
            <img src="../../images/transparent-TO-logo.png" alt="Toronto Cupcake Logo" class="logo" aria-hidden="true">
            <img src="../../images/transparent-TO-logo.png" alt="Toronto Cupcake Logo" class="logo" aria-hidden="true">
            <img src="../../images/transparent-TO-logo.png" alt="Toronto Cupcake Logo" class="logo" aria-hidden="true">
            <img src="../../images/transparent-TO-logo.png" alt="Toronto Cupcake Logo" class="logo" aria-hidden="true">
            <img src="../../images/transparent-TO-logo.png" alt="Toronto Cupcake Logo" class="logo" aria-hidden="true">
            <img src="../../images/transparent-TO-logo.png" alt="Toronto Cupcake Logo" class="logo" aria-hidden="true">
        </div>

        <div class="pink-bar">
            <span class="openNav" aria-label="Open Navigation">&#9776;</span>
            <span class="date-text"></span>
            <span class="promo-text"><a href="html-cart.cgi?action=display_cart&amp;page=cupcakes.html#" aria-label="Check out our new Corporate event logo cupcakes">Check out our new Corporate event logo cupcakes</a></span>
        </div>
    </header>

    <!-- Sidenav (Hamburger Menu) -->
    <div id="mySidenav" class="sidenav" role="navigation" aria-label="Main Navigation" aria-live="polite">
        <a href="../../index.html" aria-label="Toronto Cupcake's home page">HOME</a>
        <a href="../../about.html" aria-label="About Toronto Cupcake">ABOUT</a>
        <a href="../../CorporateEvents.html" aria-label="Page for Corporate events">CORPORATE EVENTS</a>
        <a href="../../occasions.html" aria-label="Some occasions Toronto Cupcake supports">OCCASIONS</a>
        <div class="submenu-parent">
            <a href="html-cart.cgi?action=display_cart&amp;page=cupcakes.html#" class="submenu-toggle" aria-expanded="false" aria-controls="submenu1" aria-label="Expand Cupcake options">CUPCAKES</a>
            <ul id="submenu1" class="submenu" aria-hidden="true">
                <li><a href="../../cupcakes.html#Always-Available" aria-label="Cupcakes available every day">ALWAYS AVAILABLE</a></li>
                <li><a href="../../cupcakes.html#Holidays" aria-label="Cupcakes available for different holidays">HOLIDAYS</a></li>
                <li><a href="../../cupcakes.html#Special-Events" aria-label="Cupcakes available for special events">SPECIAL EVENTS</a></li>
                <li><a href="../../cupcakes.html#Custom" aria-label="Cupcakes customized">CUSTOM</a></li>
            </ul>
        </div>
        <a href="../../givingback.html" aria-label="Toronto Cupcake's community page">COMMUNITY</a>
        <a href="../../faqs.html" aria-label="Toronto Cupcake Facts and Questions">FAQs</a>
        <a href="../../resources.html" aria-label="Resources that might prove helpful">RESOURCES</a>
        <a href="../../contact.html" aria-label="Toronto Cupcake contact information">CONTACT</a>
        <a href="../../delivery.html" aria-label="Toronto Cupcake delivery">CUPCAKE DELIVERY</a>
        <a href="html-cart.cgi?action=display_cart&amp;page=cupcakes.html" aria-label="Shopping Cart">VIEW CART</a>
    </div>

    <main id="main-content">
        <div class="content  responsive-image">
  
    <h1 id="cart"; ></h1>
                <div class="DATA" >

    <div class="empty_cart">
        <p align="center">Your shopping cart is empty.</p>
        <a href="../../cupcakes.html" class="btn">Continue Shopping</a>
    </div>
    			</div>
            </td>
          </tr>
       </table>
  </div>
    </main>

<!-- Footer Section  -->
<footer class="footer" role="contentinfo">
    <div class="footer-container">
        <!-- Quick Navigation -->
        <div class="footer-nav">
            <a href="../../index.html" aria-label="Home Page">Home</a>
            <a href="../../about.html" aria-label="About Toronto Cupcake">About</a>
            <a href="../../contact.html" aria-label="Toronto Cupcake contact information">Contact</a>
            <a href="../../CorporateEvents.html" aria-label="Page for Corporate events">Corporate Events</a>
            <a href="../../cupcakes.html" aria-label="Cupcakes">Cupcakes</a>
            <a  href="../../occasions.html" aria-label="Some occasions Toronto Cupcake supports">Occasions</a>
            <a href="../../privacy.html" aria-label="Privacy Policy">Privacy Policy</a>
            <a href="https://www.torontocupcake.com/cgi-bin/html-cart/EmploymentOpportunites.html" aria-label="Employment Opportunities">Careers</a>
        </div>
        <button class="btn" id="contrast-toggle" aria-pressed="false" aria-label="Toggle high contrast mode">Toggle High Contrast</button>
        <!-- Social Media (optional) -->
        <div class="footer-social">
            <a href="https://www.instagram.com/torontocupcake/" target="_blank">
                <img src="../../images/instagram-white.webp" alt="Instagram">
            </a>
            <a href="https://bsky.app/profile/torontocupcake.bsky.social" target="_blank">
                <img src="../../images/Bluesky_Logo.png" alt="Blue Sky">
            </a>

            <!-- Add other social media icons if needed -->
        </div>
        
        <!-- Copyright -->
        <div class="footer-copyright">
            &copy; 2024 Toronto Cupcake. All rights reserved.
        </div>
    </div>
</footer>

    <!-- Scripts -->
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            console.log('Scripts loaded: DOMContentLoaded event fired');
        
            // Utility: Apply high contrast mode
            function setupContrastToggle() {
                const contrastToggle = document.getElementById('contrast-toggle');
                const body = document.body;
        
                if (!contrastToggle) {
                    console.error('Contrast toggle button not found');
                    return;
                }
        
                const prefersHighContrast = window.matchMedia('(prefers-contrast: more)');
        
                function applyHighContrast(isHighContrast) {
                    body.classList.toggle('high-contrast', isHighContrast);
                    localStorage.setItem('high-contrast', isHighContrast);
                    contrastToggle.setAttribute('aria-pressed', isHighContrast.toString());
                }
        
                const savedContrast = localStorage.getItem('high-contrast');
                if (savedContrast === 'true') {
                    applyHighContrast(true);
                } else if (savedContrast === 'false') {
                    applyHighContrast(false);
                } else if (prefersHighContrast.matches) {
                    applyHighContrast(true);
                }
        
                contrastToggle.addEventListener('click', () => {
                    const isCurrentlyHighContrast = body.classList.contains('high-contrast');
                    applyHighContrast(!isCurrentlyHighContrast);
                });
        
                prefersHighContrast.addEventListener('change', (e) => {
                    if (localStorage.getItem('high-contrast') === null) {
                        applyHighContrast(e.matches);
                    }
                });
            }
    
                    // Sidenav Setup
            function setupSidenav() {
            const sidenav = document.getElementById('mySidenav');
            const openNavButton = document.querySelector('.openNav');
            if (!sidenav || !openNavButton) return;
  
            function openNav() {
                sidenav.classList.add('open');
                document.body.classList.add('sidenav-open');
            }
  
            function closeNav() {
                sidenav.classList.remove('open');
                document.body.classList.remove('sidenav-open');
            }
  
            openNavButton.addEventListener('click', openNav);
            const sidenavSubmenuToggles = sidenav.querySelectorAll('.submenu-toggle');

            sidenavSubmenuToggles.forEach((toggle) => {
                toggle.addEventListener('click', function (event) {
                    event.preventDefault();
                    event.stopPropagation();

                    const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
                    toggle.setAttribute('aria-expanded', (!isExpanded).toString());

                    const submenu = sidenav.querySelector(`#${toggle.getAttribute('aria-controls')}`);
                    submenu.setAttribute('aria-hidden', isExpanded.toString());

                    toggle.parentElement.classList.toggle('open');
                });
            });

            // Close sidenav when clicking outside or on a regular link (except submenu toggles)
            document.addEventListener('click', function (event) {
                const isSubmenuToggle = event.target.closest('.submenu-toggle');
                if (!sidenav.contains(event.target) && !event.target.closest('.openNav') && !isSubmenuToggle) {
                    sidenav.querySelectorAll('.submenu-parent.open').forEach((parent) => {
                        parent.classList.remove('open');
                        parent.querySelector('.submenu-toggle').setAttribute('aria-expanded', 'false');
                        parent.querySelector('.submenu').setAttribute('aria-hidden', 'true');
                    });
                    sidenav.classList.remove('open');
                    document.body.classList.remove('sidenav-open');
                }
            });
            }
        
            // Utility: Lazy loading for images
            function setupLazyLoading() {
                const images = document.querySelectorAll('img[data-src]');
                const observer = new IntersectionObserver((entries) => {
                    entries.forEach((entry) => {
                        if (entry.isIntersecting) {
                            const img = entry.target;
                            img.src = img.dataset.src;
                            observer.unobserve(img);
                        }
                    });
                });
        
                images.forEach((img) => observer.observe(img));
            }
        
            // Utility: Accordion functionality
            function setupAccordion() {
                document.querySelectorAll('.accordion-btn').forEach((button) => {
                    button.addEventListener('click', () => {
                        const expanded = button.getAttribute('aria-expanded') === 'true';
                        button.setAttribute('aria-expanded', !expanded);
                        const content = button.nextElementSibling;
                        content.style.display = expanded ? 'none' : 'block';
                    });
                });
            }
        
            // Utility: Update Toronto date and time
            function updateDateTime() {
                const options = { timeZone: 'America/Toronto', weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
                const now = new Date().toLocaleString('en-CA', options);
                document.querySelector('.date-text').textContent = `${now} - Toronto`;
            }
        
            // Initialize all utilities
            setupContrastToggle();
            setupSidenav();
            setupLazyLoading();
            setupAccordion();
            updateDateTime();
        });
        </script>
        
        <script>
            document.addEventListener('DOMContentLoaded', () => {
                const disabledDaysSet = new Set([
                    "10-14-2025","10-15-2025","10-16-2025","10-17-2025","10-18-2025","10-19-2025","11-7-2025","11-8-2025","11-23-2025","12-4-2025","12-18-2025","12-19-2025","12-20-2025","12-25-2025","1-25-2026","1-27-2026","2-21-2026","2-22-2026"
                ]);
        
                const isDateDisabled = (date) => {
                    const formattedDate = `${date.getMonth() + 1}-${date.getDate()}-${date.getFullYear()}`;
                    const isDisabled = disabledDaysSet.has(formattedDate);
                    return [!isDisabled, "", isDisabled ? "Unavailable date" : ""];
                };
        
                const getTorontoTime = () => {
                    const options = { timeZone: "America/Toronto", hour: "numeric", hourCycle: "h23" };
                    const torontoHour = new Intl.DateTimeFormat("en-CA", options).format(new Date());
                    return parseInt(torontoHour, 10);
                };
        
                const currentTorontoHour = getTorontoTime();
                const minDateOffset = currentTorontoHour < 17 ? 1 : 2;
        
                const datepickerField = $('#datepicker1');
                const errorMessage = document.getElementById('datepickerError');
                const form = document.querySelector('form'); // Update with your form's ID if necessary
        
                // Regex pattern for expected date format: "Friday, January 24, 2025"
                const dateFormatRegex = /^[A-Za-z]+,\s[A-Za-z]+\s\d{1,2},\s\d{4}$/;
        
                // Initialize datepicker
                datepickerField.datepicker({
                    dateFormat: 'DD, MM d, yy',
                    beforeShowDay: isDateDisabled,
                    minDate: minDateOffset,
                    numberOfMonths: 2,
                    onSelect: function () {
                        errorMessage.style.display = 'none'; // Hide error on valid selection
                        datepickerField.removeClass('error-highlight'); // Remove highlight
                    }
                });
        
                // Adjust datepicker for responsiveness
                window.addEventListener('resize', () => {
                    datepickerField.datepicker('option', 'numberOfMonths', window.innerWidth < 768 ? 1 : 2);
                });
        
                // Validate the date format on form submission
                form.addEventListener('submit', (event) => {
                    const dateValue = datepickerField.val().trim();
        
                    if (!dateFormatRegex.test(dateValue)) {
                        // Show error message
                        errorMessage.textContent = 'Please select a valid date in the format: Day, Month Date, Year.';
                        errorMessage.style.display = 'inline';
        
                        // Add visual cue (red border) and focus on the field
                        datepickerField.addClass('error-highlight').focus();
        
                        // Prevent form submission
                        event.preventDefault();
                    } else {
                        // Hide error if the date is valid
                        errorMessage.style.display = 'none';
                        datepickerField.removeClass('error-highlight'); // Remove highlight
                    }
                });
        
                // Hide error when refocusing on the date field
                datepickerField.on('focus', function () {
                    errorMessage.style.display = 'none';
                    datepickerField.removeClass('error-highlight'); // Remove highlight
                });
            });
        </script>
<script>
    function toggleFields() {
        // Get the selected option for Pickup_Status
        const isDeliverySelected = document.querySelector('input[name="Pickup_Status"][value="Deliver"]').checked;
        
        // Get the delivery and pickup sections
        const deliveryTimeSection = document.getElementById("delivery-time-section");
        const pickupTimeSection = document.getElementById("pickup-time-section");

        // Show/hide sections based on the selected radio button
        if (isDeliverySelected) {
            deliveryTimeSection.style.display = "block";
            pickupTimeSection.style.display = "none";
        } else {
            deliveryTimeSection.style.display = "none";
            pickupTimeSection.style.display = "block";
        }
    }

    // Initialize the correct visibility on page load
    document.addEventListener('DOMContentLoaded', toggleFields);
</script>
<!-- Tawk -->
<script type="text/javascript">
    var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
    (function(){
    var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
    s1.async=true;
    s1.src='https://embed.tawk.to/647d6f3f7957702c744bc774/1h24vl45j';
    s1.charset='UTF-8';
    s1.setAttribute('crossorigin','*');
    s0.parentNode.insertBefore(s1,s0);
    })();
    </script>  
<!-- End of Tawk -->
    <datalist id="countries">
        <option value="Canada"></option>
        <option value="United States"></option>
        <option value="Afghanistan"></option>
        <option value="Albania"></option>
        <option value="Algeria"></option>
        <option value="Andorra"></option>
        <option value="Angola"></option>
        <option value="Antigua and Barbuda"></option>
        <option value="Argentina"></option>
        <option value="Armenia"></option>
        <option value="Australia"></option>
        <option value="Austria"></option>
        <option value="Azerbaijan"></option>
        <option value="Bahamas"></option>
        <option value="Bahrain"></option>
        <option value="Bangladesh"></option>
        <option value="Barbados"></option>
        <option value="Belarus"></option>
        <option value="Belgium"></option>
        <option value="Belize"></option>
        <option value="Benin"></option>
        <option value="Bhutan"></option>
        <option value="Bolivia"></option>
        <option value="Bosnia and Herzegovina"></option>
        <option value="Botswana"></option>
        <option value="Brazil"></option>
        <option value="Brunei"></option>
        <option value="Bulgaria"></option>
        <option value="Burkina Faso"></option>
        <option value="Burundi"></option>
        <option value="Cabo Verde"></option>
        <option value="Cambodia"></option>
        <option value="Cameroon"></option>
        <option value="Canada"></option>
        <option value="Central African Republic"></option>
        <option value="Chad"></option>
        <option value="Chile"></option>
        <option value="China"></option>
        <option value="Colombia"></option>
        <option value="Comoros"></option>
        <option value="Congo, Democratic Republic of the"></option>
        <option value="Congo, Republic of the"></option>
        <option value="Costa Rica"></option>
        <option value="Cote d'Ivoire"></option>
        <option value="Croatia"></option>
        <option value="Cuba"></option>
        <option value="Cyprus"></option>
        <option value="Czech Republic"></option>
        <option value="Denmark"></option>
        <option value="Djibouti"></option>
        <option value="Dominica"></option>
        <option value="Dominican Republic"></option>
        <option value="Ecuador"></option>
        <option value="Egypt"></option>
        <option value="El Salvador"></option>
        <option value="Equatorial Guinea"></option>
        <option value="Eritrea"></option>
        <option value="Estonia"></option>
        <option value="Eswatini"></option>
        <option value="Ethiopia"></option>
        <option value="Fiji"></option>
        <option value="Finland"></option>
        <option value="France"></option>
        <option value="Gabon"></option>
        <option value="Gambia"></option>
        <option value="Georgia"></option>
        <option value="Germany"></option>
        <option value="Ghana"></option>
        <option value="Greece"></option>
        <option value="Grenada"></option>
        <option value="Guatemala"></option>
        <option value="Guinea"></option>
        <option value="Guinea-Bissau"></option>
        <option value="Guyana"></option>
        <option value="Haiti"></option>
        <option value="Honduras"></option>
        <option value="Hungary"></option>
        <option value="Iceland"></option>
        <option value="India"></option>
        <option value="Indonesia"></option>
        <option value="Iran"></option>
        <option value="Iraq"></option>
        <option value="Ireland"></option>
        <option value="Israel"></option>
        <option value="Italy"></option>
        <option value="Jamaica"></option>
        <option value="Japan"></option>
        <option value="Jordan"></option>
        <option value="Kazakhstan"></option>
        <option value="Kenya"></option>
        <option value="Kiribati"></option>
        <option value="Korea, North"></option>
        <option value="Korea, South"></option>
        <option value="Kuwait"></option>
        <option value="Kyrgyzstan"></option>
        <option value="Laos"></option>
        <option value="Latvia"></option>
        <option value="Lebanon"></option>
        <option value="Lesotho"></option>
        <option value="Liberia"></option>
        <option value="Libya"></option>
        <option value="Liechtenstein"></option>
        <option value="Lithuania"></option>
        <option value="Luxembourg"></option>
        <option value="Madagascar"></option>
        <option value="Malawi"></option>
        <option value="Malaysia"></option>
        <option value="Maldives"></option>
        <option value="Mali"></option>
        <option value="Malta"></option>
        <option value="Marshall Islands"></option>
        <option value="Mauritania"></option>
        <option value="Mauritius"></option>
        <option value="Mexico"></option>
        <option value="Micronesia"></option>
        <option value="Moldova"></option>
        <option value="Monaco"></option>
        <option value="Mongolia"></option>
        <option value="Montenegro"></option>
        <option value="Morocco"></option>
        <option value="Mozambique"></option>
        <option value="Myanmar"></option>
        <option value="Namibia"></option>
        <option value="Nauru"></option>
        <option value="Nepal"></option>
        <option value="Netherlands"></option>
        <option value="New Zealand"></option>
        <option value="Nicaragua"></option>
        <option value="Niger"></option>
        <option value="Nigeria"></option>
        <option value="North Macedonia"></option>
        <option value="Norway"></option>
        <option value="Oman"></option>
        <option value="Pakistan"></option>
        <option value="Palau"></option>
        <option value="Panama"></option>
        <option value="Papua New Guinea"></option>
        <option value="Paraguay"></option>
        <option value="Peru"></option>
        <option value="Philippines"></option>
        <option value="Poland"></option>
        <option value="Portugal"></option>
        <option value="Qatar"></option>
        <option value="Romania"></option>
        <option value="Russia"></option>
        <option value="Rwanda"></option>
        <option value="Saint Kitts and Nevis"></option>
        <option value="Saint Lucia"></option>
        <option value="Saint Vincent and the Grenadines"></option>
        <option value="Samoa"></option>
        <option value="San Marino"></option>
        <option value="Sao Tome and Principe"></option>
        <option value="Saudi Arabia"></option>
        <option value="Senegal"></option>
        <option value="Serbia"></option>
        <option value="Seychelles"></option>
        <option value="Sierra Leone"></option>
        <option value="Singapore"></option>
        <option value="Slovakia"></option>
        <option value="Slovenia"></option>
        <option value="Solomon Islands"></option>
        <option value="Somalia"></option>
        <option value="South Africa"></option>
        <option value="South Sudan"></option>
        <option value="Spain"></option>
        <option value="Sri Lanka"></option>
        <option value="Sudan"></option>
        <option value="Suriname"></option>
        <option value="Sweden"></option>
        <option value="Switzerland"></option>
        <option value="Syria"></option>
        <option value="Taiwan"></option>
        <option value="Tajikistan"></option>
        <option value="Tanzania"></option>
        <option value="Thailand"></option>
        <option value="Timor-Leste"></option>
        <option value="Togo"></option>
        <option value="Tonga"></option>
        <option value="Trinidad and Tobago"></option>
        <option value="Tunisia"></option>
        <option value="Turkey"></option>
        <option value="Turkmenistan"></option>
        <option value="Tuvalu"></option>
        <option value="Uganda"></option>
        <option value="Ukraine"></option>
        <option value="United Arab Emirates"></option>
        <option value="United Kingdom"></option>
        <option value="United States"></option>
        <option value="Uruguay"></option>
        <option value="Uzbekistan"></option>
        <option value="Vanuatu"></option>
        <option value="Vatican City"></option>
        <option value="Venezuela"></option>
        <option value="Vietnam"></option>
        <option value="Yemen"></option>
        <option value="Zambia"></option>
        <option value="Zimbabwe"></option>
    </datalist> 

</body>

</html>
