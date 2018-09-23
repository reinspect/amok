![AMOK](https://image.prntscr.com/image/861SmuubRlS2DpZ6of7n-g.png)

[![Build](https://travis-ci.org/reinspect/amok.svg?branch=master)](https://travis-ci.org/reinspect/amok) [![License](https://img.shields.io/github/license/reinspect/amok.svg)](https://github.com/reinspect/amok/blob/master/LICENSE) ![Downloads](https://img.shields.io/github/downloads/reinspect/amok/total.svg) [![Donate](https://img.shields.io/badge/Donate-PayPal-009cde.svg)](https://paypal.me/reinspect)

AMOK is a Clean, Organized, and Simple Web Server running by Python.
## Features
- Flexible Configuration
- Supports HTML
- Runs in the Background *(Optional)*

## To-do
- Let's Encrypt Support
- Preprocessor Support (Handlebars, Pug, SASS, etc.)
---
## Prerequisites
- Python 3.x
- a Terminal (Command Prompt should work fine, too.)

## Installation
Just simply clone this repository into a directory!
```git
$ git clone https://github.com/reinspect/amok.git
```

## How to use?
To start AMOK:
```shell
$ python3 start.py
```
To stop AMOK:
```shell
$ python3 stop.py
```

## Configuration
```json
{
	"ip" : "127.0.0.1",
	"port" : 8000,
	"runInBackground" : 1,
	"publicDir" : "./public/www/",
	"errorDir" : "./public/error/",
	"indexFile" : "index.html",
	"error404" : "404.html"
}
```
To turn off your server from running in the background, set **runInBackground** to **0**

## Contributions
Here's a list of [Contributors](https://github.com/reinspect/amok/graphs/contributors)

## License
This Open-Source project was developed under the [MIT License](https://github.com/reinspect/amok/blob/master/LICENSE).

MIT © [Reinspect](https://github.com/reinspect)