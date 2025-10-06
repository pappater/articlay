#!/bin/bash
# Daily runner script for Articlay
# Add to crontab with: crontab -e
# Example cron entry: 0 9 * * * /path/to/articlay/run-daily.sh

# Set working directory
cd "$(dirname "$0")"

# Activate virtual environment if you have one
# source venv/bin/activate

# Set GitHub token from environment or hardcode (not recommended)
# export GITHUB_TOKEN="your_token_here"

# Run articlay
python articlay.py --magazines 10 --articles 5

# Optional: Log the output
# python articlay.py --magazines 10 --articles 5 >> logs/articlay-$(date +%Y-%m-%d).log 2>&1

# Optional: Send notification on completion
# echo "Articlay completed at $(date)" | mail -s "Articlay Daily Run" your@email.com
