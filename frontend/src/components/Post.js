import React from 'react';
import CommentList from './CommentList';
import NewCommentForm from './NewCommentForm';

function Post({ post }) {
    return (
        <div className="Post">
            <h2>{post.title}</h2>
            <p>{post.content}</p>
            <NewCommentForm postId={post.id} />
            <CommentList postId={post.id} />
        </div>
    );
}

export default Post;
