from stopwatch import Stopwatch
import asyncio
from nullable import nullable

sw = Stopwatch(True)

async def main():
    nn = nullable[int](None)
    nnn = nullable[int](1)
    print('nn == nnn:', nn == nnn)
    print('nn != nnn:', nn != nnn)
    print('nn.__str__:', nn.__str__())

    # for _ in range(10):
    #     print(sw.is_running)
    #     await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())