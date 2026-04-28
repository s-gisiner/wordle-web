async function startGame(filename) {
    const response = await fetch(`/static/game/words/${filename}`);
    const text = await response.text();
    
    words = text.split('\n').map(w => w.trim().toUpperCase()).filter(w => w.length === 5);
    
    targetWord = words[Math.floor(Math.random() * words.length)];
    console.log("Target word:", targetWord);

    resetBoard();
}

function resetBoard() {
    attempts = 0;

    const board = document.getElementById("game-board");
    board.innerHTML = "";

    for (let i = 0; i < 6; i++) {
        const row = document.createElement("div");
        row.className = "game-row";
        row.id = `row-${i}`;

        for (let j = 0; j < 5; j++) {
            const tile = document.createElement("div");
            tile.className = "tile"; // Base styling
            row.appendChild(tile);
        }

        board.appendChild(row);
    }

    const input = document.getElementById("guess-input");
    input.value = "";
    input.hidden = false;
    input.focus();

    const submitButton = document.getElementById("submit-guess");
    submitButton.hidden = false;
}

window.startGame = startGame;