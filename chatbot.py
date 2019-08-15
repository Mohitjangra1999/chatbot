from nltk.chat.util import Chat, reflections
pairs = [
    [ r"my name is (.*)",
        ["Hello %1, How are you today ?"]
    ],
    [
     r"(.*)(smdp|SMDP|smdpc2sd|SMDP2SD|SMDP-C2SD)(.*)",
     ["SMDP is a programme initiated under Digital India Program Institutions.For more information click on 'About' button."]
     ],
    [
     r"(.*)(job|vacancy|requirement|work)(.*)",
     ["For %2 at SMDP:\n1.Go to 'Vacancy' button\n2.Read about different position requirements\n3.Apply  at relevant position"]
     ],
     [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot ?"]
    ],
    [r'what do you do(.*)',
     [ "I am here to help you.",
       "I chat to help you."]],
     [
      r"who are you(.*)",
      ["i am a chatbot to help  you.","i am chatty to help you."]
     ],
     [r'How are you(.*)',
     [ "I am fine. Thank You. How are you?",
       "I am fine. How about you?",
       "Fine. Thank You. How about you?"]
     ],
     [
      r"i am (fine|good|nice)",
      ["Good to hear you."]
     ],
    [
        r"(.*)sorry(.*)",
        ["Its alright","Its OK, never mind"]
    ],
    [
        r"(.*)(created|built|made)(.*)",
        ["Mohit created me using Python's NLTK library.","it's a secret :)",]
    ],
    [
     r"(.*)(thanks|thank|thank you)(.*)",
     ["It's my duty to  help you","it's my pleasure to help you."]
     ],
    [
        r"i am (.*)",
        ["Nice to hear you %1","Alright :)"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hi dear"]
    ],
    [
     r"(.*)help(.*)",
     ["what do you need, please ask specifically" ]
     ],
    [
     r"(.*)(internship|intern|training)(.*)",
     ["SMDP offers three types of internships:\n1.Intel\n2.Menter\n3.NXP\nFor applying or getting information click on  intership button on homepage and go into required section."]
     ],
    
    [
     r"(.*)chatty(.*)",
     ["I am bot to help you."]
     ],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
[
 r"(.*)(institutes|institute)(.*)",
 ["For knowing about institutes under smdp:\n1.Go to home screen\n2.Click on C2SD link \n3.Go to Institutes section"]
 ],
[r"(.*)(investigators|Investigators|Investigator|investigator)(.*)",
 ["For knowing about investigators :\n1.Go to home screen\n2.Click on C2SD link \n3.Go to Investigators section"]
 ],
[r"(.*)(Technical Advisory Committee)(.*)",
 ["For knowing about TAC :\n1.Go to home screen\n2.Click on C2SD link button \n3.Go to TAC members section"]
 ],
[r"(.*)(National Steering Committee|NSC)(.*)",
 ["For knowing about NSC :\n1.Go to home screen\n2.Click on C2SD link button \n3.Go to NSC members section"]
 ],
[r"(.*)Resources(.*)",
 ["For knowing about Resources :\n1.Go to home screen\n2.Click on Resources link button\n3.Select required section on list"]
 ],
[r"(.*)(Instruction Enhancement Programmes|IEP)(.*)",
 ["For knowing about IEP :\n1.Go to home screen\n2.Click on resources link button \n3.Go to IEP section"]
 ],
[r"(.*)(International Guest Faculty Lectures)(.*)",
 ["For knowing about Guest Faculty Lectures:\n1.Go to home screen\n2.Click on resources link button \n3.Go to International Guest Faculty Lectures section"]
 ],
[r"(.*)(Short Term Courses|Cources)(.*)",
 ["For knowing about Short Term Courses:\n1.Go to home screen\n2.Click on resources link button \n3.Go to Short term cources section"]
 ],
[r"(.*)(Model Syllabus|Syllabus)(.*)",
 ["To download model syllabus:\n1.Go to home screen\n2.Click on resources link button \n3.Go to model syllabus section and download."]
 ],
[r"(.*)(Designs|Design)(.*)",
 ["For knowing about design submission:\n1.Go to home screen\n2.Click on 10BestDesigns\n3.Submit your design"]
 ],
[r"(.*)(Contact)(.*)",
 ["To contact SMDP project leaders:\n1.Go to home screen\n2.Click on contact link button"]
 ],
[r"(.*)Login(.*)",
 ["To LogIn into SMDP:\n1.From the top menu, click on Login .\n2.Enter username and password\n3.Then click on Sign In"
  ]
 ],
[ r".*",
 ["please ask relevant questions."]
 ]
]
def chatty():
    print("Hi, I am Chatty, your Personal Digital Assistant. I can try to help you in getting answer to your queries related to SMDP.")
    chat = Chat(pairs, reflections)
    chat.converse()
chatty()
