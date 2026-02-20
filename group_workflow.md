# Group Workflow using GitHub

Project setup & workflow using PyCharm IDE (preferred) or terminal.
## Project Setup
1. Go to the GitHub repository and grab the HTTPS url
2. On the welcome screen of PyCharm click "Clone Repository" (or "File>Project from Version Control")
3. Paste the repository URL & select a local folder, then click "Clone"

PyCharm will now have your project locally, with Git tracking enabled.
- side bar should show a `Project` tab (Ctrl+Shift+E) and a `Commit` tab (Alt+0)
- the project directory should include a `test.py` file; feel free to practice commit & pushing with this file following the workflow below.
- bottom left should have a `Git` button (Ctrl+Shift+G) which displays Local & Remote branches (we should be )

If using terminal, you may need an SSH key if using SSH instead of HTTPS. We will primarily be using the free version of PyCharm for this project.

## Workflow
**Step 1 Pull**: Always pull the latest version files (origin main) before working to prevent conflicts
- in PyCharm navigate to `VCS > Git > Pull`
- in terminal use `git pull`

After pulling the directory, check `test.py` and feel free to add a contribution. This serve as a garbage file for everyone to test that their GitHub is configured properly.

**Step 2 Commit**: After making edits you must commit them with a message. Please make this message descriptive for others to see what changed.
- in PyCharm open the `Commit` tab (Alt+0). Check any changed files into the commit & write a message in the box (below) before clicking "Commit"
- in terminal use `git add .` (current directory files), then `git commit -m "Message description here"`. To see which files have been added to the commit use `git status`.

**Step 3 Push**: After all modified files have been commited, you can push them to the remote repository.
- in PyCharm navigate to `VCS > Git > Push`
- in terminal use `git push`

**Step 4 Merge**: If you get a merge conflict that means two people edited the same line. Follow these steps:
1. Pull the repository again (`VCS > Git > Pull`)
2. PyCharm will show conflict markers like this:

```
<<<<<<< HEAD
your code
=======
their code
>>>>>>> branch-name
```

3. Manually fix the conflict
4. Remove the markers
5. Commit (Alt+0) with descriptive message including merge resolution
6. Push (`VCS > Git > Push`)
7. If confused, message the group