#!/bin/bash
# Send a GET request with the custom header and display the response body.
curl -s -H "X-School-User-Id: 98" "$1"
