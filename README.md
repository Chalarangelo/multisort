# Multisort
stupidly inefficient hybrid sorting algorithm

## Usage

Use `python3` to run `multisort.py`, providing it with a valid filename and a number for the random seed. Optionally, you can add a 1 at the end to show full output of the execution. Oh, and remember to pipeline your output to another file.

#### Example

```bash
python3 multisort.py numbers1.txt 42 1 >> numbers1sorted42full.txt
```

## How it works

1. Reads a list of numbers from the file specified (space separated, can contain newlines and tabs).
2. Starts a `random` generator, using the provided seed.
3. While the list is not sorted (and yes, it compares it every step of the way with a sorted version of itself), it picks a sorting algorithm at random and uses some random values to sort part of the list (usually quite poorly).

The following sorting algorithms are implemented:
- Bubble sort (one full pass of the list)
- Insertion sort (until a preset amount of swaps is executed)
- Merge sort (works on a subset of the list)
- Quick sort (random pivot, no recursion)
- Selection sort (single position on the list receives its final value)
- Bucket sort (random amount of buckets, no recursion)
- ~~Radix sort (based on least-significant digit)~~ *Not used due to low speed and problems caused in sorting*
- Patience sort (single iteration, reversed stacks)
- Gnome sort (works on a subset of the list)
- Odd-even sort (single step of the algorithm, specified at random if odd or even)
- Stooge sort (works on subset of the list)

## License

MIT License, feel free to do whatever you want with this.
