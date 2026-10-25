# V1 Data Model Memo

## Core design

V1 separates the legal territory (`Market`), the authority used for classification (`Authority`), the source material (`RuleSource`), the category defined by that authority and source (`ReportingCategory`), and the specialist's recorded decision (`ImpactClassification`). This avoids treating research regions such as ASEAN/LATAM as markets or authorities, and prevents matching category codes such as `IB` from being treated as interchangeable across regulators. Existing `Change`, `Product`, and `DosageForm` models establish the products in scope and provide product context.

| Model | Key relationships / purpose |
|---|---|
| `Change` | References affected `Product` records. |
| `Product` | References its `DosageForm`; has `License` records. |
| `Market` | Stores a legal territory and its country codes; may cover one or multiple countries. |
| `License` | Links one `Product` to one `Market` and one `Authority`; records whether the license is active. |
| `Authority` | Identifies the regulator whose category framework is used. |
| `RuleSource` | Records source reference, publisher, verification status, and available version/effective-period details. |
| `ReportingCategory` | Links a code and description to one `Authority` and its supporting `RuleSource`. |
| `ImpactClassification` | Links one `Change`, affected `Product`, applicable `License`, selected `ReportingCategory`, and assessment date. |

The seed data are not a complete authorization or regulatory register. `ImpactClassification` rows represent completed decisions. A missing row is a classification gap. Category eligibility must be checked against authority, source verification, and the assessment date.

## Deliberately unmodeled in v1

- **A complete territory and license register:** only representative markets/licenses are seeded. V1 uses the actual license records supplied to the assessment rather than inferring authorization coverage from geography. Add register snapshots/reconciliation or explicit coverage-verification records if the register cannot attest that coverage is complete.
- **Every national scheme and unverified jurisdiction:** unsupported categories are not seeded as confirmed choices; affected cases stay unresolved. Add a jurisdiction's categories only after its primary sources are verified or confirmed by the relevant authority.
- **Procedural filing routes and downstream workflow:** no filing route, submission, approval, or implementation model is included because the assignment ends when the category is decided. Model these only if a later product scope includes filing planning or execution.
- **Automatic legal classification from a change description:** the specialist records the category; V1 does not infer it. Automated rules would require separately validated decision logic and maintained regulatory content.

## Open questions and owners

- How is completeness of the license register confirmed? The license-register owner and GRA Lead should decide how an unknown or incomplete register is represented; current `License` rows alone cannot prove that no other active licenses exist.
- Which authority and sources govern each authorization procedure? The Regulatory Affairs subject-matter expert should resolve cases where grantor, scientific assessor, rule publisher, or national procedure differ, especially for EU centralized versus national/MRP/DCP authorizations.
- How is a source established as applicable to a particular change and date? The Regulatory Affairs subject-matter expert should define the applicability rule where authority and effective dates alone are insufficient; if applicability varies by change type or procedure, add an explicit relationship/rule model.
- Is one category sufficient per change/product/license? The product owner and Regulatory Affairs subject-matter expert should confirm the uniqueness assumption, especially when one `Change` groups multiple technical modifications.
- Do Cambodia, Laos, Myanmar, and Timor-Leste actually use the AVG categories, or do they have undocumented national categories? We relied on the primary source (E4) and did not model them as AVG for v1. The Regulatory Affairs Domain Lead must confirm their true legal frameworks before we seed their categories.
- Is WHO Prequalification (WHO-PQ) in scope for v1? It appears in the rule matrices but is a global listing, not a national market as defined in the scope brief. The Product Manager must decide if UN listings should be modeled alongside national licenses.
