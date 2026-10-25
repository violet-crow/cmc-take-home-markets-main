When a pharmaceutical manufacturer changes how a product is made or tested (switching suppliers, moving a packaging site, changing an analytical specification, etc.) regulatory affairs must determine how that change is classified. This has to happen before the change can be implemented, and in every market where the product being changed is licensed.

1. Change initiation
First, a CMC (Chemistry, Manufacturing, and Controls) technical lead creates a change record (`Change`) summarizing the proposed modification and identifying the affected `Product` records (detailed by a `DosageForm`).

2. Determining the market 
Next, the GRA (Global Regulatory Affairs) Lead looks up the company's license register to find every active marketing authorization (License) held by the changed products across the sale markets (`Market`). In Europe, this involves checking whether a product holds a centralized EU/EEA authorization (all 27 EU member states plus EEA states Norway, Iceland, and Liechtenstein) or separate national authorizations (granted in individual states like Germany or France). They may have to distinguish the `Market` from an internal list with different groupings.

3. Authority & rulebook lookup
For each affected License, a Regional Regulatory Specialist identifies the governing regulatory agency (`Authority`) for that market. Examples include the US FDA, the European Commission/EMA for an EU centralized License, BfArM for a German national License, HSA for Singapore, or ANVISA for Brazil. Each Authority has its own rules about what type of changes require what type of process/notification, which the Specialist must consult.

4. Record a category
The specialist must evaluate the proposed change against the authority's rules and record the applicable variation category (`ReportingCategory`) as an `ImpactClassification`. Examples include PAS in the US, IA_IN or IB in the EU, MAV-1 in Singapore, or BR-SYN-MAJ in Brazil. The v1 model relies on a decision made by the specialist, and does not automatically infer a category from the change description.

5. Routing and coverage checking
Each recorded reporting category carries a procedural filing route (`ReportingRoute`) such as prior approval, notify-then-wait, notify-at-implementation, do-and-document, or no filing. Once every affected License on the change has been classified, the GRA Lead reviews the complete classification table before handing it off to submission planning (at which point, the next steps are outside of scope).


Scope & Terminology
These stories specify the in-scope data needed to represent licensing coverage and record a classification. The terms below should be used consistently across data.
`Product` and `Change`: These are existing concepts in the worked example. An assessment includes only the products linked to the change.
`Market`: The legal territory in which an authorization applies. A territory can be national or span multiple countries. This is distinct from a country, region, or internal grouping like LATAM or ASEAN.
`License`: A specific marketing authorization associated with a product and its authorized market or territory. Separate national authorizations which might also exist are separate records.
`Authority`: The regulatory body used to determine the applicable classification rules for a license. The body that grants an authorization and the one that publishes scientific guidance are distinct.
`ReportingCategory`: A category defined under the rules applicable to an authority and license. A code may have different meaning under different authorities.
`ImpactClassification`: The category recorded for one Change x Product x License combination.


There are a few places where things can easily go wrong.
1. Confusing authorization territory with geography. A centrally authorized product and separately nationally authorized products must be represented according to the actual authorization records and applicable procedure. Do not create duplicate national assessments solely because a country belongs to a region, and do not assume coverage solely from geography.

2. Not differentiating between research groupings and licensing authorities. Internal reference spreadsheets group rules under regional buckets like LATAM or ASEAN. However, there is no "ASEAN" or "LATAM" License; every ASEAN marketing authorization is granted by one of the 11 national authorities. As a result, managers routinely assign generic ASEAN codes (MaV, MiV-PA, MiV-N) to markets like Singapore (which has its own HSA categories) and Indonesia and Vietnam (which enforce national statutory schemes), or incorrectly handle Cambodia, Laos, Myanmar, and Timor-Leste, where primary sources are unverified.

3. Treating similar codes as interchangeable. The UK (MHRA), Switzerland (Swissmedic), Saudi Arabia (SFDA), and South Africa (SAHPRA) all reuse EU numbering (IA, IB, II). Specialists may assume identical behavior, missing small variations such as the UK not adopting the EU's 2024/1701 variation reform or that a Type IB in South Africa requires prior approval rather than the EU's 30-day notify-then-wait procedure.

4. Lack of validation. Spreadsheets with free-text entry and which don't have validation allow specialists to type a category code that does not belong to the License's governing authority (e.g. entering the FDA's CBE-30 code on a Mexican COFEPRIS License) or they may leave an affected product's License blank.


User Stories & Acceptance Criteria
Every entity and field in the v1 specification traces directly to one or more of the stories below.