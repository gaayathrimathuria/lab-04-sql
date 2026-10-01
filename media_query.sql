SELECT users.username, users.email, posts.caption, posts.likes, posts.post_date 
FROM users JOIN posts ON users.user_id = posts.user_id
WHERE posts.likes > 10;

