--
-- PostgreSQL database dump
--

-- Dumped from database version 15.7
-- Dumped by pg_dump version 15.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    order_id integer NOT NULL,
    order_name character varying(150) NOT NULL,
    description character varying(2000) NOT NULL,
    creation_date timestamp without time zone NOT NULL,
    status character varying(12) NOT NULL
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- Name: orders_order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_order_id_seq OWNER TO postgres;

--
-- Name: orders_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;


--
-- Name: orders order_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (order_id, order_name, description, creation_date, status) FROM stdin;
1	Audi RS3 - order 1	Client ordered the RS3 model in standard configuration. Color: red.	2024-06-23 15:59:45	New
2	Audi RS3 - order 2	Client ordered the RS3 model in standard configuration. Color: red.	2024-06-23 16:03:30	New
3	Audi A4 - order 2	Client ordered the A4 model in standard configuration. Color: white.	2024-06-23 16:05:43	In Progress
5	Audi SQ5 - order 5	Client ordered the SQ5 model in standard configuration. Color: black.	2024-06-23 16:09:25	In Progress
6	Audi Q7 - order 6	Client ordered the Q7 model in standard configuration. Color: silver.	2024-06-23 16:11:22	Completed
4	Audi A3 - order 4	Client ordered the A3 model in standard configuration. Color: white.	2024-06-23 16:07:49	Completed
7	Audi Q8 - order 7	Client ordered the Q8 model in standard configuration. Color: gold.	2024-06-23 15:59:45	In Progress
8	Audi A5 - order 8	Client ordered the A5 model in s-line configuration. Color: green.	2024-06-23 16:11:22	New
9	Audi A4 - order 9	Client ordered the A4 model in s-line configuration. Color: blue.	2024-06-24 22:12:49	New
10	Audi A4 - order 10	Client ordered the A4 model in s-line configuration. Color: yellow.	2024-06-24 22:12:49	New
11	Audi R8 - order 11	Client ordered the R8 model in standard configuration. Color: red.	2024-06-24 22:12:49	In Progress
12	Audi RS7 - order 12	Client ordered the RS7 model in standard configuration. Color: black.	2024-06-24 22:12:49	In Progress
13	Audi RS6 - order 13	Client ordered the RS6 model in standard configuration. Color: green.	2024-06-24 23:06:31	New
\.


--
-- Name: orders_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_order_id_seq', 1, false);


--
-- Name: orders orders_order_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_order_name_key UNIQUE (order_name);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- PostgreSQL database dump complete
--

