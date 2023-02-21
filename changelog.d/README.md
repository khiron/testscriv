# Adding changelog entries
This directory is used to store changelog fragments for the next release
of the project.  Each file should contain a small changelog fragment
that will be added to the full changelog when the release is made.
The file is created using 
```
scriv create --edit
``` 
to create a change entry 

This will create a file with the correct name and format and commented out sample categories, and load it into your .git editor

Uncomment the category of change you are making and add a short description of the
change as a markdown bullet point.  For example:

Contributors
  * khiron

ENH
  * Added a new feature that allows users to do Y

DEP
  * Removed deprecated feature Z

BUG
  * Fixed a bug that caused the project to crash when a user did X
    by doing Y instead

DOC
  * Documented feature Z

Check the file in with your changes.  

---
# Building a changelog

To build the changelog for the next release, run 

```
scriv collect --version="x.y.z"
```

This will create a file called CHANGELOG.md in the root of the project.  This file will contain the full changelog for the project, including all the fragments that have been added to the changelog.d directory and remove those fragments.

---
# Releasing a new version
To release a version of the project, run 

```
scriv release
```

This will create a new tag in the git repository, and create a new release on github.  The release will contain the full changelog for the project, and the tag will be annotated with the full changelog as well.  Note you will need to have a github classic personal access token set up in your environment (GITHUB_TOKEN) for this to work. 

If you are using VS code and powershell you can add the following to your settings.json file to set the environment variable for the terminal.  If you are using a different terminal you will need to set the environment variable in the appropriate way for your terminal.

```json

"terminal.integrated.env.windows": {

        "GITHUB_TOKEN": "ghp_...",
    }
```

---