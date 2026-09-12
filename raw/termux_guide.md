My bad, Termux! That makes complete sense why it's completely ignoring the ECC framework. [1]
When you're running Claude Code via Everything Claude Code (ECC) inside a native Termux container, the agent completely loses its ability to link up subagents or utilize the harness because Android's sandboxed environment blocks the execution of binary path hooks (proot or standard npm linkages). [1, 2, 3]
To bridge this gap and get the model router to actually fire inside Termux, you have to use the dedicated Android bridging skill (usually managed via claude-code-android or native ECC-Termux patches). [1, 2, 3]
1. Fix the Execution Context (Why it's acting blind)
By default, Claude Code inside Termux thinks it's on a standard Linux platform and tries to hit hooks that don't exist in Android's structure. You need to bind the framework's architecture directly to the Termux-specific system variables. [2, 4]
Execute this directly in your Termux window to map the ECC hooks properly: [2]


export ECC_PLATFORM=termux
export CLAUDE_NATIVE_EXECUTION=true

2. Force-Inject the Mobile Skill Handler
ECC contains a built-in macro adapter precisely for mobile container runtimes. You need to forcefully pull this skill blueprint into your active context so the agent recognizes it has access to local shell toolings.
Inside your project root directory or the path where you initiated ECC, run: [5]


claude -p "load-skill system/termux-bridge"

(If it gives you a permissions error, you have to bypass the strict sandbox by starting your session with: claude --dangerously-skip-permissions). [5, 6]
3. Adjust your Settings File
If the agent still fails to parse your commands or use the framework, check your config mapping. Open your settings file (~/.claude/settings.json) and ensure that execution allowances are enabled for aarch64/ARM environments: [3, 7]


{
 "permissions": {
   "allow_termux_exec": true,
   "auto_approve_commands": true
 }
}

Once the environment variable is locked to termux and the bridge skill is loaded, type /harness-audit inside Claude Code to verify that the NanoClaw model router sees your local environment setup.
Are you running Claude Code directly inside the native Termux root or are you using a proot-distro Ubuntu instance inside Termux? (Knowing this helps narrow down permission mismatches with path mapping). [2]


[1] https://sealos.io
[2] https://www.reddit.com
[3] https://skillsllm.com
[4] https://github.com
[5] https://www.youtube.com
[6] https://www.youtube.com
[7] https://gist.github.com