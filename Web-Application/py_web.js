const themeToggle = document.getElementById('themeToggle');
const body= document.body;

const savedTheme = localStorage.getItem('theme');
if(savedTheme ==='light'){
    body.classList.add('light');
    themeToggle.textContent = '☀️';
}
else{
    themeToggle.textContent = '🌙';
}

themeToggle.addEventListener('click', ()=>{
    body.classList.toggle('light');

    if (body.classList.contains('light')){
        themeToggle.textContent = '☀️';
        localStorage.setItem('theme', 'light');
    } else {
        themeToggle.textContent ='🌙';
        localStorage.setItem('theme', 'dark');
    }
});

const animationObserver = new IntersectionObserver((entries) =>{
    entries.forEach(entry =>{
        if(entry.isIntersecting){
            entry.target.classList.add('visible');
            animationObserver.unobserve(entry.target);
        }
    });
}, {
    rootMargin: '0px 0px -10% 0px'
});

const animatedElements = document.querySelectorAll('.project-card, .skills-section, .footer');
animatedElements.forEach((element) =>{
    animationObserver.observe(element);
});

