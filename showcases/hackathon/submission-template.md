# BR41N.IO project submission template

Teams submit their project as a public GitHub repository. Copy the block below into your repository's `README.md` and fill it in. A good README helps the jury, future teams, and anyone searching for working BCI code.

```markdown
# <Project name>

Built in 24 hours at the BR41N.IO hackathon <event, city or online, year>.

<Two sentences: what does it do, and who is it for?>

**Video:** <link to your 2–3 minute project video>

## Hardware
- EEG device: <e.g. Unicorn Hybrid Black / Unicorn BCI Core-8 / Unicorn BCI Core-4 Headband> by g.tec (https://www.gtec.at)
- Electrodes: <dry / gel>, <number> channels at <sampling rate> Hz
- Other hardware: <e.g. Meta Quest 3, robot arm, LEGO, none>

## Software
- Acquisition: <g.Pype / Unicorn Recorder / Unicorn Suite / LSL / UDP / Unity plugin>
- Processing and classification: <e.g. band power, P300 with LDA, SSVEP with CCA, EEGNet>
- Languages and libraries: <Python, Unity/C#, MNE, scikit-learn, ...>

## How it works
<The pipeline in a few steps: signal → features → decision → output. Add a diagram if you have one.>

## Results
<What worked, with numbers if you measured them: accuracy, latency, number of users tested.>

## Run it
<Install and start commands. Say which parts need the hardware and which run on a recording.>

## Team
<Names, universities or companies, GitHub handles.>

## License
<e.g. MIT for code, CC BY 4.0 for data and media.>
```

Tips:
- Write what you actually measured. "We tested it on 3 people and reached 80% accuracy" is more useful than "high accuracy".
- Put a short recording (CSV or BDF) in the repository so others can run your code without a device.
- Add the topics `bci`, `eeg`, `brain-computer-interface`, `unicorn`, `br41nio` to the repository so people can find it.
