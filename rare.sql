CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  "created_on" date,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 1) ;
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO Reactions ('label', 'image_url') VALUES ('angry', 'https://pngtree.com/so/angry');
INSERT INTO Posts ('user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved') VALUES (1, 1, 'Title', 1, 'image', 'content', null);
INSERT INTO Users VALUES (1, "Ricky", "Spanish", 'ricky@spanish.com', "Here's my bio", "ricky", "password", "null", "20211025", 0);
INSERT INTO Users VALUES (2, "Isla", "Fischer", 'Isla@fischer.com', "Here's my bio", "isla", "isla", "null", "20211025", 0);

SELECT *
FROM Categories

INSERT INTO Posts VALUES (null, 2, 1, "alien 21", "10/25/2021", null, "IT WAS ALIENS!!!!!", true);
INSERT INTO Posts VALUES (null, 2, 2, "alien 2", "10/25/2021", null, "IT WAS ALIENS!!!!!", true);

INSERT INTO Comments Values (null, 1, 3, "Thanks for calling the petey pablo hotline.");
INSERT INTO Comments Values (null, 1, 3, "Thanks for calling the petey pablo hotline.", 10/24/2021);
INSERT INTO Comments Values (null, 1, 1, "Thanks for calling the petey pablo hotline.", 10242021);

INSERT INTO Categories ('label') VALUES ('Sports')
INSERT INTO Categories ('label') VALUES ('Science')
INSERT INTO Categories ('label') VALUES ('Tech')

ALTER TABLE Comments 
ADD COLUMN created_on DATE;

SELECT *
FROM Users;

SELECT *
FROM Posts;

SELECT *
FROM Comments;

SELECT *
FROM Tags;
SELECT *
FROM PostTags;

