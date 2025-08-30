# CodeAct: Executable Code as Unified Action Space for Language Model Agents

## Abstract

CodeAct introduces a novel paradigm for Large Language Model (LLM) agents by utilizing executable code as a unified action space. This approach enables agents to perform complex tasks through dynamic code execution and action refinement, achieving up to 20% higher success rates compared to traditional text/JSON-based action spaces.

## 1. Introduction

Traditional LLM agents rely on predefined action spaces that limit their adaptability and expressiveness. CodeAct addresses these limitations by proposing executable Python code as the primary interface for agent actions, creating a more flexible and powerful framework for autonomous task execution.

### 1.1 Problem Statement

Current LLM agents face several challenges:
- Rigid action spaces that constrain problem-solving capabilities
- Limited ability to adapt actions based on execution feedback
- Difficulty in handling complex, multi-step reasoning tasks
- Poor generalization to out-of-domain scenarios

### 1.2 Contributions

1. **Unified Action Space**: Introduction of executable code as a universal interface for agent actions
2. **Dynamic Action Revision**: Framework enabling agents to modify actions based on execution results
3. **CodeActInstruct Dataset**: 7,000 multi-turn interactions for training code-based agents
4. **Comprehensive Evaluation**: Performance analysis across 17 LLMs and multiple benchmarks

## 2. Methodology

### 2.1 Core Architecture

CodeAct employs a modular architecture consisting of:

- **LLM Serving Layer**: Handles model inference and response generation
- **Interaction Interface**: Manages multi-turn conversations and context
- **Code Execution Engine**: Provides secure, containerized Python execution
- **Action Space Translator**: Converts natural language intentions to executable code

### 2.2 Executable Action Space

Instead of predefined actions like `search(query)` or `calculate(expression)`, CodeAct allows agents to write arbitrary Python code:

```python
# Traditional approach
search("weather in New York")

# CodeAct approach  
import requests
response = requests.get("https://api.weather.com/v1/current", 
                       params={"location": "New York"})
weather_data = response.json()
print(f"Current temperature: {weather_data['temperature']}°F")
```

### 2.3 Dynamic Action Refinement

The system supports iterative refinement where agents can:
1. Execute initial code
2. Analyze execution results
3. Modify code based on feedback
4. Re-execute until task completion

## 3. Training and Data

### 3.1 CodeActInstruct Dataset

The training dataset comprises:
- **Size**: 7,000 multi-turn interactions
- **Domains**: Mathematics, data analysis, web scraping, file operations
- **Format**: Natural language instructions paired with executable Python solutions
- **Quality**: Human-verified and tested for correctness

### 3.2 Model Training

Two primary models were developed:
- **CodeActAgent-Mistral-7b-v0.1** (recommended)
- **CodeActAgent-Llama-7b**

Training process:
1. Fine-tuning on CodeActInstruct dataset
2. Reinforcement learning from code execution feedback
3. Multi-turn conversation optimization

## 4. Experimental Results

### 4.1 Performance Metrics

CodeAct demonstrates superior performance across multiple benchmarks:

| Benchmark | Text/JSON Actions | CodeAct | Improvement |
|-----------|------------------|---------|-------------|
| HumanEval | 65.2% | 78.4% | +20.2% |
| MBPP | 71.8% | 85.1% | +18.5% |
| GSM8K | 82.3% | 89.7% | +9.0% |

### 4.2 Cross-Model Evaluation

Performance across 17 different LLMs shows consistent improvements when using CodeAct's executable action space compared to traditional approaches.

### 4.3 Out-of-Domain Generalization

CodeAct agents demonstrate better generalization to unseen tasks:
- 15% higher success rate on novel problem types
- Maintained conversational abilities
- Reduced hallucination in complex reasoning scenarios

## 5. Technical Implementation

### 5.1 Security and Isolation

Each chat session runs in an isolated Docker container:
```bash
docker run -it --rm python:3.9 python -c "user_code_here"
```

### 5.2 API Integration

OpenAI-compatible API interface:
```python
import openai
client = openai.OpenAI(base_url="http://localhost:8000/v1")
response = client.chat.completions.create(
    model="CodeActAgent-Mistral-7b-v0.1",
    messages=[{"role": "user", "content": "Calculate fibonacci(10)"}]
)
```

### 5.3 Deployment Options

- **Local Development**: Python script execution
- **Web Interface**: Browser-based interaction
- **Container Orchestration**: Kubernetes deployment support

## 6. Use Cases and Applications

### 6.1 Data Analysis
```python
# Agent can dynamically explore datasets
import pandas as pd
df = pd.read_csv('sales_data.csv')
print(df.describe())
correlation = df.corr()['revenue'].sort_values(ascending=False)
```

### 6.2 Web Scraping and API Integration
```python
# Flexible web interaction
import requests
from bs4 import BeautifulSoup
response = requests.get('https://example.com/api/data')
if response.status_code == 200:
    data = response.json()
    # Process and analyze results
```

### 6.3 File System Operations
```python
# Dynamic file handling
import os
import glob
files = glob.glob('*.txt')
for file in files:
    with open(file, 'r') as f:
        content = f.read()
        # Process file content
```

## 7. Limitations and Future Work

### 7.1 Current Limitations

1. **Security Concerns**: Code execution requires careful sandboxing
2. **Resource Usage**: Higher computational overhead compared to simple actions
3. **Error Handling**: Complex debugging for failed code execution
4. **Model Size**: Current models limited to 7B parameters

### 7.2 Future Directions

1. **Larger Models**: Scaling to 13B+ parameter models
2. **Multi-Language Support**: Extending beyond Python to other languages
3. **Enhanced Security**: Improved sandboxing and permission systems
4. **Real-World Integration**: Production-ready deployment frameworks

## 8. Conclusion

CodeAct represents a paradigm shift in LLM agent design by introducing executable code as a unified action space. The approach demonstrates significant performance improvements across various benchmarks while maintaining flexibility and expressiveness. The dynamic nature of code execution enables agents to adapt to complex, multi-step tasks more effectively than traditional action-based systems.

The contribution of CodeAct extends beyond performance metrics, offering a new framework for thinking about agent capabilities and interactions. By treating code as the primary interface for actions, agents gain access to the full expressiveness of programming languages while maintaining the natural language understanding capabilities of modern LLMs.

## References

- Original Repository: https://github.com/xingyaoww/code-act
- CodeActInstruct Dataset: Available through the repository
- Model Checkpoints: HuggingFace Model Hub
- Evaluation Benchmarks: HumanEval, MBPP, GSM8K

## Appendix

### A.1 Installation and Setup
```bash
git clone https://github.com/xingyaoww/code-act.git
cd code-act
pip install -r requirements.txt
python run_agent.py --model CodeActAgent-Mistral-7b-v0.1
```

### A.2 Example Interaction
```
User: "Analyze the trend in this CSV file and create a visualization"

Agent: I'll help you analyze the CSV file and create a visualization. Let me start by examining the data structure:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load and examine the data
df = pd.read_csv('data.csv')
print(df.head())
print(df.info())
```

[Execution output shows data structure]

Now I'll create a trend visualization based on the temporal columns I found:

```python
# Create trend visualization
plt.figure(figsize=(12, 6))
df['date'] = pd.to_datetime(df['date'])
df_sorted = df.sort_values('date')
plt.plot(df_sorted['date'], df_sorted['value'], marker='o')
plt.title('Trend Analysis Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('trend_analysis.png', dpi=300, bbox_inches='tight')
plt.show()
```

The analysis shows an upward trend with seasonal variations. The visualization has been saved as 'trend_analysis.png'.
```