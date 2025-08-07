"""
Bug bite classification constants for the derma-classify project.

This module contains all the classification dictionaries, keywords, and configuration
constants used for identifying different types of bug bites and skin conditions.
"""

# Define bug bite types with specific keywords (FIXED - removed overly generic terms)
BUG_TYPES = {
    'mosquito': [
        'mosquito', 'mosquitos', 'mosquitoes', 'skeeter', 'skeeters',
        'itchy', 'itching', 'itch', 'itches', 'scratching',
        'red bumps', 'small bumps', 'tiny bumps', 'welts', 'welt',
        'swollen', 'swelling', 'inflammation', 'inflamed'
    ],
    'spider': [
        'spider', 'spiders', 'arachnid', 'eight legs', 'web',
        'black widow', 'brown recluse', 'recluse', 'widow',
        'fang marks', 'fangs', 'puncture', 'necrosis', 'necrotic'
    ],
    'bed_bug': [
        'bed bug', 'bedbug', 'bed bugs', 'bedbugs',
        'hotel', 'motel', 'mattress', 'bed', 'sleeping',
        'line of bites', 'breakfast lunch dinner', 'three bites',
        'cluster', 'clustered', 'pattern', 'row'
    ],
    'flea': [
        'flea', 'fleas', 'pet', 'dog', 'cat', 'pets',
        'ankle', 'ankles', 'lower leg', 'feet', 'foot',
        'carpet', 'jumping', 'tiny bites'
    ],
    'tick': [
        'tick', 'ticks', 'lyme', 'bullseye', 'bulls eye',
        'hiking', 'woods', 'forest', 'outdoors', 'camping',
        'embedded', 'attached', 'circular rash', 'rash'
    ],
    'ant': [
        'ant', 'ants', 'fire ant', 'fire ants',
        'burning', 'burn', 'stinging', 'sting',
        'pustule', 'pustules', 'pus', 'white head'
    ],
    'bee': [
        'bee', 'bees', 'wasp', 'wasps', 'hornet', 'hornets',
        'sting', 'stinger', 'stung', 'swollen', 'allergic',
        'yellow jacket', 'bumble bee'
    ],
    'chigger': [
        'chigger', 'chiggers', 'harvest mite', 'red bug',
        'grass', 'tall grass', 'vegetation', 'mowing',
        'waistline', 'waist', 'belt line', 'socks'
    ],
    'mite': [
        'mite', 'mites', 'dust mite', 'scabies',
        'burrow', 'tunnels', 'between fingers', 'wrists'
    ],
    'unknown': [
        'unknown', 'unidentified', 'mystery', 'unclear', 'unsure'
        # REMOVED: 'bug', 'bite', 'what bit', 'help', 'identify' - these were too generic!
    ]
}

# Enhanced contextual clues for better classification
CONTEXTUAL_CLUES = {
    'location_hints': {
        'bed_bug': ['bed', 'mattress', 'hotel', 'motel', 'sleeping', 'woke up'],
        'flea': ['pet', 'dog', 'cat', 'ankle', 'lower leg', 'carpet'],
        'mosquito': ['outside', 'evening', 'dusk', 'water', 'pond', 'lake'],
        'tick': ['hiking', 'woods', 'forest', 'camping', 'outdoors', 'grass'],
        'spider': ['corner', 'basement', 'garage', 'shed', 'dark'],
        'chigger': ['grass', 'lawn', 'mowing', 'gardening']
    },
    'pattern_hints': {
        'bed_bug': ['line', 'row', 'breakfast lunch dinner', 'three', 'cluster'],
        'flea': ['multiple', 'scattered', 'random'],
        'mosquito': ['single', 'isolated', 'few'],
        'spider': ['two', 'pair', 'double', 'fang']
    },
    'symptom_hints': {
        'mosquito': ['itchy', 'itch', 'scratching', 'red', 'swollen'],
        'spider': ['pain', 'necrosis', 'spreading', 'severe'],
        'bee': ['swollen', 'allergic', 'immediate', 'painful'],
        'ant': ['burning', 'fire', 'pustule', 'pus']
    }
}

