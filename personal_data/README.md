# Personal Data in Python, PII and non-PII

- The re.sub() function belongs to the Regular Expressions (re) module in Python. It returns a string where all matching occurrences of the specified pattern are replaced by the replace string. To use this function, we need to import the re module first.

import re
The re.sub() function stands for a substring and returns a string with replaced values. Multiple elements can be replaced using a list when we use this function.

Syntax
re.sub(pattern, repl, string, count=0, flags=0)

- According to NIST, PII can be divided into two categories: linked and linkable information.

- Linked information is more direct. It could include any personal detail that can be used to identify an individual. Examples of this kind of PII include:

Full name
Home address
Email address
Social security number
Passport number
Driver’s license number
Credit card numbers
Date of birth
Telephone number
Owned properties e.g. vehicle identification number (VIN)
Login details
Processor or device serial number*
Media access control (MAC)*
Internet Protocol (IP) address*
Device IDs*
Cookies*

- Linkable information is indirect and on its own may not be able to identify a person, but when combined with another piece of information could identify, trace or locate a person.

Here are some examples of PII that can be considered linkable information:

First or last name (if common)
Country, state, city, zip code
Gender
Race
Non-specific age (e.g. 30-40 instead of 30)
Job position and workplace

- Non-personally identifiable information (non-PII) is data that cannot be used on its own to trace, or identify a person.Examples of non-PII include, but are not limited to:

Aggregated statistics on the use of product / service
Partially or fully masked IP addresses
However, the classification of PII and non-PII is vague. Moreover, NIST doesn’t reference cookie IDs and device IDs, so many AdTech companies, advertisers, and publishers consider them as non-PII. As we’ll see, this is in contrast to the definition of personal data, which treats such digital tackers as information that could identify an individual.

- src: https://piwik.pro/blog/what-is-pii-personal-data/#what-is-personally-identifiable-information-(pii)?