storage_gb = float(input("Enter storage in GB: "))
storage_mb = storage_gb * 1024
print("Storage in MB:", storage_mb)
storage_tb = storage_gb / 1024
print("Storage in TB:", round(storage_tb, 4))