# Powerful BCI Innovations: Spring School Day 2

- **Published:** 2020-04-22 on gtec.at
- **Original:** https://www.gtec.at/2020/04/22/powerful-bci-innovations-spring-school-day-2/
- **g.tec products:** g.HIamp, g.USBamp, g.Nautilus, recoveriX, g.Estim, g.HIsys, g.BSanalyze
- **Topics:** TMS-EEG, education, stroke rehabilitation

> **Summary:** BCI & Neurotechnology Spring School. This makes it the biggest BCI event ever!

---

## MOTOR REHABILITATION WITH ? BRAIN-COMPUTER INTERFACES

## More than 3.500 people from all around the world signed up for the virtual

BCI & Neurotechnology Spring School. This makes it the biggest BCI event ever! Needless to say, this large turnout is the result of the global COVID-19 pandemic because conferences and events were suddenly cancelled. But, the turnout also reflects the growing interest in BCIs. We are delighted to host participants from Argentina all the way to Japan and New Zealand. Thanks for being part of it!

DOWNLOAD PPT SLIDES

## READ FAQ

## The first talk was from Christoph Guger about

Motor rehabilitation with BCI, which was the topic of day 2.

Christoph explained how to use motor imagery for recoveriX, a BCI-based stroke rehabilitation system. Motor Imagery leads to changes over the sensorimotor cortex that are called “even-related desynchronization” (ERD). The BCI is able to pick up these changes when a stroke patient is imaging a hand or foot movement and triggers a functional electrical stimulation of the corresponding limb.

As an instruction, recoveriX shows a virtual avatar that is performing a hand movement on a computer screen. This prompts the patient to imagine this specific movement.

For recoveriX treatment, 16 active EEG electrodes are necessary on the patient’s head for high quality recordings. The BCI algorithm analyzes the brain activity in real-time. When the BCI system detects a right-hand movement imagination by the patient, the right hand will be stimulated immediately for about 4-5 seconds.

This closed-loop setup pairs the cognitive processing with motor behavior. Furthermore, Christoph explained the differences among acute, sub-acute and chronic cases to pin-point the functional improvements that recoveriX is producing.

In the second talk, Marc Sebastian demonstrated how to use a BCI system for stroke treatment. Marc is a physiotherapist in the recoveriX Flagship Gym Barcelona and has many years of experience in treating patients.

He showed the audience how to assemble EEG electrodes, how to place the FES electrodes and how to calibrate the BCI system for every patient. Then, he ran the rehabilitation procedure. Besides stroke rehabilitation, Marc assesses the patient’s results with the Fugl Meyer Scale, the Box and Block test, the 9-hole PEG test, and many more tests, just to objectively show the functional improvement resulting from recoveriX therapy.

What he always recognizes is that patients are eager to come back for a treatment. They can see a positive effect even 10, 20, 30 years after the stroke.

The third talk was from Francisco Fernandes who demonstrated how to run EEG and FES systems in closed-loop experiments.

This demo used g.HIsys real-time processing software to read data from the g.HIamp, g.USBamp and g.Nautilus biosignal amplifiers. The software is a rapid prototyping environment that works with MATLAB and Simulink. It allows you to quickly realize new applications by just dragging and dropping blocks into a Simulink model.

Francisco connected an amplifier block to EEG pre-processing blocks in order to clean the data. Additionally, he used Common Spatial Patterns (CSP) to extract the most important EEG channels to find differences between left and right hand movement imaginations. The output of the CSPs was connected to a variance block to obtain features that were put in a real-time LDA to make a decision about whether the patient just imagined left or right hand movement. This command can be sent to a g.Estim FES block, which controls the electrical stimulator to stimulate the left or right hand muscle of the patient.

Such a model can be easily extended with customized signal processing blocks and many other experiments.

Jose Azorin from University of Elche in Spain gave the keynote talk of Day 3 about BCIs for upper and lower limb robotic exoskeletons. José M. Azorín is the Director of the Brain-Machine Interface Systems Lab and Associate Professor.

In his presentation, Jose explained how to use EEG and BCI technology to read information while patients are training with upper and lower limb exoskeletons. On top of this, he showed videos of how BCI technology can be used to control exoskeletons to have a more efficient rehabilitation.

## In

Lecture 5: Evoked Potentials (EP), Francisco Fernandes introduced different kinds of EPs, such as auditory, visual, vibro-tactile or also electrical stimuli. If you want to conduct an auditory EP experiment, g.HIsys is the best way to go. It offers you a Simulink model that controls the loudspeaker of a computer. It generates accurate trigger signals when the actual stimulation is given to the subject. This is possible with a trigger box that is connected to the biosignal amplifier.

This way, your EEG data is perfectly aligned to the auditory stimuli, which can be analyzed afterwards in g.BSanalyze to average the data that produced the Evoked Potential.

When visual stimulations are performed, it’s important to have accurate trigger signals captured from the computer screen. This can be done very precisely with photo-sensors on a screen or with software triggers generated in the Simulink model.

For mid-latency EPs like the P300, the software commands have enough resolution to calculate an accurate EP.

## Finally, Ren Xu talked about

TMS and tDCS studies with brain-computer interfaces.

Ren presented a research protocol to treat stroke patients with recoveriX in combination with TMS and tDCS. Therefore, the BCI technology must be compatible with TMS and tDCS.

TMS uses big coils to apply a magnetic stimulation to the brain. This coil is placed close to the brain region that should be stimulated. In the case of stroke rehabilitation in Ren’s study, the TMS coil must be close to the hand motor region. He stimulates the paretic and the healthy side prior to the recoveriX treatment in order to enhance the effect of the BCI training.

The tDCS is a direct current stimulation of the brain. In this case, the electrodes are placed over the sensorimotor cortex to stimulate the hand region before recoveriX rehabilitation training is performed.

---
*Source: g.tec medical engineering, [https://www.gtec.at/2020/04/22/powerful-bci-innovations-spring-school-day-2/](https://www.gtec.at/2020/04/22/powerful-bci-innovations-spring-school-day-2/). Text reused under CC BY 4.0.*
