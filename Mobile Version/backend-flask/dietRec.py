def getRecommendations(disease):

    # returns [Tips], [Foods to Take], [Foods not to Take], [warnings]

    tips, food_to_take, food_not_to_take, warnings = [], [], [], []

    if disease == "Acne":

        tips, food_to_take, food_not_to_take, warnings = (
            [
                "Eating a healthy diet that is rich in fruits, vegetables, and whole grains.",
                "Limiting processed foods, sugary drinks, and unhealthy fats.",
                "Drinking plenty of water.",
                "Eating foods that are high in omega-3 fatty acids, such as fish, flaxseeds, and walnuts.",
                "Avoiding foods that are high in dairy and refined carbohydrates.",
            ],
            ["Fruits and vegetables", "Whole grains", "Omega-3 fatty acids"],
            [
                "Dairy products",
                "Refined carbohydrates",
                "Processed foods",
            ],
            [],
        )

    elif disease == "Actinic Keratosis":
        tips, food_to_take, food_not_to_take, warnings = (
            [
                "If you notice any rough, scaly patches on your skin, it is best to see a dermatologist to get a diagnosis.",
                "Early detection and treatment of Actinic keratosis can help to prevent the development of SCC.",
                "To avoid developing Actinic keratosis, it is important to protect yourself from the sun by wearing sunscreen with an SPF of 30 or higher and protective clothing when you are outdoors.",
            ],
            [],
            [],
            [],
        )

    elif disease == "Vasculitis":
        tips, food_to_take, food_not_to_take, warnings = (
            [
                "Get regular exercise. Exercise helps to reduce inflammation and improve overall health.",
                "Avoid smoking. Smoking can damage the blood vessels and worsen inflammation.",
                "Get enough sleep. Sleep is essential for healing and immune function.",
                "Manage stress. Stress can worsen inflammation. Find healthy ways to manage stress, such as exercise, relaxation techniques, and spending time with loved ones.",
            ],
            [],
            [],
            [],
        )

    elif disease == "Vascular Tumors":
        tips, food_to_take, food_not_to_take, warnings = (
            [
                "Avoid smoking : Smoking can damage the blood vessels and increase the risk of developing vascular tumors.",
                "Maintain a healthy weight : Obesity can increase the risk of developing vascular tumors.",
                "Eat a healthy diet : A diet that is rich in fruits, vegetables, and whole grains can help to reduce inflammation and improve overall health.",
                "Get regular exercise : Exercise helps to improve blood circulation and reduce inflammation.",
                "Manage stress : Stress can increase inflammation and worsen vascular tumors.",
            ],
            [],
            [],
            ["It is advised to consult a consult a Doctor"],
        )
    elif disease == "Warts Molluscum":
        tips, food_to_take, food_not_to_take, warnings = (
            [
                "Keep your skin clean and dry.",
                "Avoid sharing personal items such as towels, razors, and clothing.",
                "Wash your hands frequently with soap and water.",
                "Avoid touching, scratching or picking at warts or molluscum bumps.",
                "Cover warts and molluscum bumps with clothing or bandages to prevent them from spreading.",
                "Use over-the-counter or prescription medications to treat warts and molluscum contagiosum.",
                "See a doctor if you have any concerns about warts or molluscum contagiosum.",
            ],
            [],
            [],
            [],
        )
    elif disease == "Tinea Ringworm Candidiasis":
        tips, food_to_take, food_not_to_take, warnings = (
            [
                "Keep your skin clean and dry.",
                "Avoid wearing tight-fitting clothing.",
                "Change your socks and underwear daily.",
                "Avoid sharing personal items such as towels, razors, and clothing.",
                "Wash your hands frequently with soap and water.",
                "Use over-the-counter or prescription antifungal medications as directed by your doctor."
                "See a doctor if your infection does not improve with treatment or if you have any concerns.",
            ],
            [
                "Fruits and vegetables",
                "Whole grains",
                "Probiotic foods",
                "Anti-fungal foods(garlic, ginger, turmeric, and coconut oil)",
            ],
            [],
            [],
        )
    elif disease == "Melanoma":
        tips, food_to_take, food_not_to_take, warnings = (
            [],
            [],
            [],
            [
                "It is suspected that You may have some serious condition. It is very much advised to Consult a Doctor",
            ],
        )

    # Hair Disorders
    elif disease == "acne keloidalis":
        tips, food_to_take, food_not_to_take, warnings = (
            [
                "Avoid picking at or scratching acne breakouts.",
                "Treat acne breakouts promptly.",
                "Avoid shaving or waxing areas of skin that are prone to keloids.",
                "Use a sunscreen with an SPF of 30 or higher when you are outdoors.",
            ],
            [],
            [],
            [],
        )
    elif disease == "alopecia areata":
        tips, food_to_take, food_not_to_take, warnings = (
            [
                "Protect your scalp from the sun by wearing a hat or scarf.",
                "Use a mild shampoo and conditioner.",
                "Avoid using harsh hair styling products.",
                "Be gentle with your hair when styling it.",
            ],
            [],
            [],
            [],
        )
    elif disease == "trichotillomania":
        tips, food_to_take, food_not_to_take, warnings = (
            [
                "Identify your triggers : What are the things that make you want to pull your hair? Once you know your triggers, you can start to develop strategies to avoid them or cope with them in a healthy way.",
                "Find a support system : Talking to other people with trichotillomania can be helpful. There are also online support groups and forums where you can connect with others who understand what you are going through",
                "Be patient with yourself : Recovery from trichotillomania takes time. Don't get discouraged if you have setbacks along the way.",
                "Seek professional help. A therapist can teach you coping skills and help you develop a treatment plan.",
            ],
            [],
            [],
            [],
        )

    return (tips, food_to_take, food_not_to_take, warnings)
