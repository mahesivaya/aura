PGDMP       3                |           postgres    16.3    16.3 	               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            	           1262    5    postgres    DATABASE     j   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
    DROP DATABASE postgres;
                postgres    false            
           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3593                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false                       0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            �            1259    16409    aurapatients    TABLE       CREATE TABLE public.aurapatients (
    firstname character varying(255),
    lastname character varying(255),
    age integer,
    address character varying(255),
    phonenumber integer,
    dateregistered timestamp without time zone DEFAULT now() NOT NULL
);
     DROP TABLE public.aurapatients;
       public         heap    postgres    false                      0    16409    aurapatients 
   TABLE DATA           f   COPY public.aurapatients (firstname, lastname, age, address, phonenumber, dateregistered) FROM stdin;
    public          postgres    false    216   C          �   x�]���0@��

�̲?qI�����Ȍ9`b��Q�ޛ�'���i�@iJ��` $�1�uE�ȣWb�����Vj۞�#^K�����j��9�E������J.y�@�����hJ9��`�ݼs�m�*:     