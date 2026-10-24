# Tools & Tricks About How To Record TMS & EEG Simultaneously

- **Published:** 2021-04-08 on gtec.at
- **Original:** https://www.gtec.at/2021/04/08/how-to-record-tms-eeg-simultaneously/
- **g.tec products:** g.HIamp, g.USBamp, g.Nautilus, g.LADYbird, g.SCARABEO, g.HIsys, g.BSanalyze, g.Recorder
- **Topics:** TMS-EEG

> **Summary:** Transcranial Magnetic Stimulation and electroencephalography recordings are used more and more in neuroscience research and clinical settings. The technical requirements are pretty demanding, but if they are handled correctly; new scientific experiments can be carried out and new results can be found.

---

Transcranial Magnetic Stimulation and electroencephalography recordings are used more and more in neuroscience research and clinical settings. The technical requirements are pretty demanding, but if they are handled correctly; new scientific experiments can be carried out and new results can be found. But before we dive into it, let’s talk basics.

Transcranial Magnetic Stimulation (TMS) is used to magnetically stimulate certain regions of the brain to study and treat the patient. This is often combined with EEG recordings to see the reaction of the brain to the magnetic stimulation. A combination of TMS and BCI technology can be used e.g. in neurorehabilitation settings.

You can use either a series of single TMS pulses and measure the TMS induced evoked potentials or you can do repetitive Transcranial Magnetic Stimulation and look for electroencephalography and ERP changes after the treatment or for diagnostic purposes.

## How do you record EEG & TMS simultaneously?

So called Transcranial Magnetic Stimulation coils are placed over certain brain regions that should be stimulated and then the magnetic field is applied. At the same time EEG electrodes are recording the brain function of the human brain with biosignal amplifiers. Then the data is transmitted to the computer and is visualized and stored for later analysis or it is analyzed in real-time.

## What factors must be considered before carrying out EEG & TMS recordings?

For the EEG recordings it is important to use pretty flat EEG electrodes in order to enable the TMS coil to be as close as possible to the head in order to maximize the magnetic pulse to a certain brain region. Typically, the magnetic fields cause some stimulation artifacts in the EEG data that can be minimized with proper filters and signal processing techniques in the EEG system.

Very important is the proper positioning of the Transcranial Magnetic Stimulation coil over a certain brain region. First of all, the magnetic field has to stimulate the region and secondly it must be ensured that the coil stays at the proper position. Therefore, the users are looking e.g. at motor responses to see if the magnetic pulse is hitting a motor region or people are investigating EEG responses to understand if the magnetic stimulation is effective. The coil needs to be placed: at the right spot at the optimal distance to the electrodes in the correct angle to the head surface in the best orientation to reduce artifacts A further important consideration is the sampling frequency that the recording should have.

## What equipment do you need to successfully perform simultaneous EEG & TMS recordings?

You can use the wireless g.Nautilus EEG headsets, the g.USBamp or g.HIamp amplifiers for the EEG recordings. Here is a list of g.tec’s electroencephalography amplifiers that can be configured in the online product configurator and that can be used for simultaneous TMS recordings: g.Nautilus PRO 8/16/32 EEG channels wearable headset g.Nautilus PRO Flexible 8/16/32 EEG channels wearable headset g.Nautilus Multi-Purpose 8/16/32/64 EEG channels wearable headset g.Nautilus RESEARCH 8/16/32/64 EEG channels wearable headset g.USBamp RESEARCH 16 channels biosignal amplifier g.HIamp 256 channels biosignal amplifier PRODUCT CONFIGURATOR Depending on your application you can chose the proper equipment. The g.Nautilus wearable EEG headsets can sample up to 500 Hz, while g.USBamp and g.HIamp biosignal amplifiers can sample up to 38.4 kHz and this determines the highest EEG signal components that can be recorded. For short lasting evoked potentials, g.USBamp and g.HIamp are required. All of g.tec’s biosignal amplifiers allow EEG/EMG/ECG recordings with passive or active EEG electrodes.

What is the difference between passive and active EEG electrodes and what is best for TMS recordings?

Passive electrodes don’t have a pre-amplifier inside the electrode and therefore require abrasive gel to bring the electrode impedance down. The advantage is that the TMS stimulation artifact is smaller because the electrode is just smaller.

If active electrodes like g.LADYbird active or g.SCARABEO active EEG are used, then the pre-amplifier is inside the electrode and this allows a quick assembling. But the electrodes are a bigger and therefore the Transcranial Magnetic Stimulation artifact is longer.

## Can the TMS pulse damage the EEG amplifiers during the recording?

If you use g.USBamp and g.HIamp biosignal amplifiers, the main amplifier is far away from the TMS coil and therefore the magnetic field is very small and does not damage anything.

