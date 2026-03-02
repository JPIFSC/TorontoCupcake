document.addEventListener('DOMContentLoaded', () => {
	const nav = document.getElementById('nav');

	if (!nav) {
		return;
	}

	const toggleNavOnScroll = () => {
		if (window.scrollY > 24) {
			nav.classList.add('scrolled');
			return;
		}

		nav.classList.remove('scrolled');
	};

	toggleNavOnScroll();
	window.addEventListener('scroll', toggleNavOnScroll, { passive: true });
});
