# Take-home: where a change must be classified

A pharmaceutical manufacturer changes things all the time: a new supplier, a new site, a tighter specification. Before a change ships, every market where the product is licensed must be told in its own terms. Some want prior approval, some a notification, some only a line in the annual report. Our product helps a regulatory team assess a change's impact: for each product it touches, everywhere that product is licensed, what category of change is it, and so what has to be filed?

This repository is the shared data specification for that product. It has a worked example (`DosageForm`, `Product`, `Change`) and nothing yet about where products are licensed or how a change is classified. That is your job.

## The problem

The places a product is licensed are licensed and regulated in very different ways, and the evidence describes them in the domain team's own terms. How should the specification model them, and how a change is classified in each?

The words in this brief and in the evidence use everyday language rather than entity names. Which concepts exist, what they are called and how they relate is part of what we are asking you to decide.

## Scope

**In scope:** where products are licensed and how those places relate to each other, who regulates them, the reporting categories a change can fall into, and the classification a user records for each product in each of those places on a change's impact assessment.

**Out of scope:** everything after the category is decided, including planning and preparing filings, submissions, approvals, and implementation.

## What to do

1. **Work out the real user journey.** How does a regulatory affairs team actually assess a change's impact everywhere its products are licensed today? Who does what, in what order, with what information, and where does it go wrong? Draw on your own experience, public guidance, or people you can ask. We have deliberately not written requirements for you.
2. **Write the stories.** Turn the in-scope part of the journey into user stories with acceptance criteria, specific enough that a user could fail one. These are the requirements your model must meet, and they are yours to define.
3. **Design the model.** Add the models your stories need to `cmc_spec/models/`, following the worked example. Seed enough rows in `cmc_spec/data/` to show the model handling the cases in the evidence. A complete register is out of scope.

## Design bar

This is the data model for a **first build**. Part of the task is deciding what to cut: model what v1 needs to classify correctly, and for edge cases you know about but don't model, say how v1 copes and what would make them worth modelling properly. A special case does not justify its own entity.

- Model the fewest concepts that serve your stories.
- Every entity and field traces to a story that reads it. If you can't name one, leave it out.
- Don't store what you can compute from other stored facts.
- Name each concept once and use that name everywhere.
- Where the evidence doesn't settle something, say so and name who should decide. Don't guess.

## Evidence

[`evidence/`](evidence/) is the domain team's source material. The content is accurate, but it is structured for the team's own research: its groupings, hierarchies and relationships are not necessarily the right ones for our model. Restructure it however your model needs. Public sources are fine too.

## Deliverables

Before you start, make the folder a git repository (`git init && git add -A && git commit -m start`), and commit as you go. When you are done, zip the whole folder, including `.git`, and upload it through the submission link in your assignment email. It should contain:

1. **`STORIES.md`:** the journey and the stories, with acceptance criteria.
2. **Your models and seed rows** in `cmc_spec/`. Nothing needs to run, and you don't need to write tests.
3. **`MEMO.md`,** one page at most: the core concepts in your model and why; the model as a table or diagram; known edge cases you deliberately didn't model, how v1 copes with each, and what would trigger modelling it; open questions, each with who should answer it.

AI tools are welcome. Your submission is due **24 hours after the assignment email arrives**. If you run out of time, submit what you have and note what you would do next. Late submissions will not be reviewed.

## Working in the code

There is nothing to install. The models are plain Python files using [Pydantic](https://docs.pydantic.dev), and you can write them in any editor. If you want to check that a file loads, run `pip install -U pydantic` (Python 3.11 or later), then `python -c "import cmc_spec.data.dosage_forms"` from this folder, with your own module in place of `dosage_forms`.

Follow the worked example's patterns. A model references another through a `*_strid` field typed with that model's `Ref` alias. A seeded list is a `@reference_data` model keyed on a `ReferenceCode`, with its rows written out in full in `data/`.
