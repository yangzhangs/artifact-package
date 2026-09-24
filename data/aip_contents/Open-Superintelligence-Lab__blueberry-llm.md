### This is the same thing just harder to understand:

Implements per-layer adaptive sparse attention with progressive sparsity scheduling to improve upon Exp1's uniform DeepSeek Sparse Attention approach. PLASA adapts sparsity levels based on transformer layer hierarchy: dense early layers (k=L), aggressive sparse middle layers (k=L/4), and moderate sparse late layers (k=L/2).

The first method is using common and familiar words like "token", "layer" and "attention", so it's a lot easier to understand.

---

0. If you didn't read your AI generated text / code, don't expect others to (don't submit it 🤗). AI generated experiment descrption and code are mid.
1. AI can not replace your thinking - understand what is happening. Experiments can be very simple and small, that is not an issue.
2. Reviewers can quickly tell low-effort, unreviewed AI output from quality work — especially in PR descriptions. Clearly and concisely explain what you did, why, and how, even if the experiment failed / results were negative - those are also valuable. 📝
3. Make your first 1-2 sentences of pull request show the value of your contribution. ✨
4. Ask questions. 🤔
5. Don't create contributions just to appear as contributor (eg. "typo fix"). 🚫
6. Remember - science is not a chase for clout or quick dopamine - it's a journey of your curiosity (and low effort contributions will repulse employers, not attract them). 💪
