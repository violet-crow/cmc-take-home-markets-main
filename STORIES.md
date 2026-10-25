When a pharmaceutical manufacturer changes how a product is made or tested (switching suppliers, moving a packaging site, changing an analytical specification, etc.) regulatory affairs must determine how that change is classified. This has to happen before the change can be implemented, and in every market where the product being changed is licensed.

1. Change initiation
First, a technical lead opens a change record (`Change`) summarizing the proposed modification and linking the products (Product and DosageForm) it affects. This is done by someone in CMC (Chemistry, Manufacturing, and Controls).

2. Determining the market 
Next, the GRA (Global Regulatory Affairs) Lead looks up the company's license register to find every active marketing authorization (License) held by the changed products across the sale markets (`Market`). In Europe, this involves checking whether a product holds a centralized EU/EEA authorization (all 27 EU member states plus EEA states Norway, Iceland, and Liechtenstein) or separate national authorizations (granted in individual states like Germany or France).

3. Authority & rulebook lookup
For each affected License, a Regional Regulatory Specialist identifies the governing regulatory agency (`Authority`) for that market. Examples include the US FDA, the European Commission/EMA for an EU centralized License, BfArM for a German national License, HSA for Singapore, or ANVISA for Brazil. Each Authority has its own rules about what type of changes require what type of process/notification, which the Specialist must consult.

4. Impact classification
The specialist must evaluate the change being made against the authority's rules and record the applicable variation category (`ReportingCategory`) for each License (`ImpactClassification`). Examples include PAS in the US, IA_IN or IB in the EU, MAV-1 in Singapore, or BR-SYN-MAJ in Brazil.

5. Routing
Each recorded reporting category carries a procedural filing route (`ReportingRoute`) such as prior approval, notify-then-wait, notify-at-implementation, do-and-document, or no filing. Once every affected License on the change has been classified, the GRA Lead reviews the complete classification table before handing it off to submission planning.


There are a few places where things can easily go wrong currently.
1. Europe is complicated. Teams tracking assessments in spreadsheets frequently conflate the EU/EEA region with individual European countries. A specialist may forget that Norway (non-EU, EEA) is covered by a centralized EU marketing authorization, or might mistakenly file a duplicate national assessment where a centralized License already applies.

2. Not differentiating between research groupings and licensing authorities. Internal reference spreadsheets group rules under regional buckets like LATAM or ASEAN. However, there is no "ASEAN" or "LATAM" License; every ASEAN marketing authorization is granted by one of the 11 national authorities. As a result, managers routinely assign generic ASEAN codes (MaV, MiV-PA, MiV-N) to markets like Singapore (which has its own HSA categories) and Indonesia and Vietnam (which enforce national statutory schemes), or incorrectly handle Cambodia, Laos, Myanmar, and Timor-Leste, where primary sources are unverified.

3. Similar looking category codes with different legal rules. The UK (MHRA), Switzerland (Swissmedic), Saudi Arabia (SFDA), and South Africa (SAHPRA) all reuse EU numbering (IA, IB, II). Specialists often assume identical behavior, missing small variations such as the UK not adopting the EU's 2024/1701 variation reform or that a Type IB in South Africa requires prior approval rather than the EU's 30-day notify-then-wait procedure.

4. Lack of validation. Spreadsheets with free-text entry and which don't have validation allow specialists to type a category code that does not belong to the License's governing authority (e.g. entering the FDA's CBE-30 code on a Mexican COFEPRIS License) or they may leave an affected product's License blank.


User Stories & Acceptance Criteria
Every entity and field in the v1 specification traces directly to one or more of the stories below.