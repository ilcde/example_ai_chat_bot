# Create a clean env (recommended)
python -m venv ai-env
ai-env\Scripts\activate

# Install CUDA-enabled PyTorch (auto-selects the right build)
pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Quick check
python - << 'PY'
import torch
print("CUDA available:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")
PY