# Commit and Push Changes

Analyze the current git changes and commit them with a meaningful message following conventional commits format.

## Steps

1. Check git status to see what files have changed
2. Review the changes using git diff
3. Generate a meaningful commit message that:
   - Follows conventional commits format (feat:, fix:, docs:, chore:, etc.)
   - Clearly describes what was changed and why
   - References the component/area affected (e.g., "backend", "frontend", "docs")
4. Stage all relevant changes
5. Show me the proposed commit message for approval
6. After approval, commit with the message
7. Push to the current branch

## Conventional Commit Prefixes

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `chore:` - Maintenance tasks (dependencies, config)
- `refactor:` - Code restructuring without changing behavior
- `test:` - Adding or updating tests
- `style:` - Code formatting changes

## Example Messages

- `feat(backend): add user authentication endpoints`
- `fix(frontend): resolve login form validation issue`
- `docs: update octofit story requirements`
- `chore(backend): update Django dependencies`
