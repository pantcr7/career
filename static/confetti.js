
    // Confetti BOOM when page loads
    window.onload = () => {
        // Big BOOM burst
        confetti({
            particleCount: 120,
            spread: 90,
            startVelocity: 60,
            origin: { y: 0.6 }
        });

        // Side bursts for extra vibe
        setTimeout(() => {
            confetti({
                particleCount: 80,
                angle: 60,
                spread: 55,
                origin: { x: 0 }
            });

            confetti({
                particleCount: 80,
                angle: 120,
                spread: 55,
                origin: { x: 1 }
            });
        }, 300);
    }
