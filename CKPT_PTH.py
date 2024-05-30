import os.path

CKPTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ckpts")

LLAVA_CLIP_PATH = os.path.join(CKPTS_DIR, "clip-vit-large-patch14-336")
LLAVA_MODEL_PATH = os.path.join(CKPTS_DIR, "llava-v1.5-13b")
SDXL_CLIP1_PATH = os.path.join(CKPTS_DIR, "clip-vit-large-patch14")
SDXL_CLIP2_CKPT_PTH = os.path.join(
    CKPTS_DIR, "CLIP-ViT-bigG-14-laion2B-39B-b160k", "open_clip_pytorch_model.bin"
)
