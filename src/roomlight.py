
class Configuration:
    def __init__(self, name, lumen, temp):
        self.name = name
        self.lumen = lumen
        self.temp = temp


class Light:
    def __init__(self, location, name, lumen=450, temp=3500):
        self.name = name
        self.lumen = lumen
        self.temp = temp
        self.location = location
        self.group = None

    def apply_config(self, config: Configuration):
        self.lumen = config.lumen
        self.temp = config.temp


class LightGroup:
    def __init__(self, name):
        self.name = name
        self.lights = []
        self.config = None

    # Add single light
    def add_light(self, light: Light):
        light.group = self.name
        self.lights.append(light)
    # Add list of lights for easy initialisation or global config

    def add_lights(self, lights):
        for light in lights:
            self.add_light(light)

    # used if light is set in somewhere else (group)
    def remove_light(self, light: Light):
        if light in self.lights:
            self.lights.remove(light)

    def apply_config(self):
        if self.config is None:
            return
        for light in self.lights:
            light.apply_config(self.config)
    # Clear all confs before global conf

    def clear(self):
        self.lights.clear()


# ---------- INIT ----------
# Sample data for demo and developing purposes

def initialize_lights():
    light_list = []
    # Load lights to empty list
    light_list.extend([Light("Room1", "L0"),
                       Light("Room1", "L1", 850, 6000),
                       Light("Room1", "L2",),
                       Light("Room2", "L3"),
                       Light("Room2", "L4"),
                       Light("Room2", "L5"),
                       Light("Corridor", "L6"),
                       Light("Corridor", "L7"),
                       Light("Corridor", "L8")])

    return light_list


def init_groups(lights):
    g1 = LightGroup("Room1")
    g1.add_lights(lights[0:3])

    g2 = LightGroup("Room2")
    g2.add_lights(lights[3:6])

    global_group = LightGroup("GLOBAL")

    return [g1, g2, global_group]


def init_configurations():
    return {
        "c1": Configuration("c1", 200, 4000),
        "c2": Configuration("c2", 300, 4000),
        "c3": Configuration("c3", 150, 4000),
    }


# ---------SHOW operations----------#

def show_lights(lights):
    print("\nLights:")
    for l in lights:
        print(f"{l.name} | {l.location} | group: {l.group}")


def show_setups(lights):
    print("\nLight setups:")
    for l in lights:
        print(f"{l.name}: {l.lumen} lm, {l.temp} K")


def show_groups(groups):
    print("\nGroups:")
    for g in groups:
        if g.config:
            conf = g.config.name
        else:
            conf = None
        print(f"\n{g.name} (config: {conf})")
        for l in g.lights:
            print(f"  - {l.name}")


def show_configs(configs):
    print("\nConfigurations:")
    for name, c in configs.items():
        print(f"{name}: {c.lumen} lm, {c.temp} K")


# --------------------

def create_configuration(configs):
    show_configs(configs)

    name = input("Name: ")
    if not name:
        return configs

    lumen = int(input("Lumens: "))
    temp = int(input("Temperature: "))

    configs[name] = Configuration(name, lumen, temp)
    print("Created.")

    return configs


def assign_config_to_group(groups, configs):
    show_configs(configs)
    conf_name = input("Select config: ")

    if conf_name not in configs:
        print("Not found")
        return

    show_groups(groups)
    group_name = input("Select group: ")

    for g in groups:
        if g.name == group_name:
            g.config = configs[conf_name]
            print("Assigned.")
            return

    print("Group not found")


def deploy(groups):
    for g in groups:
        g.apply_config()
    print("Configurations applied.")


def create_group(groups, lights):
    show_lights(lights)

    name = input("New group name: ")
    new_group = LightGroup(name)

    lights_by_name = {}
    for i in lights:
        lights_by_name[i.name] = i

    while True:
        choice = input("Add light (0 to stop): ")
        if choice == "0":
            break

        light = lights_by_name.get(choice)
        if not light:
            print("Not found")
            continue

        # remove from old group
        for g in groups:
            if light in g.lights:
                g.remove_light(light)

        new_group.add_light(light)
        print(f"Added {choice}")

    groups.append(new_group)


def global_config(groups, lights, configs):
    show_configs(configs)
    name = input("Select config: ")

    if name not in configs:
        print("Not found")
        return

    # clear all
    for g in groups:
        g.clear()

    # find GLOBAL
    for g in groups:
        if g.name == "GLOBAL":
            g.add_lights(lights)
            g.config = configs[name]
            g.apply_config()
            print("Global config applied")


# ---------- UI ----------

def menu():
    print("""
1 - Show lights
2 - Show deployed setups
3 - Show saved groups
4 - Create config
5 - Create group
6 - Assign config to group
7 - Deploy
8 - Global config
0 - Exit
""")


def main():
    lights = initialize_lights()
    configs = init_configurations()
    groups = init_groups(lights)

    while True:
        menu()
        choice = input("Choice: ")

        if choice == "1":
            show_lights(lights)
        elif choice == "2":
            show_setups(lights)
        elif choice == "3":
            show_groups(groups)
        elif choice == "4":
            configs = create_configuration(configs)
        elif choice == "5":
            create_group(groups, lights)
        elif choice == "6":
            assign_config_to_group(groups, configs)
        elif choice == "7":
            deploy(groups)
        elif choice == "8":
            global_config(groups, lights, configs)
        elif choice == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
