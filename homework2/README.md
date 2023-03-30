# Graph Mining HW2

## Please install anaconda & cuda 11.3 (if you want to use gpu) first.

## Create the Environment
```
conda create --name hw2 pip -y
conda activate hw2
pip install scipy numpy
```
* with gpu support
  ```
  # for cuda 11.3
  pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
  
  ```
* without gpu support
  ```
  # Your OS is not linux
  pip3 install torch torchvision torchaudio
  
  # Your OS is linux 
  pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
  ```

## Run
```
python3 main.py 
```
* You can pass arguments like this.
```
python3 main.py --input_file target_nodes_list.txt --data_path ./data/data.pkl --model_path saved-models/gcn.pt
```

## Dataset
* Cora citation network
* Select the largest connected components of the graph and use 10%/10% nodes for training/validation.
* Stats:
  
| #nodes | #edges | #features | #classes |
|--------|--------|-----------|----------|
| 2485   | 10138  | 1433      | 7        |

## TODO
* attacker.py
  * implement your own attacker
* main.py
  * setup your attacker

## My Environment

python --> 3.8.8

How to run the code?

```bash
python main.py --input_file target_nodes_list.txt --data_path ./data/data.pkl --model_path ./saved-models/gcn.pt
```

I didn't use GPU, if you want it, just add --use-gpu.

And my python3 command is just python, that maybe different between our environments, so you can just modify it according to your environment.

I didn't use any other modules than the ones used in TA's example.
