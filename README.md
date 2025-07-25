# 👾 QuickDrop Game (Pygame) 🍬

![Catch the Objects Game Demo](https://via.placeholder.com/600x350?text=Screenshot+or+GIF+of+Catch+the+Objects+Game+in+Action)
*(Replace this placeholder image link with an actual screenshot or, ideally, an animated GIF of your Catch the Objects game running!)*

---

## ✨ Project Overview

This project is a simple, interactive arcade-style game developed using **Python** and the **Pygame** library. The objective of the game is for the player to control a moving catcher at the bottom of the screen to collect randomly falling objects, while avoiding missing too many.

This game serves as a practical demonstration of fundamental game development concepts, including:
* Real-time user input handling
* Object spawning and movement
* Collision detection
* Score tracking
* Managing different game states (active gameplay, game over).

---

## 🛠️ Technologies Used

* **Python:** The core programming language used to build the game's logic and structure.
  
* **Pygame:** A set of Python modules designed for writing video games, utilized for graphics rendering, managing the game loop, handling user input (keyboard), and detecting collisions.

---

## 🌟 Key Features

* **Player-Controlled Catcher:** Move the catcher left and right using arrow keys to catch falling objects.
  
* **Random Object Spawning:** Objects appear randomly from the top of the screen at varying X-coordinates.
  
* **Scoring System:** Points are awarded for each caught object.
  
* **Missed Object Tracking:** A counter tracks missed objects, leading to a "Game Over" state if a threshold is reached.
  
* **Game Over Screen:** Displays the final score and options to restart or quit.
  
* **Basic Collision Detection:** Accurately determines when an object is "caught" by the catcher.
  
* **Simple Game Loop:** Manages game updates, rendering, and event processing at a consistent frame rate.

---

## 📋 How to Run Locally

To get the "Catch the Objects" game running on your local machine:

1.  **Prerequisites:**
    * Ensure you have Python installed (Python 3.x is recommended).
    * You will need the Pygame library.

2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/leilas25/Catch-the-Objects-Game.git](https://github.com/leilas25/Catch-the-Objects-Game.git)
    ```

3.  **Navigate to the project directory:**
    ```bash
    cd Catch-the-Objects-Game
    ```
    *(Ensure your `main.py` file is directly within this directory, and any other assets are in their respective subfolders if applicable.)*

4.  **Install Pygame:**
    ```bash
    pip install pygame
    ```
    *(If you have a `requirements.txt` file in your repository, you can use `pip install -r requirements.txt` instead.)*

5.  **Run the game:**
    ```bash
    python main.py
    ```
    A new Pygame window should open, and the game will start.

---

## 🎮 Gameplay Instructions

* Use the **Left Arrow Key** to move the catcher to the left.
* Use the **Right Arrow Key** to move the catcher to the right.
* Catch as many falling pink circles as you can.
* The game ends if you miss 3 objects.
* On the "GAME OVER" screen, press **'R' to Restart** or **'Q' to Quit**.

---

## 💡 What I Learned

* **Pygame Initialization & Setup:** Practical experience setting up a Pygame window, managing display properties, and handling basic drawing operations.
  
* **Game Loop Implementation:** Deeper understanding of the core game loop structure, including event processing, game state updates, and rendering.
  
* **Collision Detection:** Implemented `colliderect` for precise interaction between game objects.
  
* **Randomization:** Used `random` module to control object spawning locations.
  
* **Game State Management:** Learned to transition between different game states (active gameplay, game over) and manage associated logic.
  
* **Score & UI Elements:** Implemented basic text rendering for displaying scores and game messages.
  
* **Keyboard Input:** Handled continuous and single-press keyboard inputs for player control.

---

## 📞 Contact

Feel free to connect with me:

* **GitHub:** [github.com/leilas25](https://github.com/leilas25)
* **LinkedIn:** https://www.linkedin.com/in/leila-sono
* **Email:** leilasono1@gmail.com
---
