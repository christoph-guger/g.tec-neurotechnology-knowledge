# Using Brain Waves and Computer Interface Technology as a Communication System

- **Published:** 2025-03-10 on gtec.at
- **Original:** https://www.gtec.at/2025/03/10/using-brain-waves-for-communication/
- **g.tec products:** Unicorn, Hybrid Black
- **Topics:** AI, BCI communication

> **Summary:** Effective communication plays a crucial role in emergency situations, yet, according to the Oregon Health and Science University, conventional methods of Individual Emergency Alert Systems such as communication through mobile devices often fall short in providing timely and discreet communication, particularly in cases of neuromuscular diseases and autoimmune conditions. These conditions, such as amyotrophic lateral sclerosis, Charcot-Marie-Tooth disease, chronic inflammatory demyelinating polyneuropathy, Guillain-Barré syndrome, multiple sclerosis, Lambert-Eaton syndrome, myasthenia gravis syndrome, spinal muscular atrophy disorder, and peripheral neuropathy disorder significantly restrict physical movement and can also lead to speech impairments.

---

Effective communication plays a crucial role in emergency situations, yet, according to the Oregon Health and Science University, conventional methods of Individual Emergency Alert Systems such as communication through mobile devices often fall short in providing timely and discreet communication, particularly in cases of neuromuscular diseases and autoimmune conditions. These conditions, such as amyotrophic lateral sclerosis, Charcot-Marie-Tooth disease, chronic inflammatory demyelinating polyneuropathy, Guillain-Barré syndrome, multiple sclerosis, Lambert-Eaton syndrome, myasthenia gravis syndrome, spinal muscular atrophy disorder, and peripheral neuropathy disorder significantly restrict physical movement and can also lead to speech impairments. Despite the brain generating signals capable of communication, these conditions present significant challenges for individuals to communicate those signals.

## READ THE ORIGINAL PUBLICATION

In 2019, a retrospective cohort study conducted in Ontario, Canada, revealed a growing prevalence of neuromuscular diseases among young adults and children, with disease prevalence increasing, on average, 8% per year for adults and 10% for children, all accompanied by a decrease in mortality rates. The study’s outcomes, while not necessarily generalizable, underscore the urgent necessity for disability inclusion at all levels of community and healthcare systems. This inclusion is vital in motivating individuals with impairments, enabling them to lead fulfilling and healthy lives.

To address this need, the purpose of this experiment is to explore the potential of brain-computer interface (BCI) technology to facilitate communication between both able-bodied individuals and those with disabilities. By using BCI, researchers aim to capture users’ commands by calibrating their brain’s electric signals, enabling them to programmatically send messages through a system.

This research has high novelty by exploring the practical application of BCI technology in emergency systems and disability assistance. Prior to this study, the integration of BCIs in these contexts has not been established, marking a significant gap in the field. Although prior research laid the theoretical foundation for BCIs in emergency systems and assistance for disabled individuals, this study presents a novel implementation that can address practical needs.

Specifically, this pilot study focuses on the development of an emergency alert system that uses BCI technology to bridge the communication gap for individuals with neuromuscular diseases and autoimmune conditions. By harnessing the power of BCI, this system aims to empower disabled individuals to communicate effectively, particularly in emergency situations. The overall aims of this pilot study are to explore the viability and efficacy of BCI-based communication during emergency scenarios, appraise the precision and dependability of user command capture through BCI technology, and evaluate the potential influence of this technology on enhancing the general well-being and quality of life for individuals with disabilities.

BCI is dependent on the electrode sensors that acquire electroencephalography (EEG) signals from different brain areas. These electrodes are placed over different regions of the brain to measure brain waves. The BCI calibrates the user’s brain waves captured by considering movements like jaw clenching, blinking eyes, or focusing on a specific picture or characters.

These brain waves are stored by using a custom computer software that amplifies the brain waves and converts them to an electric signal output, which may be used to trigger the command to any smart device, such as a smartphone or smart tablet. By advancing the understanding and application of BCI technology in the context of emergency communication, this research can contribute to the development of inclusive and accessible solutions that promote the health and safety of individuals with neuromuscular diseases and autoimmune conditions.

## Methods

The study protocol was approved by DiscoverSTEM, and all participants were fully informed and consented to participate in the study. The study was conducted in a controlled laboratory setting at DiscoverSTEM, from Jan 2022 to Aug 2023. For all minor participants, the parent/guardian consent was taken for their child’s involvement in the study.

## Study Population

A call for volunteers was used to recruit individuals from the local area to participate in the study. Eligibility to participate was based on age (at least 8 years old) and ability to complete the experimental protocol, which requires the participant to concentrate and sit still for 20 trials.

## Equipment

The BCI system used in this study involves a wearable EEG headset consisting of electrodes, amplifiers, A/D converter (Unicorn BI) to read and capture brain signals. A microcontroller (model No. TRJG0926HEN, TRXCOM) was used to process the signal from the EEG headset and relay the signal to a computer with Unicorn Hybrid Black Application Suite installed. This software records the user’s peak brain waves in a set interval by applying Fourier transformation. When the software calibrates the frequency of the peak with that of the customized menu, then the user selection is confirmed.

