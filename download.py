from datasets import load_dataset, Audio

dataset = load_dataset("DBD-research-group/BirdSet", "POW", 
                       cache_dir="D:/birdset/datasets",
                       trust_remote_code=True)

dataset = dataset.cast_column("audio", Audio(sampling_rate=32000))

