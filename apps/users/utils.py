import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity
from apps.users.models import UserProfile
def user_profile_to_vector(profile):
    # Categorical - > One - hot
    travel_style_map = {'budget':0,'lucury':1, 'adventure':2, 'cultural' :3}
    pace_map = {'relaxed':0, 'moderate':1,'fast_paced':2}
    accom_map ={'hostel':0, 'hotel':1, 'inn':2, 'camping':3}

    cats=[
        travel_style_map.get(profile.travel_style,1),
        pace_map.get(profile.pace, -1),
        accom_map.get(profile.accomodation_preference, -1),
    ]

# Numerical
    nums=[
            profile.budget_level,
            profile.adventure_level,
            profile.social_level,
        ]

    dest_vector =[0] *5
    dest_keywords=['mountain','city', 'temples','nature', 'lake']
    for dest in profile.preferred_destinations.lower().replace(' ',' ').split(','):
        for i , kw in enumerate(dest_keywords):
            if kw in dest:
             dest_vector[i]=1;

# Combining everything

    vector = np.array(cats + nums + dest_vector, dtype=float)

# Scaling numerical features 0-1
    scaler = MinMaxScaler(feature_range=(0,1))
    vector[3:6] = scaler.fit_transform(vector[3:6].reshape(-1,1)).flatten()
    return vector


# Find similar users matching
def find_similar_users(current_profile, limit=9, min_similarity=0.65):
   
   current_vector= user_profile_to_vector(current_profile)
   similar =[]

   for other in UserProfile.objects.exclude(user= current_profile.user).select_related('user'):
        other_vector =user_profile_to_vector(other)

        sim = cosine_similarity(
         current_vector.reshape(1, -1),
        other_vector.reshape(1,-1)
      )[0][0]

        if sim >= min_similarity:
         similar.append((other, round(sim,3)))


 #  Sorting by similarity descending
   similar.sort(key=lambda x : x[1], reverse=True)
   
   return similar[:limit]



  
