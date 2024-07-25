component_data = {
    "001": {
        "name": "Gearbox",
        "description": "The gearbox is used to increase torque while reducing speed.",
        "material": "Steel",
        "specifications": {
            "Gear Ratio": "5:1",
            "Weight": "25 kg"
        }
    },
    "002": {
        "name": "Conveyor Belt",
        "description": "A conveyor belt is used for transporting materials from one location to another.",
        "material": "Rubber",
        "specifications": {
            "Length": "10 m",
            "Width": "0.5 m"
        }
    },
    "003": {
        "name": "Motor",
        "description": "An electric motor converts electrical energy into mechanical motion.",
        "material": "Copper, Steel",
        "specifications": {
            "Power": "1.5 kW",
            "Voltage": "230V"
        }
    }
}

def get_component_description(component_id):
    component = component_data.get(component_id, None)
    if component:
        print(f"Component Name: {component['name']}")
        print(f"Description: {component['description']}")
        print(f"Material: {component['material']}")
        for spec, value in component['specifications'].items():
            print(f"{spec}: {value}")
    else:
        print("Component not found.")

# Example usage
get_component_description("001")
