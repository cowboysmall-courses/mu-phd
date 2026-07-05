# SDC Research

## Running the Research

Ensure that [uv](https://docs.astral.sh/uv/getting-started/installation/) is installed, and then run the following:

```zsh

> uv run sdc-parity

```

you should see output similar to the below:

```

SDC: Parity

Parity(10100100) = 1
Tile(left_instruction=0, right_instruction=1, left_input='10', right_input='10', value=1)
Tile(left_instruction=1, right_instruction=0, left_input='10', right_input='01', value=0)
Tile(left_instruction=0, right_instruction=1, left_input='01', right_input='00', value=1)
Tile(left_instruction=1, right_instruction=1, left_input='00', right_input='--', value=1)

Parity(00100100) = 0
Tile(left_instruction=0, right_instruction=0, left_input='00', right_input='10', value=0)
Tile(left_instruction=0, right_instruction=1, left_input='10', right_input='01', value=1)
Tile(left_instruction=1, right_instruction=0, left_input='01', right_input='00', value=0)
Tile(left_instruction=0, right_instruction=0, left_input='00', right_input='--', value=0)

Parity(11111111) = 0
Tile(left_instruction=0, right_instruction=0, left_input='11', right_input='11', value=0)
Tile(left_instruction=0, right_instruction=0, left_input='11', right_input='11', value=0)
Tile(left_instruction=0, right_instruction=0, left_input='11', right_input='11', value=0)
Tile(left_instruction=0, right_instruction=0, left_input='11', right_input='--', value=0)

Parity(00000000) = 0
Tile(left_instruction=0, right_instruction=0, left_input='00', right_input='00', value=0)
Tile(left_instruction=0, right_instruction=0, left_input='00', right_input='00', value=0)
Tile(left_instruction=0, right_instruction=0, left_input='00', right_input='00', value=0)
Tile(left_instruction=0, right_instruction=0, left_input='00', right_input='--', value=0)

```
