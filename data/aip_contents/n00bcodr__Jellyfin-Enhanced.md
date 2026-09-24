### Code Style

1. **Comments are Essential**

   - Use JSDoc comments for functions and classes
   - Add inline comments to explain complex logic
   - Document parameters, return values, and side effects

   Example:
   ```javascript
   /**
    * Creates a bookmark at the specified timestamp
    * @param {string} itemId - The Jellyfin item ID
    * @param {number} timestamp - The video timestamp in seconds
    * @param {string} label - User-provided label for the bookmark
    * @returns {Promise<Object>} The created bookmark object
    */
   async function createBookmark(itemId, timestamp, label) {
       // Validate timestamp is within video duration
       if (timestamp > videoDuration) {
           throw new Error('Timestamp exceeds video duration');
       }

       // Create bookmark object with metadata
       const bookmark = {
           id: generateId(),
           itemId,
           timestamp,
           label,
           createdAt: new Date().toISOString()
       };

       return await saveBookmark(bookmark);
   }
   ```

2. **Code Understanding**

   - Ensure you understand what your changes do
   - Be prepared to answer questions about your implementation
   - Test your changes thoroughly

3. <mark>**AI-Assisted Code (VibeCoded PRs)**</mark>

   - <mark>AI-assisted contributions are welcome! However:</mark>
     - You must understand what the code does
     - Be able to explain your implementation
     - Respond to code review comments
     - <mark>Clearly indicate in your PR description that AI tools were used</mark>

   Example PR description:
   ```markdown
   ## Description
   Adds feature X to improve Y

   ## Implementation Notes
   This PR was developed with AI assistance (Claude/GPT/etc.). I have reviewed
   and tested all changes and understand the implementation.

   ## Testing
   - [ ] Tested on Jellyfin 10.11
   - [ ] Verified no basic errors
   ```

---

### Pull Request Process

1. **Fork and Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

2. **Make Your Changes**

   - Write clean, commented code
   - Follow existing code patterns
   - Test thoroughly

3. **Commit Messages**

   - Use clear, descriptive commit messages
   - Reference issues when applicable

   Example:
   ```
   feat: add bookmark sync across duplicate items

   - Implements automatic bookmark syncing based on TMDB/TVDB IDs
   - Adds UI option to manage sync preferences
   - Fixes #123
   ```

4. **Submit PR**

   - Provide a clear description of changes
   - Include screenshots/videos for UI changes as applicable
   - List any breaking changes
   - <mark>Mention if you used AI assistance</mark>

5. **Code Review**

   - Be responsive to feedback
   - Be prepared to make requested changes
   - If you want me to make any further changes, let me know
