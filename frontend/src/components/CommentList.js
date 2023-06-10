import React, { useState, useEffect } from 'react';
import Comment from './Comment';

function CommentList({ postId }) {
    const [comments, setComments] = useState([]);

    useEffect(() => {
        fetchComments();
    }, []);

    const fetchComments = async () => {
        // Replace with your actual API endpoint
        const response = await fetch(`http://localhost:5000/posts/${postId}/comments`);
        const data = await response.json();
        setComments(data);
    };

    return (
        <div className="CommentList">
            {comments.map(comment => <Comment key={comment.id} comment={comment} />)}
        </div>
    );
}

export default CommentList;
