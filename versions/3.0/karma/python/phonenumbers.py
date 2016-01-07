us_area_codes = ["211", "242", "246", "264", "268", "284", "311", "345", "411", "441", "456", "473", "500", "511", "555", "600", "611", "649", "664", "684", "700", "710", "711", "758", "767", "784", "800", "809", "811", "822", "829", "833", "844", "849", "855", "866", "868", "869", "876", "877", "880", "881", "882", "888", "898", "900", "911", "976", "999", "52 55", "403", "587", "780", "825", "907", "205", "251", "256", "334", "479", "501", "870", "480", "520", "602", "623", "928", "236", "250", "604", "778", "209", "213", "310", "323", "341", "369", "408", "415", "424", "442", "510", "530", "559", "562", "619", "626", "627", "628", "650", "657", "661", "669", "707", "714", "747", "760", "764", "805", "818", "831", "858", "909", "916", "925", "935", "949", "951", "303", "719", "720", "970", "203", "475", "860", "959", "202", "302", "239", "305", "321", "352", "386", "407", "561", "689", "727", "754", "772", "786", "813", "850", "863", "904", "927", "941", "954", "229", "404", "470", "478", "678", "706", "762", "770", "912", "671", "808", "319", "515", "563", "641", "712", "208", "217", "224", "309", "312", "331", "464", "618", "630", "708", "773", "779", "815", "847", "872", "219", "260", "317", "574", "765", "812", "316", "620", "785", "913", "270", "502", "606", "859", "225", "318", "337", "504", "985", "339", "351", "413", "508", "617", "774", "781", "857", "978", "204", "431", "240", "301", "410", "443", "207", "231", "248", "269", "278", "313", "517", "586", "616", "679", "734", "810", "906", "947", "989", "218", "320", "507", "612", "651", "763", "952", "314", "417", "557", "573", "636", "660", "816", "975", "670", "228", "601", "662", "769", "406", "506", "252", "336", "704", "828", "910", "919", "980", "984", "701", "308", "402", "603", "201", "551", "609", "732", "848", "856", "862", "908", "973", "709", "505", "575", "957", "782", "902", "702", "775", "212", "315", "347", "516", "518", "585", "607", "631", "646", "716", "718", "845", "914", "917", "216", "234", "283", "330", "380", "419", "440", "513", "567", "614", "740", "937", "405", "539", "580", "918", "226", "289", "343", "365", "416", "437", "519", "548", "613", "647", "705", "807", "905", "503", "541", "971", "215", "267", "412", "484", "570", "610", "717", "724", "814", "835", "878", "787", "939", "418", "438", "450", "481", "514", "579", "819", "873", "401", "803", "843", "864", "605", "306", "639", "423", "615", "731", "865", "901", "931", "210", "214", "254", "281", "325", "361", "409", "430", "432", "469", "512", "682", "713", "737", "806", "817", "830", "832", "903", "915", "936", "940", "956", "972", "979", "385", "435", "801", "276", "434", "540", "571", "703", "757", "804", "340", "802", "206", "253", "360", "425", "509", "564", "262", "414", "608", "715", "920", "304", "681", "307", "867"]
                 
def isUSAreaCode(phonenumber):
    areacode = phonenumber[0:3]
    if areacode in us_area_codes:
        return True
    return False


def phoneExchange(phonenumber):
    "Return the first six digits of a phone if it is a 10-digit USA phone, ie, starts with 1-."
    result = ''
    if phonenumber.startswith("+1-"):
        tenDigitPhone = phonenumber[3:]
        if tenDigitPhone.isdigit() and len(tenDigitPhone.decode("utf-8")) == 10:
            result = tenDigitPhone[0:6]
    else:
        if phonenumber.isdigit() and len(phonenumber.decode("utf-8")) == 10:
            if isUSAreaCode(phonenumber):
                result = phonenumber[0:6]
    return result



def getPhoneCountryCode(phone_clean):
    idx = phone_clean.find("-")
    if idx != -1:
        cc = phone_clean[0:idx]
        if cc.startswith("+"):
            cc = cc[1:]
        return cc
    return ''

def getLocalPhoneNumber(phone_clean):
    idx = phone_clean.find("-")
    if idx != -1:
        return phone_clean[idx+1:]
    return phone_clean

