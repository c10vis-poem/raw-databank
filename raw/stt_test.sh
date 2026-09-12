#!/bin/bash
# A robust script to capture the output of termux-speech-to-text
# It stores the result in a temporary file to avoid issues with stdout redirection.

TMP_FILE=$(mktemp)
termux-speech-to-text > "$TMP_FILE"

STT_RESULT=$(cat "$TMP_FILE")
rm "$TMP_FILE"

if [ -n "$STT_RESULT" ]; then
  echo "STT successful. Result:"
  echo "$STT_RESULT"
else
  echo "STT failed. No text was captured."
fi
