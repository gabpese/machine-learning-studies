# Security policy

## Reporting a vulnerability

Please **do not open a public issue** for a security problem.

Report it privately through GitHub: open the **Security** tab of this repository and choose **Report a vulnerability**. Only the maintainer can see the report.

A good report says what is affected, how to reproduce it and what an attacker could do. A short proof of concept helps.

This is a one-person, open source project, so replies are best effort. I will acknowledge a report as soon as I can, say whether I could reproduce it, and fix confirmed problems in the `main` branch. Please give me reasonable time to do so before you share the details publicly.

## What is covered

Only the `main` branch is maintained. There are no released versions.

This is a personal study repository: a learning path from Python basics to Machine Learning. It is not an application or a service, it is not deployed anywhere and it does not handle real user data. The lesson scripts are small examples meant to be run locally.

Problems that matter most are the ones in the repository itself:

- a secret committed by mistake (API key, token, password or credential file)
- a dependency in `requirements.txt` with a known vulnerability
- lesson code that teaches an unsafe pattern, for example running untrusted input with `eval`, unsafe deserialization or building file paths from user input without checks
- personal data in a dataset or file that should not be public

Reports about hardening that a production deployment would need are welcome but have low priority, since nothing here is meant for production.
