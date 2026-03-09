<p align="center">
  <img src="banner.jpg" alt="AgentForge" width="100%">
</p>

# AgentForge for OpenClaw 🔧

> **v2.0** (2026-03-09) — 9-step agent pipeline with 4-level memory, self-improvement system, team alignment

Create skills and agents for OpenClaw. Full pipeline from idea to production-ready agent.

## Why

Most people create an agent by writing one AGENTS.md file and calling it done. Then they wonder why the agent gives generic answers, doesn't know who they are, forgets everything after context reset, and feels like a new hire on day one — every single time.

AgentForge codifies real battle-tested experience with dozens of skills and agents into a step-by-step process with checklists and templates.

## Three Modes

| Mode | What it does | Steps |
|------|-------------|-------|
| **A: Skill** | New skill from idea to test | 11 steps |
| **B: Agent** | New agent with memory and self-improvement | 9 steps |
| **C: Improve** | Upgrade existing skill or agent | 5 steps |

## What You Get

### Skill:
```
skills/my-skill/
├── SKILL.md              # Logic + examples
├── data/                 # Data files (safe from cleanup crons)
└── references/           # Details, dictionaries, guides
```

### Agent (full):
```
~/.openclaw/agents/my-agent/agent/
├── AGENTS.md             # Role, team, skills, memory, self-improvement
├── SOUL.md               # Personality and principles
├── USER.md               # Owner profile (adapted for agent's role)
├── IDENTITY.md           # Name and description
├── MEMORY.md             # Key facts summary
├── TOOLS.md              # Real tools with commands
├── BOOTSTRAP.md          # Context recovery after compactification
├── memory/
│   ├── lessons.md        # Lessons and rules
│   ├── patterns.md       # Self-improvement patterns
│   ├── projects-log.md   # Task history
│   ├── architecture.md   # Self-description
│   └── handoff.md        # "Save game" of current conversation
└── skills -> /shared/    # Symlink to shared skills
```

## Key Features

### 4-Level Memory System
1. **Contextual** — current session
2. **File-based** — lessons.md, patterns.md, projects-log.md (read on startup)
3. **Vector** — memory_search across past conversations
4. **Identity** — AGENTS.md, SOUL.md, USER.md (auto-loaded)

### Auto Handoff (solves "agent gets dumb" problem)
Every hour a background task reads the session history and writes a "save game" — current topic, decisions, TODOs. When context resets, the agent recovers 95% of context in seconds. Before: lost 30-50%. Now: max 5%.

### Self-Improvement System
```
Mistake → patterns.md → 3 repeats → new rule in lessons.md
```
The agent learns from corrections and stops repeating errors.

### 22 Battle-Tested Pitfalls
14 agent pitfalls + 8 skill pitfalls. Each one cost hours of debugging. You won't have to.

### Skill Typology
4 types: Workflow / Role / Data-driven / Hybrid — with templates for each.

### Agent Typology
3 types: Full (own bot, memory, skills) / Specialized (own ecosystem) / Mask (systemPrompt role)

## Installation

```bash
# 1. Copy the skill
mkdir -p <workspace>/skills/agent-forge/references
cp SKILL.md <workspace>/skills/agent-forge/
cp references/agent-templates.md <workspace>/skills/agent-forge/references/

# 2. Restart
openclaw gateway restart
```

Done. Tell your agent "create a skill" or "create an agent".

## Quick Start

### Skill:
> "Create a skill for competitor analysis"

The agent asks 3-4 questions, determines the type, shows a draft, waits for approval, creates the structure.

### Agent:
> "Create a marketer agent"

The agent asks about: role, tools, memory, connections, binding. Creates config + all workspace files.

## Examples

5 ready-made skills of different types in `examples/`:

| Example | Type | What it does |
|---------|------|-------------|
| weather-bot | Workflow | Weather by city |
| code-reviewer | Role | Code review with rules |
| task-tracker | Data-driven | Task tracker with data/ |
| content-planner | Hybrid | Role + Workflow + references/ |
| meeting-prep | Workflow | Meeting preparation |

## Files

| File | Contents |
|------|---------|
| `SKILL.md` | Main skill (521 lines, 3 modes, Russian) |
| `references/agent-templates.md` | Templates for all 13 agent files |
| `examples/` | 5 example skills |

## Triggers

"создай скилл", "новый скилл", "создай агента", "новый агент", "улучши скилл", "agent creator", "skill creator"

## Requirements

- OpenClaw (any current version)
- Any model (Claude Sonnet 4.5+ recommended)

---

## Author

**Aleksei Ulianov** — building AI agents on OpenClaw and sharing the experience.

- 🎬 YouTube: [@alekseiulianov](https://youtube.com/@alekseiulianov)
- 📱 Telegram: [@Sprut_AI](https://t.me/Sprut_AI)

## Want More?

This repo gives you the tool. But the full picture — my complete agent architecture, step-by-step setup guides, regular updates, Q&A, and everything I build for myself — lives in the private channel:

👉 [**AI ОПЕРАЦИОНКА** — join](https://t.me/tribute/app?startapp=sAFx)

I build and improve my own agent system daily. Everything I learn, every new skill, every architectural decision — goes there first. It's not just instructions, it's a living knowledge base that grows with my experience.

## License

© 2026 Aleksei Ulianov. Free for personal use. Commercial use and redistribution without author's permission is prohibited.
