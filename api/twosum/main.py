from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def solve_twosum(nums: str, target: int):
    arr = list(map(int, nums.split(",")))
    lookup = {}

    for i, n in enumerate(arr):
        diff = target - n
        if diff in lookup:
            return {"indices": [lookup[diff], i]}
        lookup[n] = i

    return {"message": "No solution"}
