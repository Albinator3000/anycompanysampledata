import pandas as pd

# Load inventory data
inventory_data = pd.read_excel('Inventory_Count.xlsx')

def check_inventory(component_id):
    component = inventory_data[inventory_data['Component ID'] == component_id]
    if not component.empty:
        print(f"Component ID: {component['Component ID'].values[0]}")
        print(f"Component Name: {component['Component Name'].values[0]}")
        print(f"Quantity: {component['Quantity'].values[0]}")
        print(f"Location: {component['Location'].values[0]}")
    else:
        print("Component not found in inventory.")

# Example usage
check_inventory('001')
