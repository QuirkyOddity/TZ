import json
import sys
def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
def save_json_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
def fill_values(test_structure, values_map):
    if isinstance(test_structure, dict):
        if 'id' in test_structure and 'value' in test_structure:
            test_id = test_structure['id']
            if test_id in values_map:
                test_structure['value'] = values_map[test_id]
        if 'values' in test_structure:
            for item in test_structure['values']:
                fill_values(item, values_map)
    elif isinstance(test_structure, list):
        for item in test_structure:
            fill_values(item, values_map)
def main():
    if len(sys.argv) != 4:
        sys.exit(1)
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]
    values_data = load_json_file(values_path)
    tests_data = load_json_file(tests_path)
    values_map = {item['id']: item['value'] for item in values_data['values']}
    fill_values(tests_data, values_map)
    save_json_file(tests_data, report_path)
if __name__ == "__main__":
    main()
