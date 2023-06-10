import React, { useState, useEffect } from 'react';
import PostList from './PostList';
import NewPostForm from './NewPostForm';

function App() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        // Fetch posts from API and update state
        fetchPosts();
    }, []);

    const fetchPosts = async () => {
        // Replace with your actual API endpoint
        const response = await fetch('http://localhost:5000/posts');
        const data = await response.json();
        setPosts(data);
    };

    return (
        <div className="App">
            <h1>My Blog App</h1>
            <NewPostForm />
            <PostList posts={posts} />
        </div>
    );
}

export default App;
