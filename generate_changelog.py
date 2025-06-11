#!/usr/bin/env python3
import subprocess
from datetime import datetime
import re

def get_git_log():
    """Get git log in a structured format"""
    cmd = [
        'git', 'log', '--pretty=format:%H|%an|%ad|%s',
        '--date=short',
        '--no-merges'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.split('\n')

def parse_commits(log_lines):
    """Parse commit messages into structured data"""
    commits = []
    for line in log_lines:
        if not line:
            continue
        parts = line.split('|', 3)
        if len(parts) == 4:
            commits.append({
                'hash': parts[0],
                'author': parts[1],
                'date': parts[2],
                'message': parts[3]
            })
    return commits

def group_by_type(commits):
    """Group commits by conventional commit type"""
    groups = {
        'feat': [],
        'fix': [],
        'docs': [],
        'style': [],
        'refactor': [],
        'perf': [],
        'test': [],
        'chore': [],
        'other': []
    }
    
    pattern = re.compile(r'^(\w+)(\([^)]+\))?: (.+)$')
    
    for commit in commits:
        match = pattern.match(commit['message'])
        if match:
            commit_type = match.group(1)
            scope = match.group(2) or ''
            message = match.group(3)
            
            if commit_type in groups:
                groups[commit_type].append({
                    'scope': scope,
                    'message': message,
                    'hash': commit['hash'][:7],
                    'author': commit['author'],
                    'date': commit['date']
                })
            else:
                groups['other'].append({
                    'scope': scope,
                    'message': message,
                    'hash': commit['hash'][:7],
                    'author': commit['author'],
                    'date': commit['date']
                })
        else:
            groups['other'].append({
                'scope': '',
                'message': commit['message'],
                'hash': commit['hash'][:7],
                'author': commit['author'],
                'date': commit['date']
            })
    
    return groups

def generate_changelog(groups, version):
    """Generate markdown changelog"""
    changelog = f"# {version}\n\n"
    changelog += f"*Released on {datetime.now().strftime('%Y-%m-%d')}*\n\n"
    
    type_titles = {
        'feat': 'Features',
        'fix': 'Bug Fixes',
        'docs': 'Documentation',
        'style': 'Code Style',
        'refactor': 'Refactors',
        'perf': 'Performance',
        'test': 'Tests',
        'chore': 'Chores',
        'other': 'Other Changes'
    }
    
    for type_key in ['feat', 'fix', 'docs', 'refactor', 'perf', 'test', 'chore', 'other']:
        if groups[type_key]:
            changelog += f"## {type_titles[type_key]}\n\n"
            for item in groups[type_key]:
                scope = f" **{item['scope'][1:-1]}**:" if item['scope'] else ""
                changelog += f"-{scope} {item['message']} ({item['hash']})\n"
            changelog += "\n"
    
    return changelog

if __name__ == "__main__":
    version = subprocess.run(
        ['git', 'describe', '--tags', '--abbrev=0'],
        capture_output=True, text=True
    ).stdout.strip()
    
    log = get_git_log()
    commits = parse_commits(log)
    grouped = group_by_type(commits)
    changelog = generate_changelog(grouped, version)
    
    with open('CHANGELOG.md', 'w') as f:
        f.write(changelog)
    
    print("Changelog generated successfully!")
