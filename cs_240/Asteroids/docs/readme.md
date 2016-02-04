# Asteroids

This project is an Android game where users can build and fly spaceships to blow up asteroids to survive.

The purpose of this project is to learn how to understand a problem and decompose it into small, but meaningful parts and pieces.  Focus on naming objects and methods well and breaking down objects and functions so they have a single responsibility.

## Design Diagram

A Design Diagram is included in this project which decomposes the structure of the database and defines the objects used to build and run the game.

A `gamedata.json` file is included which defines the data needed to build and run the game.  This file will be parsed and loaded into a `SQLite3` database, which will be read and written to throughout the program lifecycle.  `docs/AsteroidsData.pdf` explains the data stored in Asteroids JSON files.
