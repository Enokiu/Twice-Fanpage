const angle = 20;
const rotateCard = window;

const lerp = (start, end, amount) => {
	return (1 - amount) * start + amount * end;
};

const remap = (value, oldMax, newMax) => {
	const newValue = ((value + oldMax) * (newMax * 2)) / (oldMax * 2) - newMax;
	return Math.min(Math.max(newValue, -newMax), newMax);
};

window.addEventListener("DOMContentLoaded", (event) => {
	const cards = document.querySelectorAll(".card");
	cards.forEach((e) => {
		e.addEventListener("mousemove", (event) => {
			const rect = e.getBoundingClientRect();
			const centerX = (rect.left + rect.right) / 2;
			const centerY = (rect.top + rect.bottom) / 2;
			const posX = event.pageX - centerX;
			const posY = event.pageY - centerY;
			const x = remap(posX, rect.width / 2, angle);
			const y = remap(posY, rect.height / 2, angle);
			e.dataset.rotateX = x;
			e.dataset.rotateY = -y;
		});

		e.addEventListener("mouseout", (event) => {
			e.dataset.rotateX = 0;
			e.dataset.rotateY = 0;
		});
	});

	const update = () => {
		cards.forEach((e) => {
			let currentX = parseFloat(e.style.getPropertyValue('--rotateY').slice(0, -1));
			let currentY = parseFloat(e.style.getPropertyValue('--rotateX').slice(0, -1));
			if (isNaN(currentX)) currentX = 0;
			if (isNaN(currentY)) currentY = 0;
			const x = lerp(currentX, e.dataset.rotateX, 0.05);
			const y = lerp(currentY, e.dataset.rotateY, 0.05);
			e.style.setProperty("--rotateY", x + "deg");
			e.style.setProperty("--rotateX", y + "deg");
		})
	}
	setInterval (update,1000/60)
});


// JavaScript, um die Höhe des Headers anzupassen
window.addEventListener('load', function () {
	const header = document.querySelector('.header');
	const imageMax = document.querySelector('.image-max');

	if (header && imageMax) {
		header.style.height = imageMax.clientHeight + 'px';
	}
});

// Parallax-Effekt und dunkler Header beim Scrollen sticky machen
window.addEventListener('load', function () {
	const header = document.querySelector('.header');
	const imageMax = document.querySelector('.image-max');
	const background = document.querySelector('.background');
	const darkHeader = document.querySelector('.dark-header'); // Fehlendes Element darkHeader hinzufügen
  
	if (header && imageMax) {
	  header.style.height = imageMax.clientHeight + 'px';
	}
  
	// Initialisiere den dunklen Header als sticky
	darkHeader.style.backgroundColor = '#333';
	darkHeader.style.height = '80px';
	darkHeader.style.position = 'sticky';
	darkHeader.style.top = '0';
  
	window.addEventListener('scroll', () => {
	  const scrollY = window.scrollY;
	  const translateY = scrollY / 2;
  
	  // Prüfe, ob der Header die obere Seite erreicht hat, und ändere die Position entsprechend
	  if (scrollY >= imageMax.clientHeight) {
		darkHeader.style.position = 'fixed';
	  } else {
		darkHeader.style.position = 'sticky';
	  }
  
	  imageMax.style.transform = `translateY(${translateY}px)`;
	  background.style.transform = `translateY(${translateY}px)`;
	});
  
	// Initialisierung
	header.style.height = `${imageMax.offsetHeight}px`;
  });
  


