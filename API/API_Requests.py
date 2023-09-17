import requests as r
import matplotlib.pyplot as plt
from plotly.graph_objs import Bar
from plotly import offline

'''
Simple example to quickly get started with the requests package. Here we request the starts of popular Git repos.

'''
class APiRequests:
    def __init__(self, url):
        self.url = url
    def make_a_request(self):
        url = self.url
        headers = {'Accept': 'application/vnd.github.v3+json'}
        results = r.get(self.url, headers=headers)
        print(f'The Status code is {results.status_code}')
        print(f'The Status code is {results.json().keys()}')
        #Make a visualization with name of the repo and the stargazers count
        repo_dicts = results.json()['items']
        stargazers_counts, repo_links , labels=[], [] ,[]

        for repo_dict in repo_dicts:
            repo_name = repo_dict['name']
            repo_url = repo_dict['html_url']
            repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
            repo_links.append(repo_link)
            stargazers_counts.append(repo_dict['stargazers_count'])
            owner = repo_dict['owner']['login']
            description = repo_dict['description']
            label = f"{owner}<br /> -> {description}"
            labels.append(label)

        #Now plot the value
        #plt.style.use('seaborn')
        '''
        fig, ax = plt.subplots()
        ax.plot(name_of_the_repos, stargazers_counts, c='red')
        ax.set_title("Name and Stars", fontsize=24)
        ax.set_ylabel("Stars", fontsize=16)
        plt.show()
        '''
        data = [{
            'type': 'bar',
            'x': repo_links,
            'y': stargazers_counts,
            'hovertext': labels,
            'marker': {
                'color': 'rgb(60, 100, 150)',
                'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
            },
            'opacity': 0.6,
        }]
        my_layout = {
            'title': 'Most-Starred Python Projects on GitHub',
            'xaxis': {'title': 'Repository'},
            'yaxis': {'title': 'Stars'},
        }

        fig = {'data': data, 'layout': my_layout}
        offline.plot(fig, filename='python_repos.html')


api = APiRequests('https://api.github.com/search/repositories?q=language:python&sort=stars')
api.make_a_request()