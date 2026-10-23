#Exercise 1
print('first exercise Lists')
empt_list = list()
lst = ['banana', 'burger', 'hotdog,', 'mountain', 'dragon', 'car', 'plane']
print('length of list: ', len(lst))
print('first item: ', lst[0]) #or [0:1]
print('middle item: ', lst[3]) #or [3:4]
print('last item: ', lst[-1]) #or [6]

mixed_data_types = ['planet', 21, 177, 'address']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('IT companies: ', it_companies)
print('number of companies: ', len(it_companies))
print('first comapany: ', it_companies[0])
print('second company: ', it_companies[3])
print('last company: ', it_companies[-1])
it_companies[0] = 'Nvidia'
print('list after modifying: ', it_companies)
it_companies.append('Whatsapp')
it_companies.insert(4, 'Netflix')
it_companies[0] = it_companies[0].upper()
hash_list = ['#']
joined_list = it_companies + hash_list
print('does Google exist in it_companies? ', 'Google' in it_companies)
it_companies.sort()
it_companies.reverse()
nvidia_google_microsoft = it_companies[0:3]
amazong_oracle_ibm = it_companies[-1:-3]
middle_companies = it_companies[2:6]
it_companies.remove('NVIDIA')
it_companies.remove('Apple')
it_companies.pop()
it_companies.clear()
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_program_list = front_end + back_end
full_stack = joined_program_list.copy()
full_stack.insert(5, 'python',)
full_stack.insert(6, 'SQL')
print('Full Stack: ', full_stack)

#Exercise 2
print('Second Exercise math lists')
student_ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
student_ages.sort()
min_age = min(student_ages)
max_age = max(student_ages)
print('sorted student ages: ', student_ages)
print('Min Ages: ', min_age)
print('Max ages: ', max_age)
student_ages.append(19)
student_ages.append(26)
print('Sorted Age group: ', sorted(student_ages))
median_age = (24+24)/2
print('median age: ', median_age)
average_age = (sum(student_ages))/(len(student_ages))
print('Average Age: ', average_age)
range_of_age = max_age-min_age
print('range of ages: ', range_of_age)
min_age_difference = abs(min_age-average_age)
max_age_difference = abs(max_age-average_age)
print('Min Age Difference: ',min_age_difference)
print('Max Age Difference: ', max_age_difference)
#Exercise 3 
print('third exerices, Countries')
countries = [
      'Afghanistan',  'Albania',  'Algeria',  'Andorra',  'Angola',  'Antigua and Barbuda',  'Argentina',  'Armenia',  'Australia',  'Austria',  'Azerbaijan',  'Bahamas',  'Bahrain',  'Bangladesh',  'Barbados',  'Belarus',  'Belgium',  'Belize',  'Benin',  'Bhutan',  'Bolivia',  'Bosnia and Herzegovina',  'Botswana',  'Brazil',  'Brunei',  'Bulgaria',  'Burkina Faso',  'Burundi',  'Cabo Verde', 'Cambodia',  'Cameroon',  'Canada',  'Central African Republic',  'Chad',  'Chile',  'China',  'Colombia',  'Comoros',  'Congo, Democratic Republic of the',  'Congo, Republic of the',  'Costa Rica',  "Côte d'Ivoire",  'Croatia',  'Cuba',  'Cyprus',  'Czech Republic',  'Denmark',  'Djibouti',  'Dominica',  'Dominican Republic',  'East Timor (Timor-Leste)',  'Ecuador',  'Egypt',  'El Salvador',  'Equatorial Guinea',  'Eritrea',  'Estonia',  'Eswatini',  'Ethiopia',  'Fiji',  'Finland',  'France',  'Gabon',  'Gambia',  'Georgia',  'Germany',  'Ghana',  'Greece',  'Grenada',  'Guatemala',  'Guinea',  'Guinea-Bissau',  'Guyana',  'Haiti',  'Honduras',  'Hungary',  'Iceland',  'India',  'Indonesia',  'Iran',  'Iraq',  'Ireland',  'Israel',  'Italy',  'Jamaica',  'Japan',  'Jordan',  'Kazakhstan',  'Kenya',  'Kiribati',  'Korea, North',  'Korea, South',  'Kuwait',  'Kyrgyzstan',  'Laos',  'Latvia',  'Lebanon',  'Lesotho',  'Liberia',  'Libya',  'Liechtenstein',  'Lithuania',  'Luxembourg',  'Madagascar',  'Malawi',  'Malaysia',  'Maldives',  'Mali',  'Malta',  'Marshall Islands',  'Mauritania',  'Mauritius',  'Mexico',  'Micronesia',  'Moldova',  'Monaco',  'Mongolia',  'Montenegro',  'Morocco',  'Mozambique',  'Myanmar',  'Namibia',  'Nauru',  'Nepal',  'Netherlands',  'New Zealand',  'Nicaragua',  'Niger',  'Nigeria',  'North Macedonia',  'Norway',  'Oman',  'Pakistan',  'Palau',  'Palestine',  'Panama',  'Papua New Guinea',  'Paraguay',  'Peru',  'Philippines',  'Poland',  'Portugal',  'Qatar',  'Romania',  'Russia',  'Rwanda',  'Saint Kitts and Nevis',  'Saint Lucia',  'Saint Vincent and the Grenadines',  'Samoa',  'San Marino',  'Sao Tome and Principe',  'Saudi Arabia',  'Senegal',  'Serbia',  'Seychelles',  'Sierra Leone',  'Singapore',  'Slovakia',  'Slovenia',  'Solomon Islands',  'Somalia',  'South Africa',  'South Sudan', 'Spain', 'Sri Lanka',  'Sudan',  'Suriname', 'Sweden',  'Switzerland',  'Syria',  'Tajikistan',  'Tanzania', 'Thailand',  'Togo',  'Tonga',  'Trinidad and Tobago',  'Tunisia',  'Turkey', 'Turkmenistan',  'Tuvalu',  'Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe'
]
print('Number Of Countries: ', len(countries))
middle_country = int(len(countries)//2) +1
print('Middle Country: ', middle_country)
first_half = countries[0:98]
second_half = countries[98:]
print('first half: ', len(first_half))
print('second half: ', len(second_half))

unpack_country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = unpack_country
print(china, russia, usa, 'now scandic', scandic)

# Day 5 Complete w wish me luck guys