import requests

headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'pipeline_run': {
        'variables': {
            'key1': 'value1',
            'key2': 'value2',
        },
    },
}

response = requests.post(
    'http://localhost:6789/api/pipeline_schedules/1/pipeline_runs/7bb3a54c7c9245faacd17f30e0c73f86',
    headers=headers,
    json=json_data
)

print(response.json())
