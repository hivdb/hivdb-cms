A report option "XML 2009" has been added since 2009. Compared to the detail report, it has a more consistent structure and a published schema available at [here][xsd]. The following is a list of differences between the detail report and this new report (element names are enclosed with the less-than and greater-than symbols that denote XML tags in XML files):

## Header

* The `<Stanford_Algorithm_Interpretation>` (root) element has been changed to `<DrugResistance_Interpretation>`.
* The following element has been added: `<algorithmName>`. Currently, the value for this tag is always set to HIVDB.
* The following element has been added: `<schemaVersion>`. This corresponds to the version of the schema for the XML located at [here][xsd].
* The following element has been added: `<submissionName>`. When the report is done from the hivdb website (as opposed to a web services request), this is set by the user. This value will be able to be set by the web services user sometime in the future.
* The following element has been added: `<dateTime>`. This is the date/time that the report was started in the following format: day of month-3 character month-year (space) time in 24 hour format (space) timezone of the server where the report was generated, e.g., 06-May-2009 15:18:21 PDT. When the report is done from the hivdb website (as opposed to a web services request), this may be overridden by the user.

## Report Structure

* The major elements in the detail report XML were the `<success>` and `<failure>` elements. The `<result>` element now replaces these elements. The `<success>` sub-element of the `<result>` element, with possible values of "`true`" or "`false`", now indicates whether an interpretation of the sequence or set of mutations was successful or not (last updated on 03/03/10; [this is an example showing how the previous version compares to the current one](/DR/webservices/example_changesInElementsResultQuality.html)).

## Input Sequence

* The following element has been added: `<inputSequence>`. The sub-elements `<name>` and `<md5sum>` replace the "`name`" and "`md5sum`" attributes of the `<sequence>`. The new `<sequence>` element now only has the sequence value itself without any attributes.

## GtoA Hypermutation

* Two new boolean elements, both named `<GAHypermutated>`, were added on 03/03/10; one under complexType `<Result>` and the other under `<Mutation>`.
* The boolean element, `<GAHypermutated>`, under complexType `<Result>` will be true if the sequence (including multiple genes, if applicable) is G-to-A hypermutated. The Sierra program will not produce this element if the sequence is not G-A hypermutated.
* Similarly, the boolean element, `<GAHypermutated>`, under complexType `<Mutation>` will be true if the mutation is G-to-A hypermutated. The Sierra program will not produce this element if the mutation is not G-A hypermutated.

## Aligned Sequence

* Gene data has been restructured. Previously, there were several elements which contained gene data: `<summary>`, mutation elements (`<PR_mutations>`, `<RT_mutations>` and `<IN_mutations>`) and `<SequenceQA>`. The `<summary>` and `<SequenceQA>` contained gene child elements (`<PR>`, `<RT>`, `<IN>`). Gene data is now consolidated under a single element, `<geneData>`.
* The gene indentity, instead of being contained in the tag name (`<PR>`, `<RT>` or `<IN>`) is now a value in the `<gene>` element under the `<geneData>` element. The detail report XML `<subtype>` element with the "`type`" and "`percentSimilarity`" attributes now has sub-elements, `<type>` and `<percentSimilarity>`.
* Mutations are contained as a sub-element of `<geneData>` with the tag of `<mutation>`, instead of having the separate elements of `<PR_mutations>`, `<RT_mutations>` and `<IN_mutations>`. The classification of the mutation, which used to be an attribute, is now contained in the element `<classification>`. The mutation, which used to be the value of the `<mutation>` element, is now contained in the `<mutationString>` element.
* New elements for the new `<mutation>` element are:
  * `<type>` - can be one of 3 values: "`mutation`", "`insertion`" and "`deletion`"
  * `<wildType>` - the amino acid wildtype
  * `<position>` - the amino acid position in the gene
  * `<nucleicAcid>` - the mutation nucleic acid
  * `<translatedNA>` - the translated nucleic acid (amino acid)
  * `<atypical>` - if the amino acid is atypical, this element has the value of "`true`"
* If the mutation is an insertion, the following elements will be present
  * `<insertionString>` - the amino acid value at the mutation position, followed by an underscore, followed by the insertion amino acid, e.g., `S_XX`. Note: Mixtures are translated to "`X`".
  * `<insertionNucleicAcid>` - the full nucleic acid of the insertion
  * `<insertionTranslatedNA>` - the translated nucleic acid of the insertion (mixtures are translated to "`X`")

