const REPO_OWNER = 'gcf0082';
const REPO_NAME = 'hn_insights';
const BRANCH = 'master';
const INSIGHTS_PATH = 'insights';

const API_URL = `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contents/${INSIGHTS_PATH}`;
const RAW_BASE_URL = `https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${BRANCH}/${INSIGHTS_PATH}`;

let allPosts = [];
let currentFilter = 'all';

async function fetchPosts() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const files = await response.json();
        
        allPosts = files
            .filter(f => f.type === 'file' && f.name.endsWith('.md'))
            .map(f => parseFileName(f.name, f.sha))
            .sort((a, b) => b.timestamp - a.timestamp);
        
        renderList();
    } catch (err) {
        document.getElementById('post-list').innerHTML = 
            `<div class="error">加载失败: ${err.message}</div>`;
    }
}

function parseFileName(filename, sha) {
    const nameWithoutExt = filename.replace(/\.md$/, '');
    const parts = nameWithoutExt.split('_');
    
    const dateStr = parts[0] || '';
    const timeStr = parts[1] || '';
    const id = parts[2] || '';
    const type = parts[3] || '';
    
    const year = dateStr.slice(0, 4);
    const month = dateStr.slice(4, 6);
    const day = dateStr.slice(6, 8);
    const hour = timeStr.slice(0, 2);
    const minute = timeStr.slice(2, 4);
    const second = timeStr.slice(4, 6);
    
    const timestamp = new Date(`${year}-${month}-${day}T${hour}:${minute}:${second}`).getTime();
    const formattedDate = `${year}-${month}-${day} ${hour}:${minute}`;
    
    let title = '';
    if (parts.length > 4) {
        title = parts.slice(4).join('_');
    }
    
    return {
        filename,
        date: formattedDate,
        timestamp: timestamp || 0,
        id,
        type: type.toLowerCase(),
        title: title || `Insight ${id}`,
        sha
    };
}

function renderList() {
    const container = document.getElementById('post-list');
    const filteredPosts = currentFilter === 'all' 
        ? allPosts 
        : allPosts.filter(p => p.type === currentFilter);
    
    if (filteredPosts.length === 0) {
        container.innerHTML = '<div class="loading">暂无内容</div>';
        return;
    }
    
    container.innerHTML = filteredPosts.map(post => `
        <div class="post-item type-${post.type}" data-filename="${post.filename}">
            <div class="post-header">
                <span class="post-date">${post.date}</span>
                <span class="post-type ${post.type}">${post.type.toUpperCase()}</span>
            </div>
            <div class="post-title">${escapeHtml(post.title)}</div>
        </div>
    `).join('');
    
    container.querySelectorAll('.post-item').forEach(item => {
        item.addEventListener('click', () => showDetail(item.dataset.filename));
    });
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

async function showDetail(filename) {
    const listView = document.getElementById('list-view');
    const detailView = document.getElementById('detail-view');
    const content = document.getElementById('post-content');
    
    listView.classList.add('hidden');
    detailView.classList.remove('hidden');
    content.innerHTML = '<div class="loading">加载中...</div>';
    
    try {
        const url = `${RAW_BASE_URL}/${encodeURIComponent(filename)}`;
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const markdown = await response.text();
        
        marked.setOptions({
            breaks: true,
            gfm: true,
            highlight: function(code, lang) {
                if (lang && hljs.getLanguage(lang)) {
                    return hljs.highlight(code, { language: lang }).value;
                }
                return hljs.highlightAuto(code).value;
            }
        });
        content.innerHTML = marked.parse(markdown);
    } catch (err) {
        content.innerHTML = `<div class="error">加载失败: ${err.message}</div>`;
    }
}

function showList() {
    document.getElementById('list-view').classList.remove('hidden');
    document.getElementById('detail-view').classList.add('hidden');
}

document.addEventListener('DOMContentLoaded', () => {
    fetchPosts();
    
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentFilter = btn.dataset.type;
            renderList();
        });
    });
    
    document.getElementById('back-btn').addEventListener('click', showList);
});

window.addEventListener('hashchange', () => {
    const hash = window.location.hash.slice(1);
    if (hash && hash.endsWith('.md')) {
        showDetail(hash);
    } else {
        showList();
    }
});