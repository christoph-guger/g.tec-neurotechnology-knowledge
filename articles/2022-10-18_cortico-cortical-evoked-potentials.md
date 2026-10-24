# How to record high-quality Cortico-Cortical Evoked Potentials (CCEP)?

- **Published:** 2022-10-18 on gtec.at
- **Original:** https://www.gtec.at/2022/10/18/cortico-cortical-evoked-potentials/
- **g.tec products:** g.HIamp, g.Estim, g.HIsys
- **Topics:** brain mapping

> **Summary:** Many people spend a lot of time to get clean CCEPs (cortico-cortical evoked potentials) to map cortical networks like the language network. CCEPs have been developed by Riki Matsumoto during his PhD.

---

Many people spend a lot of time to get clean CCEPs (cortico-cortical evoked potentials) to map cortical networks like the language network. CCEPs have been developed by Riki Matsumoto during his PhD. Nowadays, many labs are using it. In this article, we introduce you to a method that helps you to record clean, artifact-free and high-quality CCEPs.

## Default

CCEP recordings are done by electically stimulating e.g. the expressive language region via two bipolar ECoG channels with a few mA. The activation of this region will lead to EPs of cortical regions that are needed for language: The auditory cortex to hear a question, the receptive language region to understand a question and motor-mouth region to move the lips and tongue to finally tell the answer to the questions. The expressive language region, which is stimulated, produces the answer. This means by just stimulating one cortical region, a whole cortical network can be identified.

This has major implications for neurosurgery. Dr. Kyousuke Kamada is a neurosurgeon who developed very impressive surgical techniques to treat elipepsy and tumor patients by using CCEPs. He does it very effeciently with g.tec’s g.HIamp biosignal amplifier because it has a super high signal-to-noise (SNR) ratio. The SNR is so high that researchers like Nuri Firat Ince can record ultra-high gamma activity, reaching to 1kHz. In the past, researchers assumed that there is no information at these frequency bands and clinical recording systems often cut at 80 Hz making it impossible to do such experiments.

The Switching Unit for g.Estim PRO allows to select certain electrodes that should deliver the electrical stimulation. The switching unit is available with 64, 128 or 256 channels and is connected to the g.HIamp to measure EEG or ECoG data. A control interface allows to select certain electrode channels that should deliver the electrical stimulation pulses from g.Estim PRO. When g.HIsys is used, the amplifier block can read in the EEG or ECoG data and analyze it.

Another major issue is the switching artifact that occures when the electrical cortical stimulator is connected to the ECoG electrodes but disconnected from the recording amplifier to select e.g. the two bipolar channels to stimulate the expressive language area. All 256 input channels of the g.HIamp biosignal amplifier can be switched away from the ECoG grids to prevent the electrical stimulation current flowing into the amplifier instead of the cortex.

After the stimulation, the ECoG grid is switched back to the input of the biosignal amplifier. Especially this stimulation event and the switching procudes very high artifacts in the data and makes the ECoG recording bad and does not deliver clean CCEPs. This happens because the switching is not done fast and accurate enough and many systems don’t allow to switch all 256 channels. Imagine, if only 16 out of 256 channels are switched away, it is difficult to control where the electrical current is actually flowing. This is why neuroscientists assume that the current flows into the brain, and into the amplifier.

All these issues are solved with g.tec’ g.HIamp biosignal amplifier in combination with the Switching Unit that allows to switch all 256 channels fast and accurate to guarantee that the current flows into the cortex with a very short stimulation artifact below 2 ms. This gives perfect CCEPs.

Follow us on.

---
*Source: g.tec medical engineering, [https://www.gtec.at/2022/10/18/cortico-cortical-evoked-potentials/](https://www.gtec.at/2022/10/18/cortico-cortical-evoked-potentials/). Text reused under CC BY 4.0.*
