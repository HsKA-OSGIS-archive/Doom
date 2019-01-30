# Overview
This project was created by DOOM team, a team of MSc (International) Geomatics students at the Karlsruhe University of Applied Sciences. The task was to create trash reporting system for Karlsruhe city. When someone find waste outside from trash or the trash is overloaded he/she can to report the corresponding authority using mobile device. Anyone can inform authority using their mobile just take a picture, take coordinate from picture and submit to web system. While users submit the location coordinate through geocoder, the location will appear in the web map. This application based one python, postgreSql, and javascript. Python is used for backend development, PostgreSQL used for database and leaflet javascript library is used for front development.

# Database Setup
This guide is assuming that you wish to simply use the sample data that is available in this repository.
Set up your PostgreSQL database by following the guide provided by the PostgreSQL wiki.
Install pgAdminIII or pgAdmin4 from the pgAdmin website. This step is not necessary but recommended for beginners, as it provides a visual interface in which to perform the remaining steps.
Create a database, either in pgAdmin or manually from the command line.
Set up the required extensions by executing the following queries on this new database:
CREATE EXTENSION postgis

# Libraries used
**OS_path-** This module implements some useful functions on pathnames. To read or write files see open(), and for accessing the filesystem see the os module. The path parameters can be passed as either strings, or bytes. 
Flask - Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. Wikipedia
 
 
**WTForms-** WTForms is a flexible forms validation and rendering library for Python web development. It is framework agnostic and can work with whatever web framework and template engine you choose. 
 
**Passlib.hass -** The passlib.hash module contains all the password hash algorithms built into Passlib. While each hash has its own options and output format, they all inherit from the PasswordHash base interface. 
 
**Functool -** The functools module is for higher-order functions: functions that act on or return other functions. In general, any callable object can be treated as a function for the purposes of this module.
 
**Flask-mail -** The Flask-Mail extension provides a simple interface to set up SMTP with Flask application and to send messages from views and scripts.
 
**Datetime-** The datetime module supplies classes for manipulating dates and times in both simple and complex ways.
geopy.geocoders - geopy is a Python 2 and 3 client for several popular geocoding web services. geopy makes it easy for Python developers to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoders and other data sources.
JSON- 
**Geo-Json-** This library implements all the `GeoJSON Objects`_ described in `The GeoJSON Format Specification`_. The objects contained in GeometryCollection and FeatureCollection can be indexed directly.
 
**UUID-** This module provides immutable UUID objects (the UUID class) and the functions uuid1(), uuid3(), uuid4(), uuid5() for generating version 1, 3, 4, and 5 UUIDs as specified in RFC 4122.
Fileinput- This module implements a helper class and functions to quickly write a loop over standard input or a list of files. If you just want to read or write one file see open().

# JAVASCRIPT Library
* jQuery
* Openlayers
* Bootstrap
* Leaflet
* AJAX

 
# Team Members
1. Kristóf
2. Md Raqibul Islam
3. Oliver Hennhöfer
4. Shaiful Islam
5. Yair Preiss

 
 
# License information
MIT license: Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
