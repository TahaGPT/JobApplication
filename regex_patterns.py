import re

# It's recommended to compile these for better performance if used in a loop
# For example: compiled_regex['full_name'] = re.compile(regex_patterns['full_name'], re.IGNORECASE)

regex_patterns = {
    "email": r'\b(?:e-?mail|email(?: address)?)\b',
    "password": r'\b(password|pass|secret)\b',
    "full_name": r'\b(?:full|complete|legal) name\b',
    "first_name": r'\b(?:first|given|fore) name\b',
    "last_name": r'\b(?:last|family|sur)name\b',
    "phone": r'\b(?:phone(?: no\.?| number)?|contact(?: no\.?| number)?|mobile|cell)\b',
    "address": r'\b(?:address|street(?: address)?|mailing address)\b',
    "city": r'\b(city)\b',
    "state": r'\b(?:state|province|region)\b',
    "zip_code": r'\b(?:zip|postal|post) code\b',
    "country": r'\b(country|nation)\b',
    "date_of_birth": r'\b(?:date of birth|dob|birthdate)\b',
    "nationality": r'\b(nationality)\b',
    "linkedin": r'\b(?:linkedin(?: url| profile)?)\b',
    "github": r'\b(?:github(?: url| profile)?|git)\b',
    "portfolio": r'\b(?:portfolio|website|url)\b',
    "university": r'\b(?:university|college|institution|school)\b',
    "college": r'\b(?:college|university|institution|school)\b',
    "degree": r'\b(?:degree|education|qualification)\b',
    "major": r'\b(?:major|field of study|specialization)\b',
    "minor": r'\b(minor)\b',
    "graduation_year": r'\b(?:graduat(?:ion|ed)(?: year)?|year of graduation|completion year)\b',
    "expected_graduation": r'\b(?:expected graduation(?: date| year)?|grad year)\b',
    "gpa": r'\b(?:gpa|grade point average)\b',
    "relevant_coursework": r'\b(?:relevant )?coursework\b',
    "current_position": r'\b(?:current|present) (?:position|job title|role)\b',
    "current_company": r'\b(?:current|present) (?:company|employer)\b',
    "years_experience": r'\b(?:years of )?(?:experience|exp)\b',
    "total_experience": r'\b(?:total|overall) (?:experience|exp)\b',
    "previous_company": r'\b(?:previous|past) (?:company|employer)\b',
    "previous_position": r'\b(?:previous|past) (?:position|job title|role)\b',
    "internship_experience": r'\b(?:internship|co-op) experience\b',
    "work_history": r'\b(?:work|employment) history|experience\b',
    "programming_languages": r'\b(?:programming |technical )?languages|skills\b',
    "frameworks": r'\b(frameworks|libraries)\b',
    "databases": r'\b(databases)\b',
    "tools": r'\b(tools|technologies)\b',
    "soft_skills": r'\b(?:soft|interpersonal) skills\b',
    "certifications": r'\b(certifications|licenses|credentials)\b',
    "desired_salary": r'\b(?:desired|expected) salary|salary expectations?\b',
    "salary_range_min": r'\b(?:salary|pay) (?:range|scale) min(?:imum)?\b',
    "salary_range_max": r'\b(?:salary|pay) (?:range|scale) max(?:imum)?\b',
    "work_authorization": r'\b(?:work authorization|employment eligibility|visa status)\b',
    "visa_sponsorship": r'\b(?:visa|sponsorship) (?:sponsorship|required|needed)\b',
    "willing_to_relocate": r'\b(?:willing to )?relocate\b',
    "remote_work": r'\b(?:remote|wfh|work from home)\b',
    "start_date": r'\b(?:available|earliest) start date|availability\b',
    "availability": r'\b(availability|available to start)\b',
    "notice_period": r'\bnotice period\b'
}

# Example of how to use it:
test_string = "Please enter your full name:"
if re.search(regex_patterns['full_name'], test_string, re.IGNORECASE):
    print("Found a match for 'full_name'")