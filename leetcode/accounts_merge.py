# https://leetcode.com/problems/accounts-merge/

from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_to_names = {}
        emails_graph = defaultdict(set)

        for account in accounts:
            name = account[0]
            emails = account[1:]

            if emails:
                emails_to_names[emails[0]] = name
                for email in emails[1:]:
                    emails_graph[email].add(emails[0])
                    emails_graph[emails[0]].add(email)
                    emails_to_names[email] = name

        print(emails_graph)

        # Returns a list of all emails reachable using DFS.
        def dfs(email, seen_so_far, output):
            seen_so_far.add(email)
            output.append(email)
            for connected_email in emails_graph[email]:
                if connected_email not in seen_so_far:
                    dfs(connected_email, seen_so_far, output)

        seen_so_far = set()
        output = []
        for email, name in emails_to_names.items():
            if email not in seen_so_far:
                email_list = []
                dfs(email, seen_so_far, email_list)
                output.append([name] + sorted(email_list))
        return output
