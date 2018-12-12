--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.15
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-1.pgdg14.04+1)

-- Started on 2018-12-12 16:09:02 CET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 9 (class 2615 OID 94914)
-- Name: d; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA d;


ALTER SCHEMA d OWNER TO postgres;

--
-- TOC entry 1 (class 3079 OID 11893)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 3450 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- TOC entry 2 (class 3079 OID 93516)
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- TOC entry 3451 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry, geography, and raster spatial types and functions';


--
-- TOC entry 1783 (class 1247 OID 97039)
-- Name: holder; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.holder AS (
	geom public.geometry
);


ALTER TYPE public.holder OWNER TO postgres;

--
-- TOC entry 1350 (class 1255 OID 97050)
-- Name: fibonacci(integer); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.fibonacci(n integer) RETURNS text
    LANGUAGE plpgsql
    AS $$ 
DECLARE
   counter INTEGER := 0 ; 
   i TEXT; 
   j INTEGER := 1 ;
BEGIN
 
 IF (n < 1) THEN
 RETURN 0 ;
 END IF; 
 
 WHILE counter <= n LOOP
 counter := counter + 1 ; 
 SELECT geom from d.point where gid = counter;
 END LOOP ; 
 
 RETURN i ;
END ;
$$;


ALTER FUNCTION public.fibonacci(n integer) OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 193 (class 1259 OID 94959)
-- Name: point; Type: TABLE; Schema: d; Owner: postgres
--

CREATE TABLE d.point (
    gid integer NOT NULL,
    longitude double precision,
    latitude double precision,
    cp_file_name character varying,
    address character varying DEFAULT 'No address'::character varying,
    geom public.geometry(Point,4326),
    created_at timestamp without time zone DEFAULT now(),
    fk_trash_type integer
);


ALTER TABLE d.point OWNER TO postgres;

--
-- TOC entry 192 (class 1259 OID 94957)
-- Name: point_gid_seq; Type: SEQUENCE; Schema: d; Owner: postgres
--

CREATE SEQUENCE d.point_gid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE d.point_gid_seq OWNER TO postgres;

--
-- TOC entry 3452 (class 0 OID 0)
-- Dependencies: 192
-- Name: point_gid_seq; Type: SEQUENCE OWNED BY; Schema: d; Owner: postgres
--

ALTER SEQUENCE d.point_gid_seq OWNED BY d.point.gid;


--
-- TOC entry 197 (class 1259 OID 95416)
-- Name: remove_access; Type: TABLE; Schema: d; Owner: postgres
--

CREATE TABLE d.remove_access (
    id integer NOT NULL,
    acess_type character varying
);


ALTER TABLE d.remove_access OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 95414)
-- Name: remove_access_id_seq; Type: SEQUENCE; Schema: d; Owner: postgres
--

CREATE SEQUENCE d.remove_access_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE d.remove_access_id_seq OWNER TO postgres;

--
-- TOC entry 3453 (class 0 OID 0)
-- Dependencies: 196
-- Name: remove_access_id_seq; Type: SEQUENCE OWNED BY; Schema: d; Owner: postgres
--

ALTER SEQUENCE d.remove_access_id_seq OWNED BY d.remove_access.id;


--
-- TOC entry 195 (class 1259 OID 95405)
-- Name: trash_type; Type: TABLE; Schema: d; Owner: postgres
--

CREATE TABLE d.trash_type (
    id integer NOT NULL,
    trash character varying
);


ALTER TABLE d.trash_type OWNER TO postgres;

--
-- TOC entry 194 (class 1259 OID 95403)
-- Name: trash_type_id_seq; Type: SEQUENCE; Schema: d; Owner: postgres
--

CREATE SEQUENCE d.trash_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE d.trash_type_id_seq OWNER TO postgres;

--
-- TOC entry 3454 (class 0 OID 0)
-- Dependencies: 194
-- Name: trash_type_id_seq; Type: SEQUENCE OWNED BY; Schema: d; Owner: postgres
--

ALTER SEQUENCE d.trash_type_id_seq OWNED BY d.trash_type.id;


