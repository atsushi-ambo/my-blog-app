import React, { useState } from 'react';

function NewCommentForm({ postId }) {
    const [content, setContent] = useState('');

    const handleSubmit = async event => {
        event.preventDefault();
        // Replace with your actual API endpoint
        const response = await fetch(`http://localhost:5000/posts/${postId}/comments`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ content }),
        });
        const data = await response.json();
        console.log(data);
    };

    return (
        <form onSubmit={handleSubmit}>
            <textarea value={content} onChange={e => setContent(e.target.value)} placeholder="Comment" required />
            <button type="submit">Add Comment</button>
        </form>
    );
}

export default NewCommentForm;
