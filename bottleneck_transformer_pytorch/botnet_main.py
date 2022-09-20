import torch
from torch import nn
from torchvision.models import resnet50

from bottleneck_transformer_pytorch import BottleStack


if torch.cuda.is_available():
    CUDA = True
    device = torch.device("cuda")
    print("Training on CUDA")
elif torch.backends.mps.is_available() and torch.backends.mps.is_built():
    device = torch.device("mps")
    print("Training on mps")
else:
    CUDA = False
    device = torch.device("cpu")
    print("Training on CPU")




num_classes = 2
layer = BottleStack(
    dim=256,
    fmap_size=24,  # set specifically for Pcam's 96 x 96
    dim_out=1024,
    proj_factor=4,
    downsample=True,
    heads=4,
    dim_head=128,
    rel_pos_emb=True,
    activation=nn.ReLU()
)

resnet = resnet50()

# model surgery

backbone = list(resnet.children())

model = nn.Sequential(
    *backbone[:5],
    layer,
    nn.AdaptiveAvgPool2d((1, 1)),
    nn.Flatten(1),
    nn.Linear(1024, 512),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Linear(512, num_classes),
    nn.Softmax(dim=1)
)

x = torch.randn(2, 3, 96, 96,device=device)
# layers = list(model.modules())
# for i, _ in enumerate(layers):
#     print(x.shape)
#     print(layers[0][i])
#     x = layers[0][i](x)
#     print(x.shape)

# use the 'BotNet'


preds = model(x)  # (2, 1000)
print(preds)