--
-- TOC entry 191 (class 1259 OID 94922)
-- Name: user; Type: TABLE; Schema: d; Owner: postgres
--

CREATE TABLE d."user" (
    gid integer NOT NULL,
    email character varying NOT NULL,
    encrypted_password character varying NOT NULL,
    remove_access boolean DEFAULT false,
    fk_request_access integer DEFAULT 3,
    confirmed boolean DEFAULT false
);


ALTER TABLE d."user" OWNER TO postgres;

--
-- TOC entry 190 (class 1259 OID 94920)
-- Name: user_gid_seq; Type: SEQUENCE; Schema: d; Owner: postgres
--

CREATE SEQUENCE d.user_gid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE d.user_gid_seq OWNER TO postgres;

--
-- TOC entry 3455 (class 0 OID 0)
-- Dependencies: 190
-- Name: user_gid_seq; Type: SEQUENCE OWNED BY; Schema: d; Owner: postgres
--

ALTER SEQUENCE d.user_gid_seq OWNED BY d."user".gid;


--
-- TOC entry 200 (class 1259 OID 97053)
-- Name: bbox; Type: TABLE; Schema: public; Owner: desweb
--

CREATE TABLE public.bbox (
    gid integer NOT NULL,
    id integer,
    geom public.geometry(MultiPolygon,4326)
);


ALTER TABLE public.bbox OWNER TO desweb;

--
-- TOC entry 199 (class 1259 OID 97051)
-- Name: bbox_gid_seq; Type: SEQUENCE; Schema: public; Owner: desweb
--

CREATE SEQUENCE public.bbox_gid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bbox_gid_seq OWNER TO desweb;

--
-- TOC entry 3456 (class 0 OID 0)
-- Dependencies: 199
-- Name: bbox_gid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: desweb
--

ALTER SEQUENCE public.bbox_gid_seq OWNED BY public.bbox.gid;


--
-- TOC entry 3293 (class 2604 OID 94962)
-- Name: point gid; Type: DEFAULT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d.point ALTER COLUMN gid SET DEFAULT nextval('d.point_gid_seq'::regclass);


--
-- TOC entry 3297 (class 2604 OID 95419)
-- Name: remove_access id; Type: DEFAULT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d.remove_access ALTER COLUMN id SET DEFAULT nextval('d.remove_access_id_seq'::regclass);


--
-- TOC entry 3296 (class 2604 OID 95408)
-- Name: trash_type id; Type: DEFAULT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d.trash_type ALTER COLUMN id SET DEFAULT nextval('d.trash_type_id_seq'::regclass);


--
-- TOC entry 3289 (class 2604 OID 94925)
-- Name: user gid; Type: DEFAULT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d."user" ALTER COLUMN gid SET DEFAULT nextval('d.user_gid_seq'::regclass);


--
-- TOC entry 3298 (class 2604 OID 97056)
-- Name: bbox gid; Type: DEFAULT; Schema: public; Owner: desweb
--

ALTER TABLE ONLY public.bbox ALTER COLUMN gid SET DEFAULT nextval('public.bbox_gid_seq'::regclass);


--
-- TOC entry 3435 (class 0 OID 94959)
-- Dependencies: 193
-- Data for Name: point; Type: TABLE DATA; Schema: d; Owner: postgres
--