# Seasonal patterns for additional context
SEASONAL_PATTERNS = {
    'mosquito': ['summer', 'warm', 'humid', 'rain'],
    'tick': ['spring', 'summer', 'fall', 'warm weather'],
    'chigger': ['late summer', 'fall', 'humid']
}

# Reddit scraping strategy configurations
STRATEGY_CONFIGS = {
    'balanced': {
        'sort_method': 'top',
        'time_filter': 'month',
        'description': 'Top posts from past month with good engagement'
    },
    'discussion_heavy': {
        'sort_method': 'controversial',
        'time_filter': 'all',
        'description': 'Controversial posts (all time) that generate discussion'
    },
    'recent_active': {
        'sort_method': 'hot',
        'time_filter': 'week',
        'description': 'Currently hot posts from past week'
    },
    'controversial': {
        'sort_method': 'controversial',
        'time_filter': 'month',
        'description': 'Most controversial posts from past month'
    },
    'quality_focused': {
        'sort_method': 'top',
        'time_filter': 'year',
        'description': 'Highest quality posts from past year'
    }
}

# Comment upvote weighting tiers for community validation
COMMENT_SCORE_WEIGHTS = {
    'very_high': {'threshold': 10, 'multiplier': 2.5},
    'high': {'threshold': 5, 'multiplier': 2.0},
    'moderate': {'threshold': 2, 'multiplier': 1.5, 'use_avg': True},
    'slight': {'threshold': 1, 'multiplier': 1.2, 'use_avg': True},
    'none': {'threshold': 0, 'multiplier': 1.0}
}

# Weight values for different keyword types
KEYWORD_WEIGHTS = {
    'generic': 0.5,      # Very low weight for generic terms like 'bug', 'bite'
    'short': 1.0,        # Short terms (3 chars or less)
    'specific': 2.0,     # Longer, more specific terms
    'location': 3.0,     # Location context is very valuable
    'pattern': 2.5,      # Pattern context is valuable
    'symptom': 2.0       # Symptom context helps
}

# Default configuration values
DEFAULT_CONFIG = {
    'reddit_subreddit': 'bugbites',
    'reddit_user_agent': 'PersonalApp/1.0 by reupped',
    'reddit_posts_count': 15,
    'reddit_fetch_strategy': 'balanced',
    'time_filter': 'month',
    'sort_method': 'top',
    'comment_load_limit': 20,
    'api_delay_seconds': 1.5,
    'max_comments_per_thread': 2
}

# Test cases for validation
TEST_CASES = [
    {
        'title': "What bit me?",
        'comments': "Those look like bed bug bites to me. I had the same pattern when I stayed at a hotel.",
        'comment_scores': [15, 8, 3],  # High upvotes = more confidence
        'expected_improvement': "Should classify as bed_bug due to high-scoring comment"
    },
    {
        'title': "Any idea what these bites are from?",
        'comments': "Definitely ticks. I can see the characteristic bullseye pattern.",
        'comment_scores': [12, 5],  # High upvotes = more confidence
        'expected_improvement': "Should classify as tick due to expert comment"
    },
    {
        'title': "Help identify these bites",
        'comments': "Could be anything really. Maybe mosquito? Not sure tbh.",
        'comment_scores': [0, -2, 1],  # Low/negative scores = less confidence
        'expected_improvement': "Should remain unknown due to uncertain comments"
    }
]

# Sample problematic titles that were previously classified as unknown
PROBLEMATIC_TITLES = [
    "What bit me?",
    "Any idea what these bites are from?",
    "Help identify these bites",
    "Can someone help me identify this bite?",
    "What kind of bug bite is this?",
    "Strange bites appeared overnight",
    "Mystery bites on my arm",
    "Woke up with these bites"
]
