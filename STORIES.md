When a pharmaceutical manufacturer changes how a product is made or tested (switching suppliers, moving a packaging site, changing an analytical specification, etc.) regulatory affairs must determine how that change is classified. This has to happen before the change can be implemented, and in every market where the product being changed is licensed.

1. Change initiation
First, a CMC (Chemistry, Manufacturing, and Controls) technical lead creates a change record (`Change`) summarizing the proposed modification and identifying the affected `Product` records (detailed by a `DosageForm`).

2. Determining the market 
Next, the GRA (Global Regulatory Affairs) Lead looks up the company's license register to find every active marketing authorization (License) held by the changed products across the sale markets (`Market`). In Europe, this involves checking whether a product holds a centralized EU/EEA authorization (all 27 EU member states plus EEA states Norway, Iceland, and Liechtenstein) or separate national authorizations (granted in individual states like Germany or France). They may have to distinguish the `Market` from an internal list with different groupings.

3. Authority & rule-source lookup
For each affected `License`, a Regional Regulatory Specialist identifies the governing regulatory `Authority` and the applicable regulatory source/ruleset (`RuleSource`) used to determine the reporting categories available for that classification. The source must be appropriate to the license's market, authorization type, proposed change, and assessment date.

The body that grants an authorization and the body that publishes scientific or regulatory guidance may have different roles. These must be represented distinctly rather than combined into a label. The applicable source, its version or effective dates where available, and its verification status must be identifiable. If the authority, source, or applicability of the rules cannot be verified, the case remains unresolved.

4. Record a category
The specialist must evaluate the proposed change against the authority's rules and record the applicable variation category (`ReportingCategory`) as an `ImpactClassification`. Examples include PAS in the US, IA_IN or IB in the EU, MAV-1 in Singapore, or BR-SYN-MAJ in Brazil. The v1 model relies on a decision made by the specialist, and does not automatically infer a category from the change description.

5. Coverage and completeness checking
The GRA Lead reviews the assessment across every affected product and its active authorizations. Missing authorization records, unsupported categories, or unverified rules remain visible and prevent further steps from being carried out. Once classification is complete, later filing planning is outside of this specification.


Scope & Terminology
These stories specify the in-scope data needed to represent licensing coverage and record a classification. The terms below should be used consistently across data.
`Change` (via example): The proposed manufacturing or testing modification, e.g. a supplier change.
`Product` (via example): The pharmaceutical product affected by the change, e.g. Product A.
`DosageForm` (via example): The form in which the product is administered.
`Market`: The legal territory in which an authorization applies. A territory can be national or span multiple countries, e.g. UK. This is distinct from a country, region, or internal grouping like LATAM or ASEAN.
`License`: A specific marketing authorization for a product in a defined territory.
`Authority`: The regulatory authority governing the classification rules, e.g. MHRA.
`RuleSource`: A regulation, guideline, or other reference used to establish the reporting categories applicable for a classification. It identifies the source material and, if possible, its version or effective period and verification status.
`ReportingCategory`: A category specific to an authority and source that the specialist may select (e.g. UK IB).
`ImpactClassification`: The selected category for one change/product/license combination.


There are a few places where things can easily go wrong.
1. Confusing authorization territory with geography. A centrally authorized product and separately nationally authorized products must be represented according to the actual authorization records and applicable procedure. Do not create duplicate national assessments solely because a country belongs to a region, and do not assume coverage solely from geography.

2. Not differentiating between research groupings and licensing authorities. Internal reference spreadsheets group rules under regional buckets like LATAM or ASEAN. However, there is no "ASEAN" or "LATAM" License; every ASEAN marketing authorization is granted by one of the 11 national authorities. As a result, managers routinely assign generic ASEAN codes (MaV, MiV-PA, MiV-N) to markets like Singapore (which has its own HSA categories) and Indonesia and Vietnam (which enforce national statutory schemes), or incorrectly handle Cambodia, Laos, Myanmar, and Timor-Leste, where primary sources are unverified.