COPY d.point (gid, longitude, latitude, cp_file_name, address, geom, created_at, fk_trash_type) FROM stdin;
209	9.35013359999999949	48.6616037000000006		Falkenwasenwiesen,  Unterensingen,  Vereinbarte Verwaltungsgemeinschaft der Stadt Nürtingen,  Landkreis Esslingen,  Regierungsbezirk Stuttgart	0101000020E6100000D034176EAF544840247612B644B32240	2018-12-06 16:49:02.981799	1
212	8.40224699999999913	48.9935729999999978		DB 20 BW,  Poststraße,  Südweststadt Östlicher Teil,  Südweststadt,  Karlsruhe	0101000020E610000024986A662D7F484006D49B51F3CD2040	2018-12-08 18:15:01.434533	1
213	8.46308900000000008	49.0016820000000024		DB BahnPark,  Hauptbahnstraße,  Alt-Durlach,  Durlach,  Karlsruhe	0101000020E6100000F67EA31D3780484052465C001AED2040	2018-12-08 18:22:48.436966	6
235	9.3501341999999994	48.661642999999998		Falkenwasenwiesen,  Unterensingen,  Vereinbarte Verwaltungsgemeinschaft der Stadt Nürtingen,  Landkreis Esslingen,  Regierungsbezirk Stuttgart	0101000020E61000004C50C3B7B0544840186C34CA44B32240	2018-12-10 16:24:44.725463	1
237	9.3501341999999994	48.6233999999999966		42,  Ersbergstraße,  Roßdorf,  Nürtingen,  Vereinbarte Verwaltungsgemeinschaft der Stadt Nürtingen	0101000020E6100000C7293A92CB4F4840186C34CA44B32240	2018-12-10 16:26:57.531865	1
240	9.3501341999999994	48.6234249999999975		42,  Ersbergstraße,  Roßdorf,  Nürtingen,  Vereinbarte Verwaltungsgemeinschaft der Stadt Nürtingen	0101000020E61000002041F163CC4F4840186C34CA44B32240	2018-12-10 16:29:32.442758	1
242	9.3501341999999994	48.6234377999999978		42,  Ersbergstraße,  Roßdorf,  Nürtingen,  Vereinbarte Verwaltungsgemeinschaft der Stadt Nürtingen	0101000020E61000008B0B51CFCC4F4840186C34CA44B32240	2018-12-10 16:30:55.119398	1
243	9.35046780000000055	48.6234377999999978	pic_f816c0fa-be2d-4700-a008-b288a589eb11.jpeg	42,  Ersbergstraße,  Roßdorf,  Nürtingen,  Vereinbarte Verwaltungsgemeinschaft der Stadt Nürtingen	0101000020E61000008B0B51CFCC4F4840269AF68370B32240	2018-12-10 16:33:52.220364	1
244	8.41091499999999925	48.6616037000000006		Alte Weinstraße,  Forbach,  Landkreis Rastatt,  Regierungsbezirk Karlsruhe,  Baden-Württemberg	0101000020E6100000D034176EAF54484026DF6C7363D22040	2018-12-10 17:15:44.18083	1
246	7.66159379999999857	51.4332366999999948		Im Berge,  Iserlohner Heide,  Iserlohn,  Märkischer Kreis,  Regierungsbezirk Arnsberg	0101000020E6100000A6F6D84C74B7494008F258D878A51E40	2018-12-12 01:19:49.056116	1
248	8.39013600000000004	49.0108279999999965		69,  Stephanienstraße,  Innenstadt West,  Innenstadt-West,  Karlsruhe	0101000020E6100000C7F0D8CF6281484009FCE1E7BFC72040	2018-12-12 01:31:41.547976	1
249	8.39013600000000004	49.010824999999997	index_d0fbed7e-a08b-4be4-aa67-72131ae6bcff.png	69,  Stephanienstraße,  Innenstadt West,  Innenstadt-West,  Karlsruhe	0101000020E6100000567DAEB66281484009FCE1E7BFC72040	2018-12-12 01:52:27.194293	1
250	8.4040619999999997	49.015310999999997		Blauer Strahl,  Innenstadt-West Östlicher Teil,  Innenstadt-West,  Karlsruhe,  Regierungsbezirk Karlsruhe	0101000020E61000007022FAB5F5814840DA1CE736E1CE2040	2018-12-12 15:21:15.35462	1
\.


--
-- TOC entry 3439 (class 0 OID 95416)
-- Dependencies: 197
-- Data for Name: remove_access; Type: TABLE DATA; Schema: d; Owner: postgres
--

COPY d.remove_access (id, acess_type) FROM stdin;
1	removed
2	yes
3	no
4	not yet
\.


--
-- TOC entry 3437 (class 0 OID 95405)
-- Dependencies: 195
-- Data for Name: trash_type; Type: TABLE DATA; Schema: d; Owner: postgres
--

