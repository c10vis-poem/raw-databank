#!/usr/bin/env bash
#
# AESOP XI: CROSS-ACCOUNT RESOURCE INGESTION & CREDIT HARNESS
# Subsystem: Cloud-to-Edge Data Ingestion & Credit-Funded RAG Auditing
#
set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

clear
echo -e "${CYAN}====================================================================${NC}"
echo -e "${CYAN}  AESOP XI: GCP CROSS-ACCOUNT INGESTION & IAM PERMISSION BRIDGE     ${NC}"
echo -e "${CYAN}====================================================================${NC}"

if ! command -v gcloud &>/dev/null; then
    echo -e "${RED}X ERROR: Google Cloud SDK (gcloud) is not installed in this shell.${NC}"
    exit 1
fi

echo -e "\n${YELLOW}[STEP 1/3] Fetching Personal Credit-Consumer Project Details...${NC}"
read -p "Enter your PERSONAL GCP Project ID (holding credits): " PERSONAL_PROJECT_ID

gcloud config set project "$PERSONAL_PROJECT_ID" &> /dev/null

PROJECT_NUMBER=$(gcloud projects list --filter="projectId=$PERSONAL_PROJECT_ID" --format="value(projectNumber)")
if [ -z "$PROJECT_NUMBER" ]; then
    echo -e "${RED}X ERROR: Failed to retrieve project number for $PERSONAL_PROJECT_ID.${NC}"
    exit 1
fi

SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-discoveryengine.iam.gserviceaccount.com"
echo -e "${GREEN}✓ Personal Project Number: ${PROJECT_NUMBER}${NC}"
echo -e "${GREEN}✓ Personal Vertex AI Service Account: ${SERVICE_ACCOUNT}${NC}"

echo -e "\n${YELLOW}[STEP 2/3] Configuring Read-Only Access on Business Resource Bucket...${NC}"
read -p "Enter the secure GCS Bucket Name (e.g., business-secure-vault-bucket): " BUCKET_NAME
BUCKET_NAME=${BUCKET_NAME#gs://}

echo -e "\nSelect Execution Mode:"
echo -e "1) ${CYAN}Execute Now:${NC} Apply IAM update directly (Requires Business Admin auth)."
echo -e "2) ${CYAN}Generate Handoff Block:${NC} Output CLI command for Business Administrator."
read -p "Select [1 or 2]: " EXEC_MODE

if [ "$EXEC_MODE" == "1" ]; then
    echo -e "\nApplying policy binding on GCS bucket: ${YELLOW}gs://${BUCKET_NAME}${NC}..."
    gcloud storage buckets add-iam-policy-binding "gs://${BUCKET_NAME}" \
        --member="serviceAccount:${SERVICE_ACCOUNT}" \
        --role="roles/storage.objectViewer"
    echo -e "${GREEN}✓ SUCCESS: Cross-account permission bridge active!${NC}"
else
    echo -e "\n${CYAN}================== BUSINESS ADMIN HANDOFF COMMAND ==================${NC}"
    echo -e "${YELLOW}gcloud storage buckets add-iam-policy-binding gs://${BUCKET_NAME} \\"
    echo -e "    --member=\"serviceAccount:${SERVICE_ACCOUNT}\" \\"
    echo -e "    --role=\"roles/storage.objectViewer\"${NC}"
    echo -e "${CYAN}====================================================================${NC}"
fi

echo -e "\n${YELLOW}[STEP 3/3] Finalizing Data Store Creation Instructions...${NC}"
echo -e "1. Open the Personal Vertex AI Agent Builder Console."
echo -e "2. Create a new Data Store pointing to: ${GREEN}gs://${BUCKET_NAME}/${NC}"
echo -e "3. Select 'Unstructured Documents' and enable 'Continuous Import'."
echo -e "${CYAN}====================================================================${NC}\n"