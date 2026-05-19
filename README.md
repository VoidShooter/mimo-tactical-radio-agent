# MiMo Tactical Radio Agent

An intelligent technical assistant specialized in defense communications and radio systems, fully powered by Xiaomi MiMo-V2.5-Pro.

## Overview

This project leverages the advanced reasoning capabilities of the Xiaomi MiMo model to provide expert-level insights into defense technology. It acts as a specialized agent capable of explaining technical specifications, classification schemas, and networking protocols of tactical radio communication systems. 

This project is built to demonstrate the integration of the MiMo Orbit 100T Token Plan API endpoints into a Python-based AI workflow.

## Features

* OpenAI-Compatible Integration: Seamlessly connects to Xiaomi's dedicated API endpoints.
* Expert System Prompting: Configured with defense-sector domain knowledge contexts for high-accuracy technical responses.
* Lightweight & Extensible: Built to be easily expanded with external search APIs for parsing real-time equipment databases.

## Quick Start

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/mimo-tactical-radio-agent.git
cd mimo-tactical-radio-agent

### 2. Install dependencies

pip install -r requirements.txt

### 3. Configure the Environment

Set your Xiaomi Token Plan API key (starting with tp-) in your terminal:

export MIMO_API_KEY="tp-your-api-key-here"

### 4. Run the Agent

python agent.py

## Model Configuration

| Setting | Value |
| --- | --- |
| Model Name | mimo-v2.5-pro |
| Base URL | https://token-plan-cn.xiaomimimo.com/v1 |
| Temperature | 0.3 |

## License

This project is licensed under the MIT License.

---
Built for the Xiaomi MiMo Orbit 100T Token Plan evaluation.
