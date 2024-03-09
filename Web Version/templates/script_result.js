let inputVal = document.getElementById("resultContainerEl").textContent.trim();

document.addEventListener("DOMContentLoaded", function () {
  let gt_diet = document.getElementById("get_diet_plan");
  let recommendations = document.getElementById("docRecommendation");

  let list = ["Class: Melanoma", "Class: Vasculitis", "Class: Acne"];

  if (list.includes(inputVal)) {
    recommendations.style.display = "block";
  } else {
    gt_diet.style.display = "block";
  }
});

let allClassList = [
  "Class: Actinic Keratosis",
  "Class: Vasculitis",
  "Class: Vascular Tumors",
  "Class: Warts Molluscum",
  "Class: Tinea Ringworm Candidiasis"
];

let dietObj = {
  "Class: Actinic Keratosis": "1 If you notice any rough, scaly patches on your skin, it is best to see a dermatologist to get a diagnosis.2 Early detection and treatment of AK can help to prevent the development of SCC.3 To avoid developing AK, it is important to protect yourself from the sun by wearing sunscreen with an SPF of 30 or higher and protective clothing when you are outdoors.",
  "Class: Vasculitis": "Here are some additional tips for managing vasculitis:1 Get regular exercise. Exercise helps to reduce inflammation and improve overall health.2 Avoid smoking. Smoking can damage the blood vessels and worsen inflammation.3 Get enough sleep. Sleep is essential for healing and immune function.4 Manage stress. Stress can worsen inflammation. Find healthy ways to manage stress, such as exercise, relaxation techniques, and spending time with loved ones.",
  "Class: Vascular Tumors": "Here are some tips for reducing the risk of developing vascular tumors:1 Avoid smoking. Smoking can damage the blood vessels and increase the risk of developing vascular tumors.2 Maintain a healthy weight. Obesity can increase the risk of developing vascular tumors.Eat a healthy diet. A diet that is rich in fruits, vegetables, and whole grains can help to reduce inflammation and improve overall health.3 Get regular exercise. Exercise helps to improve blood circulation and reduce inflammation.4 Manage stress. Stress can increase inflammation and worsen vascular tumors.If you have any questions or concerns about vascular tumors, please talk to your doc",
  "Class: Warts Molluscum": "Warts and molluscum contagiosum are not cancerous. They are both common skin conditions caused by viruses.1 Avoid sharing personal items such as towels, razors, and clothing.2 Wash your hands frequently with soap and water.3 Avoid touching warts or molluscum bumps.4 Cover warts and molluscum bumps with clothing or bandages to prevent them from spreading.",
  "Class: Tinea Ringworm Candidiasis": "Here are some tips for preventing fungal infections:Here are some tips for preventing fungal infections:1 Keep your skin clean and dry.2 Avoid wearing tight-fitting clothing.3 Change your socks and underwear daily.4 Avoid sharing personal items such as towels, razors, and clothing.5 Wash your hands frequently with soap and water."
};

if (allClassList.includes(inputVal)) {
  if (dietObj.hasOwnProperty(inputVal)) {
    console.log(dietObj[inputVal]);
  }
}