COPY d.trash_type (id, trash) FROM stdin;
1	Papier
2	Mischt
3	Glass
4	Andere
5	Wertstef
6	Restmuel
7	Biologisch
\.


--
-- TOC entry 3433 (class 0 OID 94922)
-- Dependencies: 191
-- Data for Name: user; Type: TABLE DATA; Schema: d; Owner: postgres
--

COPY d."user" (gid, email, encrypted_password, remove_access, fk_request_access, confirmed) FROM stdin;
4	pyair86@gmail.com1	$5$rounds=535000$RnbulygB7u9AfHcF$Exr/38VNj9FgNpr3PPNz7amNSKT5oXYOacRGXVZMuV9	f	\N	f
7	pyair1@walla.co.iljkhkjhjk	$5$rounds=535000$/iZtdYZDeKguUhYI$GW50YBIdg72kx6vaeV1zXm5LvSr2wnWkV4UXZyhmKl1	f	\N	f
8	pyair1@walla.co.il12	$5$rounds=535000$Uwyp1s/NMBBInE8O$1VDYHyz4wGjxye8NAvoqzjDrZOKuRwAxM..vSX/EYu9	f	\N	f
9	shaifulislam797@gmail.com	$5$rounds=535000$uPXzPToEjEYH9c2T$b4PNUoSm4dz6nqlPrT2sJSL8LxwkqDU/7uBosTax6D8	f	3	f
10	egeiudhvduihiuhuijugtg@giufhuiehguie.com	$5$rounds=535000$YOD/dAKjs4KuLQHT$JWrURoho6yBTOOyXDDYGU9Ytyh9Bgp.jhnYtJL41BEA	f	2	f
11	tfifty@6ytoyogyo	$5$rounds=535000$idTqIJLJPyui8D4E$cF.XZe1F0lLlkE8Mzpa/P.zkBdBEEpRMXrsYs5/pIz6	f	3	f
12	uyky@khfk.com	$5$rounds=535000$a7j3uhz31b0p2Fyz$jXc2qwwnVT2eKzA7l83UxEJUjjmXDj3EKTFF8tEw4n6	f	2	f
13	hlghg@tfkyfk.com	$5$rounds=535000$t7oWpx4LdLIa2N2h$LlbIFZtgDrFupS3MX4qPikjpxa81O0Il.MJJG7/xHEC	f	2	f
14	vgvjhkvhjv@yuglul.com	$5$rounds=535000$baYsfYFRvFsfju4p$i9nmKAIOdyDQbp4qchH8ZuckoAXZWRVxexoQ3/bkUo7	f	2	f
15	vgvjhfggddffkvhjv@yuglul.com	$5$rounds=535000$UpxX.aV57mDnYXi9$VoihNGZvZF/hX1Axc3WwTsB5S.sopX7D9H8voTx0dpA	f	2	f
18	3vgvjhfggddffkvhjv@yuglul.com	$5$rounds=535000$kNS6oPDrN8gq2fR9$M8PuHjyvgR78Xo7JoFMX.Kg9rzih3C4U7fd4ddScsS6	f	2	f
23	pyair1@walla.co.il	$5$rounds=535000$PcqmsltbjTAjZQn1$7FqREzP3yrDiAQMwmL1gqIofTVtf3oQtH5ozbuSpHr6	f	2	t
26	tgtgrgrt	$5$rounds=535000$32PD8WyoInoeFaC3$p2q9.QNa8JJrv3NLAHzeHqPEawIM/0o9UcieZzuG3c8	t	2	f
25	pyair86@gmail.com	$5$rounds=535000$/nduTEsQJdFGr0OS$alZIMvN5jO69XieBg1M9OWJtZNG7cKaPINDdzFzBS/3	t	2	t
\.


--
-- TOC entry 3441 (class 0 OID 97053)
-- Dependencies: 200
-- Data for Name: bbox; Type: TABLE DATA; Schema: public; Owner: desweb
--

COPY public.bbox (gid, id, geom) FROM stdin;
1	0	0106000020E6100000010000000103000000010000000500000000000000A820214000000000F0764840000000001089204000000000F0764840000000001089204000000000168E484000000000A820214000000000168E484000000000A820214000000000F0764840
\.


