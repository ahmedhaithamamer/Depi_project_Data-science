"""
Stage 1 Pipeline - Feature Engineering
========================================
This script runs all Stage 1 feature engineering tasks sequentially.
Can be run from either the project root or the stage1/ directory.
"""

import os
import sys

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)  # Change to script directory to ensure correct paths

print("STAGE 1 PIPELINE - FEATURE ENGINEERING")
print("\nPipeline Flow:")
print("  Stage1.2 -> [1.3.1] -> Time Features -> [1.3.2] -> Lag Features")
print("  -> [1.3.3] -> Encoding -> [1.3.4] -> Normalization -> Final\n")

# Step 1.3.1: Time-based features
print("[1/4] STEP 1.3.1: TIME-BASED FEATURES")
exit_code = os.system(f"{sys.executable} step_1_3_1_time_features.py")
if exit_code != 0:
    print(f"\nERROR: Step 1.3.1 failed with exit code {exit_code}")
    sys.exit(1)

# Step 1.3.2: Lag features
print("[2/4] STEP 1.3.2: LAG & ROLLING FEATURES")
exit_code = os.system(f"{sys.executable} step_1_3_2_lag_features.py")
if exit_code != 0:
    print(f"\nERROR: Step 1.3.2 failed with exit code {exit_code}")
    sys.exit(1)

# Step 1.3.3: Categorical encoding
print("[3/4] STEP 1.3.3: CATEGORICAL ENCODING")
exit_code = os.system(f"{sys.executable} step_1_3_3_encode_categorical.py")
if exit_code != 0:
    print(f"\nERROR: Step 1.3.3 failed with exit code {exit_code}")
    sys.exit(1)

# Step 1.3.4: Normalization
print("[4/4] STEP 1.3.4: FEATURE NORMALIZATION")
exit_code = os.system(f"{sys.executable} step_1_3_4_normalize_features_final.py")
if exit_code != 0:
    print(f"\nERROR: Step 1.3.4 failed with exit code {exit_code}")
    sys.exit(1)

# Final summary
print("STAGE 1 PIPELINE COMPLETED SUCCESSFULLY!")
print("\nFinal Outputs:")
print("  processed_data/Stage1.3.4_Final/")
print("     |- train_final.csv (421,570 rows x 49 features)")
print("     |- test_final.csv (115,064 rows x 31 features)")
print("     `- normalization_params.json")
print("\nReady for Stage 2 (Advanced Analysis)!")

