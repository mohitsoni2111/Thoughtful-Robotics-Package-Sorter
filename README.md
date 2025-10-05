# 📦 Thoughtful Robotics Package Sorter

## 🧭 Objective

You work in **Thoughtful’s robotic automation factory**, where robotic arms dispatch packages into stacks based on their **volume** and **mass**.  
This program determines which stack each package belongs to.

---

## ⚙️ Rules

Each package is classified using the following criteria:

- A package is **bulky** if:
  - Its volume (`width × height × length`) is **≥ 1,000,000 cm³**, or  
  - Any of its dimensions (`width`, `height`, or `length`) is **≥ 150 cm**.

- A package is **heavy** if:
  - Its mass is **≥ 20 kg**.

---

## 🧩 Stack Categories

| Stack Type  | Criteria |
|--------------|-----------|
| **STANDARD** | Not bulky **and** not heavy |
| **SPECIAL**  | Bulky **or** heavy (but not both) |
| **REJECTED** | Both bulky **and** heavy |

---

## 💻 Implementation

### Function: `sort(width, height, length, mass)`

```python
def sort(width, height, length, mass):
    # Calculate volume
    volume = width * height * length

    # Determine if the package is bulky
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150

    # Determine if the package is heavy
    is_heavy = mass >= 20

    # Dispatch according to the rules
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
```

## How to run
1. Clone the repo
```
git clone https://github.com/mohitsoni2111/Thoughtful-Robotics-Package-Sorter.git
```
2. Run the sorter script
```
python sorter.py
```
3. Run the test cases
```
python -m unittest test_sorter.py
```
