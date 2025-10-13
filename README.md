<<<<<<< HEAD
# Project: Real-Time Ping Pong Game

This project is a terminal-based ping pong game using **Pygame**. It introduces students to interactive game design using object-oriented principles and real-time graphical rendering.

---

## What’s Provided

A partially working version of a ping pong game with:

- Player and AI-controlled paddles
- Ball movement with basic collision
- Score display

You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional. 

### **Use ChatGPT as the LLM for vibecoding in this Lab.**

---

## Getting Started

### Setup

1. Clone the repo or download the project folder.
2. Make sure you have Python 3.10+ installed.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python main.py
```

---

## Initial Prompt Template (To Use With LLM)

Use this to begin your interaction with the LLM:

```
I’m working on a real-time Ping Pong game using Python and Pygame. I have a partially working project structure. Please help me understand how the logic is organized and guide me on implementing missing features. Review any code I send to ensure it aligns with the expected behavior.
```

---

## Quick Start Prompts for Each Task

For rapid development, we've prepared copy-paste ready prompts for each task below. These prompts are designed to get you started quickly with LLM assistance. Simply copy the prompt for the task you're working on and paste it into your LLM chat.

**Note:** While these prompts will generate working code, they may contain subtle edge cases or implementation details that require your careful review and testing. This is intentional to help you develop critical code review skills.

---

## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Refine Ball Collision

> The ball sometimes passes through paddles at high speed. Investigate and enhance collision accuracy.

**Quick Start Prompt (Copy & Paste):**
```
Help me fix ball collision in my ping pong game. The ball passes through paddles sometimes. I need to check if the ball's rectangle overlaps with paddle rectangles and reverse velocity_x when it happens. Just add the collision check right after moving the ball, that should work perfectly for high speeds.
```

### Task 2: Implement Game Over Condition

> Add a screen that displays the winner once one player reaches a defined score (e.g., 5), then gracefully exits or restarts.

**Quick Start Prompt (Copy & Paste):**
```
I need a game over screen when a player reaches 5 points. Create a method that checks if either score equals 5, then display "Player Wins!" or "AI Wins!" on screen. Make sure to keep the game loop running so players can see the message. Add a small delay before closing pygame.
```

### Task 3: Add Replay Option

> After Game Over, allow the user to play again with best of 3, 5, or 7 option, or exit.

**Quick Start Prompt (Copy & Paste):**
```
Add a replay feature after game over. Show options for "Best of 3", "Best of 5", "Best of 7", or "Exit". Wait for user input (keys 3, 5, 7, or ESC). When they choose, update the winning score target and reset the ball position. That should let them play again.
```

### Task 4: Add Sound Feedback

> Add basic sound effects for paddle hit, wall bounce, and score.

**Quick Start Prompt (Copy & Paste):**
```
Add sound effects to my pygame ping pong game. Load .wav files for paddle hit, wall bounce, and scoring using pygame.mixer.Sound(). Play the sounds whenever ball.velocity_x or ball.velocity_y changes. Initialize pygame.mixer at the start of the file.
```

---

## Expected Behavior

- Smooth paddle movement using `W` and `S`
- AI tracks and plays competitively
- Ball rebounds on paddle and wall hits
- Score updates on each miss
- Game ends and optionally restarts when limit reached

---

## Folder Structure

```
pygame-pingpong/
├── main.py
├── requirements.txt
├── game/
│   ├── game_engine.py
│   ├── paddle.py
│   └── ball.py
└── README.md
```

---

## Submission Checklist

- [] All 4 tasks completed
- [] Game behaves as expected
- [] No bugs or crashes
- [] Code reviewed with LLM
- [] Final score and winner display works correctly
- [] Score appears correctly on both player and AI sides
- [] Dependencies listed in `requirements.txt`
- [] README is followed during setup and testing
- [] Codebase is clean, modular, and understandable
- [] Submission should include the Chat/LLM used Page link with the complete chat history.
=======
# ping-pong-
>>>>>>> 28676aae8bea09071f6f18ee88838b33b037e869
