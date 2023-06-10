import React, { useState } from 'react';

function NewPostForm() {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    const handleSubmit = async event => {
        event.preventDefault();
        // Replace with your actual API endpoint
        const response = await fetch('http://localhost:5000/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, content }),
        });
        const data = await response.json();
        console.log(data);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={title} onChange={e => setTitle(e.target.value)} placeholder="Title" required />
            <textarea value={content} onChange={e => setContent(e.target.value)} placeholder="Content" required />
            <button type="submit">Create Post</button>
        </form>
    );
}

export default NewPostForm;
