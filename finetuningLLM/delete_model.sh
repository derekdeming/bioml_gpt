#!/bin/bash

OPENAI_API_KEY="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"

#model name or id is accepted 
FINE_TUNED_MODEL="ffile-kMR1F9o5rYbUbhnP1HgFCELb"

curl -X "DELETE" "https://api.openai.com/v1/models/$FINE_TUNED_MODEL" \
  -H "Authorization: Bearer $OPENAI_API_KEY"
