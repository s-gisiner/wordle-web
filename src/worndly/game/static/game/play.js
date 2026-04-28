async function startGame(filename) {
    const response = await fetch(`/static/game/words/${filename}`);
    const text = await response.text();
    
    words = text.split('\n').map(w => w.trim().toUpperCase()).filter(w => w.length === 5);
    
    targetWord = words[Math.floor(Math.random() * words.length)];
    console.log("Target word:", targetWord);
}

window.startGame = startGame;