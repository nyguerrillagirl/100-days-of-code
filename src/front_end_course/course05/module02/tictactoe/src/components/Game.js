import Board from './Board';
import { useState } from 'react';

export default function Game() {
    const [xIsNext, setXIsNext] = useState(true);
    const [history, setHistory] = useState([{
        squares: Array(9).fill(null),
    }]);    

    const currentSquares = history[history.length - 1].squares;

    function handlePlay(nextSquares) {
        setHistory([...history, { squares: nextSquares }]);
        setXIsNext(!xIsNext);
    }

    return (
        <div className="game">
            <div className="game-board">
                <Board xIsNext={xIsNext} squares={currentSquares} onPlay={handlePlay} />
            </div>
            <div className="game-info">
                <ol>{/* TODO */}</ol>
            </div>
        </div>
    );
}