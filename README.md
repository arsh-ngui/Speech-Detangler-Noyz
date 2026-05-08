# Speech Detangler - Noyz

### Real-time multi-speaker speech separation and transcription pipeline for noisy and overlapping conversations.

---

## Overview

Speech Detangler is an AI-powered multi-speaker speech separation and transcription system designed for noisy and overlapping conversations. The project combines speech enhancement, speaker separation, and Whisper-based transcription into a unified pipeline to improve transcription accuracy in real-world environments such as meetings, call recordings, classrooms, and crowded spaces.

---

## Key Features

- Multi-speaker speech separation using deep learning models
- Noise reduction and audio preprocessing
- Whisper-based multilingual speech transcription
- Modular AI pipeline for experimentation and scalability
- Research-driven architecture for overlapping speech handling
- Designed for future real-time deployment

---

## What makes it better

Unlike standard transcription systems that fail under overlapping speech conditions, Speech Detangler combines:

- Deep-learning-based source separation
- Speaker-aware processing
- Noise filtering
- Robust transcription

into a single integrated workflow.

### Core USP

**"Separate first, understand later."**

Instead of directly transcribing mixed audio, Speech Detangler first isolates speakers and enhances speech quality, significantly improving transcription accuracy in noisy real-world environments.

---

## System Architecture

```text
Input Audio
     │
     ▼
Audio Preprocessing
(Resampling / Normalization / Noise Filtering)
     │
     ▼
Speech Separation Model
(Asteroid DPRNN-Based Pipeline)
     │
     ▼
Separated Speaker Streams
     │
     ├──────────────┐
     ▼              ▼
Speaker 1        Speaker 2
Audio            Audio
     │              │
     ▼              ▼
Whisper STT     Whisper STT
     │              │
     ▼              ▼
Individual Transcripts
     │
     ▼
Final Combined Output
```

---

## Technologies Used

### Languages
- Python
- MATLAB

### Frameworks & Libraries
- PyTorch
- Asteroid
- OpenAI Whisper
- NumPy
- SciPy
- Librosa
- Torchaudio

### Development Tools
- Git
- GitHub
- Jupyter Notebook
- VS Code

### AI/ML Concepts Used
- Deep Learning
- Source Separation
- Sequence Modeling
- Spectral Analysis
- Automatic Speech Recognition (ASR)

---

## Installation

```bash
git clone https://github.com/arsh-ngui/speech-detangler.git
cd speech-detangler
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Run Speech Separation

```bash
python separate.py --input sample.wav
```

### Run Transcription

```bash
python transcribe.py --input separated_audio.wav
```

### Full Pipeline

```bash
python main.py --input mixed_audio.wav
```

---

## References

### Research Papers

- Dual-Path RNN: Efficient Long Sequence Modeling for Time-Domain Single-Channel Speech Separation
- Conv-TasNet: Surpassing Ideal Time-Frequency Magnitude Masking for Speech Separation
- SepFormer: Speech Separation Using Transformer Networks
- OpenAI Whisper Research

### Frameworks

- Asteroid Speech Separation Toolkit
- PyTorch Documentation
- OpenAI Whisper Repository

---

## Author

Arsh Handa
