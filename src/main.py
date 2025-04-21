from action import Action
from chronograf import Chronograf
import asyncio
from nullable import nullable

cg = Chronograf(auto_start=True)


def log(a) -> None:
    print(a)


def loglog(a):
    print(__name__)


on_nantara = Action()


async def main():
    nn = nullable[int](None)
    nnn = nullable[int](1)
    print("nn == nnn:", nn == nnn)
    print("nn != nnn:", nn != nnn)
    print("nn.__str__:", nn.__str__())

    on_nantara.add(log)
    on_nantara.add(loglog)

    cg.start()
    for i in range(1000):
        on_nantara.fire(i.__str__())
        if cg.is_running:
            print(cg.elapsed.value.total_seconds())
        await asyncio.sleep(0.01)
    cg.stop()


if __name__ == "__main__":
    asyncio.run(main())
