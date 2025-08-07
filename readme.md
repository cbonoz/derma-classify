# Reddit Bug Bites Image Analysis

This notebook uses PRAW (Python Reddit API Wrapper) to pull the r/bugbites subreddit, analyze comments for bug types, and download images with structured naming conventions.
<!-- https://www.reddit.com/r/bugbites/ -->

## Features:
- Pulls posts from r/bugbites
- Analyzes comments to identify bug types
- Downloads images with naming convention: `BUGTYPE_N.jpg`
- Handles rate limiting and error handling
- Saves metadata about scraped content
