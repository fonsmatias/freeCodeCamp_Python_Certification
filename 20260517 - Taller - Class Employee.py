class Employee:
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.salary = Employee._base_salaries[level]

    def __str__(self):
        return f'{self.name}: {self.level}'

    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

# getter de name: sólo referencia el parámetro

    @property
    def name(self):
        return self._name

# setter de name: verifica que sea str y asigna el nuevo nombre

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

# getter de level: sólo referencia el parámetro

    @property
    def level(self):
        return self._level

# setter de level: antes de la asignación verifica que 
# (1) sea str (2) coincidencia de nombre con organigrama 
# (3) esté creado + que no sea igual al existente
# (4) esté creado + que no sea menor al existente
# finalmente asigna nuevo nivel y llama al setter de salario

    @level.setter
    def level(self, new_level):
        if not isinstance(new_level, str):
            raise TypeError("'level' must be a string.")
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if hasattr(self, '_level') and new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        if hasattr(self, '_level') and Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError("Cannot change to lower level.")
        print(f"'{self.name}' promoted to '{new_level}'.")
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level

# getter de salary: sólo referencia el parámetro

    @property
    def salary(self):
        return self._salary

# setter de salary: antes de la asignación verifica que 
# (1) sea int o float 
# (2) esté creado + que no sea menor al existente
# finalmente asigna salario (que será devuelto por el getter cuando se lo llame)

    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(f'Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.')
        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')

charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')
charlie_brown.level = 'junior'