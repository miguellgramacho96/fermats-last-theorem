import sys
import time

def check_fermats_last_theorem(start, end, toThePowerOf):
    if toThePowerOf <= 2:
        raise ValueError("Your power must be greater than 2.")
    for a in range(start, end):
        for b in range(start, end):
            for c in range(start, end):
                if a**toThePowerOf + b**toThePowerOf == c**toThePowerOf:
                    return (a, b, c)
    return None

def main():
    start_time = time.time()

    if len(sys.argv) < 4:
        print("Usage: python theorem.py <start> <end> <power>")
        return

    start = int(sys.argv[1])
    end = int(sys.argv[2])
    power = int(sys.argv[3])

    result = check_fermats_last_theorem(start, end, power)
    if result:
        a, b, c = result
        print(f"Found a solution: {a}^{power} + {b}^{power} = {c}^{power}")
    else:
        print("No solution found in the given range.")

    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()