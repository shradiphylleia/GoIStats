import pandas as pd

data ={
    "name":[
        "Andhra_Pradesh", "Arunachal_Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi", "Goa",
        "Gujarat", "Haryana", "Himachal_Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya_Pradesh",
        "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
        "Sikkim", "Tamil_Nadu", "Telangana", "Tripura", "Uttar_Pradesh", "Uttarakhand", "West_Bengal",
        "Andaman_N_Island", "Chandigarh", "Dadra_Nagar_Haveli_Daman_Diu", "Jammu_Kashmir",
        "Ladakh", "Lakshadweep", "Puducherry", "India"
    ],
    "mpce_rural": [
        4870, 5276, 3432, 3384, 2466, 6576, 7367, 3798, 4859, 5561, 2763, 4397, 5924, 3113,
        4010, 4360, 3514, 5224, 4393, 2950, 5315, 4263, 7731, 5310, 4802, 5206, 3191, 4641,
        3239, 7332, 7467, 4184, 4296, 4035, 5895, 6590, 3773
    ],
    "mpce_urban": [
        6782, 8636, 6136, 4768, 4483, 8217, 8734, 6621, 7911, 8075, 4931, 7666, 7078, 4987,
        6657, 4880, 6433, 7655, 7098, 5187, 6544, 5913, 12105, 7630, 8158, 7405, 5040, 7004,
        5267, 10268, 12575, 6298, 6179, 6215, 5475, 7706, 6459
    ],
    "mpce_rural_imputation": [
        4996, 5300, 3546, 3454, 2575, 6595, 7388, 3820, 4912, 5573, 2796, 4578, 5960, 3158,
        4076, 4370, 3530, 5243, 4457, 2996, 5363, 4348, 7787, 5457, 4959, 5301, 3277, 4721,
        4307, 7332, 7467, 4229, 4357, 4062, 5979, 6627, 3860
    ],
    "mpce_urban_imputation": [
        6877, 8649, 6210, 4819, 4557, 8250, 8761, 6630, 7948, 8083, 4946, 7781, 7102, 5011,
        6683, 4902, 6450, 7664, 7159, 5223, 6577, 5970, 12125, 7742, 8251, 7473, 5104, 7034,
        5426, 10268, 12575, 6306, 6200, 6227, 5511, 7741, 6521
    ]
}
