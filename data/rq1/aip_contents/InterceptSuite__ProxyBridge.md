### <mark>AI-Generated Code</mark>

<mark>We **accept and welcome** code written with AI assistance (such as Claude, GitHub Copilot, or other AI coding tools), provided it meets our quality and optimization standards.</mark>

<mark>**Requirements for AI-Generated Code:**</mark>

1. **Code Quality Standards**
   - Code must be well-written, optimized, and follow project coding standards
   - Follow the same review process as manually written code
   - Must be thoroughly tested and verified before submission

2. **Optimization is Critical**
   - We take code optimization **very seriously**
   - All code must be optimized for performance and clarity
   - <mark>Contributors are responsible for understanding and optimizing AI-generated code</mark>

3. **Contributor Responsibility**
   - <mark>**Understand what the code does** - Don't blindly submit AI-generated code</mark>
   - **Review and optimize** - If code seems verbose or inefficient, refactor it
   - **Question verbosity** - If you feel the code is too large or can be written better, optimize it
   - **Benchmark when needed** - For performance-critical code, verify optimization claims

**Our Two Optimization Priorities:**

1. **Performance First**
   - Code must be optimized for best performance
   - Choose algorithms and data structures wisely
   - Minimize memory allocations, CPU cycles, and I/O operations
   - Profile performance-critical sections

2. **Simplicity and Brevity**
   - Prefer clear, concise code over verbose implementations
   - **If 10 lines can do what 20-30 lines do, use 10 lines**
   - Even without performance difference, we prefer shorter, clearer code
   - Avoid unnecessary abstractions, boilerplate, or redundant code
   - Write code that is easy to read, understand, and maintain

**Examples:**

✅ **Good - Optimized and concise:**
```c
// Fast hash lookup, minimal code
if (connection_table[hash] && connection_table[hash]->port == port) {
    return connection_table[hash];
}
```

❌ **Bad - Verbose, unnecessary:**
```c
// Same functionality but unnecessarily verbose
ConnectionInfo* info = connection_table[hash];
if (info != NULL) {
    if (info->port == port) {
        return info;
    }
}
return NULL;
```

<mark>**Before Submitting AI-Generated Code:**</mark>

- [ ] I understand what this code does and how it works
- [ ] I have reviewed it for optimization opportunities
- [ ] I have removed unnecessary code, variables, or abstractions
- [ ] I have verified it follows project coding standards
- [ ] I have tested it thoroughly
- [ ] Performance-critical code has been profiled/benchmarked
- [ ] Code is as simple and concise as possible while remaining clear

<mark>**Remember:** Using AI tools is encouraged, but you are responsible for the quality and optimization of the code you submit. AI-generated code that is verbose, inefficient, or poorly optimized will be rejected.</mark>
