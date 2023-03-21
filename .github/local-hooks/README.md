## Local .git hooks stored in the repository to ensure that all developers use the same hooks

To install hooks in this folder into your .git, run the following command from the root of the repository:

```bash
git config core.hooksPath .github/local-hooks
```

And on linux make the files executable using 

```
chmod +x pre-commit
```

This will ensure that before every commit Black is run to format the code and ISort is run to sort the imports using the project pinned versions of Black and ISort.
