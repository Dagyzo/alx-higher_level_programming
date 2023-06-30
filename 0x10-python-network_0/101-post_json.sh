#!/bin/bash

url="http://localhost:5000/endpoint"  # Replace with the appropriate URL
filename=$1

# Read the contents of the file into a variable
file_content=$(cat "$filename")

# Send the POST request with curl and display the response body
response=$(curl -X POST -H "Content-Type: application/json" -d "$file_content" "$url")
echo "$response"
