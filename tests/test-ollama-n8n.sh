#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Testing LocalNest Chat API${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Base URL for n8n webhooks
BASE_URL="http://localhost:5678/webhook-test"

# Test the chat endpoint
echo -e "${YELLOW}Testing Chat Endpoint...${NC}"
echo -e "${BLUE}POST ${BASE_URL}/chat${NC}\n"

chat_response=$(curl -s -X POST ${BASE_URL}/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "Hello, tell me about yourself", "role_id": 1}' 2>&1)

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Chat endpoint called successfully${NC}"
    echo -e "${BLUE}Response:${NC}"
    echo "$chat_response" | python3 -m json.tool 2>/dev/null || echo "$chat_response"
    echo ""
else
    echo -e "${RED}✗ Failed to call chat endpoint${NC}"
    echo -e "${RED}Error: $chat_response${NC}\n"
fi

# Test the code endpoint
echo -e "${YELLOW}Testing Code Endpoint...${NC}"
echo -e "${BLUE}POST ${BASE_URL}/code${NC}\n"

code_response=$(curl -s -X POST ${BASE_URL}/code \
    -H "Content-Type: application/json" \
    -d '{"question": "Write a hello world function", "language_id": 1}' 2>&1)

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Code endpoint called successfully${NC}"
    echo -e "${BLUE}Response:${NC}"
    echo "$code_response" | python3 -m json.tool 2>/dev/null || echo "$code_response"
    echo ""
else
    echo -e "${RED}✗ Failed to call code endpoint${NC}"
    echo -e "${RED}Error: $code_response${NC}\n"
fi

# Summary
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Test Summary${NC}"
echo -e "${BLUE}========================================${NC}\n"

if [[ -n "$chat_response" ]] && [[ -n "$code_response" ]]; then
    echo -e "${GREEN}✓ Both endpoints are responding${NC}"
    echo -e "\n${YELLOW}Endpoints available:${NC}"
    echo "  • Chat API: ${BASE_URL}/chat"
    echo "  • Code API: ${BASE_URL}/code"
else
    echo -e "${RED}✗ Some endpoints failed${NC}"
    echo -e "\n${YELLOW}Make sure:${NC}"
    echo "  1. n8n is running (http://localhost:5678)"
    echo "  2. The LocalNest Chat API workflow is activated"
    echo "  3. Ollama is running with llama3:8b model loaded"
    echo "  4. Python scripts have execute permissions"
fi
