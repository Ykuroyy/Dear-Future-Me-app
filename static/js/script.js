// ページ読み込み時のアニメーション
window.addEventListener('load', () => {
    const messageCard = document.querySelector('.message-card');
    messageCard.style.opacity = '0';
    messageCard.style.transform = 'translateY(20px)';
    
    setTimeout(() => {
        messageCard.style.transition = 'all 0.8s ease';
        messageCard.style.opacity = '1';
        messageCard.style.transform = 'translateY(0)';
    }, 100);
});

// リフレッシュボタンのアニメーション
const refreshBtn = document.querySelector('.refresh-btn');
if (refreshBtn) {
    refreshBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const icon = refreshBtn.querySelector('.btn-icon');
        icon.style.transform = 'rotate(360deg)';
        
        setTimeout(() => {
            location.reload();
        }, 300);
    });
}

// キラキラエフェクトの追加
function createSparkle() {
    const sparkle = document.createElement('span');
    sparkle.innerHTML = ['✨', '💫', '🌟'][Math.floor(Math.random() * 3)];
    sparkle.className = 'floating-sparkle';
    sparkle.style.left = Math.random() * window.innerWidth + 'px';
    sparkle.style.animationDuration = (Math.random() * 3 + 2) + 's';
    document.body.appendChild(sparkle);
    
    setTimeout(() => {
        sparkle.remove();
    }, 5000);
}

// 定期的にキラキラを生成
setInterval(createSparkle, 3000);

// スタイルの追加
const style = document.createElement('style');
style.textContent = `
    .floating-sparkle {
        position: fixed;
        top: -30px;
        font-size: 20px;
        animation: fall linear;
        pointer-events: none;
        z-index: 1000;
    }
    
    @keyframes fall {
        to {
            transform: translateY(calc(100vh + 30px)) rotate(360deg);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);