from typing import List


def get_requirements() -> List[str]:
    """
    Read requirements.txt and return a clean list of dependencies.
    """
    requirement_lst: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                # Ignore empty lines and editable install
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("Error: requirements.txt not found")
        return []

    return requirement_lst

print(get_requirements())
