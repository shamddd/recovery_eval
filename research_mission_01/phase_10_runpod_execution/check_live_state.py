import tomli
import runpod
import requests
import json

with open('/Users/shamthakare/.runpod/config.toml', 'rb') as f:
    key = tomli.load(f)['default']['api_key']

runpod.api_key = key

# 1. User & Balance
query = '''query { myself { id email clientBalance networkVolumes { id name size dataCenterId } } }'''
resp = requests.post(
    'https://api.runpod.io/graphql',
    json={'query': query},
    headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
)
user_data = resp.json().get('data', {}).get('myself', {})
balance = user_data.get('clientBalance', 0.0)
email = user_data.get('email', '')
user_id = user_data.get('id', '')
volumes = user_data.get('networkVolumes', [])

print(f"User ID: {user_id}")
print(f"User Email: {email}")
print(f"Live Account Balance: ${balance:.4f} USD")
print(f"Network Volumes Count: {len(volumes)}")
for v in volumes:
    print(f"  Volume: ID={v.get('id')}, Name={v.get('name')}, Size={v.get('size')}GB, DC={v.get('dataCenterId')}")

# 2. Existing Pods
pods = runpod.get_pods()
print(f"Existing Pods Count: {len(pods)}")
for p in pods:
    print(f"  Pod: ID={p.get('id')}, Name={p.get('name')}, DesiredStatus={p.get('desiredStatus')}, Cost/hr=${p.get('costPerHr')}")

# 3. GPU availability & pricing for RTX 4090
g_4090 = runpod.get_gpu('NVIDIA GeForce RTX 4090')
print("RTX 4090 Details:")
print(f"  Display Name: {g_4090.get('displayName')}")
print(f"  Memory: {g_4090.get('memoryInGb')} GB")
print(f"  Community Price: ${g_4090.get('communityPrice')}/hr")
print(f"  Secure Price: ${g_4090.get('securePrice')}/hr")
print(f"  Community Cloud Available: {g_4090.get('communityCloud')}")
print(f"  Secure Cloud Available: {g_4090.get('secureCloud')}")

# RTX 3090 Details
g_3090 = runpod.get_gpu('NVIDIA GeForce RTX 3090')
print("RTX 3090 Details:")
print(f"  Display Name: {g_3090.get('displayName')}")
print(f"  Memory: {g_3090.get('memoryInGb')} GB")
print(f"  Community Price: ${g_3090.get('communityPrice')}/hr")
print(f"  Secure Price: ${g_3090.get('securePrice')}/hr")
