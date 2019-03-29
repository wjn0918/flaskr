drop table if exists user;
drop table if exists post;

create table user(
  id integer auto_increment,
  username text not null,
  password text not null,
  primary key(id)
);
create table post(
  id integer auto_increment,
  author_id integer not null,
  created timestamp null default current_timestamp on update current_timestamp,
  title text not null,
  body text not null,
  primary key(id)
);
