# 📊 Agentic AI Project 9: Data Analyst Agent

![Python](https://img.shields.io/badge/Python-3.12%2B-brightgreen)
![Agentic AI](https://img.shields.io/badge/Agentic%20AI-Data%20Analyst%20Agent-blue)
![Data Analysis](https://img.shields.io/badge/AI-Data%20Analysis-orange)
![License](https://img.shields.io/badge/License-GPL--3.0-orange)

A robust, agentic, end-to-end AI-powered data analysis platform. This project empowers users to automate exploratory data analysis, visualization, and code generation using modular agents and LLMs. Built for extensibility, reproducibility, and real-world analytics workflows.

> 📁 **Repository:** `Agentic_AI_Project9_Data_Analyst_Agent`

---

## 🚀 Project Highlights

- 📈 **AI-Powered Data Analysis:**  
  Automatically explores datasets, generates insights, and produces visualizations from raw data.
- 🤖 **Agentic AI Architecture:**  
  Modular agents for EDA, code execution, and visualization—extend easily for custom analytics.
- 🧠 **LLM-Driven Automation:**  
  Uses language models to generate, execute, and explain Python data analysis code.
- 🖼️ **Interactive Visuals:**  
  Output includes charts, plots, and annotated explanations for intuitive understanding.
- 🧩 **Extensible:**  
  Add new analyst agents, data sources, or analytic modules as needed.

---

## 🧠 Technical Stack

- **Python 3.12+**
- **Agentic AI Patterns**
- **LLMs for code, analytics, and explanation**
- **Docker (for safe code execution)**
- **Streamlit (for optional web UI)**
- **Modular agent, team, and tool abstractions**

---

## 🏗️ Project Structure

```bash
Agentic_AI_Project9_Data_Analyst_Agent/
├── main.py                          # Main entry point
├── requirements.txt
├── LICENSE
├── README.md
├── 1. Project Structure.ipynb
├── Data Analyst Automation.excalidraw
├── output1.lua
├── streamlit_app.py                 # Optional web UI
├── agents/
│   ├── __init__.py
│   ├── Code_Executor_agent.py
│   └── Data_analyzer_agent.py
├── config/
│   ├── constants.py
│   ├── docker_utils.py
│   └── openai_model_client.py
├── prompts/
│   └── DataAnalyzerAgentPrompt.py
├── team/
│   └── analyzer_gpt.py
├── temp/
│   ├── data.csv                     # Example/test data
│   ├── Age_vs_survival.png
│   ├── Pclass_vs_survival.png
│   ├── Sex_vs_survival.png
│   ├── output.png
│   ├── output_gender.png
│   └── ... (auto-generated code/results)
└── __pycache__/
```

---

## ⚡ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/mdzaheerjk/Agentic_AI_Project9_Data_Analyst_Agent.git
cd Agentic_AI_Project9_Data_Analyst_Agent
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Configure Docker for safe code execution  
- Ensure Docker is installed and running for secure code evaluation.

### 5. Run the Data Analyst Agent
```bash
python main.py
```
or (for the web UI):
```bash
streamlit run streamlit_app.py
```

---

## 🧪 Example Usage

- **Automated EDA:**  
  Input your CSV or dataset to receive immediate visualizations, insights, and summary statistics.
- **Code & Explanation:**  
  See the generated Python code and natural language explanations for each analytic step.
- **Extend Easily:**  
  Add or customize agents for domain-specific analysis, advanced stats, or custom outputs.

---

## 🧩 Extensibility

- **Add More Agents:**  
  Implement agents for API data sources, advanced ML, or report generation.
- **Custom Visualizations:**  
  Modify agent logic for bespoke charts or dashboard elements.

---

## 📚 Documentation

See code comments in agents, config, and team modules for extension and workflow details.

---

## ✍️ Author

**Mohammed Zaheeruddin**  
🎓 First-Year B.Tech Student | AI/ML & GenAI Enthusiast  
🏫 Shetty Institute of Technology, Gulbarga  
📧 info.zaheerjk@gmail.com

---

## 📜 License

This project is licensed under the **GPL-3.0 License** – see the LICENSE file for details.

---

#### Key Features:
1. Multi-agent, LLM-powered data analysis and visualization automation
2. Modular, extensible Python codebase for analytics workflows
3. Add new agent roles, data sources, or analytic strategies
4. Designed for data science, self-study, and real-world business intelligence
