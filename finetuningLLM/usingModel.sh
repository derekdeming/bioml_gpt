#!/bin/bash

OPENAI_API_KEY="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"
PROMPT="Propose next experiments to test the hypothesis that adipocyte Wnt signaling and fatty acid production contribute to cancer pathogenesis"
FINE_TUNED_MODEL="davinci:ft-ai-sf-hackathon-team-20-2023-05-27-16-02-49"

curl https://api.openai.com/v1/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"$PROMPT\", \"model\": \"$FINE_TUNED_MODEL\"}"