A mobile device was used to display SMS text messages via iMessage (Apple). A stopwatch was used to track the duration of various experimental tasks or activities during the study. This ensures consistent timing and synchronization between the participants’ actions and the recorded brain wave data. These materials are essential for the implementation and execution of the study, enabling the capture, calibration, and analysis of brain waves, using EEG technology, as well as facilitating the communication and messaging aspect through the iPhone and iMessage platform.

## Figure 2

A mobile device was used to display SMS text messages via iMessage (Apple). A stopwatch was used to track the duration of various experimental tasks or activities during the study. This ensures consistent timing and synchronization between the participants’ actions and the recorded brain wave data. These materials are essential for the implementation and execution of the study, enabling the capture, calibration, and analysis of brain waves, using EEG technology, as well as facilitating the communication and messaging aspect through the iPhone and iMessage platform.

## Experimental Procedure

The experimental design workflow is shown in Figure 2. Study participants wore the EEG headset. Electrode gel was applied generously to the scalp to ensure optimal signal conductivity. Electrodes were then securely affixed to specific locations, positioned above each mastoid region, which corresponds to the areas behind the left and right ears. This meticulous preparation guarantees the precise capture of EEG readings.

## Figure 2

Experimental design workflow demonstrates the protocol that facilitates the transfer of commands between these two virtual applications.

Following the headset preparation, the connection and setup phase commences by first starting the Unicorn recorder. The eight channels on the Unicorn Recorder start showing the data acquired by the eight electrodes on the headset.

With the hardware in place, the BCI software was launched on the computer. Within the software, several critical configurations were performed. The content screen was modified to display specific characters randomly allocated to be flashed at a frequency of 32 ms/min. The scaling of the software was fine-tuned to a range of ±300 pV, guaranteeing the accurate measurement of brain wave signals. A bandpass filter was set to a frequency range of 0.1–30 Hz, capturing relevant brain wave frequencies. The notch frequency was adjusted to 60 Hz to eliminate interference caused by external electrical signals, such as power lines.

## Calibration

Calibration is a pivotal step in personalizing the BCI system for each user. In general, the user initiates the unicorn speller and preselects some characters or images. The system randomly flashes a series of characters and images repeatedly. The characters or images focused by the user are selected for calibration. Once the preselected and focused characters are matched, then the user’s custom calibration is complete. The user connects a smartphone to the BCI software via Bluetooth to send text messages with their mind.

In our experiment, four images were preselected to represent each of the four commands (“Emergency,” “Walking,” “Education,” and “Restroom”). Study participants were instructed to choose four images and concentrate on each one individually to complete the custom calibration process. Custom calibration data were meticulously recorded after each concentration session. Finally, the Speller board was configured with custom command buttons based on the user’s individual calibration. The user can now concentrate on each command and the respective SMS text message is sent to the configured smart device.

## Messaging and communication

The core functionality of the BCI system revolves around translating user commands into actionable messages. Based on the user’s focused command, the BCI software generates a response, subsequently triggering a custom code responsible for sending an appropriate SMS text via email. The SMS text is then routed to the configured sender through the selected cellular carrier.

## Testing

The pilot testing strategy encompasses various components, including calibration time measurement, SMS reception time measurement, BCI program control and SMS testing, and testing of negative scenarios, such as user fidgeting, sudden movements, or not focusing. The process includes repeating the experiment across 20 users for five trials for each of the four commands (20 trials per person), capturing the expected versus actual outcomes for each trial, and documenting the time taken for calibration and the reception of SMS messages in each trial. Through these strategies, the accuracy and reliability of the BCI system are evaluated, and the collected data are recorded and analyzed.

## Outcomes, Variables, and Measures

The primary outcomes of interest included the calibration time of brain signals from the EEG headset and the time taken for the receiver to receive the SMS text, based on the user’s selected command and attentiveness. Secondary outcomes included the accuracy of SMS text transmission and any observed discrepancies in negative test scenarios. The variables analyzed include calibration time, SMS reception time, actual outcomes, expected outcomes, and any confounding factors or diagnostic criteria.

Calibration time and SMS reception time evaluated user-friendliness and system responsiveness, and actual versus expected outcomes measured the BCI’s accuracy in interpreting user commands. Additionally, the study considered confounding factors and diagnostic criteria to address external influences on system performance such as user’s sudden movements and fidgeting. These variables collectively provided an evaluation of the BCI’s practicality in assisting individuals with disabilities and in emergency communication scenarios, contributing valuable insights for its advancement in these crucial contexts.

## Data Analysis

Potential confounding factors were controlled during data analysis. These may include factors such as age, sex, or previous experience with BCI technology. Summary statistics were used to describe the calibration time, SMS reception time, and other relevant variables. In addition to the success rates of SMS text message transmission for different command categories, further analysis was conducted to assess the calibration time, SMS text message reception time, and the impact of negative test scenarios on the BCI system’s performance.

## Results

