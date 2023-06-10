import React from 'react';

function Comment({ comment }) {
    return (
        <div className="Comment">
            <p>{comment.content}</p>
        </div>
    );
}

export default Comment;
