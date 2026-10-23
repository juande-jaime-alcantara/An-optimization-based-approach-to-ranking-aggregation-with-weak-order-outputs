from pathlib import Path
import random

# -------------------------
# Configurable parameters
# -------------------------
OUTPUT_DIR = Path(__file__).resolve().parent / "synthetic_instances"
SIZES = [20, 40, 60, 80, 100]
INSTANCES_PER_SIZE = 5

ALPHA = 3
BETA = 1
SEED = 42
DECIMALS = 10


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)

    instance_id = 1

    for n in SIZES:
        for _ in range(INSTANCES_PER_SIZE):
            c = [[0.0] * n for _ in range(n)]

            for r in range(n):
                c[r][r] = 0.5

                for s in range(r + 1, n):
                    value = round(
                        rng.betavariate(ALPHA, BETA),
                        DECIMALS,
                    )
                    c[r][s] = value
                    c[s][r] = 1.0 - value

            output_file = OUTPUT_DIR / f"I{instance_id}.dat"

            with output_file.open("w", encoding="utf-8") as f:
                f.write(f"n: {n}\n\n")
                f.write("c:\n[\n")

                for row in c:
                    values = " ".join(
                        f"{value:.{DECIMALS}f}" for value in row
                    )
                    f.write(f" {values}\n")

                f.write("]\n")

            print(f"Generated {output_file.name}: n = {n}")
            instance_id += 1

    print(f"\nTotal: {instance_id - 1} instances.")
    print(f"Output directory: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()