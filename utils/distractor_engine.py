# -*- coding: utf-8 -*-
"""
utils/distractor_engine.py - Standard Pharmaceutical & Clinical Distractor Pools
"""

DISTRACTOR_POOLS = {
    '1. Musculoskeleton': [
        'Colchicine 0.6 mg OD', 'Naproxen 250 mg BID', 'Allopurinol 100 mg OD', 'Febuxostat 40 mg OD',
        'Celecoxib 200 mg OD', 'Methotrexate 10 mg weekly', 'Alendronate 70 mg weekly',
        'Glucosamine sulfate 1500 mg OD', 'Hydroxychloroquine 200 mg OD', 'Prednisolone 5 mg OD',
        'Zoledronic acid 5 mg IV annually', 'Leflunomide 20 mg OD', 'Paracetamol 500 mg Q6H PRN',
        'Denosumab 60 mg SC every 6 months', 'Sulfasalazine 500 mg BID'
    ],
    '2. Cardiovascular': [
        'Amlodipine 5 mg OD', 'Losartan 50 mg OD', 'Enalapril 10 mg BID', 'Hydrochlorothiazide 25 mg OD',
        'Atorvastatin 20 mg OD', 'Simvastatin 20 mg HS', 'Bisoprolol 5 mg OD', 'Spironolactone 25 mg OD',
        'Clopidogrel 75 mg OD', 'Aspirin 81 mg OD', 'Sacubitril/Valsartan 49/51 mg BID', 'Empagliflozin 10 mg OD',
        'Diltiazem 30 mg TID', 'Warfarin 3 mg OD (target INR 2.0-3.0)', 'Furosemide 40 mg OD'
    ],
    '3. Dermatologic': [
        'Clotrimazole 1% cream', 'Hydrocortisone 1% cream', 'Triamcinolone acetonide 0.1% cream',
        'Clobetasol propionate 0.05% cream', 'Ketoconazole 2% shampoo', 'Benzoyl peroxide 2.5% gel',
        'Acyclovir 5% cream', 'Silver sulfadiazine 1% cream', 'Cetirizine 10 mg OD', 'Isotretinoin 10 mg OD',
        'Terbinafine 1% cream', 'Adapalene 0.1% gel', 'Mupirocin 2% ointment', 'Betamethasone dipropionate 0.05% cream'
    ],
    '4. Endocrine': [
        'Metformin 500 mg BID', 'Glipizide 5 mg OD', 'Empagliflozin 10 mg OD', 'Sitagliptin 100 mg OD',
        'Liraglutide 1.2 mg SC OD', 'Levothyroxine 50 mcg OD', 'Propylthiouracil 50 mg TID',
        'Methimazole 10 mg OD', 'Pioglitazone 15 mg OD', 'Insulin glargine 10 units SC HS',
        'Insulin lispro 4 units SC before meals', 'Dapagliflozin 10 mg OD', 'Semaglutide 0.5 mg SC weekly'
    ],
    '5. Gastrointestinal': [
        'Omeprazole 20 mg OD', 'Esomeprazole 20 mg OD', 'Domperidone 10 mg TID', 'Dimenhydrinate 50 mg TID',
        'Loperamide 2 mg PRN', 'Senna 2 tabs HS', 'Bisacodyl 5 mg HS', 'Lactulose 15 mL OD',
        'Amoxicillin 1000 mg BID', 'Clarithromycin 500 mg BID', 'Hyoscine butylbromide 10 mg TID',
        'Aluminium hydroxide/Magnesium hydroxide suspension', 'Metoclopramide 10 mg TID before meals'
    ],
    '6. Hematologic': [
        'Ferrous fumarate 200 mg TID', 'Folic acid 5 mg OD', 'Vitamin B12 1000 mcg IM', 'Deferoxamine 500 mg SC',
        'Erythropoietin 4000 units SC', 'Ferrous sulfate 300 mg TID', 'Vitamin C 500 mg OD',
        'Pyridoxine 50 mg OD', 'Hydroxyurea 500 mg OD', 'Blood transfusion (Packed Red Cells)'
    ],
    '7. Immunologic': [
        'Cetirizine 10 mg OD', 'Loratadine 10 mg OD', 'Fexofenadine 180 mg OD', 'Chlorpheniramine 4 mg TID',
        'Fluticasone furoate nasal spray', 'Budesonide nasal spray', 'Epinephrine 0.3 mg IM stat',
        'Dexamethasone 4 mg IV', 'Prednisolone 20 mg OD', 'Montelukast 10 mg HS',
        'Hydroxyzine 25 mg HS', 'Diphenhydramine 25 mg IV'
    ],
    '8. Infectious diseases': [
        'Amoxicillin/Clavulanate 1 g BID', 'Ceftriaxone 1 g IV OD', 'Ciprofloxacin 500 mg BID',
        'Azithromycin 500 mg OD', 'Doxycycline 100 mg BID', 'Cotrimoxazole 160/800 mg BID',
        'Metronidazole 400 mg TID', 'Nitrofurantoin 100 mg BID', 'Tenofovir/Emtricitabine 300/200 mg OD',
        'Dolutegravir 50 mg OD', 'Vancomycin 1 g IV Q12H', 'Meropenem 1 g IV Q8H', 'Cefazolin 1 g IV Q8H'
    ],
    '9. Neurologic': [
        'Phenytoin 100 mg TID', 'Sodium valproate 200 mg TID', 'Carbamazepine 200 mg BID',
        'Lamotrigine 50 mg OD', 'Levetiracetam 500 mg BID', 'Gabapentin 300 mg TID', 'Pregabalin 75 mg BID',
        'Levodopa/Benserazide 100/25 mg TID', 'Sumatriptan 50 mg stat', 'Propranolol 40 mg BID',
        'Topiramate 25 mg BID', 'Donepezil 5 mg HS', 'Alteplase (rtPA) 0.9 mg/kg IV'
    ],
    '10. Psychiatric': [
        'Fluoxetine 20 mg OD', 'Sertraline 50 mg OD', 'Escitalopram 10 mg OD', 'Venlafaxine 75 mg OD',
        'Amitriptyline 10 mg HS', 'Lorazepam 1 mg HS', 'Alprazolam 0.5 mg HS', 'Diazepam 5 mg HS',
        'Zolpidem 10 mg HS', 'Nicotine gum 2 mg PRN', 'Quetiapine 25 mg HS', 'Risperidone 2 mg OD'
    ],
    '11. Pulmonary': [
        'Salbutamol MDI 2 puffs PRN', 'Budesonide/Formoterol 160/4.5 mcg DPI BID',
        'Fluticasone/Salmeterol 250/50 mcg DPI BID', 'Tiotropium Respimat 2.5 mcg 2 puffs OD',
        'Ipratropium/Fenoterol MDI PRN', 'Montelukast 10 mg HS', 'Theophylline 200 mg BID',
        'Prednisolone 40 mg OD x 5 days', 'N-acetylcysteine 600 mg OD', 'Beclomethasone MDI 100 mcg BID'
    ],
    '12. Gynaecologic/Genitourinary': [
        'Ethinylestradiol 30 mcg + Levonorgestrel 150 mcg', 'Ethinylestradiol 30 mcg + Drospirenone 3 mg',
        'Ethinylestradiol 35 mcg + Cyproterone acetate 2 mg', 'Desogestrel 75 mcg OD (Progestin-only)',
        'Levonorgestrel 1.5 mg stat (Emergency)', 'Mefenamic acid 500 mg TID', 'Tamsulosin 0.4 mg HS',
        'Finasteride 5 mg OD', 'Oxybutynin 5 mg BID', 'Tolterodine 2 mg BID', 'Dydrogesterone 10 mg BID'
    ],
    '13. Eye disorder': [
        'Timolol 0.5% eye drops 1 drop BID', 'Latanoprost 0.005% eye drops 1 drop HS',
        'Brimonidine 0.2% eye drops 1 drop BID', 'Dorzolamide 2% eye drops 1 drop BID',
        'Tobramycin 0.3% eye drops 1 drop QID', 'Chloramphenicol 0.5% eye drops 1 drop QID',
        'Artificial tears 1 drop QID', 'Antazoline/Tetrahydrozoline eye drops 1 drop TID',
        'Prednisolone acetate 1% eye drops', 'Acetazolamide 250 mg BID'
    ],
    '14. Oncologic': [
        'Ondansetron 8 mg IV stat', 'Aprepitant 125 mg PO stat', 'Dexamethasone 12 mg IV stat',
        'Filgrastim (G-CSF) 300 mcg SC OD', 'Metoclopramide 10 mg TID', 'Lorazepam 1 mg PO PRN',
        'Morphine 10 mg PO Q4H PRN', 'Calcium folinate (Leucovorin) 50 mg IV', 'Mesna 400 mg IV stat',
        'Rasburicase 0.2 mg/kg IV', 'Palonosetron 0.25 mg IV stat'
    ],
    '15. Renal': [
        'Calcium carbonate 1000 mg TID with meals', 'Calcium acetate 667 mg TID with meals',
        'Sevelamer carbonate 800 mg TID with meals', 'Sodium bicarbonate 650 mg TID',
        'Kayexalate (Sodium polystyrene sulfonate) 15 g TID', 'Calcium gluconate 10% 10 mL IV over 5 min',
        'Furosemide 40 mg IV/PO OD', 'Erythropoietin (EPO) 4000 units SC weekly',
        'Calcitriol 0.25 mcg OD', 'Potassium chloride 500 mg BID'
    ],
    '16. Others & Toxic': [
        'N-acetylcysteine (NAC) IV infusion protocol', 'Atropine sulfate 2 mg IV Q5-10 min',
        'Pralidoxime (2-PAM) 1-2 g IV over 30 min', 'Naloxone 0.4 mg IV stat', 'Flumazenil 0.2 mg IV stat',
        'Vitamin K1 (Phytomenadione) 10 mg IV slow', 'Sodium thiosulfate 25% 50 mL IV',
        'Calcium disodium EDTA 1 g IV', 'Desferrioxamine 1 g IM/IV', 'Dimercaprol (BAL) 3 mg/kg IM',
        'Ethanol 10% IV infusion for Methanol poisoning', 'Fomepizole 15 mg/kg IV loading'
    ],
    '1. Titrations': [
        'Direct Acid-Base Titration', 'Back Acid-Base Titration', 'Redox Titration (Iodometry)',
        'Complexometric Titration (EDTA)', 'Precipitation Titration (Mohr method)',
        'Volhard Titration method', 'Fajans Adsorption Indicator method', 'Potentiometric End-point Titration',
        'Biamperometric Titration', 'Nonaqueous Acid-Base Titration'
    ],
    '2. Chromatography': [
        'Reversed-Phase HPLC (C18 column)', 'Normal-Phase HPLC (Silica column)',
        'Gas Chromatography with FID detector', 'Thin Layer Chromatography (TLC)',
        'Ion-Exchange Chromatography (IEC)', 'Size Exclusion Chromatography (SEC)',
        'Chiral HPLC Separation Column', 'HILIC (Hydrophilic Interaction LC)',
        'Ultra-High Performance LC (UHPLC)', 'GC-Mass Spectrometry (GC-MS)'
    ],
    '3. Spectroscopy & Optics': [
        'UV-Vis Spectrophotometry at lambda max', 'FTIR Spectroscopy (Attenuated Total Reflection)',
        'Proton NMR (1H-NMR) Spectroscopy', 'Carbon-13 NMR (13C-NMR) Spectroscopy',
        'Electrospray Ionization Mass Spectrometry (ESI-MS)', 'Optical Rotation via Polarimeter',
        'Refractive Index via Abbe Refractometer', 'Fluorescence Spectrophotometry',
        'Atomic Absorption Spectrophotometry (AAS)', 'Differential Scanning Calorimetry (DSC)'
    ],
    '4. Preformulation & GMP': [
        'Accelerated Stability Testing (40 C / 75% RH)', 'Long-term Stability Testing (30 C / 65% RH)',
        'Differential Scanning Calorimetry (DSC) Polymorphism', 'Moisture Sorption Isotherm analysis',
        'Good Manufacturing Practice (GMP PIC/S)', 'Standard Operating Procedure (SOP) Validation',
        'High-Density Polyethylene (HDPE) Container', 'Type I Borosilicate Glass Ampoule'
    ],
    '5. Pharmaceutical Calc': [
        'Alligation Alternate method for concentration adjustment', 'mEq / mmol Electrolyte conversion formula',
        'Osmolarity (mOsmol/L) calculation', 'Sodium Chloride Equivalent (E-value) Isotonic adjustment',
        'Creatinine Clearance via Cockcroft-Gault Equation', 'Body Surface Area (BSA) via Mosteller formula',
        'Pediatric dose calculation via Clark / Young rule', 'Displacement Value calculation for Suppositories'
    ],
    '6. Solid Dosage Forms': [
        'Direct Compression tableting method', 'Wet Granulation tableting method',
        'Dry Granulation (Roller Compaction)', 'Fluidized Bed Granulation',
        'Film Coating with Hydroxypropyl methylcellulose (HPMC)',
        'Enteric Coating with Cellulose acetate phthalate (CAP)', 'Hard Gelatin Capsule filling',
        'Soft Gelatin Capsule encapsulation', 'Microcrystalline cellulose (Avicel PH102)',
        'Magnesium stearate (Lubricant 1%)', 'Sodium starch glycolate (Superdisintegrant)'
    ],
    '7. Liquid & Semisolids': [
        'Simple Syrup USP (85% w/v Sucrose)', 'Elixir with 10-20% Alcohol cosolvent',
        'Flocculated Oral Suspension with Xanthan Gum', 'Deflocculated Suspension formulation',
        'O/W Emulsion stabilized by Polysorbate 80 / Span 80', 'W/O Emulsion with Sorbitan monooleate',
        'Carbopol 940 hydrogel neutralized with Triethanolamine', 'Oleaginous Ointment base (White Petrolatum)',
        'Absorption Ointment base (Lanolin USP)', 'Fatty Suppository base (Hard Fat / Witepsol)'
    ],
    '8. Biopharm & Drug Release': [
        'BCS Class I (High Solubility, High Permeability)', 'BCS Class II (Low Solubility, High Permeability)',
        'BCS Class III (High Solubility, Low Permeability)', 'BCS Class IV (Low Solubility, Low Permeability)',
        'In Vitro Dissolution Apparatus 1 (Basket, 100 rpm)', 'In Vitro Dissolution Apparatus 2 (Paddle, 50 rpm)',
        'Higuchi Matrix Release Kinetic model', 'First-Order Drug Release Kinetics',
        'Zero-Order Sustained Release Kinetics', 'Fickian Diffusion Concentration Gradient'
    ],
    '9. Sterile & Special Forms': [
        'Moist Heat Steam Sterilization (Autoclave 121 C, 15 psi, 15 min)',
        'Dry Heat Sterilization (Hot Air Oven 160-170 C, 2 hours)',
        'Membrane Filtration Sterilization (0.22 micron pore size)', 'Ethylene Oxide Gas Sterilization (ETO)',
        'LAL Test (Limulus Amebocyte Lysate Bacterial Endotoxin)', 'Rabbit Pyrogen Test in vivo',
        'ISO Class 5 (Grade A) Laminar Airflow Workstation', 'Metered Dose Inhaler (MDI) with HFA propellant',
        'Dry Powder Inhaler (DPI) with Carrier Lactose', 'Isotonic Sodium Chloride 0.9% Osmotic Adjustment'
    ],
    '10. Biotech Products': [
        'Recombinant DNA Human Insulin in E. coli', 'Monoclonal Antibody IgG1 (CHO Cell Expression)',
        'Polyethylene Glycol (PEG) Conjugation for extended half-life',
        'Lyophilization (Freeze-drying) with Trehalose Cryoprotectant',
        'ELISA Immunoassay for protein quantification', 'SDS-PAGE Gel Electrophoresis purity analysis',
        'Isoelectric Focusing (IEF) for charge heterogeneity', 'Immunogenicity Neutralizing Antibody Assay',
        'Polysorbate 20 surfactant to prevent protein aggregation', 'Histidine Buffer pH 6.0 formulation stability'
    ],
    '13. Medicinal Chemistry': [
        'Structure-Activity Relationship (SAR) Optimization', 'Bioisosteric Replacement (Carboxylic acid -> Tetrazole)',
        'Prodrug Design via Esterification for Oral Bioavailability', 'Cytochrome P450 CYP3A4 Phase I Oxidation',
        'Phase II Glucuronidation Conjugation by UGT', 'Log P Lipophilicity Partition Coefficient optimization',
        'Chiral Eutomer vs Distomer Pharmacological activity', 'Covalent Irreversible Enzyme Inhibition'
    ],
    '17. Herbal Medicine': [
        'Maceration with Ethanol 70% solvent', 'Soxhlet Extraction for heat-stable phytochemicals',
        'Supercritical Fluid Extraction (SFE-CO2)', 'Standardized Curcuminoids in Curcuma longa',
        'Standardized Andrographolide in Andrographis paniculata', 'Senna glycosides (Sennosides A & B) Extraction',
        'Centella asiatica (Madecassoside & Asiaticoside)', 'Gingerol quantification in Zingiber officinale'
    ],
    '18. Clinical Nutrition': [
        'Total Parenteral Nutrition (TPN) 2-in-1 formula', 'Total Nutrient Admixture (TNA) 3-in-1 formula',
        'Standard Polymeric Enteral Feeding formula (1 kcal/mL)', 'Renal Enteral Formula (High calorie, Low electrolyte)',
        'Diabetic Enteral Formula (Low GI, High MUFA)', 'Hepatic Enteral Formula with High BCAA',
        'Electrolyte & Osmolarity adjustment for Peripheral Parenteral Nutrition (<900 mOsm/L)'
    ],
    '1. Pharmacy Laws & Ethics': [
        'พ.ร.บ. ยา พ.ศ. 2510 (การจำหน่ายยาอันตรายและยาควบคุมพิเศษ)',
        'พ.ร.บ. ยาเสพติดให้โทษ พ.ศ. 2522 (ยาเสพติดให้โทษประเภท 2 และ 3)',
        'พ.ร.บ. วัตถุที่ออกฤทธิ์ต่อจิตและประสาท พ.ศ. 2559 (ประเภท 2 และ 4)',
        'พ.ร.บ. วิชาชีพเภสัชกรรม พ.ศ. 2537 และข้อบังคับจรรยาบรรณวิชาชีพ',
        'พ.ร.บ. ผลิตภัณฑ์สมุนไพร พ.ศ. 2562', 'พ.ร.บ. เครื่องสำอาง พ.ศ. 2558',
        'พ.ร.บ. หลักประกันสุขภาพแห่งชาติ พ.ศ. 2545', 'การปฏิบัติทางเภสัชกรรมชุมชน (Good Pharmacy Practice: GPP)',
        'บัญชียาหลักแห่งชาติ (National List of Essential Medicines: NLEM)',
        'เกณฑ์จริยธรรมว่าด้วยการส่งเสริมการขายยาของกระทรวงสาธารณสุข'
    ],
    '2. Pharmacy Administration & System': [
        'ระบบหลักประกันสุขภาพถ้วนหน้า (Universal Health Coverage: UC)',
        'ระบบประกันสังคม (Social Security Scheme: SSS)',
        'ระบบสวัสดิการรักษาพยาบาลข้าราชการ (Civil Servant Medical Benefit Scheme: CSMBS)',
        'นโยบายการใช้ยาอย่างสมเหตุผล (Rational Drug Use: RDU Literacy)',
        'การเฝ้าระวังการดื้อยาต้านจุลชีพ (Antimicrobial Stewardship: AMS Program)',
        'ระบบส่งต่อและเชื่อมโยงเครือข่ายบริการสุขภาพ (Health Referral System)'
    ],
    '3. Research & Biostats': [
        'Randomized Controlled Trial (Double-blind RCT)', 'Prospective Cohort Study (Relative Risk: RR)',
        'Case-Control Study (Odds Ratio: OR)', 'Cross-Sectional Survey Prevalence Study',
        'Cost-Effectiveness Analysis (Incremental Cost-Effectiveness Ratio: ICER)',
        'Cost-Utility Analysis (Quality-Adjusted Life Years: QALY)', 'Cost-Benefit Analysis (Net Monetary Benefit)',
        'Cost-Minimization Analysis (CMA)', 'Student t-test for comparing two independent means',
        'Chi-Square Test for Categorical Independence (p < 0.05)'
    ]
}
