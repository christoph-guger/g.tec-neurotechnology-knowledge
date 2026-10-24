# Revolutionizing Neuromodulation: The Exciting Potential of Open- and Closed Loop Systems with MATLAB and Simulink

- **Published:** 2024-04-04 on gtec.at
- **Original:** https://www.gtec.at/2024/04/04/open-and-closed-loop/
- **g.tec products:** g.HIamp, g.Estim, g.HIsys
- **Topics:** brain mapping, epilepsy

> **Summary:** Neuromodulation involves the deliberate alteration of nerve activity through targeted delivery of stimuli, such as electrical impulses or drugs, aiming to either enhance or inhibit neural function. This interdisciplinary field intersects neuroscience, medicine, and technology, offering promising applications for treating various neurological and psychiatric disorders.

---

## Neuromodulation in a nutshell

Neuromodulation involves the deliberate alteration of nerve activity through targeted delivery of stimuli, such as electrical impulses or drugs, aiming to either enhance or inhibit neural function. This interdisciplinary field intersects neuroscience, medicine, and technology, offering promising applications for treating various neurological and psychiatric disorders.

## Contents

## Application Fields

## Technical Realization

A complete Neuromodulation Setup

## Examples

## Impedance Measurement

Electrical Cortical Stimulation (ECS)

CCEP screening

## Summary

## Application Fields

Figure 1 illustrates the key domains of neuromodulation applications, broadly categorized into functional brain mapping and disorder treatment.

Figure 1 Application fields of open-loop and closed-loop neuromodulation.

Functional brain mapping employs various techniques to comprehend the organization and function of distinct brain regions. Electrical cortical stimulation (ECS) involves applying electrical pulses directly to the brain’s surface to elicit specific responses, aiding in mapping functional areas and pinpointing critical regions such as motor or language centers. Cortico-cortical evoked potentials (CCEPs) gauge communication between different cortical areas by stimulating one region and recording responses from another, providing insights into brain interconnections. Somatosensory evoked potentials (SEPs) evaluate sensory pathway integrity by recording brain responses to external stimuli, assisting in localizing sensory processing areas. These methods offer crucial information for surgical planning, neuroscientific research, and understanding brain function in health and disease.

The treatment of neurological and psychiatric disorders via neuromodulation encompasses several innovative techniques. Deep brain stimulation (DBS), including adaptive approaches, entails implanting electrodes into specific brain regions to administer controlled electrical pulses, effectively modulating aberrant neural activity associated with conditions like Parkinson’s disease, essential tremor, or obsessive-compulsive disorder. Vagus nerve stimulation (VNS) involves implanting a device that delivers electrical impulses to the vagus nerve, providing relief for epilepsy, depression, and other disorders by modulating neural circuits implicated in these conditions.

Responsive neurostimulation (RNS) systems are designed to detect and respond to abnormal brain activity, delivering targeted stimulation to prevent seizures in epilepsy patients. These techniques offer promising therapeutic avenues, fostering hope for improved management of various neurological and psychiatric disorders.

These application domains motivate clinical research and the development of future open-loop and closed-loop neuromodulation systems. Open-loop neuromodulation involves predetermined stimulation parameters delivered without real-time adjustment based on feedback from the patient’s neural activity, offering consistent but potentially less adaptable treatment. In contrast, closed-loop neuromodulation systems continually monitor neural signals and adjust stimulation parameters in real time, providing personalized and adaptive therapy tailored to the patient’s changing needs, potentially enhancing efficacy and minimizing side effects.

## Technical Realization

**A neuromodulation platform typically encompasses three essential functionalities:** Real-time controlled electrical stimulation of the brain: This feature allows for precise and adjustable electrical stimulation of specific brain regions to modulate neural activity effectively.

Brain signal sensing and interpretation: The platform should be capable of detecting and interpreting neural signals in real time, providing valuable feedback for adjusting stimulation parameters.

Programmatic switching of stimulation signals to dedicated brain regions: The ability to dynamically route stimulation signals is a key enabler of novel, adaptive treatment protocols. Existing protocols can be substantially simplified and shortened if no manual intervention is needed to change stimulation sites.

All of these functions must operate with minimal latency to ensure timely and accurate stimulation delivery. Additionally, all hardware components involved must adhere to stringent medical safety standards to prevent any harm to the patient throughout the neuromodulation process.

## A complete Neuromodulation Setup

## Figure 2 Hard- and software integration of a multi-purpose neuromodulation setup

