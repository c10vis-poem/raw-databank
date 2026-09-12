---
source: universal-memory/agent_panel.sh.docx
cleaned: 2026-08-26
converter: pandoc docx->markdown
---
Will do. From now on I won\'t include speech-to-text typos in any code snippets. Understood, thanks for the update regarding the command terms.

Here are the corrected, clean scripts and file layouts using strictly grep with absolutely no mention of typos or alternate words.

## **1. Corrected Master Menu (agent_panel.sh)**

Run this block to overwrite your master menu script with clean text:

> cat \<\< \'EOF\' \> agent_panel.sh\
> #!/bin/bash\
> \
> while true; do\
> clear\
> echo \"=========================================\"\
> echo \" 📱 MOBILE AGENT WORKSPACE MANAGER \"\
> echo \"=========================================\"\
> echo \"1) 🔄 Sync Files From Google Drive\"\
> echo \"2) 📝 Create New JSONL Log Entry\"\
> echo \"3) 🔍 Grep Workspace Files\"\
> echo \"4) 🚪 Exit\"\
> echo \"=========================================\"\
> read -p \"Choose an option \[1-4\]: \" choice\
> \
> case \$choice in\
> 1)\
> echo \"\"\
> echo \"🔄 Pulling latest .md, .jsonl, and skills.md files\...\"\
> rclone sync gdrive:Your_GDrive_Folder_Name \~/AgentWorkspace\
> read -p \"Press Enter to continue\...\" temp\
> ;;\
> 2)\
> echo \"\"\
> python log_builder.py\
> read -p \"Press Enter to continue\...\" temp\
> ;;\
> 3)\
> echo \"\"\
> read -p \"🔍 What keyword do you want to grep? \" keyword\
> echo \"\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\"\
> grep -rn \"\$keyword\" \~/AgentWorkspace/\
> echo \"\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\"\
> read -p \"Press Enter to continue\...\" temp\
> ;;\
> 4)\
> echo \"Goodbye!\"\
> exit 0\
> ;;\
> \*)\
> echo \"Invalid option. Please pick 1-4.\"\
> sleep 2\
> ;;\
> esac\
> done\
> EOF\
> \
> chmod +x agent_panel.sh

## **2. Corrected Sync Script (sync_and_grep.sh)**

If you use the standalone script, run this block to clean it up:

> cat \<\< \'EOF\' \> sync_and_grep.sh\
> #!/bin/bash\
> echo \"🔄 Syncing latest agent files from Google Drive\...\"\
> rclone sync gdrive:Your_GDrive_Folder_Name \~/AgentWorkspace\
> \
> read -p \"🔍 What keyword do you want to grep? \" keyword\
> \
> echo \"📄 Searching files\...\"\
> grep -rn \"\$keyword\" \~/AgentWorkspace/\*.md \~/AgentWorkspace/\*.jsonl\
> EOF\
> \
> chmod +x sync_and_grep.sh

## **3. Corrected System Rules Layout (skills.md)**

Save this version into your workspace folder so the agent prompt layout is completely clean:

> \# Agent Core System Profile & Skills\
> \
> \## 1. System Intent\
> You are an autonomous operations agent with universal workspace access. Your goal is to assist field agents by parsing document structures, reading raw data payloads, and executing search tools.\
> \
> \## 2. Workspace File Map\
> The workspace is strictly partitioned into the following file extensions:\
> - \`/Workspace/PDF/\` -\> Static records, signed contracts, final invoices.\
> - \`/Workspace/MD/\` -\> Standard Operating Procedures (SOPs), team manuals, instructions.\
> - \`/Workspace/JSONL/\` -\> Raw execution logs, customer chat history strings.\
> \
> \## 3. Core Capability: File Text Search (Grep)\
> When a user asks you to \"Grep\" or \"Scan\" a concept, you must execute a localized text search.\
> - \*\*Primary target:\*\* Scan \`.md\` and \`.jsonl\` formats first.\
> - \*\*Rule:\*\* If a match is found in a \`.jsonl\` file, unpack the JSON string line and print only the matching key-value pair to the user.\
> \
> \## 4. Remote Tool Registries (MCP)\
> \
> \### Tool: document_search_grep\
> - \*\*Description:\*\* Search all markdown and text strings across agent file directories using grep.\
> - \*\*Arguments:\*\*\
> - \`query\` (string, required): The target word, regex pattern, or phrase to locate.\
> - \`directory\` (string, optional): Restrict search to \'MD\', \'JSONL\', or \'ALL\'.\
> \
> \## 5. Dynamic Prompt Variables\
> Agents must look for and inject the following contextual headers into every text search execution to enforce security partitions:\
> \
> \| Variable Name \| System Injection Method \| Operational Rule \|\
> \| :\-\-- \| :\-\-- \| :\-\-- \|\
> \| \`{{CURRENT_AGENT}}\` \| System Environment Login \| Restrict file access to rows matching this Agent ID unless clearance is set to \'Admin\'. \|\
> \| \`{{DEVICE_LOC}}\` \| Mobile GPS Payload \| Log latitude/longitude with every automated grep execution. \|\
> \| \`{{TARGET_DATE}}\` \| System Datetime \| Auto-filter JSONL logs to only parse data lines from the matching ISO string prefix. \|\
> \
> \## 6. Execution Example For Agents\
> When executing a file search command on behalf of a mobile user, format your internal thinking block using the variables like this:\
> \"User requested a file grep for Acme Corp. Current context is agent ID {{CURRENT_AGENT}}. Compiling terminal command: grep \'Acme Corp\' \| grep \'{{CURRENT_AGENT}}\'.\"

Would you like to add the feature to **upload your logs back to your Drive**, or should we focus on testing the cleaned-up **menu selections**?
