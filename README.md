# woym.ai
What's on your mind?

This platform allows users to interact with AI personas representing different experts, each with unique knowledge domains and communication styles. The system uses parameter-efficient fine-tuning techniques to create a versatile model capable of responding as multiple personas.

## Key Features

- **Multiple Expert Personas**: Einstein, Shakespeare, Curie, and more
- **Consistent Persona Responses**: Each persona maintains its unique voice and expertise
- **Efficient Model Architecture**: Uses LoRA fine-tuning for minimal resource requirements
- **Flexible API**: Easy integration with web and mobile applications
- **Optimized Performance**: Quantization techniques for faster inference

## Technical Architecture

```
persona_ai_platform/
├── config/                 # Configuration settings
├── data/                   # Data processing and datasets
├── models/                 # Model loading and PEFT utilities
├── training/               # Training pipeline
├── inference/              # Inference and generation
├── api/                    # FastAPI server
└── utils/                  # Helper utilities
```

## Getting Started

### Prerequisites

- Python 3.8+
- PyTorch 2.0+
- Transformers 4.30+
- PEFT, BitsAndBytes, Accelerate libraries

### Installation

```bash
git clone https://github.com/mohammad17ali/woym.ai.git
cd woym
pip install -r requirements.txt
```

### Training a Model

```bash
python train.py --config configs/training_config.json
```

### Running the API

```bash
python -m api.fastapi_server
```

## Model Optimization

The platform implements several optimization techniques:

- **Quantization**: 4-bit and 8-bit quantization for efficient deployment
- **Parameter-Efficient Fine-Tuning**: LoRA adapters to minimize trainable parameters
- **Prompt Engineering**: Optimized system prompts for consistent persona responses

## Example Usage

```python
from inference.pipeline import PersonaInferencePipeline

# Initialize the pipeline
pipeline = PersonaInferencePipeline("./models/woym")

# Generate responses from different personas
einstein_response = pipeline.generate_response(
    "Can you explain the theory of relativity in simple terms?", 
    persona="einstein"
)

shakespeare_response = pipeline.generate_response(
    "What do you think about modern love?", 
    persona="shakespeare"
)

print(f"Einstein: {einstein_response}")
print(f"Shakespeare: {shakespeare_response}")
```

## Future Enhancements

- Add more diverse personas with specialized knowledge domains
- Implement multi-modal capabilities (image understanding)
- Develop persona-specific RAG (Retrieval-Augmented Generation)
- Create a web interface for interactive demos

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Hugging Face for the Transformers library
- PEFT library contributors
- TinyLlama and Llama model developer
s
