# Flaskify

A poor, browser based, imitation of Spotify using one's own music collection.

I should play most formats (mp3, ogg, flac, m4a) and will automatically scan a given directory for music files.

## Technology

It uses Python 3 and Flask for a backend and AngularJS 2 for the frontend.

## Not even Alpha

This project isn't even Alpha yet so it's futile trying to use it.

## Desired Features

* Play songs
* Play play albums
* Playlists (on the go and saved)
* Automatically detect metadata then guess it based on file structure if required
* Be able to edit song metadata
* Cover art
* Be able to play music on server (ie a Raspberry Pi)

## Configuration

To run the program you need to specify a `MUSIC_DIR` variable. This should be a full path string to a folder in your static directory (ie '/home/example/www/flaskify/static/music').

We recommend creating a system link from a Music directory elsewhere.
