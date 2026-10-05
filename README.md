# Ames crop-insurance research agent

A supervised single-agent research workflow adapted from [the Week 6 notebook](https://github.com/edwardoughton/Agentic-GeoAI/blob/main/06_01_single_research_agent_github_voice.ipynb). The first investigation has been executed by the local coding agent and preserved under runs/. Empirical superiority has not been tested.

Read [the latest voice briefing](reports/latest.md), [research brief](research_brief.md), and [study protocol](runs/20261005-ames-01/study_protocol.md).

## Run another investigation

Open this Demo folder in your coding-agent environment. Send the contents of [prompts/investigate.md](prompts/investigate.md). The agent uses its available search and filesystem tools under AGENTS.md. This follows the notebook's interactive agent design; the Python utility validates the handoff artifacts and does not independently conduct research. No API key or new environment is required.

```powershell
python scripts/check_report.py
```

## Discuss by voice

Authorize jkuhlthau/Demo in your ChatGPT GitHub connection. In a supported text conversation, paste the retrieval prompt from [prompts/voice.md](prompts/voice.md). Confirm the returned run ID and phrase match reports/latest.md. Then start voice in the same conversation and use the voice prompt. Repository access and voice availability depend on your account and workspace; retrieval in this local task does not prove access in a phone conversation.

Current official [Voice instructions](https://learn.chatgpt.com/docs/features/voice) describe desktop voice and iOS Remote after pairing with a desktop host. You must start voice and grant microphone access in your app. The original notebook also provides its GitHub connection handoff. Use the connection controls available in your account and verify actual file retrieval before discussing it.

Review the resulting decision summary and save it under decisions/. Ask the local agent to read it before continuing; the GitHub publication does not automatically launch a new research run.
