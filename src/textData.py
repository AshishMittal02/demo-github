import shutil
from utils import entity_filtering
# TEDS Parameters fixed
SCORE_THRESHOLD = 0.3
entities = []                   # empty if all the entities are tested
lang = "en"
def get_predictions(text):
    # prediction as well as entity filtering
    results = teds.analyze(
        text = text,
        score_threshold= SCORE_THRESHOLD,
        language = lang,
    )
    results = entity_filtering(results= results)
    return results
def get_info(text, results):
    # insights about the text and results
    print(f" Total entities found : {len(results)}")
    counter_entity = {}
    for result in results:
        # print(text[result['start']:result['end']], result['score'], result['entity_type'])
        counter_entity[result['entity_type']] = counter_entity.get(result['entity_type'], 0) + 1

    return counter_entity
text = '''
salarymen. Unfortunately, as regular RR commenter Natalie Mukka points out, "most are horrible". 
we are running a campiagn where the customer birthday falls between 11/15/1979 to 01 14 1961. 
I traded my bitcoin to Vilmundína Mota with wallet address 15kJ3aKGFcgWKVjPz1YKZyL4jK2fgwGdPJ. 
Hit me up at KatjaMoilanen@fleckens.hu. The name of the patient is 
Gijsbrecht Sasi and the doctor handling the case is female Marija Cvetka Muslija and 
medical license YE8568795. for this disease code 7578, we will require donor information 
11002 30 207416 q and their beneficiary 6cr3v63te69 number. For this disease code V4283,
 we will require donor information 20202 39 399953 G and their beneficiary 940192399007882907053 number. 
 My healthcare provider numbers are 808405114768232 and insurance TJ 02 75 74 B. 
 Hey, I want to talk to the doctor Peter Møller with DEA K90566995 licence number and taxpayer ID 2178892164428 number. I'm Ivo from Niger with my tax papers are sent via 06600369M and passport AT869936. Can you share your passport number? 08SW92892. Insurance ID is 604 143 1656 my healthcare provider numbers are 6056839429 and insurance gg 83 90 53 c. Hello Officer, as requested, here is my driver's license number 999218782176. We have backtracked the details of the device (01)5HZUM5WXQ5EHP4OE(21)GNJS9OYBW9LZYW2PYKM and patient records 58-68-66. They do not match to the associated ssn 2983449365843. Here's my SSN: 309-65-3654 I transfered money to wallet 1Cai8xeaTov7LePkfevaDVzpNeD4sF7NK8 through checking account 419007610 and routing number 26005652 My EIN 500328501 is wrong on my w2. I need to file my income tax 02378291D. We have backtracked the details of the device (01)98320183174744(11)328362 and patient records 50-78-15. They do not match to the associated ssn 6842883832662. We have processed the refund for the transactions between vat number FRdK576952451 and TVA number be06 2062 5992. my driver license is A312-032-153-620 please charge my credit card. number is 3574-2050-0062-4622 We have recieved the transactions from tva number FR1S 167 106 756 for the identification of 84328932F. Just posted a photo doughnutnews.de/sweet/glitter/xto7Wf4 The user has linked his aadhaar card 1179 3774 3718 to old pancard ZBGPS4033H. His new pan number GJKCQ1225Y is not reflecting in the system. The user has linked his aadhaar card 792780815272 to old pancard EGOAC1884D. His new pan number HKEAT8429S is not reflecting in the system. Can you share your passport number? 583168821. NC As requested these are my details Oberto van der Zaag and zapjGEI9z 3. Hey, I want to talk to the doctor Eva Marija Ibragimov with DEA U98958273 licence number and taxpayer ID 99269716976 number. we have processed the refund for the transactions between vat number frfq 226-529-642 and tva number be0264300254. The medical record number is 697997. for vendor's registered vat number de 717916191 we have following tax 41143769218 69 associated. Insurance ID is 4UW4N42PN34 How can we reach you? You can call me on my cell number 0389 0506426 Hi Ole, I'm contacting you about a problem I have with sending a wire transfer using this IBAN IL270126100000000544211 Yeah, the number on my ID is 94092639388. Hey, My tax papers were for adoption were prepared by P22302498. My vehicle details are : Name Maria Ruud, vin MB2D56X0415195850, and plate 141373. This ICD is updated from 37959 to M86.1 I have to report that my cni is wrongly put. my id is 678967639802 and it shows different taxid 14 22 132
'''
results = get_predictions(text)
get_info(text, results=results)
