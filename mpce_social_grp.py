import pandas as pd
# Statement  Average MPCE (Rs.) across different social groups for State/UT and All-India 
data_8R = {
    "name": [
        "Andhra_Pradesh", "Arunachal_Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi", "Goa", "Gujarat",
        "Haryana", "Himachal_Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya_Pradesh", "Maharashtra", "Manipur",
        "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil_Nadu", "Telangana",
        "Tripura", "Uttar_Pradesh", "Uttarakhand", "West_Bengal", "Andaman_N_Island", "Chandigarh",
        "Dadra_Nagar_Haveli_Daman_Diu", "Jammu_Kashmir", "Ladakh", "Lakshadweep", "Puducherry", "India"
    ],
    "Scheduled_Tribe": [
        3772, 5517, 3289, 2927, 2258, 5230, 7084, 3412, 4970, 6996, 2218, 4086, 4526, 2651, 2726, 4090, 3451, 5264, 
        4403, 2384, 5311, 3206, 7792, 4713, 4420, 4745, 2295, 4656, 2658, 6588, 5851, 3238, 3326, 4273, 5749, 4729, 3016
    ],
    "Scheduled_Caste": [
        4565, 5444, 3387, 3058, 2347, 6029, 5950, 3592, 4299, 4564, 2850, 4258, 5058, 2977, 3742, 5333, 4118, 3392, 
        4255, 2899, 4583, 3794, 6758, 4898, 4526, 5323, 2900, 3802, 3152, 3580, 6370, 4514, 4457, None, 9399, 5059, 3474
    ],
    "Other_Backward_Class": [
        4824, 4399, 3404, 3479, 2665, 7098, 6737, 3649, 4771, 5427, 2997, 4377, 5390, 3302, 4017, 4337, 5960, 2908, 
        4011, 3258, 5335, 4527, 7844, 5462, 4937, 5531, 3191, 4421, 3234, 8080, 6068, 5473, 3808, 2739, 11909, 8040, 3848
    ],
    "Others": [
        5550, 4040, 3523, 3691, 3187, 6411, 7836, 4605, 5500, 5906, 3473, 4952, 7451, 3713, 4705, 4850, 4683, None, 
        3985, 3484, 6279, 5428, 7510, 5773, 5269, 5620, 3747, 5115, 3427, 7243, 8192, 5834, 4597, 2163, 15676, 10393, 4392
    ],
    "All": [
        4870, 5276, 3432, 3384, 2466, 6576, 7367, 3798, 4859, 5561, 2763, 4397, 5924, 3113, 4010, 4360, 3514, 5224, 
        4393, 2950, 5315, 4263, 7731, 5310, 4802, 5206, 3191, 4641, 3239, 7332, 7467, 4184, 4296, 4035, 5895, 6590, 3773
    ]
}