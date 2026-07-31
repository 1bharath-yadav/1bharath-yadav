## Leaner Backups, Local LLMs, and a Big Cleanup

This week focused on safer syncs, pruning old study prompts, and adding local LLM tooling. The key lesson: prefer small, tested infra over fragile one-off scripts.

### [1bharath-yadav/dotfiles](https://github.com/1bharath-yadav/dotfiles)

_Safer backups and leaner AI tooling make the dotfiles easier to operate—yes, you really needed another sync tool._

- **Production-grade sync CLI:** Added a 715-line Bash rclone wrapper for safe syncs ([executable_syncist](https://github.com/1bharath-yadav/dotfiles/blob/b4a0c3060577dddd1df0ac16669735d42e40d10f/dot_local/bin/executable_syncist), commit [b4a0c3](https://github.com/1bharath-yadav/dotfiles/commit/b4a0c3060577dddd1df0ac16669735d42e40d10f)) (21 Jul 2026). Takeaway: Use locks and dry-runs to avoid accidental data loss.
- **Local LLM tooling added:** Registered llm-wiki-compiler, copilot-cli, and LocalAI in [dot_config/mise/config.toml](https://github.com/1bharath-yadav/dotfiles/blob/b4a0c3060577dddd1df0ac16669735d42e40d10f/dot_config/mise/config.toml), commit [b4a0c3](https://github.com/1bharath-yadav/dotfiles/commit/b4a0c3060577dddd1df0ac16669735d42e40d10f) (21 Jul 2026). Takeaway: Test local LLMs in isolation before making them default.
- **Pruned a large GATE study skill:** Removed the agents/skills/gate-god module and its prompts, consolidating study content (see commit [b4a0c3](https://github.com/1bharath-yadav/dotfiles/commit/b4a0c3060577dddd1df0ac16669735d42e40d10f)) (21 Jul 2026). Takeaway: Archive large learning content before deleting to keep history handy.
- **Retired social summariser pipeline:** Deleted the Python social digest script ([deleted executable_social_summarise], commit [b4a0c3](https://github.com/1bharath-yadav/dotfiles/commit/b4a0c3060577dddd1df0ac16669735d42e40d10f)) (21 Jul 2026). Takeaway: Replace brittle one-off scripts with small, testable agents or cron jobs.
- **Repo-wide churn and polish:** Swept obsolete agents, added utilities, and touched many files (see commit [b4a0c3](https://github.com/1bharath-yadav/dotfiles/commit/b4a0c3060577dddd1df0ac16669735d42e40d10f)) (21 Jul 2026). Takeaway: Run quick smoke tests after broad refactors to catch regressions early.

## Lessons

- Small infra wins: A focused sync tool prevents bigger recovery work later.  
- Local LLMs need guardrails: Add tooling, but keep versions and tests.  
- Archive before delete: Deletions are irreversible pain without simple history access.  
- Replace brittle scripts: Production needs repeatable, testable workflows.

## Suggestions

- Add a CI smoke test that runs a dry-run of executable_syncist against a temp folder.  
- Add a brief README for syncist explaining profiles, dry-run, and lock behavior.  
- Tag or export the removed gate-god content to an archive branch before further pruning.  
- Add pinned versions and a test matrix for the new mise LLM tools, plus a rollback plan.