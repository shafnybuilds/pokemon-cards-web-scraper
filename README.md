# Pokedex Scraper AI

![Charizard](./assets/charizard.avif.png)

A production-ready web scraping pipeline for Pokemon data extraction and processing, designed for RAG (Retrieval-Augmented Generation) applications.

# Business Usecase
- problem -> Businesses can't feed messy data to LLMs. The data should be structured in order build a production ready RAG/Generative AI solution.
- Solution -> This project demonstrates production-level web scraping, data processing, and vector database integration suitable for modern AI applications and search systems.

## Project Overview

In this project I mainly implements a comprehensive data pipeline that scrapes Pokemon information from pokemondb.net and prepares it for AI-powered applications using vector databases and hybrid search capabilities.

## Key Features

### Web Scraping Architecture
- **Scrapy Framework**: Professional-grade web scraping with built-in concurrency and error handling
- **Sitemap-Based Discovery**: Automatically discovers Pokemon pages through XML sitemap parsing
- **Structured Data Pipeline**: Custom pipeline for data processing and storage
- **Respectful Scraping**: Implements 2-second download delays and robots.txt compliance

### Data Processing & Storage
- **Multi-Format Output**: Saves data in HTML, Markdown, and JSON formats
- **HTML to Markdown Conversion**: Uses markdownify for clean text extraction
- **Structured File Organization**: Organized directory structure for each Pokemon entry
- **Metadata Extraction**: Captures URLs, names, and structured metadata

### Vector Database Integration
- **Milvus/Zilliz Integration**: Production vector database setup for similarity search
- **Hybrid Search Architecture**: Combines dense embeddings with sparse BM25 vectors
- **Schema Management**: Structured collection schema with multiple field types
- **Advanced Indexing**: COSINE similarity indexing for vector fields

### Production-Ready Features
- **Environment Configuration**: Secure credential management through environment variables
- **Logging Framework**: Comprehensive logging for debugging and monitoring
- **Type Safety**: Full type hints for better code maintainability
- **Error Handling**: Robust error handling throughout the pipeline
- **Scalable Architecture**: Modular design for easy extension and modification

## Technical Stack

- **Web Scraping**: Scrapy, XPath, Regex
- **Data Processing**: Markdownify, PyYAML, JSON
- **Vector Database**: Milvus/Zilliz (PyMilvus)
- **Search Technology**: BM25 sparse vectors + dense embeddings
- **Infrastructure**: Python 3.11+, pathlib for cross-platform compatibility

## Architecture Highlights

### Hybrid Search Implementation
- **Dense Vectors**: 768-dimensional embeddings for semantic similarity
- **Sparse Vectors**: BM25 algorithm for keyword-based search
- **Combined Retrieval**: Best of both semantic and lexical search

### Data Pipeline Optimizations
- **Namespace-Aware XML Parsing**: Proper sitemap processing with XML namespaces
- **Regex-Based URL Filtering**: Efficient Pokemon page identification
- **Custom Scrapy Items**: Structured data models for type safety
- **Pipeline Modularity**: Separate processing stages for flexibility

### Vector Database Design
- **Auto-ID Primary Keys**: Efficient document identification
- **Dynamic Fields**: Flexible schema for varying Pokemon data
- **JSON Metadata Storage**: Rich metadata support
- **Full-Text Search**: Analyzer-enabled text fields for comprehensive search

## Best Practices Implemented

- **Ethical Scraping**: Respects robots.txt and implements reasonable delays
- **Clean Code**: Type hints, logging, and modular architecture
- **Error Resilience**: Graceful handling of network and parsing errors
- **Scalable Design**: Easy to extend for additional data sources
- **Security**: Environment-based configuration for sensitive credentials
- **Cross-Platform**: Uses pathlib for OS-independent file operations