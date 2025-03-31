// SFML Template.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <SFML/Graphics.hpp>

#define SCREEN_WIDTH 1024
#define SCREEN_HEIGHT 1024

int main()
{
    sf::RenderWindow window(sf::VideoMode(SCREEN_WIDTH, SCREEN_HEIGHT),
        "Awesome SFML");

    while (window.isOpen()) {
         sf::Event event;
        while (window.pollEvent(event)) {
            // handle events
            switch (event.type) {
            case sf::Event::Closed:
                window.close();
                break;
            }
        }
        // update game logic 

        // draw
        window.clear();

        // draw SFML object

        window.display();
    }
    return EXIT_SUCCESS;
}

