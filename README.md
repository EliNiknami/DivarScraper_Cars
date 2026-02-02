# DivarScraper_Cars

A lightweight Scrapy-based crawler for collecting publicly available car advertisement data from Divar, focused on Mashhad.

This project is designed as a modular and extensible example of working with JSON-based APIs using Scrapy.

---

## Overview

The crawler retrieves car advertisement listings and their associated metadata through Divar’s public endpoints.  
It is structured following standard Scrapy project conventions to ensure clarity, maintainability, and ease of extension.

The project is intended for learning, experimentation, and research-oriented use cases.

---

## Features

- Scrapy-based architecture
- API-driven data collection (no HTML parsing)
- Pagination support
- Modular spider design
- Configurable output formats (JSON, CSV, etc.)

---
##How to Run
scrapy crawl divar_search

##Saving Output
scrapy crawl divar_search -O cars.json
scrapy crawl divar_search -O cars.csv