The wireless g.Nautilus on the other hand, is fixed on the EEG cap on the subject’s head and therefore much closer to the Transcranial Magnetic Stimulation coil. If the TMS coils is activated close to the g.Nautilus wireless EEG headset, the device is switched off for security reasons Where is the TMS coil positioned and how does it affect the EEG recordings?

The TMS coil is positioned e.g. over the left sensorimotor cortex to produce a right finger movement like illustrated below. Then, the TMS pulse is switched on and at the same time the EEG is recorded from 16 positions according to the international 10/20 system. In this case, the TMS coil is just positioned over electrode C3 to produce the left finger movement. The blue line shows the EP below the motor threshold and we don’t observe a finger movement, but we can see the reaction in the EEG data. The purple line shows the EP for a TMS pulse above the motor threshold where a finger movement in the patient can be seen.

The black rectangle shows, when the TMS pulse is applied. Typically, the EEG signal shows a huge artefact around and after the TMS pulse. Electrode C3 shows the highest TMS artifact because the coil is closest to it. All the other electrodes will show a smaller artifact that is logarithmical reduced with the distance to the coil.

## How can you reduce EEG artifact produced by TMS?

One trick is to record mostly from EEG electrodes that are far away from the coil to get artifact free data. Otherwise, it is possible to perform e.g. source derivations to kill the artifact.

Another trick is to use the right hardware: g.HIamp EEG amplifier has a special 64 Channel Passive Electrode Connector Box TMS with highly effective TMS filters inside that kill most of the magnetic artifact before the artifact is recorded by the system. This is important because the Transcranial Magnetic Stimulation pulse has pretty high frequencies and this can produce aliasing artifacts when the EEG signal is sampled. Together with g.LADYbird passive EEG electrodes, the stimulation artifact is shorter than 1 ms (compared to g.SCARABEO active EEG electrode system where the stimulation artifact is shorter than 4 ms).

Nevertheless, the magnetic pulse is so big that it will overlay the EEG signal. So, what else can you do? g.BSanalyze Offline Biosignal Analysis software has a special artifact removal algorithm that can kill such transient events to be able to record artifact free data after a very short interval.

To make the algorithm effective, it is important to sample the data with 19.2 kHz. The EEG electrodes are measured against the ground electrode on the forehead. Then a common average reference is calculated, a baseline correction is performed, the trial mean is calculated and the artifact is removed.

Generally, it helps to reduce the impedance as much as possible because then the magnetic pulse artefact is smaller.

Check out the online product configurator to get an EEG amplifier, suitable EEG electrodes and a software environment:

## PRODUCT CONFIGURATOR

What software can you use to record TMS & EEG data in real-time? g.tec offers a very powerful software: g.HIsys Professional is a rapid prototyping environment to quickly realize new experiments. The software environment has dedicated Simulink models for TMS recordings that include all necessary steps to record clean EEG data while TMS is applied. The model reads in the data from 64-256 EEG channels with the g.HIamp block. Then a CAR source derivation is calculated to remove common mode noise like power line interference and a highpass and lowpass filter is applied. In the TMS processing block, evoked potentials are calculated and the EP blocks show the EPs.

The TMS block allows to specify EOG channels to remove ocular artifacts, to specify the EP length and the pre-stimulus interval. Furthermore, an artifact rejection can be activated to remove trials with too much contamination. g.Recorder Professional has automatic TMS artifact rejection and reduction tools included and it does not require MATLAB for the recording.

## What are the necessary steps to perform a successful simultaneous TMS & EEG recording?

Prepare the equipment and feed a TMS trigger into the g.tec amplifier via digital inputs.

Assure an extra low impedance by preparing the skin (ideally below 1 kOhm for passive electrodes).

Select a high sampling rate of 4.8 kHz or higher.

Don’t use a bandpass or Notch filter, because the stimulation artifact would case the filters to swing.

Don’t use a reference electrode, just a ground electrode to ensure an easier removal of the stimulation artifact.

Use the TMS electrode connector box for g.HIamp to kill most of the artifact.

Route all electrode wires in a compact bundle from the head to the amplifier and avoid loops, route the wires perpendicular to the coil.

Position the coil with a holder arm on a tripod and use a positioning system.

Use the g.HIsys Professional package to acquire and clean the data and to perform real-time analysis.

Use g.Recorder Professional to automatically clean the data and remove trails with too much contamination.

Perform additional off-line processing with the TMS functions in g.BSanalyze

## Publications

## A quantitative physical model of the TMS-induced discharge artifacts in EEG

Reliability of M1-P15 as a cortical marker for transcallosal inhibition: a preregistered TMS-EEG study The rt-TEP tool: real-time visualization of TMS-Evoked Potential to maximize cortical activation and minimize artifacts The Unlimited Possibilities of Wearable EEG

---
*Source: g.tec medical engineering, [https://www.gtec.at/2021/04/08/how-to-record-tms-eeg-simultaneously/](https://www.gtec.at/2021/04/08/how-to-record-tms-eeg-simultaneously/). Text reused under CC BY 4.0.*
