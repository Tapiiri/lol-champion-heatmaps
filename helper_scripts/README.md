### Helper scripts
### `check_npz_data.py`

A simple script to check that bounding boxes contained in the NPZ file are within a given tolerance of size variation. Initially used to validate the usability of the DeepLeague dataset.

#### Usage
```bash
python check_npz_data.py --path PATH
```

#### Arguments
- `--path PATH`: Required. Specify the path to the NPZ file.

---