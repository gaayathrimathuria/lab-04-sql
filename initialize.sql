CREATE TABLE users (
    user_id INT PRIMARY KEY, 
    username VARCHAR(15),
    email VARCHAR(75),
    signup_date DATETIME
);

CREATE TABLE posts(
    post_id INT PRIMARY KEY,
    user_id INT,
    caption TEXT,
    likes INT,
    post_date DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users(user_id, username, email, signup_date) VALUES
(1, 'gaayu3', 'gaayathrimathuria@example.com', '2024-07-01 15:50:00'),
(2, 'profsiller', 'ksiller@example.com', '2025-09-01 10:54:00'),
(3, 'j_doe', 'janedoe@example.com', '2025-10-03 11:03:00'),
(4, 'nsarkar', 'nishsarkar@example.com', '2024-07-01 16:49:00'),
(5, 'therealtj', 'tjefferson@example.com', '1776-07-04 08:42:00'),
(6, 'ms_rita_dove', 'ritadove@example.com', '1993-04-02 13:32:00'),
(7, 'john_doe', 'jjdoe@example.com', '2023-05-03 14:53:00'),
(8, 'notgithub', 'octocat@example.com', '2024-02-14 13:30:00'),
(9, 'charlie_brown', 'charlie@example.com', '2026-09-03 14:15:00'),
(10, 'santaclaus', 'stnicholas@example.com', '2025-12-25 12:25:00');

INSERT INTO posts(post_id, user_id, caption, likes, post_date) VALUES
(101, 1, 'Hello world! Learning SQL.', 15, '2024-07-01 15:53:00'),
(102, 1, 'This is harder than I thought.', 13, '2024-07-01 20:50:00'),
(103, 1, 'Can someone help me find a good SQL tutorial?', 17, '2024-07-02 00:23:00'),
(104, 2, 'The student that made this needs to retake my class.', 18, '2025-09-01 11:00:00'),
(105, 4, 'I love fish!', 6, '2024-07-01 17:20:00'),
(106, 5, 'We hold these truths to be self evident.', 536, '1776-07-04 09:00:00'),
(107, 1, 'I finally figured it out!', 20, '2025-07-02 09:14:00'),
(108, 8, 'Sometimes I feel like the world relies on me too much.', 871, '2025-01-01 13:52:00'),
(109, 10, 'Merry Christmas! Ho ho ho.', 1225, '2025-12-25 12:30:00'),
(110, 1, 'How come I never go viral?', 11, '2026-09-30 21:02:00');
