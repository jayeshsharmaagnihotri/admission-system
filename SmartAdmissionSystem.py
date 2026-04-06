
import re

def get_name(prompt):
    while True:
        name = input(prompt).strip()
        if re.fullmatch(r"[A-Za-z][A-Za-z\s\-']+", name):
            return name.title()
        print("Invalid name format.")

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or value > max_val:
                print(f"Enter value between {min_val} and {max_val}")
                continue
            return value
        except ValueError:
            print("Invalid number.")

def evaluate(Marks, Entrance_exam_score, Extracurricular_score):
    if Marks < 40 or Entrance_exam_score < 40:
        return "REJECTED"
    elif (Marks >= 75 and Entrance_exam_score >= 75) or \
         (Marks >= 65 and Entrance_exam_score >= 65 and Extracurricular_score >= 8):
        return "ADMITTED"
    elif Marks >= 50 and Entrance_exam_score >= 50:
        return "WAITLISTED"
    else:
        return "REJECTED"

def generate_message(name, status):
    if status == "ADMITTED":
        return f"""To {name},\n\nThe Candidate of Singular Merit,

It is with the most lively satisfaction and a sense of distinguished honor that we take up the pen to address you. We have, with the utmost scrupulosity, examined the testimonials of your character and the fruits of your intellectual industry. It is rare, indeed, to encounter an individual whose scholastic attainments are matched so evenly by a reputation for such steadfast integrity.

Therefore, it is our distinct pleasure to invite you to join our upcoming assembly. We are firmly of the belief that your presence within these hallowed halls shall not only redound to your own credit but shall also add a particular luster to the reputation of this institution. Your admission is granted with the full confidence of the Board, who perceive in your previous labors the promise of a most illustrious future.

We pray you will accept this intelligence as a testament to your hard-won success. We look forward with great anticipation to the day you grace our threshold and commence your studies in earnest.

With every sentiment of esteem and congratulation,

The Board of Admissions"""
    elif status == "WAITLISTED":
        return f"""To {name},\n\nThe Candidate of Steady Character and Hopeful Merit,

We have received your petition for admission to this honorable institution and have, with the most painstaking care, weighed the testimonials of your previous industry. It is a matter of no small difficulty for the Board to adjudicate upon the merits of a soul such as yours—one who possesses a commendable degree of scholastic attainment and a character that reflects a most sober and upright nature.

Whilst we do not find ourselves in a position to grant you an immediate seat at our table, neither have we the inclination to dismiss your candidacy entirely. Your name has been inscribed upon our ledger of "Reserved Petitions." We must, with the utmost gravity, request that you exercise that most noble of virtues—patience—whilst we observe the motions of the current assembly and the availability of our resources.

Pray, do not be disheartened by this intelligence. To wait is not to fail; it is a season of refinement. We shall communicate further should the Providence of our vacancies permit your entry. Until such a time, we remain your humble servants, attentive to the progress of your endeavors.

With every sentiment of respect and cautious anticipation,

The Board of Admissions"""
    else:
        return f"""To {name},\n\n The Candidate of Presently Unmet Potential,

It is with a heavy heart and the most sincere regard for your future that we have concluded our examination of your petition for admission. We have, with the utmost diligence, sought to find a alignment between your current scholastic attainments and the rigorous demands of our curriculum; yet, we find that the season for your entry into these specific halls has not yet bloomed.

To speak with the candor that a true mentor owes a student: your application suggests that your heart and mind have, of late, been occupied by interests far removed from the sober discipline of our studies. One cannot help but feel that your true talents lie dormant, waiting for a spark of resolve to set them into motion. At present, however, the gap between your previous labors and the expectations of this Board remains too wide to bridge.

Pray, do not allow this intelligence to cast a permanent shadow upon your spirits. While these doors remain closed to you today, the world at large is a vast and varied landscape, offering many paths to a soul willing to transform. We suggest, with the most urgent sincerity, that you take this moment not as a finality, but as a clarion call to rediscover your industry and purpose.

Should you apply yourself with a new and steadfast devotion to your own improvement, we have no doubt that you shall eventually find a calling where your contributions will be both welcomed and celebrated. Every great man has known the sting of a closed door before finding the one that truly led to his destiny.

We remain, with a hopeful eye toward your future growth,

The Board of Admissions
 """

# Input
name = get_name("Enter Your Name: ")
Marks = get_valid_input("Enter Marks: ", 0, 100)
Entrance_exam_score = get_valid_input("Enter Entrance Score: ", 0, 100)
Extracurricular_score = get_valid_input("Enter Extracurricular Score: ", 0, 10)

# Process
status = evaluate(Marks, Entrance_exam_score, Extracurricular_score)
message = generate_message(name, status)

# Output
print("\n" + message)
