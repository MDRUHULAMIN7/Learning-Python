# Variables in Python

Naming Conventions 

- Apni Python-e variable prodhanoto 3 vabe likhte paren:
    - **Camel case** - sheryiansSchool
    - **Pascal case** - SheryiansSchool
    - **Snake case** - sheryians_school
- **Python PEP 8 Standard:** Variable lekhar 3ti upay thakleo, Python-er opficial style guide (PEP 8) onujayi variable abong function-er namer jonno shobshomoy **snake_case** bebohar kora uchit. **PascalCase** amader Class-er namer jonno ebong **camelCase** Python-e khub ekta bebohar kora hoy na.

# Variables in Python

- Python-e Variables promanoto memory storage hishebe bebohar kora hoy jekhane bivinno rokomer data ba value jama rakha jay (amra pore dekhbo ki ki store korte hobe).
- Apni jekono name-e variable likhte paren.
    - Eg. Name = “Akarsh”
    - Age = 12

### 🚫 Don’t use these

- **Variable-er namer shuru-te kono number ba shonkha bebohar kora jabe na.** (Jemon: `1name` hobe na, eti vul)
- **Variable-er namer majhe kono space thakte parbe na.** (Jemon: `my name` hobe na, eti vul)
- **Variable-er namer moddhe kono special character thaka jabe na.** (Jemon: `@`, `#`, `$`, `%` egulo bebohar kora jabe na)

# Advanced & Crucial Rules

- **Case-Sensitivity:** Python-e variable-er nam gulo case-sensitive hoy. Er mane holo `age`, `Age`, ebong `AGE` tinta shompurno alada variable hishebe ganno hobe.
- **Reserved Keywords:** Python-er nijossho kichu reserved ba shongrokkhito shobdo ache (Jemon: `if`, `else`, `while`, `for`, `def`, `class`, `True`, `False`), egulo kkhonoi variable-er nam hishebe bebohar kora jabe na.
- **The Underscore Exception:** Special character nishiddho holeo ekta exception ache—variable-er nam **underscore (`_`) diye shuru kora jay**. (Jemon: `_my_variable = 10` eti sothik)
- **Dynamic Typing:** Python holo ekta dynamically typed language. Er mane variable toiri korar shomoy data type (integer ba string) boley dite hoy na ebong dorkar porle porobortite eki variable-e onno type-er data-o rakha jay.
x = 5       # Ekhon eti ekta Integer
x = "Hello" # Automatic change hoye ekhon eti ekta String hoye gelo