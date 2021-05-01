import React, { Component } from 'react';

class Feed extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
          posts: JSON.parse(localStorage.getItem('posts')) || [],
          filteredPosts: []
        }
    
        this.handleNewPost = this.handleNewPost.bind(this);
        this.handleFilter = this.handleFilter.bind(this);
    }
  
    handleNewPost(post) {
        var posts = this.state.posts.concat([post]);
        this.setState({posts: posts});
        localStorage.setItem('posts', JSON.stringify(posts));      
    }
  
    render() {
      const posts = this.state.posts.map((post, index) =>
        <Post key={index} value={post} />
      );
      return (
        <div className="feed">
          {posts}
          <PostForm onSubmit={this.handleNewPost} />
        </div>
      )
    }
  }
  
  
  

export default Feed;