A total of 20 volunteers were included in the study (12 male, 8 female; mean age, 40 years; range, 8–78 years). Characteristics of the study participants are summarized in Table 1. A few participants had essential age-related tremors and preexisting health conditions such as speech problems, mild hand tremors, and mobility issues.

## Table 1

The average success rate for receiving the BCI command and accurately sending the appropriate SMS text message to the configured sender was 96–98%. The average calibration time, representing the time taken to calibrate the BCI system using the researcher’s brain signals, was found to be 17 seconds (range, 17–18 seconds). This duration reflects the setup time required for the BCI system to capture and interpret the unique brain signals of the user. Two elderly participants had a slight tremble, which contributed to extended calibration time. The youngest participants had the quickest calibration time.

## Table 2

Test results and success rates of SMS text message transmission for different command categories.

The average time taken to receive an SMS text alert, from the moment the BCI system triggered the command to the reception of the text message by the configured sender, was observed to be 2 seconds (range, 2–3 seconds). This quick response time indicates the efficiency of the BCI system in transmitting messages promptly.

In instances of negative test scenarios, where the participant either moved during calibration or lacked full focus when sending commands for text, calibration and transmission times were up to two times longer. These outcomes underscore the crucial importance of maintaining a stable and focused state during the operation of the BCI system to achieve its optimal performance.

## Discussion

The study aimed to evaluate the feasibility and effectiveness of using EEG-based BCI to send text messages through brain signals, as well as to explore the impact and potential applications of this technology. The results of our study demonstrate promising outcomes in terms of efficacy and reliability of BCI calibration, SMS text message transmission, and user acceptance.

Our results are consistent with another BCI-based study done with P300 models concerning open-loop and closed-loop control of a humanoid robot via brain signals using Cerebot, a mind-controlled humanoid robot platform. Together, these findings indicate the efficiency and reliability of the BCI system in translating brain signals into meaningful commands.

Our study focused on specific commands that are relevant to the daily activities, that is, “Education,” “Emergency,” “Walking,” and “Restroom.” The success rates for accurately sending the appropriate SMS text messages corresponding to these commands ranged from 96–98%. Comparing our findings with existing literature, we can observe a growing body of research on BCI technology and its applications in various domains.

However, the specific focus on individuals with disabilities such as amputated arms, neuromuscular disorders, and brachial plexus injuries is limited, and this represents a unique group of patients who can benefit from BCI technology. By demonstrating the feasibility and effectiveness of EEG-based BCI, our study provides novel insights into the potential of BCI technology to address the communication and rehabilitation needs of this unique population.

Through further advancements and refinements, BCI technology holds the promise to empower individuals with disabilities, promote inclusivity, improve mental health, and facilitate their more active participation in various aspects of society. Future research in this field should consider expanding the scope of commands beyond the four used in this study, as a more diverse set of commands would provide a broader range of inputs for users, such as requesting meals. Additionally, incorporating a larger sample size, such as a cohort of 100 people, including those with neurological and neuromuscular disorders, may provide additional insights and enhance the reliability and generalizability of the findings.

## Limitations

Firstly, the quality of contact between the electrodes on the BCI helmet and the user’s scalp could have had an impact on the strength and accuracy of the captured brain signals. It was observed that better scalp contact resulted in stronger brain signals on the BCI system. Therefore, ensuring consistent and optimal scalp contact through consistent placement of sensors on specific areas of the user’s scalp is crucial to minimize potential errors in the signal acquisition process.

An 8-wet patch electrode helmet was used, which generally provides sufficient spatial coverage however, depending on the stage of the user’s disease or individual factors, additional electrode coverage may be necessary for accurate calibration of their brain waves. A helmet can have a single channel to as many as 256 channels and different kinds of electrode heads for head adherence this variability can contribute to variations in the results, as more EEG channels enable better calibration, based on the disease condition, and should be considered when interpreting the data.

Furthermore, all the participants are self-reported healthy individuals. The study’s small sample size and lack of access to medical records for each participant is a limitation. Although our study provides valuable insights, a future iteration of this study with larger sample size including individuals with disabilities and a more diverse group of participants would further strengthen the results.

The study used a limited set of four text commands for data collection. A broader range of commands could provide more comprehensive data for analysis and potentially yield additional insights into the performance and accuracy of the BCI system. Lastly, external factors such as WiFi signal and carrier signal could have contributed to signal loss or interruptions, exhibiting slowness to send a text message. It is important to interpret the results within the context of these limitations and consider strategies for mitigating and addressing them in future studies.

Moving forward, continued research in this field is warranted to address the identified limitations and knowledge gaps. Future studies can provide a more comprehensive understanding of BCI technology and its integration into the lives of individuals with disabilities.

## Conclusion

In conclusion, this pilot study of EEG-based BCI technology offers a customizable emergency communication solution. The results indicate the feasibility and effectiveness of using brain waves to send SMS text messages in real time, with high success rates for selected commands across a wide age range of individuals.

READ THE ORIGINAL PUBLICATION

---
*Source: g.tec medical engineering, [https://www.gtec.at/2025/03/10/using-brain-waves-for-communication/](https://www.gtec.at/2025/03/10/using-brain-waves-for-communication/). Text reused under CC BY 4.0.*