3. Treating similar codes as interchangeable. The UK (MHRA), Switzerland (Swissmedic), Saudi Arabia (SFDA), and South Africa (SAHPRA) all reuse EU numbering (IA, IB, II). Specialists may assume identical behavior, missing small variations (e.g. a Type IB in South Africa requires prior approval rather than the EU's IB which has a 30-day notify-then-wait procedure).

4. Lack of validation. Spreadsheets with free-text entry and which don't have validation allow specialists to type a category code that does not belong to the License's governing authority (e.g. entering the FDA's CBE-30 code on a Mexican COFEPRIS License) or they may leave an affected product's License blank.


User Stories & Acceptance Criteria
Every entity and field in the v1 specification traces directly to one or more of the stories below.

User 1: Identify the products in scope
As a CMC technical lead or GRA Lead, I need an assessment to use the products affected by a Change, so that unrelated products are not classified and all affected products are included.

Acceptance criteria
1. Given a `Change` linked to one or more products, the assessment includes each distinct affected Product and excludes products not linked to that change.
2. The assessment can display the existing `DosageForm` information associated with an affected product as context.
3. A product is not counted twice because it is referenced through more than one contextual relationship.
4. The system does not report the assessment as complete just because the change record exists; authorization coverage and classification still need to be checked by User 2 and User 6.

User 2: Find every active authorization and its territory
As a GRA Lead, I need to see every active License for each affected product and the legal territory it covers, so that every required assessment is included without duplicating assessments for countries already covered by an authorization.

Acceptance criteria
1. For each affected `Product`, the assessment includes every active `License` linked to that product in the license register.
2. Each `License` identifies its `Market`. A territory may be national or multi-country; it must not be inferred solely from an internal regional label. Wherever multi-country coverage is relevant, the constituent countries/markets are explicit in the data.
3. A distinct assessment row is created for each affected product/license combination. A single authorization covering multiple countries does not generate one duplicate row per country.
4. Separate national authorizations are represented separately when the register and applicable procedure establish that they exist.
5. European coverage is represented from the authorization records and applicable legal procedure. EU membership, EEA membership, centralized procedures, and national authorizations must not be treated as interchangeable facts.
6. If an affected product has no active license record, or the register does not establish whether its coverage is complete, this is visible and prevents the assessment from being marked as complete.

User 3: Identify the authority and applicable rules
As a Regional Regulatory Specialist, I need to identify the authority and rule source applicable to each license, so that I classify a change under the correct regulatory requirements.

Acceptance criteria
1. Every license that is ready for classification has an unambiguous authority that can be used to validate its available categories.
2. An internal research grouping (for example, ASEAN or LATAM) cannot be used as a substitute for a specific authority or applicable rule basis.
3. The authority is not inferred from a category code alone.
4. Where the authorization-granting body and the body publishing guidance are different, the data does not collapse them into a combined label such as “European Commission/EMA.” The v1 data identifies the authority used for category selection and retains a reference to the supporting rule source.
5. For each license being assessed, the applicable `RuleSource` or ruleset used to determine eligible categories is explicitly identifiable. Its applicability to the license, proposed change, and assessment date is established rather than inferred solely from the authority name, regional grouping, or category code.
6. If the applicable authority, source, or its applicability cannot be verified, the license remains unresolved until Regulatory Affairs or the designated domain owner confirms it.


User 4: Use an authority-specific category set
As a Regional Regulatory Specialist, I need to see the reporting categories supported by the rules for a license, so that I can't choose a category just because its code looks familiar.

Acceptance criteria
1. Each `ReportingCategory` is associated with the authority under which it applies and includes a code and a human-readable description.
2. A category's source reference is recorded. If the source defines an effective period or version, that information is recorded so the applicable category set can be distinguished from an obsolete one.
3. The same code under two different authorities is treated as two distinct authority-specific categories unless the source evidence establishes that they are fully the same category.
4. The available category set is limited to categories supported by the `RuleSource` or ruleset applicable to the license, proposed change, and assessment date. A category from an inapplicable source or unrelated authority cannot be selected, even if its code matches a valid category elsewhere.
5. Only categories supported by verified or authority-confirmed source material are available. If the primary source has not been verified, the category is not an option; the case remains unresolved and visible for follow-up.


User 5: Record the classification for each product and license
As a Regional Regulatory Specialist, I need to record the reporting category for each affected product under each applicable license, so that the change assessment reflects the rules for every authorization the product holds.

Acceptance criteria
1. An `ImpactClassification` identifies one `Change`, one `Product`, one applicable `License`, and the selected `ReportingCategory`.
2. For v1, at most one current classification exists for a given `Change` x `Product` x `License` combination; duplicate rows for the same combination are rejected.
3. A classification can be recorded only when the product is linked to the change and the license applies to that product.
4. The selected category must belong to the authority identified for that license and be applicable on the assessment date.
5. A category from an unrelated authority is rejected rather than accepted as free text.
6. A product/license combination cannot be treated as classified while its category is missing, its license is unverified, or its governing rules are unresolved.
7. If the specialist cannot make a defensible classification from the available evidence, the case remains visibly unresolved.
8. The recorded result is the category only.


User 6: Review coverage and find gaps
As a GRA Lead, I need a complete assessment view for the change, so that I can check that every affected product and active license has been classified before the assessment leaves the classification stage.

Acceptance criteria
1. The review view shows every affected product/license combination identified under User 1 and User 2, including its `Market`, applicable Authority, and selected category when one exists.
2. Missing licenses, missing categories, unresolved authorities, and unverified rule sources are visible as incomplete items.
3. The assessment is complete only when every in-scope product/license combination has a valid, authority-specific classification and no required coverage gap remains.
4. The GRA Lead can distinguish an incomplete assessment from a complete one.

This story ends at classification review. Hand-off mechanics, submission planning, filing preparation, regulator decisions, and implementation tracking are out of scope.

Specification and Story Relationship
User 1: `Change` --> affected `Product` records. `Product` --> associated `DosageForm` context
User 2: `Product` --> active `License` records; `License` --> applicable `Market`. Verify that license coverage is complete.
User 3: `License` --> governing `Authority`; identify `RuleSource` for the license, proposed change, and assessment date.
User 4: `Authority` and applicable `RuleSource` --> eligible `ReportingCategory` records. Each category identifies its defining authority and supporting source.
User 5: `ImpactClassification` --> one `Change`, one affected `Product`, one applicable `License`, and one selected `ReportingCategory`; enforce valid relationships and category applicability.
User 6: `ImpactClassification` records, together with verified license coverage, determine whether every required Product / License combination has been classified.