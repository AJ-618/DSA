"""
--------- Maximum Guests ---------

arrival: [900, 940, 950, 1100, 1500, 1800]
depart:  [910, 1200, 1120, 1130, 1900, 2000]
o/p: 3, because if we arrive at 11:00, then we
can meet guests who arrived at 9:40, 9:50 and 11:00.

Problem: 'arrival' contains the time the guest arrived.
'depart' contains the time the same guest departed.
Our goal is to find the maximum guests we can meet at
any given time.

Time -> O(nlogn), Space -> O(1)
"""

def max_guests(arrival: list, depart: list) -> int:
    "Find max guests that can be met at a given time"

    n = len(arrival)
    curr = res = 1
    i = 1   # Because 1st arrival will undoubtedly be before 1st departure
    j = 0

    arrival.sort()
    depart.sort()   # sort to decrement 'curr' as guests depart in comparison
                    # to the arrivals
    while i < n and j < n:
        if arrival[i] < depart[j]:
            curr += 1
            i += 1
        else:
            curr -= 1
            j += 1

        res = max(res, curr)

    return res


if __name__ == '__main__':
    arrv = [900, 940, 950, 1100, 1500, 1800]
    dept = [910, 1200, 1120, 1130, 1900, 2000]
    print(max_guests(arrv, dept))
