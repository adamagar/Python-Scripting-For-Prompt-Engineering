from bs4 import BeautifulSoup
import requests

url = "https://www.python.org/jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.title

print(title)

meta_tag = soup.find('meta', attrs={'name': 'description'})

meta_description = meta_tag.get("content")

print(meta_description)

job_posts = soup.find_all('h2', class_='listing-company')

for job_post in job_posts:
	title = job_post.a.text
	print(title)