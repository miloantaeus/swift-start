# Launch Plan — AI Freelancer Swift Start Toolkit

## Current Status

- [x] Product content complete (SKILL.md + 4 template files)
- [x] README, PRICING, INSTALL, LAUNCH packaged
- [x] Factory package created
- [ ] Uploaded to Gumroad (BLOCKED — browser session expired)
- [ ] GitHub repo created
- [ ] Live sale link active

---

## Blockers

1. **Gumroad browser lane:** Milo browser at CDP 9333 has expired Gumroad session. Need owner to log in once at gumroad.com in the Milo Chrome window (user-data-dir: `~/.hermes/runtime/playwright-browser-milo`).

2. **GitHub repo:** Not yet created.

---

## Next Revenue Step (In Order)

### Step 1: Owner Re-authenticates Gumroad (5 minutes)
```
Owner action: Open the Milo Chrome window (or navigate Chrome to gumroad.com)
→ Log in with Gumroad credentials
→ This persists the session for future automated uploads
```

### Step 2: Upload to Gumroad
```bash
# Owner or automated once session is restored:
cd ~/gumroad-products/ai-freelancer-swift-start/
zip ai-freelancer-swift-start.zip 01-04-*.md INSTRUCTIONS.md SKILL.md
# Then upload via Gumroad UI at app.gumroad.com/products/new
# Price: $19, name: "AI Freelancer Swift Start Toolkit"
```

### Step 3: Create GitHub Repo (5 minutes)
```bash
gh repo create swift-start --public --description "Land your first AI-assisted freelance client in 7 days. 21 email templates, proposal frameworks, and 30+ AI prompts."
# Push factory package files to it
```

### Step 4: Social Proof
- Post to r/bjj, r/wrestling, r/Entrepreneur, r/freelance (if Reddit unblocked)
- Share the Gumroad link

---

## Revenue Math

| Item | Value |
|------|-------|
| Product price | $19 |
| Gumroad fee (10%) | -$1.90 |
| Net per sale | ~$17.10 |
| Products deployed | 11/12 |
| Remaining product | AI Freelancer Swift Start ($19) |

---

**Owner:** Log into gumroad.com in the Milo browser lane to unblock Step 1.
