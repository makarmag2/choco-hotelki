/* ============================================
   ШОКОЛАДНЫЕ ХОТЕЛКИ — Main Script v3
   Серьезный темный стиль, непрерывный графонистый шлейф
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

    // ---------- GRAPHICAL CONTINUOUS RIBBON CURSOR TRAIL ----------
    const canvas = document.getElementById('cursorCanvas');
    const ctx = canvas.getContext('2d');
    
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    const trail = [];
    const MAX_POINTS = 45;      // длина шлейфа для супер-плавности
    let mouse = { x: -200, y: -200 };
    let target = { x: -200, y: -200 };
    let prevMouse = { x: -200, y: -200 };

    window.addEventListener('mousemove', (e) => {
        target.x = e.clientX;
        target.y = e.clientY;
    });

    window.addEventListener('mouseleave', () => {
        target.x = -200;
        target.y = -200;
    });

    const renderTrail = () => {
        ctx.clearRect(0, 0, width, height);

        // Мягкое экспоненциальное сглаживание к мыши
        if (mouse.x < -100) {
            mouse.x = target.x;
            mouse.y = target.y;
            prevMouse.x = target.x;
            prevMouse.y = target.y;
        } else {
            prevMouse.x = mouse.x;
            prevMouse.y = mouse.y;
            mouse.x += (target.x - mouse.x) * 0.32;
            mouse.y += (target.y - mouse.y) * 0.32;
        }

        // Если есть движение, добавляем сглаженные точки (с суб-шагом при быстром взмахе)
        if (mouse.x > 0 && mouse.y > 0) {
            const dx = mouse.x - prevMouse.x;
            const dy = mouse.y - prevMouse.y;
            const dist = Math.hypot(dx, dy);

            if (dist > 14) {
                // Добавляем промежуточную точку для идеального закругления
                trail.unshift({
                    x: prevMouse.x + dx * 0.5,
                    y: prevMouse.y + dy * 0.5,
                    age: 1.0
                });
            }

            trail.unshift({ x: mouse.x, y: mouse.y, age: 1.0 });
        }

        // Плавное угасание возраста точек
        for (let i = trail.length - 1; i >= 0; i--) {
            trail[i].age -= 0.024;
            if (trail[i].age <= 0 || trail.length > MAX_POINTS) {
                trail.splice(i, 1);
            }
        }

        // Отрисовка непрерывной изогнутой ленты шлейфа
        if (trail.length > 2) {
            ctx.save();
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';

            // 1-й слой: Широкое мягкое золотистое свечение
            ctx.shadowColor = 'rgba(212, 175, 106, 0.75)';
            ctx.shadowBlur = 18;

            for (let i = 0; i < trail.length - 1; i++) {
                const p1 = trail[i];
                const p2 = trail[i + 1];
                const midX = (p1.x + p2.x) * 0.5;
                const midY = (p1.y + p2.y) * 0.5;

                const progress = i / trail.length;
                const smoothFade = Math.pow(1 - progress, 1.4);
                const alpha = Math.max(0, p1.age * smoothFade);
                const lineWidth = smoothFade * 13 + 1.2;

                ctx.beginPath();
                ctx.moveTo(p1.x, p1.y);
                ctx.quadraticCurveTo(p1.x, p1.y, midX, midY);
                ctx.strokeStyle = `rgba(212, 175, 106, ${alpha * 0.6})`;
                ctx.lineWidth = lineWidth;
                ctx.stroke();
            }

            // 2-й слой: Яркий шелковистый стержень (Core Beam)
            ctx.shadowColor = '#ffffff';
            ctx.shadowBlur = 6;

            for (let i = 0; i < trail.length - 1; i++) {
                const p1 = trail[i];
                const p2 = trail[i + 1];
                const midX = (p1.x + p2.x) * 0.5;
                const midY = (p1.y + p2.y) * 0.5;

                const progress = i / trail.length;
                const smoothFade = Math.pow(1 - progress, 1.6);
                const alpha = Math.max(0, p1.age * smoothFade);
                const lineWidth = smoothFade * 4.8 + 0.6;

                ctx.beginPath();
                ctx.moveTo(p1.x, p1.y);
                ctx.quadraticCurveTo(p1.x, p1.y, midX, midY);
                ctx.strokeStyle = `rgba(255, 255, 255, ${alpha * 0.95})`;
                ctx.lineWidth = lineWidth;
                ctx.stroke();
            }

            ctx.restore();
        }

        requestAnimationFrame(renderTrail);
    };

    renderTrail();

    // Отключаем на смартфонах/тачскринах
    if ('ontouchstart' in window) {
        canvas.style.display = 'none';
    }

    // ---------- STICKY HEADER ----------
    const header = document.getElementById('header');

    const onScroll = () => {
        header.classList.toggle('header--scrolled', window.scrollY > 40);
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // ---------- MOBILE MENU ----------
    const burger = document.getElementById('burger');
    const nav = document.getElementById('nav');

    burger.addEventListener('click', () => {
        burger.classList.toggle('active');
        nav.classList.toggle('active');
    });

    nav.querySelectorAll('.nav__link').forEach(link => {
        link.addEventListener('click', () => {
            burger.classList.remove('active');
            nav.classList.remove('active');
        });
    });

    // ---------- SCROLL REVEAL ----------
    const reveals = document.querySelectorAll('.reveal');

    const revealObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.15,
            rootMargin: '0px 0px -40px 0px',
        }
    );

    reveals.forEach(el => revealObserver.observe(el));

    // ---------- ORDER MODAL ----------
    const modal = document.getElementById('orderModal');
    const modalBackdrop = document.getElementById('modalBackdrop');
    const modalClose = document.getElementById('modalClose');
    const modalProduct = document.getElementById('modalProduct');
    const modalTg = document.getElementById('modalTg');
    const modalWa = document.getElementById('modalWa');

    const TELEGRAM_USERNAME = 'rgr2';
    const WHATSAPP_NUMBER = '7900148867';

    const openModal = (productName) => {
        modalProduct.textContent = productName;

        const text = encodeURIComponent(
            `Здравствуйте! Хочу заказать: ${productName}`
        );

        modalTg.href = `https://t.me/${TELEGRAM_USERNAME}?text=${text}`;
        modalWa.href = `https://wa.me/${WHATSAPP_NUMBER}?text=${text}`;

        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    };

    const closeModal = () => {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    };

    document.querySelectorAll('[data-order]').forEach(btn => {
        btn.addEventListener('click', () => {
            openModal(btn.dataset.order);
        });
    });

    modalClose.addEventListener('click', closeModal);
    modalBackdrop.addEventListener('click', closeModal);

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
    });

    // ---------- SMOOTH SCROLL ----------
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const targetId = anchor.getAttribute('href');
            if (targetId === '#') return;
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

});
