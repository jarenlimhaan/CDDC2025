#!/bin/bash

DB="History"  # Replace with your actual DB filename
PATTERN="cddc"

# List all tables
TABLES=$(sqlite3 "$DB" ".tables")

# Loop through each table
for TABLE in $TABLES; do
    echo "[*] Searching table: $TABLE"
    # Dump all row data from the table and grep for the pattern
    sqlite3 "$DB" "SELECT * FROM $TABLE;" | grep "$PATTERN"
done