## Quality

* Quality data is contained in a sub-element of `<geneData>` with the tag of `<quality>`, instead of having the separate elements of `<PR>`, `<RT>` and `<IN>` under the `<SequenceQA>` element. `<ambiguous>` and `<stop>` elements are used in the same way, denoting the amino acid positions of ambiguous mutations and stops, respectively. `<atypical>` elements are no longer contained as a part of the quality data, rather it is contained in the <mutation> element as explained earlier.
* `<AAPosition>` tag of the `<frameshift>` element has been changed to `<position>`.
* A new element has been added to the `<quality>` element - `<stopAndFrameshiftPositions>` contains (possibly) multiple elements where the value of this element contains the position of the stop codons and frameshifts.
* The "`href`" attribute of the `<image>` element has become the `<href>` element, which is now a sub-element of the `<quality>` element.
* A new element has been added: `<sequenceQualityCounts>`, which has sub-elements whose values contain counts of possible quality problems across the entire sequence (which may contain multiple genes). These elements are: `<insertions>`, `<deletions>`, `<ambiguous>`, `<stops>`, `<frameshifts>`.
* A new string element, `<criteriaFailed>`, was added on 03/03/10 under complexType `<QualityAnalysis>`. The `<criteriaFailed>` element can have 0 or more instances which describe the HIVDB quality criteria that the input sequence gene failed.

## Interpretation: Drug Scores

* The `<drugScores>` element, which served as a container of individual `<drug>` elements has been eliminated. The new `<drugScore>` element takes the place of the `<drug>` element.
* The "`code`", "`genericName`", "`type`", and "`score`" attributes of the detail report XML `<drug>` element have been replaced with the following sub-elements under the new `<drugScore>` element: `<drugCode>`, `<genericName>`, `<type>` and `<score>`.
* The detail report XML "`levelStanford`" attribute has been replaced with the `<resistanceLevel>` element. The "`levelSIR`" attribute has been replaced with the `<threeStepResistanceLevel>` element. The `<resistanceLevelText>` element tag is new and it provides the textual description of the `<resistanceLevel>` element value. Currently, this value can be one of the following: Susceptible, Potential low-level resistance, Low-level resistance, Intermediate resistance, High-level resistance.
* The detail report XML `<partialScore>` attributes "`mutation`" and "`score`" have been replaced with the sub-elements `<mutation>` and `<score>` respectively. The value of the `<mutation>` sub-element of the `<partialScore>` will match the value of one of the mutations listed.

## Interpretation: Comments

* The `<comments>` element, which served as a container of individual `<comment>` elements has been eliminated. The `<comment>` element has the same name, with the following differences:
* The `<comment>` element has changed - the `<comment>` element value from the detail report XML is contained in the `<commentString>` element. The new `<comment>` element has the following new sub-elements:
  * `<gene>` - the gene (`PR`, `RT`, `IN`).
  * `<grouping>` - the group of the comment (`NRTI`, `NNRTI`, `Major`, `Accessory`, `Other`).
  * `<position>` - the position of the mutation that the comment is associated with.
  * `<mutationString>` - the mutation (wildtype - position - amino acid mutation) that the comment is associated with.

## Score Table

* This section is new and is written between the Drug Scores and Comments. It contains the drug score and partial drug score numeric values in a format more which can be more easily transformed by an .xsl stylesheet. It contains the same data contained in the Drug Score section. The Score Table XML contains the header and total rows of the Score Table. The contents of the Score table are enclosed by the `<scoreTable>` tag. Rows in the Score Table are enclosed by the `<scoreRow>` tag. Cells in the row are enclosed by the `<score>` tag. Attributes for the `<score>` element are as follows:
  * `value`: the score or the descriptive text (drug name or mutation)
  * `pos`: the mutation position (only written for actual drug score cells)
  * `class`: the drug class (`PI`, `NNRTI`, `NNRTI`, `INSTI`) (only written for actual drug score cells)
  * `drug`: the drug for the score (not written for header cells)

[xsd]: $$CMS_PREFIX$$downloads/schema/drug-resistance.xsd
