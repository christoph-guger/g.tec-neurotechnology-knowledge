# Multimodal EEG, Eye Tracking, ECG & GSR for Flight Simulation Research

- **Published:** 2026-07-20 on gtec.at
- **Original:** https://www.gtec.at/2026/07/20/multimodal-flight-simulation-recording/
- **g.tec products:** g.Nautilus, g.HIsys, g.BSanalyze
- **Topics:** eye tracking, human factors

> **Summary:** Modern neuroscience and human factors experiments increasingly evaluate cognitive performance in realistic environments rather than highly controlled laboratory settings. In many cases, combining EEG with additional biosignals provides deeper insight into the subject’s or patient’s physiological and cognitive state, helping researchers assess stress levels and other cognitive functions.

---

Modern neuroscience and human factors experiments increasingly evaluate cognitive performance in realistic environments rather than highly controlled laboratory settings. In many cases, combining EEG with additional biosignals provides deeper insight into the subject’s or patient’s physiological and cognitive state, helping researchers assess stress levels and other cognitive functions.

The proposed model can easily be adapted to calculate different cognitive metrics and physiological biomarkers. During pilot studies, this approach helps identify which parameters and channels best capture the expected effects. Researchers can then optimize the experimental paradigm, improve subject or patient collaboration, and ensure high data quality.

## During a workshop at

University College London (UCL) with Professor Tom Carlson, we demonstrated how synchronized EEG, ECG, GSR, and eye tracking can be combined during a realistic flight simulation experiment. Students from UCL’s MSc in Rehabilitation Engineering and Assistive Technologies participated in setting up and performing the experiment.

The objective was to monitor changes in Mental Workload, Engagement, and Heart Rate Variability (HRV) during two complete flight cycles, including take-off, free flight, and landing. The multimodal approach enables simultaneous assessment of neural activity, autonomic nervous system responses, and visual attention throughout the task.

Engagement was continuously estimated using the β/(α+θ) power band ratio (1), while Mental Workload was estimated from gamma-band power (2). Although gamma-band power was generally a less reliable indicator of Mental Workload, it appeared to be particularly sensitive during stressful situations. Heart Rate Variability was extracted from the ECG signal using the RMSSD metric (3). All displayed values represent the average of consecutive five-second epochs.

The proposed model can easily be adapted to calculate different cognitive functions and biomarkers. The sensitivity (gain) of each parameter can also be adjusted because the recorded data are not normalized during acquisition.

Cognitive functions can be calculated from a single EEG channel, a pair of channels, or as an average across multiple channels, depending on the application. Likewise, the duration of the analysis epochs can be adjusted to match the requirements of different experimental paradigms.

## Experiment Design

To demonstrate multimodal biosignal acquisition during a realistic task, participants completed two flight cycles around Cape Town using the freely available GeoFS flight simulator. The experiment included take-off, free flight, and landing, providing a reproducible scenario with varying levels of cognitive workload and task complexity.

The simulation was performed using the standard Cessna aircraft and controlled with a standard computer keyboard. Although the task is easy to learn, it requires continuous attention, visual navigation, and motor coordination, making it well suited for evaluating cognitive performance under realistic operating conditions.

## Multimodal Data Collection

The experiment combined EEG, ECG, Galvanic Skin Response (GSR), and eye tracking to monitor neural activity, autonomic responses, and visual attention simultaneously. All biosignals were synchronized and recorded in real time using the g.tec neurotechnology ecosystem.

The setup included: g.Nautilus Multi-Purpose

## (28-channel wireless EEG )

ECG for Heart Rate Variability (RMSSD)

## Galvanic Skin Response (GSR)

## Tobii Pro Glasses 3 for eye tracking, pupil diameter, and gaze position

Real-time signal validity monitoring to detect connection quality during mobile recordings Data acquisition, synchronization, and real-time signal processing were performed with g.HIsys, a MATLAB Simulink-based environment that enables multimodal biosignal acquisition, feature extraction, and visualization within a single workflow. The software includes dedicated processing blocks for filtering, band-power calculation, feature extraction, and physiological metrics such as RMSSD and pNN50, allowing researchers to build custom multimodal workflows with minimal programming effort.

## Rapid Subject Preparation

The multimodal setup can be prepared within 30 minutes. The EEG cap is quickly mounted, while ECG requires only a single electrode placed opposite the EEG reference electrode (A2). GSR sensors are attached to the index and ring fingers, and the trigger output of the Tobii Pro Glasses 3 is connected directly to the amplifier to synchronize gaze events with the physiological recordings.

Once prepared, participants remain fully mobile throughout the experiment, enabling natural movement during realistic simulations.

## Offline Eye Tracking Analysis

After recording, gaze markers generated in Tobii Pro Lab are automatically imported into g.BSanalyze using the gbsImportTobiiAOIEvents_TPG3 batch tool. These synchronized markers identify events such as take-off, approach, and landing, but can also be used to define Areas of Interest (AOIs), detect when participants observe specific flight instruments, segment EEG epochs, and calculate event-related potentials such as P300.

By synchronizing EEG, eye tracking, ECG, and GSR within a single acquisition platform, researchers can objectively investigate attention, mental workload, engagement, stress, and cognitive performance during realistic tasks while maintaining precise temporal synchronization between all recorded modalities.

## References

T. McMahan, I. Parberry, and T. D. Parsons, “Evaluating electroencephalography engagement indices during video game play,” University of North Texas, Denton, TX, Rep. LARC-2015-03, 2015.

Laura K. Halderman, Bridgid Finn, J.R. Lockwood, Nicole M. Long, & Michael J. Kahana “EEG Correlates of Engagement During Assessment” ETS Research Report Series ISSN 2330-8516.

Cao X, MacNaughton P, Cadet LR, Cedeno-Laurent JG, Flanigan S, Vallarino J, Donnelly-McLay D, Christiani DC, Spengler JD, Allen JG. Heart Rate Variability and Performance of Commercial Airline Pilots during Flight Simulations. Int J Environ Res Public Health. 2019 Jan 16;16(2):237.

---
*Source: g.tec medical engineering, [https://www.gtec.at/2026/07/20/multimodal-flight-simulation-recording/](https://www.gtec.at/2026/07/20/multimodal-flight-simulation-recording/). Text reused under CC BY 4.0.*
