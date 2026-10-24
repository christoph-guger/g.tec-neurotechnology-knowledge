# Unlock Brain Connectivity: Recording CCEPs and Mapping Functional Cortical Networks

- **Published:** 2025-03-21 on gtec.at
- **Original:** https://www.gtec.at/2025/03/21/recording-cceps-mapping-networks/
- **g.tec products:** g.HIamp, cortiQ, g.Estim, g.HIsys
- **Topics:** brain mapping, epilepsy

> **Summary:** Cortico-cortical evoked potentials (CCEPs) are a neurophysiological technique used to assess functional connectivity between different regions of the brain. By delivering electrical stimulation to one cortical area and recording the resulting activity in another, CCEPs help map brain networks involved in movement, sensation, and cognition.

---

Cortico-cortical evoked potentials (CCEPs) are a neurophysiological technique used to assess functional connectivity between different regions of the brain. By delivering electrical stimulation to one cortical area and recording the resulting activity in another, CCEPs help map brain networks involved in movement, sensation, and cognition.

Clinicians use this method during epilepsy surgery and brain mapping to preserve critical functions while guiding treatment. For patients, CCEPs provide valuable insights into brain function, helping tailor surgical or therapeutic approaches to individual needs.

## LEARN MORE

## Grey Matter Stimulation and White Matter Stimulation

In clinical settings, grey matter stimulation is often used to study cortical hubs and functional areas, while white matter stimulation helps assess deep brain connectivity, ensuring critical pathways are preserved during interventions.

Axono-Cortical Evoked Potentials (ACEPs) are particularly useful in neurosurgery and brain mapping, as they help identify and preserve critical white matter tracts, such as the corticospinal tract for movement or the arcuate fasciculus for language. By stimulating white matter directly, clinicians can assess how different fiber tracts influence cortical activity, ensuring safer surgical outcomes while minimizing functional deficits.

## CCEP Protocol and Patient Safety

The standard CCEP stimulation protocol involves delivering brief electrical pulses (typically biphasic, 0.2–1 ms duration) at low frequencies (0.2–1 Hz) through implanted cortical electrodes. Stimulation is applied at subthreshold levels to avoid inducing seizures while reliably eliciting responses in connected brain regions.

To ensure patient safety, clinicians carefully monitor for afterdischarges—abnormal electrical activity that may indicate increased excitability—and adjust parameters accordingly. CCEP studies are performed in controlled settings, often under anesthesia or sedation, with real-time EEG monitoring to minimize risks and optimize data quality.

Source: g.tec medical engineering.

## Tools for CCEP Recording and Analysis

CCEPs can be recorded using the g.HIamp biosignal amplifier, which supports a 4800 Hz sampling rate across 256 channels simultaneously. The g.Estim PRO switching unit enables software-controlled stimulation targeting specific brain regions via implanted electrodes. Additionally, the g.Estim PRO can be used for direct intraoperative stimulation to evaluate white matter connectivity during resective brain surgery. cortiQ Setup: g.HIamp biosignal amplifier, which supports a 4800 Hz sampling rate across 256 channels simultaneously. g.Estim PRO Switching Unit enables software-controlled stimulation targeting specific brain regions via implanted electrodes. g.Estim PRO can be used for direct intraoperative stimulation to evaluate white matter connectivity during resective brain surgery.

## Dr. Kamada applied the CCEP technique at

Asahikawa Medical University and Megumino Hospital to monitor the disconnection of epilepsy-related networks. When CCEP responses diminished during resection, seizure propagation could be effectively suppressed.

Source: Kamada, K., Kapeller, C., Takeuchi, F., Gruenwald, J., & Guger, C. (2020).

Tailor-made surgery based on functional networks for intractable epilepsy.

Frontiers in Neurology, 11, 73. 1.Automatic CCEP Screening for Brain Connectivity Mapping Another valuable approach is automatic CCEP screening using the g.Estim PRO Switching Unit. In this method, a sequence of stimulation locations is processed in real time through the g.HIsys high-speed online system in Simulink. Stimulation occurs automatically while the patient remains seated without performing any specific task.

The software displays the evoked potential waveforms and their topographical distribution in real time. After one hour of stimulation, connectivity across more than 100 brain regions can be assessed.

A new approach to mapping brain connectivity uses single-pulse electrical stimulation to identify basis profile curves (BPCs) —distinct waveform shapes that naturally group brain regions based on their responses. Researchers utilized the g.HIamp amplifier alongside the g.Estim PRO switching unit.

Instead of relying on predefined response patterns, this method clusters input types based on their temporal dynamics, improving the classification of functional networks. By stimulating different sites and recording responses at a single location, researchers quantified connectivity more precisely.

