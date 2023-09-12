# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.7.0] - 2023-11-09

### Added

- added next turn funtion to scrabbelgame.
- add validate word inside board to test board.
- add validate word outside board to test board.

### Fixed

- fixed cell test due to low coverage report.
- fixed funtion __init__ from Class scrabbel game.

## [0.6.0] - 2023-28-08

### Added 

- Class Player with the following funtions: __init__.
- Class Scrabbel with the following funtions: __init__.

## [0.5.0] - 2023-27-08

### Added

- Class Board with the following funtions: __init__.
- Class Cell with the followinf funtions: __init__, add_letter, Calculate_value.

### Fixed

- Fixed test errors for the Tiles code.

## [0.4.0] - 2023-22-08

### Fixed

- Fixed value errors in the letters.

### Changed

- Optimizing Class BagTiles to reduce the amount of lines in the code by 
grouping repeated letters.

## [0.3.0] - 2023-21-08

### Added

- Add letters to BagTiles.

### Changed

- Changed test for the Tiles code to match the new amount of letters.

## [0.2.0] - 2023-20-08

### Changed

- Add letters to BagTiles.


## [0.1.0] - 2023-18-08

### Added

 - This CHANGELOG to document the changes to the project Scrabble.
 - Tests folder to contain every unit test that verify that the individual units of the source code fulfill their expected functionality. 
 - Game folder to contain every file that make the game work.
 - Class Tiles with following funtion: __init__
 - Class BagTiles with following funtions: __init__, take, put.