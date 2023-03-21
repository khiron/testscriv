## Local .git hooks stored in the repository to ensure that all developers use the same hooks

To install hooks in this folder into your .git, run the following command from the root of the repository:

```bash
git config core.hooksPath .github/local-hooks
```

# Linting 

This will ensure that before every commit Black is run to format the code and ISort is run to sort the imports using the project pinned versions of Black and ISort.

## Windows 

On windows copy the file ./.github/local-hooks/pre-commit.windows to **./.github/local-hooks/pre-commit.** 

## Linux

And on linux copy the file ./.github/local-hooks/pre-commit.linux to **./.github/local-hooks/pre-commit.** 

And make the files executable using 

```
chmod +x pre-commit
```