This technique refines CCEP-based mapping used at the Mayo Clinic, offering clearer insights into brain organization. An open-source code package enables clinicians to apply this method for personalized brain network analysis.

Source: g.tec medical engineering.

Source: Miller, K. J., Müller, K. R., & Hermes, D. (2021).

Basis profile curve identification to understand electrical stimulation effects in human brain networks.

PLoS computational biology, 17(9), e1008710. 2. CCEP Waveform Characteristics and Filtering Considerations The valid shape of CCEPs typically consists of an early response (10–50 ms) and a late response (50–300 ms), reflecting different synaptic transmission processes in cortical networks. These waveforms can vary in amplitude and latency depending on the stimulation site, cortical excitability, and individual brain anatomy.

However, filtering settings significantly influence the recorded waveform. High-pass filtering (e.g., >1 Hz) can distort slow components and attenuate late responses, while aggressive low-pass filtering (e.g., <500 Hz) may remove high-frequency details, affecting the interpretation of early responses.

Optimal filtering parameters should balance noise reduction while preserving the true morphology of CCEPs to ensure accurate analysis of cortical connectivity. 3. P0 Component and White Matter Stimulation (ACEPs) The P0 component in CCEPs is an early positive deflection occurring within the first 5–20 ms after stimulation. It is believed to reflect direct axonal activation or the initial excitatory response in the stimulated network.

P0 is typically observed in white matter stimulation (ACEPs) or in cases where stimulation directly activates fast-conducting pathways before synaptic processing occurs. However, the presence and clarity of P0 can be influenced by filtering and stimulation polarity.

## High-pass filtering

(e.g., >1 Hz) may attenuate slower components and enhance P0 visibility.

Alternating polarity stimulation can help distinguish true P0 from stimulation artifacts.

Careful parameter selection is crucial to avoid misinterpretation of early responses and ensure accurate CCEP waveform analysis.

Source: Acunzo, D. J., MacKenzie, G., & van Rossum, M. C. (2012).

Systematic biases in early ERP and ERF components as a result of high-pass filtering.

Journal of neuroscience methods, 209(1), 212-218. 5. Research on Electrical Stimulation Effects Researchers from the INRIA branch of the University of Montpellier investigated how electrical stimulation affects the brain when applied directly to the cortex or through white matter pathways.

Using the g.HIamp system with a DC-coupled amplifier, they recorded brain responses without applying a high-pass filter, preserving the full signal, including slow components that might otherwise be lost.

Their findings showed that white matter stimulation caused a slight delay (around 2 milliseconds) due to slower signal conduction, while direct cortical stimulation triggered additional activity, likely involving smaller, slower axons.

Despite these timing differences, the overall response patterns remained similar. These insights help neurosurgeons and neurologists better interpret brain activity during surgery and could refine techniques for epilepsy treatment and brain stimulation therapies, leading to more precise and effective interventions for patients.

Source: Turpin, C., Rossel, O., Schlosser-Perrin, F., Ng, S., Matsumoto, R., Mandonnet, E., … & Bonnetblanc, F. (2025).

Shapes of direct cortical responses vs. short-range axono-cortical evoked potentials: The effects of direct electrical stimulation applied to the human brain. Clinical Neurophysiology, 169, 91-99.

## Alternating Polarity in CCEP Stimulation

Alternating polarity in CCEP stimulation involves delivering biphasic pulses with reversed polarity across trials to minimize stimulation artifacts and direct current (DC) shifts.

This approach helps differentiate genuine neurophysiological responses from artifacts caused by electrical stimulation, particularly in early time windows. Without alternating polarity, large stimulation-induced artifacts can obscure the early components of CCEPs, making it difficult to accurately assess cortico-cortical connectivity.

However, excessive filtering combined with alternating polarity may distort the true waveform by canceling out slower components, especially in late responses. Therefore, careful signal processing is essential to preserve the authentic shape of CCEPs while effectively reducing artifacts.

Source: g.tec medical engineering.

## LEARN MORE

Useful Links:

**Publication:** Facephenes and rainbows: Causal evidence for functional and anatomical specificity of face and color processing in the human brain Video:

Intraoperative placement of an ECoG grid using cortiQ PRO 2.0

**Video:** CCEP mapping with cortiQ rapid cortical mapping system

---
*Source: g.tec medical engineering, [https://www.gtec.at/2025/03/21/recording-cceps-mapping-networks/](https://www.gtec.at/2025/03/21/recording-cceps-mapping-networks/). Text reused under CC BY 4.0.*
