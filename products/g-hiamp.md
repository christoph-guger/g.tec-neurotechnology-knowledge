# g.HIamp: high-density EEG, ECoG and sEEG amplifier

**What it is:** a biosignal amplifier for real-time neuroscience, brain mapping, EEG-TMS, BCI research and clinical research. Source: [g.HIamp product page](https://www.gtec.at/product/ghiamp-high-density-eeg-system/).

## Key specifications
| | |
|---|---|
| Channels | 16, 32, 80, 144 or 256 per device (256 monopolar or 128 bipolar); up to 1,024 synchronized channels with several devices |
| Resolution | 24-bit, DC-coupled |
| Sampling rate | up to 38.4 kHz per channel |
| Signals | EEG, ECoG, sEEG, EMG, ECG, EOG, external sensors; high-gamma up to 1 kHz and high-frequency oscillations |
| Interface | USB, hardware trigger inputs |
| File formats | EDF native, BIDS via open-source conversion scripts |
| Regulatory | FDA-cleared and CE-certified |

## Works with
Python (g.Pype), MATLAB/Simulink (g.HIsys), g.Recorder, g.BSanalyze, MNE-Python, EEGLAB, FieldTrip, BCI2000, OpenViBE, Lab Streaming Layer. Combines with TMS, fNIRS, eye tracking (Tobii Pro Fusion), motion capture, VR and electrical stimulation (g.Estim PRO). g.HIamp is the recording core of [cortiQ](cortiq.md) and [g.Pangolin](g-pangolin.md).

## Typical uses
High-density EEG and source localization, intracranial recordings for epilepsy surgery planning, high-gamma mapping, EEG-TMS, closed-loop BCI and stimulation experiments, hyperscanning.

## Published results with g.HIamp
- ECoG c-VEP BCI: 99.21% online accuracy ([Front Syst Neurosci 2014](https://doi.org/10.3389/fnsys.2014.00139)).
- Face area mapping: high-gamma ECoG found 85.7% of face areas versus 53.6% for electrical stimulation ([Front Hum Neurosci 2021](https://doi.org/10.3389/fnhum.2021.616591)).
- Epilepsy network surgery: Engel class I outcome in 13 of 14 patients, 92.8% ([Front Neurol 2020](https://doi.org/10.3389/fneur.2020.00073)).

More: [evidence/published-results.md](../evidence/published-results.md)