--
-- TOC entry 3288 (class 0 OID 93812)
-- Dependencies: 176
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spatial_ref_sys  FROM stdin;
\.


--
-- TOC entry 3457 (class 0 OID 0)
-- Dependencies: 192
-- Name: point_gid_seq; Type: SEQUENCE SET; Schema: d; Owner: postgres
--

SELECT pg_catalog.setval('d.point_gid_seq', 250, true);


--
-- TOC entry 3458 (class 0 OID 0)
-- Dependencies: 196
-- Name: remove_access_id_seq; Type: SEQUENCE SET; Schema: d; Owner: postgres
--

SELECT pg_catalog.setval('d.remove_access_id_seq', 4, true);


--
-- TOC entry 3459 (class 0 OID 0)
-- Dependencies: 194
-- Name: trash_type_id_seq; Type: SEQUENCE SET; Schema: d; Owner: postgres
--

SELECT pg_catalog.setval('d.trash_type_id_seq', 11, true);


--
-- TOC entry 3460 (class 0 OID 0)
-- Dependencies: 190
-- Name: user_gid_seq; Type: SEQUENCE SET; Schema: d; Owner: postgres
--

SELECT pg_catalog.setval('d.user_gid_seq', 26, true);


--
-- TOC entry 3461 (class 0 OID 0)
-- Dependencies: 199
-- Name: bbox_gid_seq; Type: SEQUENCE SET; Schema: public; Owner: desweb
--

SELECT pg_catalog.setval('public.bbox_gid_seq', 1, true);


--
-- TOC entry 3310 (class 2606 OID 95424)
-- Name: remove_access access_pkey; Type: CONSTRAINT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d.remove_access
    ADD CONSTRAINT access_pkey PRIMARY KEY (id);


--
-- TOC entry 3304 (class 2606 OID 94967)
-- Name: point point_pkey; Type: CONSTRAINT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d.point
    ADD CONSTRAINT point_pkey PRIMARY KEY (gid);


--
-- TOC entry 3308 (class 2606 OID 95413)
-- Name: trash_type trash_pkey; Type: CONSTRAINT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d.trash_type
    ADD CONSTRAINT trash_pkey PRIMARY KEY (id);


--
-- TOC entry 3306 (class 2606 OID 97008)
-- Name: point unique_geom; Type: CONSTRAINT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d.point
    ADD CONSTRAINT unique_geom UNIQUE (geom);


--
-- TOC entry 3300 (class 2606 OID 94932)
-- Name: user uniqueness; Type: CONSTRAINT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d."user"
    ADD CONSTRAINT uniqueness UNIQUE (email);


--
-- TOC entry 3302 (class 2606 OID 94930)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (gid);


--
-- TOC entry 3313 (class 2606 OID 97058)
-- Name: bbox bbox_pkey; Type: CONSTRAINT; Schema: public; Owner: desweb
--

ALTER TABLE ONLY public.bbox
    ADD CONSTRAINT bbox_pkey PRIMARY KEY (gid);


--
-- TOC entry 3311 (class 1259 OID 97062)
-- Name: bbox_geom_idx; Type: INDEX; Schema: public; Owner: desweb
--

CREATE INDEX bbox_geom_idx ON public.bbox USING gist (geom);


--
-- TOC entry 3314 (class 2606 OID 95430)
-- Name: user access_fkey; Type: FK CONSTRAINT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d."user"
    ADD CONSTRAINT access_fkey FOREIGN KEY (fk_request_access) REFERENCES d.remove_access(id);


--
-- TOC entry 3315 (class 2606 OID 95425)
-- Name: point trash_fkey; Type: FK CONSTRAINT; Schema: d; Owner: postgres
--

ALTER TABLE ONLY d.point
    ADD CONSTRAINT trash_fkey FOREIGN KEY (fk_trash_type) REFERENCES d.trash_type(id);


--
-- TOC entry 3449 (class 0 OID 0)
-- Dependencies: 7
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2018-12-12 16:09:07 CET

--
-- PostgreSQL database dump complete
--