The complete neuromodulation setup developed by g.tec medical engineering, depicted in Figure 2, addresses the technical requirements outlined earlier. It consists of three primary hardware components: a cortical stimulator ( g.Estim PRO) that generates bipolar electrical stimulation, a biosignal amplifier ( g.HIamp) for recording brain signals at the highest quality, and a Switching Unit that programmatically routes stimulation signals to dedicated electrodes while allowing the recording of signals from other electrodes. All hardware components are clinically certified to relevant standards.

A control PC communicates with the hardware components via C-APIs, while MATLAB and Simulink are utilized for application prototyping. Figure 3 shows an exemplary Simulink model. This model comprises three blocks controlling the g.HIamp, the g.Estim PRO, and the Switching Unit. The amplifier block receives signals acquired by the g.HIamp, which are further processed and visualized in real-time via g.SCOPE blocks. Additionally, the model includes a block for selecting the stimulation site in an interactive 3D viewer. The user input then configures and activates the Switching Unit and the g.Estim PRO to stimulate the chosen site. Stimulation parameters (for example, phase duration and amplitude) can be adjusted online using Simulink real-time control sliders.

Figure 3 Typical multi-purpose Simulink model.

GET A QUOTE

## Examples

## Impedance Measurement

Monitoring electrode impedances is crucial in a neuromodulation system to prevent high stimulation voltages that can cause discomfort or pain to the patient. The Switching Unit includes an integrated impedance measurement feature, easily accessible through a graphical user interface (GUI) designed with MATLAB AppDesigner.

Figure 4 illustrates a typical outcome of an impedance measurement conducted using this GUI. Users can select the measurement mode, channels, and frequencies before initiating the measurement. Once completed, the results are displayed, and the GUI enables easy navigation through the data for further analysis and interpretation. This capability ensures that electrode impedances are effectively monitored, contributing to patient safety and comfort during neuromodulation procedures.

Figure 4 Switching Unit impedance check.

## Electrical Cortical Stimulation (ECS)

As previously mentioned, electrical cortical stimulation (ECS) is the established clinical method for functional mapping. ECS sessions can be conveniently conducted with the g.tec neuromodulation system and MATLAB/Simulink frontend. Figure 5 illustrates the typical user interface during an ECS session.

The channel selection scope (bottom left) enables users to configure the Switching Unit and the g.Estim PRO to stimulate specific electrodes. Concurrently, brain signals recorded by the g.HIamp are displayed in the g.SCOPE (right) for visual inspection. Additionally, the patient’s behavioral response is recorded via video (top left), providing comprehensive data for effective functional mapping.

Figure 5 Electrical cortical stimulation using the g.tec neuromodulation setup and MATLAB/Simulink frontend.

## GET A QUOTE

CCEP screening g.tec’s neuromodulation setup offers automation for Cortico-Cortical Evoked Potentials (CCEP) measurements. In an automated “CCEP screening” session, the Switching Unit and g.Estim PRO are programmed to automatically cycle through a predefined set of stimulation sites. Each channel set then receives a specific number of stimulations, such as 30 bipolar rectangular pulses with 15 mA amplitude, 300 µs duration, and 1 pulse per second.

Figure 6 displays a screenshot of the Simulink user interface during such a CCEP screening session. The g.SCOPE presents recorded signals and highlights stimulation sites (left), while the g.EPScope depicts the evoked potentials (EPs) generated by the stimulation (middle). Additionally, the Bubblescope represents EP amplitudes as bubble sizes on a 3D brain model. All data are stored for subsequent analysis in MATLAB, facilitating thorough retrospective examination.

Figure 6 CCEP screening using the g.tec neuromodulation setup and MATLAB/Simulink frontend.

## Summary

In this article, we discussed the application of open- and closed-loop neuromodulation using MATLAB and Simulink. We outlined the significance of neuromodulation in targeting neural activity for both functional brain mapping and disorder treatment, such as electrical cortical stimulation (ECS), cortico-cortical evoked potentials (CCEP), and deep brain stimulation (DBS). g.tecs neuromodulation system seamlessly integrates the g.Estim PRO cortical stimulator, the g.HIamp biosignal amplifier, and the Switching Unit, which allows for stimulation control, biosignal sensing & interpretation, and channel switching – all adaptive and in real time. MATLAB and Simulink facilitate rapid application prototyping via the g.HIsys software package developed by g.tec. Overall, the presented system offers a powerful toolbox to advance the treatment of neurological and psychiatric disorders while ensuring patient safety throughout the process.

GET A QUOTE

---
*Source: g.tec medical engineering, [https://www.gtec.at/2024/04/04/open-and-closed-loop/](https://www.gtec.at/2024/04/04/open-and-closed-loop/). Text reused under CC BY 4.0.*
