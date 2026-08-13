<p align="center">
  <img src="assets/logo.PNG" alt="RS4RT" width="70%" style="max-height:200px; object-fit:contain">
</p>

<h1 align="center">RS4RT Catalog</h1>

<p align="center">
  <em>Resource Sharing for RadioTherapy &mdash; an open catalog of software for radiotherapy research</em>
</p>

<p align="center">
  <a href="https://miro-uclouvain.github.io/RS4RT_scraper/">Browse the catalog</a> &middot;
  <a href="https://research-software-directory.org/communities/rs4rt/software">RS4RT on the Research Software Directory</a>
</p>

---

## About

RS4RT is an independent initiative created after the 2024 ESTRO physics workshop
*Open-Source software and resource sharing in radiotherapy*. Its aim is to make open-source
radiotherapy software easier to find, cite and reuse.

This repository holds the tools behind the catalog: a scraper that discovers candidate
repositories on GitHub and GitLab, a review workflow for curating them by hand, and a
publisher that pushes approved entries to the
[RS4RT community](https://research-software-directory.org/communities/rs4rt/software) on the Research Software Directory.

Maintained by the MIRO laboratory, UCLouvain.

## How it works

1. **Discover** &mdash; the scraper queries GitHub and GitLab for radiotherapy and related
   terms, each discovered repo is assessed against a curated taxonomy of domain terms.
   Depending on the final score, the repository is either kept or discarded.
   The scraper is run every two months and it discards cached repositories.
2. **Review** &mdash; surviving candidates are written to `to_review/` as one folder per
   repository, split across four parts. Reviewers edit the data and metadata of each software
   to ensure relevance and the quality of the information.
3. **Publish** &mdash; approved entries are grouped, formatted and posted to the Research
   Software Directory under the RS4RT community via their API.

Discovery runs on a schedule; review and publication are triggered by hand.

## Catalog

**262** repositories &middot; sources: github, gitlab &middot; last updated 13 August 2026

| Repository | Platform | Stars | Type | Categories | Summary |
|---|---|---:|---|---|---|
| [MIRO-UCLouvain/RS4RT_scraper](https://github.com/MIRO-UCLouvain/RS4RT_scraper) | github | 0 | unclear |  | Github/Gitlab repository scraper for radiotherapy-related projects. The pipeline also include a manual review and the publishment on https://research-software-directory.org/ under  |
| [Lakshmibharathy11/xLSTM-CBCT-Dose-Prediction-Model---Proton-Therapy-Research](https://github.com/Lakshmibharathy11/xLSTM-CBCT-Dose-Prediction-Model---Proton-Therapy-Research) | github | 0 | unclear |  | Using GAN /Deep neural network for medical image optimization |
| [ankitkumarbyte/Machine-Learning-for-Real-Time-Dose-Verification-Proton-Therapy-](https://github.com/ankitkumarbyte/Machine-Learning-for-Real-Time-Dose-Verification-Proton-Therapy-) | github | 0 | unclear |  | Proton therapy treats cancer by delivering a tightly focused beam of protons that deposits most of its energy at a precise depth — the Bragg peak — then stops. |
| [shengyusideyouxi/vmat-planner](https://github.com/shengyusideyouxi/vmat-planner) | github | 0 | unclear |  | End-to-end VMAT treatment plan prediction: anatomy → deliverable beam parameters using transformer encoder-decoder with differentiable dose engine |
| [jebibault/oncoarcade](https://github.com/jebibault/oncoarcade) | github | 0 | unclear |  | Free browser mini-games to learn oncology, radiation therapy & medical physics. Pilot a VMAT arc, validate a dosimetry plan, build a proton SOBP, run a tumor board (45k+ cases). Gr |
| [AI-radiotherapy/RT-Guide](https://github.com/AI-radiotherapy/RT-Guide) | github | 4 | unclear |  | Guide สำหรับการเขียนโปรแกรมเกี่ยวกับ Radiotherapy |
| [jamie683/TOPAS-simulations](https://github.com/jamie683/TOPAS-simulations) | github | 0 | unclear |  | TOPAS and Python workflows for PHY4004 Medical Radiation Simulation assignments, covering proton/photon transport, WET/WEPL analysis, SOBP design, PBS optimisation, DVH evaluation, |
| [sjswerdloff/transcriber-radrx](https://github.com/sjswerdloff/transcriber-radrx) | github | 0 | unclear |  | A proposed framework for validating transcription, in particular for the radiation therapy domain |
| [Jared-Luxton/radiation-therapy-machine-learning](https://github.com/Jared-Luxton/radiation-therapy-machine-learning) | github | 1 | unclear |  | Developing machine learning models with telomere data to guide radiation therapy treatment decisions |
| [MLwithDyy/Adaptive-Radiotherapy](https://github.com/MLwithDyy/Adaptive-Radiotherapy) | github | 0 | unclear |  | An Intelligent System for Adaptive Radiotherapy (ART) in Cervical Cancer: Addressing Inter-Fraction Anatomical Variations using Machine Learning |
| [FotiouK/Geometry-based_framework_for_beam_angle_selection_in_proton_therapy_for_lung_cancer](https://github.com/FotiouK/Geometry-based_framework_for_beam_angle_selection_in_proton_therapy_for_lung_cancer) | github | 8 | unclear |  | Proton beam geometry optimization to minimize respiratory induced implications for lung cancer proton therapy. |
| [Mayo-Clinic-RadOnc-Foundation-Models/Beam-mask-and-sliding-window-dose-prediction](https://github.com/Mayo-Clinic-RadOnc-Foundation-Models/Beam-mask-and-sliding-window-dose-prediction) | github | 3 | unclear |  | Beam mask and sliding window-facilitated deep learning-based accurate and efficient dose prediction for pencil beam scanning proton therapy |
| [ababier/deep-dicom](https://github.com/ababier/deep-dicom) | github | 3 | unclear |  | Preprocess and standardize DICOM data for deep learning applications in radiotherapy. |
| [HassDhia/oncosim](https://github.com/HassDhia/oncosim) | github | 1 | unclear |  | Gymnasium environments for reinforcement learning in radiation therapy treatment planning |
| [romanaruqia/PINN-Radiotherapy](https://github.com/romanaruqia/PINN-Radiotherapy) | github | 0 | unclear |  | Using Physics-Informed Neural Networks (PINNs) to simulate radiation transport profiles in clinical tissue |
| [anucha-p/radiomics_student_project](https://github.com/anucha-p/radiomics_student_project) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [SangWoonJeong/RT_stress_prediction](https://github.com/SangWoonJeong/RT_stress_prediction) | github | 0 | unclear |  | Research on multi-class and binary classification of stress in radiation therapy patients using various artificial intelligence techniques |
| [NereaRuizdelarbol/Treatment-of-liver-metastases-with-SBRT-Analysis-of-variables-and-results-using-Machine-Learning](https://github.com/NereaRuizdelarbol/Treatment-of-liver-metastases-with-SBRT-Analysis-of-variables-and-results-using-Machine-Learning) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [GuobinZhangTJU/SSC-nnUNet](https://github.com/GuobinZhangTJU/SSC-nnUNet) | github | 12 | unclear |  | Accurately and reliably defining organs at risk (OARs) and tumors are the cornerstone of radiation therapy (RT) treatment planning for lung cancer. Almost all segmentation networks |
| [dg1an3/pheonixrt](https://github.com/dg1an3/pheonixrt) | github | 4 | unclear |  | Information-theoretic inverse planning for radiation treatment |
| [yoganathansa/Virtual-Patient-Specific-QA-for-Proton-Therapy](https://github.com/yoganathansa/Virtual-Patient-Specific-QA-for-Proton-Therapy) | github | 0 | unclear |  | This project presents a virtual quality assurance (QA) framework for proton therapy that predicts measurement fluence from Treatment Planning System (TPS) data. The goal is to redu |
| [Hoco807/Range-Verification-in-Carbon-Ion-Therapy](https://github.com/Hoco807/Range-Verification-in-Carbon-Ion-Therapy) | github | 0 | unclear |  | This section documents experimental data on a single CeBr3 crystal at the carbon ion therapy terminal. |
| [andre-meneses/simulador-cnpem](https://github.com/andre-meneses/simulador-cnpem) | github | 0 | unclear |  | A Proton Beam Therapy Simulator |
| [inesfaria26/Pipeline_Model_Development](https://github.com/inesfaria26/Pipeline_Model_Development) | github | 0 | unclear |  | Radiomics and machine learning pipeline for predicting brain metastasis recurrence after radiotherapy. Includes CT/MRI preprocessing, mask generation, feature extraction, clinical  |
| [matteomaspero/rt-complexity-lens](https://github.com/matteomaspero/rt-complexity-lens) | github | 5 | unclear |  | DICOM RT plan complexity analysis |
| [kashyapHebbar/CBCT_Reconstruction](https://github.com/kashyapHebbar/CBCT_Reconstruction) | github | 2 | unclear |  | Included by heuristic/manual filtering. |
| [zahraadaher/Proton-therapy](https://github.com/zahraadaher/Proton-therapy) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [SIVERT-pCT/pbs-spot-rejection-rate](https://github.com/SIVERT-pCT/pbs-spot-rejection-rate) | github | 0 | unclear |  | Implementation of "Uncertainty-aware spot rejection rate as quality metric for proton therapy" |
| [HiLab-git/SepNet](https://github.com/HiLab-git/SepNet) | github | 20 | unclear |  | Code for Automatic Segmentation of Organs-at-Risk from Head-and-Neck CT using Separable Convolutional Neural Network with Hard-Region-Weighted Loss. |
| [JanaDannaoui/DenseNet-Model-for-IMRT-QA-](https://github.com/JanaDannaoui/DenseNet-Model-for-IMRT-QA-) | github | 1 | unclear |  | Included by heuristic/manual filtering. |
| [BrynCurrie/MDPH405-ROMP-Sandbox](https://github.com/BrynCurrie/MDPH405-ROMP-Sandbox) | github | 1 | unclear |  | Interactive Python sandbox for MDPH405 Radiation Oncology Medical Physics. Students can play with voxel models, dose calculations (convolution/superposition, Monte Carlo, etc.), in |
| [Meenakshi1609/prompt-gamma-analysis](https://github.com/Meenakshi1609/prompt-gamma-analysis) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [hollyakt/neuroseg](https://github.com/hollyakt/neuroseg) | github | 0 | unclear |  | Brain tumor segmentation pipeline using 3D U-Net on BraTS 2021 MRI dataset with Streamlit demo |
| [mazenElzeiny/AURORA-RT](https://github.com/mazenElzeiny/AURORA-RT) | github | 0 | unclear |  | "Real-time Cherenkov-based adaptive radiotherapy with hypoxia-targeted dose modulation" |
| [gmbenson/SFRT_MILP_Optimization](https://github.com/gmbenson/SFRT_MILP_Optimization) | github | 0 | unclear |  | A suite of scripts used for reading dicom files and, via dependency on PortPy, create optimal treatment plans for Spatially Fractionated Radiation Therapy |
| [LabAIRT/TransAnaNet](https://github.com/LabAIRT/TransAnaNet) | github | 2 | unclear |  | Transformer-based anatomy change prediction network for head and neck cancer radiotherapy |
| [Mohitasudani/Segthor19-using-ResU-net](https://github.com/Mohitasudani/Segthor19-using-ResU-net) | github | 20 | unclear |  | The recent advances in the field of computer vision has led to the wide use of Convolutional Neural Networks (CNNs) in organ segmentation of computed tomography (CT) images. Image  |
| [UCLHp/gate-pbt](https://github.com/UCLHp/gate-pbt) | github | 3 | unclear |  | Program for simulating proton therapy treatments using GATE/Geant4 |
| [xiaodacong/Spot-scanning_Proton_Arc_therapy_simulator](https://github.com/xiaodacong/Spot-scanning_Proton_Arc_therapy_simulator) | github | 1 | unclear |  | Included by heuristic/manual filtering. |
| [ggarillot/hadronTherapy](https://github.com/ggarillot/hadronTherapy) | github | 0 | unclear |  | Hadron Therapy GEANT4 quick simulation |
| [schillingalex/proton-rv-dtc](https://github.com/schillingalex/proton-rv-dtc) | github | 0 | unclear |  | Proton therapy range verification and spot rejection rate implementation with a digital tracking calorimeter |
| [Cellur-574/opentps](https://gitlab.com/Cellur-574/opentps) | gitlab | 0 | unclear |  | Open source TPS for proton and photon therapy |
| [Arunim10/UW_Madison_GI_Tract_Segmentation](https://github.com/Arunim10/UW_Madison_GI_Tract_Segmentation) | github | 0 | unclear |  | Deep learning-based solution for automatic segmentation of stomach and intestines in MRI scans to streamline MR-Linac guided radiotherapy and improve cancer treatment efficiency. |
| [simulproton/mspt](https://github.com/simulproton/mspt) | github | 4 | unclear |  | MSPT: Motion Simulator for Proton Therapy |
| [davidpadron76/ESAPI_RegistrationQA](https://github.com/davidpadron76/ESAPI_RegistrationQA) | github | 2 | unclear |  | ESAPI / VMS.IRS plugin in C# & WPF for automated quantitative quality assurance (QA) and clinical audit of rigid and deformable image registrations based on AAPM TG-132 and TG-233  |
| [tnnandi/modulus_radiation_therapy](https://github.com/tnnandi/modulus_radiation_therapy) | github | 1 | unclear |  | Included by heuristic/manual filtering. |
| [nhowley72/Proton-Beam-Radiotherapy-IMI-](https://github.com/nhowley72/Proton-Beam-Radiotherapy-IMI-) | github | 0 | unclear |  | Contracted Data Sci Work for Institute for Mathematical Innovation 2022 |
| [eminozcann/geant4-bragg-peak](https://github.com/eminozcann/geant4-bragg-peak) | github | 0 | unclear |  | Proton (Bragg Peak) ve Gama ışınlarının su fantomu içindeki enerji depolama profillerini karşılaştıran Geant4 simülasyonu. Geant4 simulation comparing the energy deposition profile |
| [ryancinsight/helios](https://github.com/ryancinsight/helios) | github | 0 | unclear |  | Helios (Helios-rs): unified radiation-therapy simulation/planning and radiation imaging on the Atlas stack — VoLO-class TomoTherapy helical delivery + MVCT imaging. |
| [gmartincor/KERMA-Project](https://github.com/gmartincor/KERMA-Project) | github | 0 | unclear |  | KERMA-Project: Platform for data analysis, modeling, and radiotherapy treatment planning with support for DICOM, dinalog, and other file formats. |
| [aioz-ai/LDR_ALDK](https://github.com/aioz-ai/LDR_ALDK) | github | 17 | unclear |  | Light-weight Deformable Registration using Adversarial Learning with Distilling Knowledge (IEEE Transactions on Medical Imaging 2021)) |
| [Cissise/FatPIN](https://github.com/Cissise/FatPIN) | github | 4 | unclear |  | code for "Automatic radiotherapy treatment planning with deep functional reinforcement learning" |
| [JereKoskela/proton-beam-sde](https://github.com/JereKoskela/proton-beam-sde) | github | 2 | unclear |  | Simulator for an SDE describing a the path of a proton in proton beam therapy |
| [MREYE-LUMC/OPT_tumourmodels](https://github.com/MREYE-LUMC/OPT_tumourmodels) | github | 1 | unclear |  | Generate polynomial tumour models, as commonly used in ocular proton therapy, based on 3D tumour delineations |
| [shreyasbhat132/Intensity-Modulated-Radiation-Therapy--Advanced-Optimization-Model](https://github.com/shreyasbhat132/Intensity-Modulated-Radiation-Therapy--Advanced-Optimization-Model) | github | 1 | unclear |  | An Advanced Optimization project to formulate a multi-objective optimization model for effective cancer radiation therapy. |
| [cy1034429432/A-data-efficient-surrogate-modeling-method-for-a-cyclotron-based-proton-therapy-beamline](https://github.com/cy1034429432/A-data-efficient-surrogate-modeling-method-for-a-cyclotron-based-proton-therapy-beamline) | github | 0 | unclear |  | A data-efficient surrogate modeling method for a cyclotron-based proton therapy beamline based on active learning |
| [rotemlv/CapstoneProject](https://github.com/rotemlv/CapstoneProject) | github | 0 | unclear |  | Our project focuses on advancing the field of gastrointestinal (GI) tract segmentation, aiming to enhance the differentiation between healthy organs and tumor tissues for improved  |
| [radsimbio/MINT_OM](https://github.com/radsimbio/MINT_OM) | github | 0 | unclear |  | Machine learning Integrated Normal tissue Toxicity prediction (MINT) for severe Oral Mucositis (OM) |
| [Yeon-Choi-git/whyModelBasedApproach_radiotherapy](https://github.com/Yeon-Choi-git/whyModelBasedApproach_radiotherapy) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [sujatachaudhury/survival-analysis-cox-model](https://github.com/sujatachaudhury/survival-analysis-cox-model) | github | 0 | unclear |  | This project investigates whether cardiac calcification (measured via the Agatston Score) and other clinical and dosimetric variables are associated with overall survival in lung c |
| [Sliveyu/Computational-Simulation](https://github.com/Sliveyu/Computational-Simulation) | github | 0 | unclear |  | Research paper showing data-driven comparison of radiotherapy modalities with simulation, dose optimisation, and quantitative analysis. |
| [ChrisDean15/Depth-Parameterised-Proton-SDE](https://github.com/ChrisDean15/Depth-Parameterised-Proton-SDE) | github | 0 | unclear |  | Adaptation of the code found in https://github.com/JereKoskela/proton-beam-sde. The code simulates the path of a proton in proton beam therapy using a time-changed SDE model. |
| [jamtheim/LUND-PROBE](https://github.com/jamtheim/LUND-PROBE) | github | 17 | unclear |  | LUND-PROBE – LUND Prostate Radiotherapy Open Benchmarking and Evaluation dataset |
| [Eurados/pregdos](https://github.com/Eurados/pregdos) | github | 4 | unclear |  | Tool for MC calculating dose to fetus in proton therapy, and RTDOSE in general. |
| [dmitryhits/ProtonBeamTherapy](https://github.com/dmitryhits/ProtonBeamTherapy) | github | 1 | unclear |  | A collection of python helper scripts to run GATE(GEANT4) based simulations for proton beam therapy application |
| [xuqifan897/EndtoEnd](https://github.com/xuqifan897/EndtoEnd) | github | 1 | unclear |  | Continuous optimization of photon dose radiotherapy |
| [Pyramid-Technical-Consultants/scan-kit](https://github.com/Pyramid-Technical-Consultants/scan-kit) | github | 0 | unclear |  | Free and open-source proton pencil beam scanning data analysis tool kit. |
| [openmcsquare/opentps](https://gitlab.com/openmcsquare/opentps) | gitlab | 18 | unclear | Treatment Planning and dosimetry | OpenTPS is an open-source treatment planning system (TPS) for research in radiation therapy and proton therapy. |
| [PierreLansonneur/Viewer](https://github.com/PierreLansonneur/Viewer) | github | 5 | unclear |  | Some visualization tools for radiotherapy |
| [thanhtaiphys/CBCT_Imaging_Analysis](https://github.com/thanhtaiphys/CBCT_Imaging_Analysis) | github | 4 | unclear |  | This repository contains Python code to calculate the Normal Tissue Complication Probability (NTCP) for CBCT imaging dose in radiation therapy |
| [kildealab/NLP-ML-for-incident-learning](https://github.com/kildealab/NLP-ML-for-incident-learning) | github | 0 | unclear |  | Supervised machine learning model for radiotherapy incident learning |
| [qwon135/SBRT_TumorVesselBiomarker](https://github.com/qwon135/SBRT_TumorVesselBiomarker) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [DaniRip/RT_Sampling_Pipeline](https://github.com/DaniRip/RT_Sampling_Pipeline) | github | 0 | unclear |  | Sampling-to-fluence map optimization pipeline for intensity modulated radiation therapy treatment plan design |
| [PyJay77/Geant4-MR_LINAC](https://github.com/PyJay77/Geant4-MR_LINAC) | github | 0 | unclear |  | In this project I am simulating an MR LINAC , to see the effect of the magnetic field on the secondary electrons together with the absorbed dose. I am still working on hit. |
| [pyanno4rt/pyanno4rt](https://github.com/pyanno4rt/pyanno4rt) | github | 31 | unclear | Treatment Planning and dosimetry | pyanno4rt is a Python package for conventional and outcome prediction model-based inverse photon and proton treatment plan optimization, including radiobiological and machine learn |
| [npnelson3/DynamicCollimationMonteCarloPackage](https://github.com/npnelson3/DynamicCollimationMonteCarloPackage) | github | 8 | unclear |  | This is a TOPAS-based Monte Carlo package to help enable the simulation of pencil beam scanning proton therapy beamlines and collimation devices. |
| [vmsatya/ProtonTherapy-TCP-Relapse-SecondCancer](https://github.com/vmsatya/ProtonTherapy-TCP-Relapse-SecondCancer) | github | 2 | unclear |  | We incorporated tumour relapse kinetics into the TCP framework and calculate the associated second cancer risks. To calculate proton therapy-induced secondary cancer induction, we  |
| [OpenGATE/IDEAL](https://github.com/OpenGATE/IDEAL) | github | 2 | unclear |  | Independent DosE cAlculation for Light ion beam therapy using Geant4/GATE. The name of the corresponding python module is pyidc. |
| [Particle-Therapy-Group-Bergen/PTPB](https://github.com/Particle-Therapy-Group-Bergen/PTPB) | github | 1 | unclear |  | Particle Therapy Project Bergen |
| [api-evangelist/varian-medical-systems](https://github.com/api-evangelist/varian-medical-systems) | github | 1 | unclear |  | Varian Medical Systems is a leading manufacturer of medical devices and software for treating cancer with radiotherapy, radiosurgery, proton therapy, and brachytherapy. Acquired by |
| [oncoray/UQ_OutcomeModelling](https://github.com/oncoray/UQ_OutcomeModelling) | github | 1 | unclear |  | Illustrative example for uncertainty quantification in outcome modelling in radiation therapy |
| [johnfishbein/SBRT-Risk-Classificaiton](https://github.com/johnfishbein/SBRT-Risk-Classificaiton) | github | 1 | unclear |  | Classification of Patient Risk from Stereotactic Body Radiation Therapy when treating thoracic cancers |
| [pauldubois98/AIME2024](https://github.com/pauldubois98/AIME2024) | github | 0 | unclear |  | Paper on Radiotherapy Optimization with Clinical Knowledge. |
| [jamtheim/RTStructEvalPublic](https://github.com/jamtheim/RTStructEvalPublic) | github | 0 | unclear |  | Framework for evaluation of radiation therapy segmentation models |
| [Pyramid-Technical-Consultants/spot-check](https://github.com/Pyramid-Technical-Consultants/spot-check) | github | 0 | unclear |  | A free engineering tool for checking data collected against DICOM RT ion plans. Not for clinical use. |
| [e0404/matRad](https://github.com/e0404/matRad) | github | 288 | unclear | Treatment Planning and dosimetry | Matrad is an open source software for radiation treatment planning of intensity-modulated photon, proton, and carbon ion therapy. |
| [radiofisica-hgugm/kali_mc](https://github.com/radiofisica-hgugm/kali_mc) | github | 13 | unclear |  | Software for calculating IORT treatments with a LIAC HWL linac, based on precalculated Monte Carlo dose distributions in water. |
| [gregoire-moreau/radio_rl](https://github.com/gregoire-moreau/radio_rl) | github | 8 | unclear |  | Using DQN and DDPG on a model of tumoural development to optimise treatment schedules of radiation therapy. |
| [cyrilvoyant/LQ-Equiv](https://github.com/cyrilvoyant/LQ-Equiv) | github | 7 | unclear |  | Biological effects and equivalent doses in radiotherapy: A software solution |
| [jacyap/ClatterbridgeTreatmentLine](https://github.com/jacyap/ClatterbridgeTreatmentLine) | github | 7 | unclear |  | TOPAS model of the Clatterbridge Cancer Centre, UK 60 MeV Ocular Proton Therapy Beamline |
| [CCIG-Champalimaud/waw-tace-radiomics](https://github.com/CCIG-Champalimaud/waw-tace-radiomics) | github | 3 | unclear |  | Included by heuristic/manual filtering. |
| [indranilmallick/dvh-predict](https://github.com/indranilmallick/dvh-predict) | github | 3 | unclear |  | Prediction of dose-volumes of the rectum, bladder and PTV for prostate cancer radiation therapy from volumes of rectum, bladder, PTV60 and PTV44 and overlap volumes using different |
| [Image-X-Institute/MarkerlessHNGTVTracking](https://github.com/Image-X-Institute/MarkerlessHNGTVTracking) | github | 2 | unclear |  | Code used to create the results described in the paper "A conditional generative adversarial network approach for segmenting head and neck tumors in kV images acquired during radia |
| [jamiedean/fda-ntcp-models](https://github.com/jamiedean/fda-ntcp-models) | github | 1 | unclear |  | Functional data analysis normal tissue complication probability (NTCP) models of severe acute mucositis and dysphagia |
| [voacado/AutoTreatmentPlanningRadiationTherapyGANs](https://github.com/voacado/AutoTreatmentPlanningRadiationTherapyGANs) | github | 1 | unclear |  | Automated Treatment Planning in Radiation Therapy using Generative Adversarial Networks (Mahmood, R., Babier, A., McNiven, A., Diamant, A. &amp; Chan, T.C.Y.. (2018)) |
| [RamonBrison/Proton-Therapy-](https://github.com/RamonBrison/Proton-Therapy-) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [haiyiluo/An-Experimental-Proposal-to-Quantify-Particle-Therapy-Efficacy](https://github.com/haiyiluo/An-Experimental-Proposal-to-Quantify-Particle-Therapy-Efficacy) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [bentmha/G4DARI](https://github.com/bentmha/G4DARI) | github | 0 | unclear |  | Interface on MS Windows for GATE/GEANT4 dosimetry simulations for cancer using CT images |
| [yfchenkeepgoing/stimulation-and-calculation-of-ionization-chamber-using-Geant4](https://github.com/yfchenkeepgoing/stimulation-and-calculation-of-ionization-chamber-using-Geant4) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [stefvcb/opentps](https://gitlab.com/stefvcb/opentps) | gitlab | 0 | unclear |  | Open source TPS for proton and photon therapy |
| [casper402/ldm-cbct-sct](https://github.com/casper402/ldm-cbct-sct) | github | 3 | unclear |  | A PyTorch implementation of Latent Diffusion Models (LDMs) for high-fidelity Cone-Beam CT (CBCT) to synthetic CT (sCT) translation in Adaptive Radiation Therapy. |
| [deffets/openpr](https://gitlab.com/deffets/openpr) | gitlab | 0 | unclear |  | Proton radiography analysis software |
| [Zeinab-Haroon/AIMS-Project-Uveal-Melanoma-Python](https://github.com/Zeinab-Haroon/AIMS-Project-Uveal-Melanoma-Python) | github | 0 | unclear |  | Final Thesis: investigated the optic nerve shape changes under different gaze angles to improve the proton therapy planning for uveal melanoma patients using MeVislab Software. |
| [dcpt-research/guiPMC](https://gitlab.com/dcpt-research/guiPMC) | gitlab | 0 | unclear |  | A user interface with Dicom Ion plan reader for integration with goPMC the OpenCL Proton Monte Carlo binaries (THIS PROJECT DOES NOT CONTAIN goPMC ONLY AN INTERFACE) |
| [bnsreenu/digitalpathology-spatial-immune-rdf](https://github.com/bnsreenu/digitalpathology-spatial-immune-rdf) | github | 0 | unclear |  | Spatial immune analysis from H&E using the radial distribution function. Cellpose nucleus segmentation, rule-based cell classification, Gaussian tumor nest mask, and boundary-based |
| [NafisaMaliat/GBM_Radiotherapy_ABM](https://github.com/NafisaMaliat/GBM_Radiotherapy_ABM) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [sugam1409/MATHEMATICS-IN-CANCER-TREATMENT-](https://github.com/sugam1409/MATHEMATICS-IN-CANCER-TREATMENT-) | github | 0 | unclear |  | Mathematics plays a pivotal role in advancing cancer treatment through its application in tumor growth modeling, radiation therapy planning, drug dosage optimization, image analysi |
| [jamiedean/ntcp-modelling-functional-data-analysis](https://github.com/jamiedean/ntcp-modelling-functional-data-analysis) | github | 0 | unclear |  | NTCP modelling using functional data analysis methods |
| [wjcheon/Matlab_DVHAnalyzer](https://github.com/wjcheon/Matlab_DVHAnalyzer) | github | 0 | unclear |  | For Eclipse TPS |
| [Murielle-tcham/Lyprox-project](https://github.com/Murielle-tcham/Lyprox-project) | github | 0 | unclear |  | This project aims to optimize locoregional radiotherapy target volumes in early-stage breast cancer by combining large-scale clinical data analysis with probabilistic modeling of l |
| [radiation-treatment-planning/tcp-ntcp-calculation](https://gitlab.com/radiation-treatment-planning/tcp-ntcp-calculation) | gitlab | 0 | unclear |  | Tumor Control Probability calculation with Poisson Model and Normal Tissue Complication Probability calculation with Poisson relative seriality model. |
| [StellarStorm/opentps](https://gitlab.com/StellarStorm/opentps) | gitlab | 0 | unclear |  | Open source TPS for proton therapy |
| [fpli/opentps](https://gitlab.com/fpli/opentps) | gitlab | 0 | unclear |  | Open source TPS for proton therapy |
| [icmeyer/opentps](https://gitlab.com/icmeyer/opentps) | gitlab | 0 | unclear |  | Open source TPS for proton therapy |
| [MichaelColonel/opentps](https://gitlab.com/MichaelColonel/opentps) | gitlab | 0 | unclear |  | Open source TPS for proton therapy |
| [summerycshen/dosedistributionprediction](https://github.com/summerycshen/dosedistributionprediction) | github | 2 | unclear |  | as a supplementary code for Song Ying's radiation therapy dose distribution prediction codes |
| [fmhr12/orn-prognosis](https://github.com/fmhr12/orn-prognosis) | github | 1 | unclear |  | A compiled R Shiny application designed to predict the individualized risk of Osteoradionecrosis (ORN) in Head and Neck Cancer (HNC) patients treated with Intensity-Modulated Radia |
| [KaleyWhite/dvh-points-investigation](https://github.com/KaleyWhite/dvh-points-investigation) | github | 1 | unclear |  | Data analysis of how two TPSs determine which DVH points to export |
| [Nikhil-Guleria-44/IsoVerify](https://github.com/Nikhil-Guleria-44/IsoVerify) | github | 0 | unclear |  | 🛠 Analyze and verify isocenter accuracy in radiotherapy with this web-based QA tool for Winston–Lutz analysis, generating official reports effortlessly. |
| [lxaibl/CycleGAN-CBCT-to-CT](https://github.com/lxaibl/CycleGAN-CBCT-to-CT) | github | 41 | unclear |  | Convert CBCT images to CT like images |
| [clrp-code/egs_brachy](https://github.com/clrp-code/egs_brachy) | github | 25 | unclear |  | egs_brachy is an application for doing Monte Carlo brachytherapy simulations based on EGSnrc/egs++. |
| [pablojrios/fluence_maps](https://github.com/pablojrios/fluence_maps) | github | 8 | unclear |  | Deep learning models to predict the gamma index of treatment plans based on calculated fluence maps for intensity modulated radiation therapy (IMRT). |
| [GregoryButi1/opentps](https://gitlab.com/GregoryButi1/opentps) | gitlab | 1 | unclear |  | Open source TPS for proton therapy |
| [bhushan-choudhari/Radiation-Therapy-Optimization](https://github.com/bhushan-choudhari/Radiation-Therapy-Optimization) | github | 0 | unclear |  | Mathematical Model to optimize beam intensity levels for treatment of cancer |
| [ayf-9797/Cross-cohort-augmented-prediction-of-acute-radiation-dermatitis](https://github.com/ayf-9797/Cross-cohort-augmented-prediction-of-acute-radiation-dermatitis) | github | 0 | unclear |  | The code of "Predicting acute radiation dermatitis to inform personalized supportive care in breast cancer proton therapy: a cross-cohort machine learning study with temporal valid |
| [ArmorBearerSlave/U-Net-Project](https://github.com/ArmorBearerSlave/U-Net-Project) | github | 0 | unclear |  | Advanced Radiation Therapy Class Project 2 - Lulin Yuan |
| [fire-sketch/ImageQualityProtonTherapy](https://github.com/fire-sketch/ImageQualityProtonTherapy) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [stevend12/SolutioCpp](https://github.com/stevend12/SolutioCpp) | github | 14 | unclear |  | A C++ library for applications of physics in medicine, particularly radiation therapy and medical imaging |
| [openmcsquare/MCsquare](https://gitlab.com/openmcsquare/MCsquare) | gitlab | 12 | unclear | Treatment Planning and dosimetry | Fast Monte Carlo dose calculation algorithm for the simulation of PBS proton therapy. |
| [PRECISE-RT/PBT-Gym](https://github.com/PRECISE-RT/PBT-Gym) | github | 5 | unclear |  | Reinforcement Learning for Proton Beam Therapy treatment planning |
| [nnaakkaaii/RealTime-4DCT-Reconstruction](https://github.com/nnaakkaaii/RealTime-4DCT-Reconstruction) | github | 4 | unclear |  | Machine Learning model to reconstruct 4D-CT in real-time from cine-MR acquired during radiation therapy. Aimed to enhance treatment precision and adaptability. |
| [sh2439/IMRT-Optimization](https://github.com/sh2439/IMRT-Optimization) | github | 2 | unclear |  | Included by heuristic/manual filtering. |
| [dilipkumar801770/Medical-Particle-Accelerators-Engineering-Healthcare-Applications-and-Emerging-Technologies](https://github.com/dilipkumar801770/Medical-Particle-Accelerators-Engineering-Healthcare-Applications-and-Emerging-Technologies) | github | 1 | unclear |  | This article reviews the biomedical applications of particle accelerators in medical imaging, radioisotope production, proton and heavy-ion therapy, radiation biology, and AI-enabl |
| [RBatty97/PHYS488-Proton-Beam-Therapy](https://github.com/RBatty97/PHYS488-Proton-Beam-Therapy) | github | 1 | unclear |  | Included by heuristic/manual filtering. |
| [Atul280/radiation_therapy](https://github.com/Atul280/radiation_therapy) | github | 0 | unclear |  | Radiation therapy is a method used for treatment of cancer cells. This project is all about that in which we can adjust the intensities of the radiation beams .This project was bui |
| [jy-rep/gliomaRadiationModel](https://github.com/jy-rep/gliomaRadiationModel) | github | 0 | unclear |  | the manuscript "A multi-compartment model of glioma response to fractionated radiation therapy parameterized via time-resolved microscopy data" |
| [hannahgsimon/HALModeling2024Graphs](https://github.com/hannahgsimon/HALModeling2024Graphs) | github | 0 | unclear |  | Created code to develop and analyze statistical graphs for the spatial radiotherapy model, which can be found at https://github.com/hannahgsimon/HALModeling2024. This project was i |
| [1ali2003ah1-lgtm/ProtonAI](https://github.com/1ali2003ah1-lgtm/ProtonAI) | github | 0 | unclear |  | Clinical AI Platform for Proton Therapy |
| [imran1gee/MonteCarlo-Radiation-Dose](https://github.com/imran1gee/MonteCarlo-Radiation-Dose) | github | 0 | unclear |  | Monte Carlo simulation for radiation dose calculation in a water phantom |
| [sithin-cnao/t2w_stability](https://github.com/sithin-cnao/t2w_stability) | github | 0 | unclear |  | Stability of T2w radiomics features to variations in "Fat Saturation" |
| [danielbjorkman88/OCULARIS](https://github.com/danielbjorkman88/OCULARIS) | github | 0 | unclear |  | The research treatment planning system for Ocular Proton Therapy |
| [VladAndreiToma/ProtonTherapy_ProtonBeam_OnPlatsticScintillator_Geant4SIM](https://github.com/VladAndreiToma/ProtonTherapy_ProtonBeam_OnPlatsticScintillator_Geant4SIM) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [runefeather/prescription-plan-IMRT](https://github.com/runefeather/prescription-plan-IMRT) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [sellipyrtqa/pyRTQA](https://github.com/sellipyrtqa/pyRTQA) | github | 5 | unclear |  | Quality Assurance (QA) tool for Radiation Therapy Medical Physicists |
| [xueli2245/MRI-to-CT-generation](https://github.com/xueli2245/MRI-to-CT-generation) | github | 2 | unclear |  | Synthetic CT Generation from 0.35T MR Images for MR-only Radiation Therapy Planning Using Unet With Perceptual Loss Models |
| [sfrt-optimization/sfrt_optimization](https://github.com/sfrt-optimization/sfrt_optimization) | github | 2 | unclear |  | an open source repository for spatially fractionated radiation therapy treatment planning decision making optimization and analysis |
| [higumalu/pydicomRT](https://github.com/higumalu/pydicomRT) | github | 2 | unclear |  | Python library for handling Radiation Therapy DICOM files. |
| [flash-center/PRaLine](https://github.com/flash-center/PRaLine) | github | 2 | unclear |  | PRaLine code (Proton Radiography Linear reconstruction, the "reconstruction" is silent) |
| [mfkasim1/nonlinear-proton-radiography](https://github.com/mfkasim1/nonlinear-proton-radiography) | github | 1 | unclear |  | [Full version coming soon] This is matlab codes to invert nonlinear proton radiography images to obtain the deflection of the proton beam. |
| [VictorCallejas/varian_Junction2019](https://github.com/VictorCallejas/varian_Junction2019) | github | 1 | unclear |  | Improving decision-making and engagement between patient, oncologist and physicist for cancer treatment with radiation therapy. |
| [john9francis/g4-mesh-rad-therapy](https://github.com/john9francis/g4-mesh-rad-therapy) | github | 1 | unclear |  | A Geant4 application that allows you to import a mesh geometry and run radiation therapy on it |
| [weintraubje/Radiation-Therapy-Optimization](https://github.com/weintraubje/Radiation-Therapy-Optimization) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [kezoltan/MSc-Thesis-Proton-Therapy-Monte-Carlo-](https://github.com/kezoltan/MSc-Thesis-Proton-Therapy-Monte-Carlo-) | github | 0 | unclear |  | Supporting Python code in relation to the MSc thesis which estimates the absorbed dose a monoenergetic proton beam in a water phantom using techniques from the finite element metho |
| [weisadre/autodelineation](https://gitlab.com/weisadre/autodelineation) | gitlab | 0 | unclear |  | Deep learning delineation of organs for radiation therapy |
| [cvelten/ProfileEvaluation](https://github.com/cvelten/ProfileEvaluation) | github | 0 | unclear |  | Radiotherapy profile evaluation and comparison tool (supporting DICOM, CSV, MCC) |
| [csgf/iort-portlet](https://github.com/csgf/iort-portlet) | github | 0 | unclear |  | Code of the portlet to run the IntraOperative Electron Radiotherapy application on Grid |
| [mialar/autoscript_lung](https://github.com/mialar/autoscript_lung) | github | 0 | unclear |  | Automatic proton treatment planning script for LA-NSCLC patients |
| [MGHPhysicsResearch/moquimc](https://github.com/MGHPhysicsResearch/moquimc) | github | 31 | unclear |  | MOnte carlo code for QUIck proton dose calculation |
| [The-Grant2002/SFRT_Optimization](https://github.com/The-Grant2002/SFRT_Optimization) | github | 2 | unclear |  | Implementation of Optimization Techniques centered around the Maximum Independent Set problem for Spatially Fractionated Radiation Therapy |
| [Will-Bethard/Single-Element-Transducer-Holders](https://github.com/Will-Bethard/Single-Element-Transducer-Holders) | github | 1 | unclear |  | See: "Development of Single-element Transducer Holders for Isotropy Quantification of Ultrasound Transducers Used in Proton Therapy Thermoacoustic Range Verification" abstract. Dev |
| [obour2021/BreastCancerProject](https://github.com/obour2021/BreastCancerProject) | github | 0 | unclear |  | This is a Breast Cancer Data Set with 286 instances of real patient data obtained from the Institute of Oncology, Ljubljana. The data set is publicly available from UCI Machine Lea |
| [obour2021/BreastCancerCapstone](https://github.com/obour2021/BreastCancerCapstone) | github | 0 | unclear |  | This is a Breast Cancer Data Set with 286 instances of real patient data obtained from the Institute of Oncology, Ljubljana. The data set is publicly available from UCI Machine Lea |
| [vmsatya/SequentialTherapySecondCancer](https://github.com/vmsatya/SequentialTherapySecondCancer) | github | 0 | unclear |  | We employed a biologically motivated mathematical model to estimate the radiation and chemotherapy-induced relative risks of thyroid malignancies in four childhood cancer study sur |
| [yacibbbbb/RCI_radiation](https://github.com/yacibbbbb/RCI_radiation) | github | 0 | unclear |  | Simulate radiation in ROS 2 and Gazebo for radiation-aware robot navigation, mapping, and obstacle avoidance |
| [sjswerdloff/MCsquare](https://gitlab.com/sjswerdloff/MCsquare) | gitlab | 0 | unclear |  | Source code of the fast Monte Carlo dose calculation MCsquare |
| [kels271828/FluenceMapOpt](https://github.com/kels271828/FluenceMapOpt) | github | 15 | unclear |  | A nonconvex optimization approach to IMRT planning with dose-volume constraints |
| [ryanneph/RTTypes](https://github.com/ryanneph/RTTypes) | github | 9 | unclear |  | Library for handling common data formats seen in Radiation Therapy |
| [eduardoh27/FilmQADose](https://github.com/eduardoh27/FilmQADose) | github | 7 | unclear |  | FilmQADose is an open-source software for the analysis of radiochromic films in radiation therapy QA (Quality Assurance). It provides intuitive calibration tools and dose map gener |
| [jmartens/med-phys-scripts](https://github.com/jmartens/med-phys-scripts) | github | 5 | unclear |  | Scripts used in the RayStation medical radiation dosimetry treatment planning system |
| [abbasmzs/FluenceMapOptimization](https://github.com/abbasmzs/FluenceMapOptimization) | github | 2 | unclear |  | Included by heuristic/manual filtering. |
| [mikkelskaarup/Longitudinal-image-analysis-of-biological-effects](https://github.com/mikkelskaarup/Longitudinal-image-analysis-of-biological-effects) | github | 1 | unclear |  | This repository contains code to analyse biological effects of radiation and radiotherapy over time. It uses hybrid templates to register images and create a voxel-by-voxel data se |
| [majidkazemi89/GATE-JPET_ComptonCamera](https://github.com/majidkazemi89/GATE-JPET_ComptonCamera) | github | 1 | unclear |  | GATE code for simulation of J-PET as a Compton camera for proton range verification |
| [liq07lzucn/Grid-Sampling-for-Intensity-Modulated-Radiation-Therapy](https://github.com/liq07lzucn/Grid-Sampling-for-Intensity-Modulated-Radiation-Therapy) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [ruchi86/radiation_therapy](https://github.com/ruchi86/radiation_therapy) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [Nnamdi-Ike/Proton-therapy-patient-QA-optimizer](https://github.com/Nnamdi-Ike/Proton-therapy-patient-QA-optimizer) | github | 0 | unclear |  | Re-organizes proton therapy patient QA for shortest time... |
| [EliasFink122/Proton_Radiography](https://github.com/EliasFink122/Proton_Radiography) | github | 0 | unclear |  | Automating the analysis of proton radiography RCF films at York Plasma Institute |
| [anqif/opt_frac](https://github.com/anqif/opt_frac) | github | 0 | unclear |  | Optimal Dose Scheduling for Radiotherapy |
| [annalifousi/gene-expression-analysis](https://github.com/annalifousi/gene-expression-analysis) | github | 0 | unclear |  | This project investigates the impact of low-dose radiation therapy (RT) on CAR T-cell efficacy in a mouse model of CD19+ lymphoma, focusing on gene expression changes in irradiated |
| [perezmalau/pbt-secondary-particle-biasing](https://github.com/perezmalau/pbt-secondary-particle-biasing) | github | 0 | unclear |  | Proton therapy Geant4 simulation with directional biasing of secondary radiation towards a Compton camera. |
| [GunnarssonJust/Stereotaxy](https://github.com/GunnarssonJust/Stereotaxy) | github | 0 | unclear |  | Simple stereotactic radio surgery (SRS) - protocol according to ICRU 91 for stereotactic surgery in radiation therapy, python |
| [jawka/Simulations_GATE](https://github.com/jawka/Simulations_GATE) | github | 0 | unclear |  | GATE scripts for the PET-based proton range verification simulations |
| [renatobellotti/Juliana.jl](https://github.com/renatobellotti/Juliana.jl) | github | 5 | unclear | Treatment Planning and dosimetry | Accelerates proton radiotherapy research. Flexible, modular toolkit. |
| [mcode/rttd-summary-webapp](https://github.com/mcode/rttd-summary-webapp) | github | 1 | unclear |  | A react-based web application for viewing Radiation Therapy Treatment Data (RTTD) summaries |
| [jacyap/FilmProtocol](https://github.com/jacyap/FilmProtocol) | github | 1 | unclear |  | Protocol for plotting calibration curves and beam profiles from film with MATLAB & ImageJ |
| [RuiGSValente/IMRT-Project](https://github.com/RuiGSValente/IMRT-Project) | github | 1 | unclear |  | Computational methods for beam angle optimization in intensity modulated radiotherapy |
| [gakugaku3333/radiation-therapy-textbook](https://github.com/gakugaku3333/radiation-therapy-textbook) | github | 0 | unclear |  | 放射線治療部門 異動前準備教科書 ＋ ポッドキャストスクリプト |
| [VMHengo/Assisted-Radiation-Therapy](https://github.com/VMHengo/Assisted-Radiation-Therapy) | github | 0 | unclear |  | A small uni project that can be used to assist in radiation therapy. Enables 3D MRT Scans to be inspected |
| [jamiedean/glioblastoma-radiation-therapy-schedule](https://github.com/jamiedean/glioblastoma-radiation-therapy-schedule) | github | 0 | unclear |  | Code accompanying the paper "A phase I study of a novel glioblastoma radiation therapy schedule exploiting cell-state plasticity". |
| [reriri0426/radiation-therapy](https://github.com/reriri0426/radiation-therapy) | github | 0 | unclear |  | Included by heuristic/manual filtering. |
| [elishapruner/Makerspace-VR-Challenge](https://github.com/elishapruner/Makerspace-VR-Challenge) | github | 0 | unclear |  | Developing VR apps that help with patient care during chemotherapy and radiation therapy treatments |
| [MIRO-UCLouvain/RT-Probabilistic-Evaluation](https://github.com/MIRO-UCLouvain/RT-Probabilistic-Evaluation) | github | 0 | unclear |  | Probabilistic evaluation library for radiation therapy treatment based on OpenTPS |
| [Kachop/PHYS488-Project](https://github.com/Kachop/PHYS488-Project) | github | 0 | unclear |  | A proton beam therapy simulation which uses DICOM files to build the body to act as a target. |
| [pCT-collaboration/pypct](https://github.com/pCT-collaboration/pypct) | github | 0 | unclear |  | Python helpers for proton CT |
| [PortPy-Project/PortPy](https://github.com/PortPy-Project/PortPy) | github | 193 | unclear | Treatment Planning and dosimetry | PortPy, short for Planning and Optimization for Radiation Therapy, is an initiative aimed at creating an open-source Python library for cancer radiotherapy treatment planning optim |
| [e0404/pyRadPlan](https://github.com/e0404/pyRadPlan) | github | 43 | unclear | Artificial Intelligence, Treatment Planning and dosimetry | Related to matRad. Aims to facilitate AI integration into treatment planning workflows (research only). |
| [choijinkyung/RT-VIEWER](https://github.com/choijinkyung/RT-VIEWER) | github | 15 | unclear |  | Web/App based DICOM RT Viewer |
| [KitwareMedical/x-ray-genius](https://github.com/KitwareMedical/x-ray-genius) | github | 9 | unclear |  | A web-based application image generation tool that generates synthetic X-rays (DRRs) from CT scans, enabling research and AI development in orthopedics and beyond. |
| [ZhouD-CHN/dicomViewer](https://github.com/ZhouD-CHN/dicomViewer) | github | 9 | unclear |  | This program is a prototype of a Dicom-RT file viewer based on Python3. The GUI of the viewer is based on wxpython. Further update and optimization implemented with my research on  |
| [Mark-William-Schumacher/Medical-3D-Printing](https://github.com/Mark-William-Schumacher/Medical-3D-Printing) | github | 7 | unclear |  | Project I worked on for a year and a half during my undergrad, coded fully in python . The Project is used to create 3d printed moulds from a patients X-ray CT scans. These moulds  |
| [mfkasim1/invert-shadowgraphy](https://github.com/mfkasim1/invert-shadowgraphy) | github | 7 | unclear |  | This is matlab codes to invert shadowgraphy or proton radiography images to obtain the deflection of the light beam (or proton beam in proton radiography case). |
| [victorgabr/DVH-Check](https://github.com/victorgabr/DVH-Check) | github | 6 | unclear |  | Read RT DICOM files, evaluate protocol constraints using dicompyler and bokeh |
| [IdahoLabUnsupported/SERA](https://github.com/IdahoLabUnsupported/SERA) | github | 5 | unclear |  | Simulation Environment for Radiotherapy Applications (SERA) is a package to help create treatment plans for treating tumors with boron neutron capture therapy. SERA allows calculat |
| [HAWAIILAB/CLAIRE-ROP](https://github.com/HAWAIILAB/CLAIRE-ROP) | github | 2 | unclear |  | Rapid Partitioning-based Deformable Image Registration on Multi-GPU Accelerator |
| [ErAK1006/Syntactic-Processing-Assignment-Aditya](https://github.com/ErAK1006/Syntactic-Processing-Assignment-Aditya) | github | 1 | unclear |  | “The patient was a 62-year-old man with squamous cell lung cancer, which was first successfully treated by a combination of radiation therapy and chemotherapy.” |
| [dusse/KAP](https://github.com/dusse/KAP) | github | 1 | unclear |  | kinetic code for proton radiography |
| [Varada-K/Breast-Cancer-Stage-Simulation](https://github.com/Varada-K/Breast-Cancer-Stage-Simulation) | github | 0 | unclear |  | This repository contains Python code developed for a class in advanced topics in decision making, with a focus on comparing the cost-effectiveness of Radiation Therapy and Breast C |
| [Damilola-design/NER_Healthcare_Data](https://github.com/Damilola-design/NER_Healthcare_Data) | github | 0 | unclear |  | The following snippet of medical data may be generated when a doctor is writing notes to his/her patient or as a review of a therapy that he or she has done. "The patient was a 62- |
| [SylwekFr/lung_analysis](https://github.com/SylwekFr/lung_analysis) | github | 0 | unclear |  | Master thesis project, comparison of lung tissues before and after Radiation therapy |
| [Torros6/Paper-2022](https://github.com/Torros6/Paper-2022) | github | 0 | unclear |  | Script used in the paper: Uncertainties in Proton Therapy and Their Impact on Treatment Precision |
| [SebastiaanBreedveld/TROTS](https://github.com/SebastiaanBreedveld/TROTS) | github | 12 | unclear |  | Scripts for working with the TROTS (The Radiotherapy Optimisation Test Set) dataset |
| [mrmushfiq/qalma](https://github.com/mrmushfiq/qalma) | github | 12 | unclear | Quality Assurance | A Matlab based toolkit with GUI for quantitative analysis of Quality Assurance tests for Medical Linear Accelerators in Radiation Therapy. |
| [anqif/adarad](https://github.com/anqif/adarad) | github | 3 | unclear |  | Operator Splitting for Adaptive Radiation Therapy |
| [DataMedSci/PTAM](https://github.com/DataMedSci/PTAM) | github | 1 | unclear |  | Collection of Particle Therapy Analytical Models |
| [inata169/rt-dicom-toolkit](https://github.com/inata169/rt-dicom-toolkit) | github | 0 | unclear |  | Comprehensive toolkit for anonymizing and validating radiotherapy (RT) DICOM files. Includes modern GUI and CLI. |
| [RosaPetit/Review-Radiotherapy-](https://github.com/RosaPetit/Review-Radiotherapy-) | github | 0 | unclear |  | Medical physicists have long had an integral role in radiotherapy. This space is dedicated to a theoretical review of the principles topics of radiation physics amount other aspect |
| [medical-physics-usz/ARTEMIS](https://github.com/medical-physics-usz/ARTEMIS) | github | 0 | unclear |  | ARTEMIS: Adaptive Radiation Therapy Enhanced by Magnetic Resonance Imaging Systems |
| [Radcorder/rt-viewer](https://github.com/Radcorder/rt-viewer) | github | 0 | unclear |  | A high-performance static web viewer for Radiation Therapy planning data. Optimized for speed, security, and zero-footprint deployment. |
| [zhailei-scu/TRTimeRecord](https://github.com/zhailei-scu/TRTimeRecord) | github | 0 | unclear |  | A QT-based GUI package for Proton-radiation therapy time record. |
| [ABiteofPi/MedData](https://github.com/ABiteofPi/MedData) | github | 0 | unclear |  | This project aims to help chemo/radiation therapy patients with sensitive skin better prepare against the damages of UV radiation. |
| [capaldid/TBILungBlock](https://github.com/capaldid/TBILungBlock) | github | 0 | unclear |  | Tungsten filled 3D printed lung blocks for total body irradiation |
| [GuillaumeEsclozas/CBCT-Reconstruction-Simulator](https://github.com/GuillaumeEsclozas/CBCT-Reconstruction-Simulator) | github | 0 | unclear |  | Fast CBCT image reconstruction simulator demonstrating trade-offs between acquisition speed and image quality for adaptive proton therapy |
| [qatrackplus/qatrackplus](https://github.com/qatrackplus/qatrackplus) | github | 71 | unclear | Quality Assurance | QATrack+ is a fully configurable, free, and open source (MIT License) web application for managing QA data for radiation therapy and medical imaging equipment |
| [bungun/conrad](https://github.com/bungun/conrad) | github | 8 | unclear |  | convex radiation treatment planning |
| [MatthewPeterKelly/FluenceMapping](https://github.com/MatthewPeterKelly/FluenceMapping) | github | 4 | unclear |  | Trajectory optimization to match fluence profiles. |
| [danielsuareza/Cost_Effective_ART_MDP](https://github.com/danielsuareza/Cost_Effective_ART_MDP) | github | 1 | unclear |  | GitHub Repo for "Cost-Effectiveness of Personalized Policies for Implementing Organ- at-Risk Sparing Adaptive Radiation Therapy in Head and Neck Cancer: A Markov Decision Process A |
| [jamillambert/QA-tools](https://github.com/jamillambert/QA-tools) | github | 1 | unclear |  | Tools for routine proton therapy QA, mostly written in Python, c++ and Matlab |
| [dchansen/protonCT](https://github.com/dchansen/protonCT) | github | 1 | unclear |  | A library for proton CT reconstruction |
| [Bogdan-Belogurov/SwiftCare](https://github.com/Bogdan-Belogurov/SwiftCare) | github | 0 | unclear |  | App for the Radiotherapy Treatment Optimization |
| [Image-X-Institute/Markerless-tracking-phantom](https://github.com/Image-X-Institute/Markerless-tracking-phantom) | github | 0 | unclear |  | Repo for the code and stl files for a markerless tracking phantom to assist with performance characterisation and quality assurance for radiation therapy |
| [arthur-chakwizira/bed](https://github.com/arthur-chakwizira/bed) | github | 0 | unclear |  | Biologically Effective Dose calculator for radiation therapy. |
| [jjgomezcadenas/PTCryspMC.jl](https://github.com/jjgomezcadenas/PTCryspMC.jl) | github | 0 | unclear |  | Proton Therapy CRYSP simulations MC (in Julia) |
| [LukaPasaricek/MC_intercomparison_EURADOS_WG6_9_11](https://github.com/LukaPasaricek/MC_intercomparison_EURADOS_WG6_9_11) | github | 0 | unclear |  | Relevant information about the comparison exercise, including the input files for the article "Assessing Stray Neutron Dose Variability Across Monte Carlo Codes in a Proton Therapy |
| [andresperezrobinson/Thesis-IRIS](https://github.com/andresperezrobinson/Thesis-IRIS) | github | 0 | unclear |  | This is the work, data and code, I used/built for my thesis "Fast Monte Carlo Simulations of Dose Deposit in Proton Therapy" |
| [rvroerm/PT-clinical](https://github.com/rvroerm/PT-clinical) | github | 0 | unclear |  | Make some data analysis on public clinical data in order to assess the future needs for proton therapy |
| [Ben12345678901/Proton-Radiograpy](https://github.com/Ben12345678901/Proton-Radiograpy) | github | 0 | unclear |  | Simple proton radiography code that utilises a lorentz function to track the trajectories of charged particles passing through a magnetic field |
| [nsmela/Fabolus-v16](https://github.com/nsmela/Fabolus-v16) | github | 10 | unclear |  | Modifies STL files representing bolus for radiation therapy. Prepares them for 3D printing. Now using MVVM. |
| [nsmela/Fabolus](https://github.com/nsmela/Fabolus) | github | 8 | unclear | Software Engineering and Data Infrastructure | Fabolus is a Windows-based app designed to assist radiation therapy prepare bolus meshes for 3D printing |
| [dfhoyosg/17-021_RT_IpiNivo](https://github.com/dfhoyosg/17-021_RT_IpiNivo) | github | 1 | unclear |  | Mutation calling code for the paper: Radiation Therapy Enhances Immunotherapy Response in Microsatellite-stable Colorectal and Pancreatic Adenocarcinoma in a Phase II Trial |
| [api-evangelist/radionetics-oncology](https://github.com/api-evangelist/radionetics-oncology) | github | 0 | unclear |  | Radionetics Oncology is a clinical-stage biotechnology company developing precision radiopharmaceutical treatments for cancer. The company designs small-molecule radioligands that  |
| [lixinzhan/RT-DP](https://github.com/lixinzhan/RT-DP) | github | 0 | unclear |  | Radiation Therapy Disaster Preparedness System |
| [rw565/PGRT-Monte-Carlo-Studies](https://github.com/rw565/PGRT-Monte-Carlo-Studies) | github | 0 | unclear |  | Monte Carlo and data analysis code associated with various studies related to Positron Guided Radiation Therapy |
| [jon-jacky/CNTS](https://github.com/jon-jacky/CNTS) | github | 0 | unclear |  | Web site about the Clinical Neutron Therapy System, a computer-controlled radiation therapy machine |
| [SnowyLea/KhanRadiationPhysicsHandbookSolutions](https://github.com/SnowyLea/KhanRadiationPhysicsHandbookSolutions) | github | 0 | unclear |  | solutions to the review problems in Khan's Lectures: Handbook of the Physics of Radiation Therapy |
| [MikeBao99/Radiation-Optimizer](https://github.com/MikeBao99/Radiation-Optimizer) | github | 0 | unclear |  | Cancer Radiation Therapy Linear Optimization |
| [kstawiski/rtpipeline](https://github.com/kstawiski/rtpipeline) | github | 6 | unclear | Clinical workflow and applications | RTpipeline is a comprehensive, research-grade pipeline that transforms raw DICOM radiotherapy exports into analysis-ready data. It bridges the technical gap between clinical Treatm |
| [OpenTOPAS/OpenTOPAS](https://github.com/OpenTOPAS/OpenTOPAS) | github | 76 | unclear | Treatment Planning and dosimetry | The TOPAS toolkit aims to provide an intuitive Monte Carlo framework for medical physicists and researchers in related fields |
| [IsoAnalytica/Sentinel-Public](https://github.com/IsoAnalytica/Sentinel-Public) | github | 35 | unclear | Quality Assurance | Sentinel is an automated log-file analysis application for Varian linacs (TrueBeam, Halcyon, Edge). |
| [brjdenis/VarianESAPI-EQD2Converter](https://github.com/brjdenis/VarianESAPI-EQD2Converter) | github | 21 | unclear | Treatment Planning and dosimetry | A Varian Eclipse scripting plugin for converting dose to EQD2 (equivalent dose in 2 Gy fractions). Automates the calculation of EQD2 for plans. |
| [Quantico-Bullet/PyBeam-QA](https://github.com/Quantico-Bullet/PyBeam-QA) | github | 18 | unclear | Quality Assurance | A Python library for performing beam quality assurance tests in radiotherapy. The software is in an early stage of development. |
| [cutright/DVH-Analytics](https://github.com/cutright/DVH-Analytics) | github | 86 | unclear | Software Engineering and Data Infrastructure | Public archive, no longer supported as of Feb 2, 2022. Designed for building local database of radiation oncology treatment planning data. |
| [didymo/OnkoDICOM](https://github.com/didymo/OnkoDICOM) | github | 72 | unclear | Imaging and Image Processing | Cross-platform. Provides DVH output, clinical data capture (radiomics), Pyradiomics output, anonymization, ROI manipulation. |
| [LDClark/PlanCheck](https://github.com/LDClark/PlanCheck) | github | 58 | unclear | Quality Assurance | A Varian Eclipse scripting plugin for treatment plan verification. Automates the process of checking a plan against a set of rules. |
| [alanphys/LinaQA](https://github.com/alanphys/LinaQA) | github | 42 | unclear | Quality Assurance | LinaQA (pronounced Linakwa) is a GUI frontend for pylinac and pydicom. |
| [MIC-DKFZ/RTTB](https://github.com/MIC-DKFZ/RTTB) | github | 32 | unclear | Treatment Planning and dosimetry | RTToolbox is a software library to support quantitative analysis of treatment outcome for radiotherapy. |
| [victorgabr/ApertureComplexity](https://github.com/victorgabr/ApertureComplexity) | github | 30 | unclear | Treatment Planning and dosimetry | Contains complete functionality of aperture complexity analysis. Extends methodology to any TPS exporting DICOM-RP. |
| [samuelpeet/conehead](https://github.com/samuelpeet/conehead) | github | 46 | unclear | Treatment Planning and dosimetry | Early experimental development, code expected to change dramatically. Uses Python/Cython. |
| [PhysicsResearch/AMIGOpy](https://github.com/PhysicsResearch/AMIGOpy) | github | 8 | unclear | Treatment Planning and dosimetry | Welcome to AMIGOpy (A Medical Image-based Graphical platfOrm - Python)! This is an evolution of the previously developed MATLAB-based software AMIGOBrachy. |
| [AIM-Harvard/pyradiomics](https://github.com/AIM-Harvard/pyradiomics) | github | 1438 | unclear | Imaging and Image Processing | PyRadiomics is an open-source python package for the extraction of Radiomics features from medical imaging |
| [pymedphys/pymedphys](https://github.com/pymedphys/pymedphys) | github | 364 | unclear | Quality Assurance | PyMedPhys is an open-source Medical Physics Python library built by an open community that values code sharing, review, improvement, and learning from each other. |
| [bastula/dicompyler](https://github.com/bastula/dicompyler) | github | 287 | unclear | Software Engineering and Data Infrastructure | Archived by owner on Feb 2, 2022, no longer supported. Built on pydicom, wxPython, Pillow, matplotlib. |
| [brjdenis/pyqaserver](https://github.com/brjdenis/pyqaserver) | github | 48 | unclear | Quality Assurance | A Python-based server for performing Quality Assurance tests. Provides a web interface for managing and running tests. |
| [samuelpeet/flashgamma](https://github.com/samuelpeet/flashgamma) | github | 32 | unclear | Quality Assurance | Code written for personal educational purposes. Performed similarly to proprietary gamma analysis codes internally, but not guaranteed bug-free. |

---

<sub>This file is generated automatically. Edit `src/render_readme.py` rather than `README.md`.</sub>
