drop table if exists user;
drop table if exists post;

create table user(
  id int auto_increment,
  username varchar(10) not null,
  password varchar(20) not null,
  primary key(id)
);

create table post(
  id int auto_increment,
  author_id int not null,
  created timestamp null default current_timestamp on update current_timestamp,
  title varchar(20) not null,
  body varchar(255) not null,
  primary key(id)
);
