# LaunchPad Demo API

A tiny fictional Python pricing service used to demonstrate the Python support of **LaunchCare**, the AI
support engineer for the fictional hosting platform LaunchPad Cloud. All data here is fictional demo data.

`main` is healthy: `mypy app` and `pytest` pass. Each `scenario/*` branch is `main` plus one commit that breaks
CI in a different, deliberate way. LaunchCare investigates the failed run and opens a **draft** pull request
with a fix. It never merges.

| Branch                          | What breaks                                                                 |
| ------------------------------- | --------------------------------------------------------------------------- |
| `scenario/1-rounding-tests`     | A refactor floors a discount instead of rounding it; two tests fail by a cent |
| `scenario/2-signature-mismatch` | A function now takes a `Discount`; one caller still passes an `int` (mypy)  |
| `scenario/3-missing-package`    | An import of a package that is not in `requirements.txt`                    |

Scenario 3 is the one LaunchCare does not patch: it explains the cause and hands it to a person, because it
cannot add Python packages.

CI runs `pip install -r requirements.txt`, `mypy app` and `pytest` (Python 3.12).
