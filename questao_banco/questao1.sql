CREATE SCHEMA banco
    AUTHORIZATION postgres;

CREATE TABLE banco.conta
(
    id_conta serial,
    conta integer NOT NULL,
    agencia integer NOT NULL,
    CONSTRAINT conta_pkey PRIMARY KEY (id_conta)
)
TABLESPACE pg_default;

CREATE TABLE banco.conta_transacao
(
    id_conta_transacao integer NOT NULL,
    agencia integer NOT NULL,
    conta integer NOT NULL,
    documento integer NOT NULL,
    codigo_banco integer NOT NULL,
    CONSTRAINT conta_transacao_pkey PRIMARY KEY (id_conta_transacao)
)
TABLESPACE pg_default;

CREATE TABLE banco.transacao
(
    id_transacao integer NOT NULL,
    tipo_transacao text NOT NULL,
    valor numeric NOT NULL,
    id_conta_transacao integer,
    id_conta integer NOT NULL,
    data_transacao timestamp with time zone,
    CONSTRAINT transacao_pkey PRIMARY KEY (id_transacao),
    CONSTRAINT fk_conta FOREIGN KEY (id_conta)
        REFERENCES banco.conta (id_conta) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_conta_transacao FOREIGN KEY (id_conta_transacao)
        REFERENCES banco.conta_transacao (id_conta_transacao) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_tipo_transacao FOREIGN KEY (tipo_transacao_id)
        REFERENCES banco.tipo_transacao (id_tipo_transacao) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
TABLESPACE pg_default;

CREATE INDEX fki_fk_conta
    ON banco.transacao USING btree
    (id_conta ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX fki_fk_conta_transacao
    ON banco.transacao USING btree
    (id_conta_transacao ASC NULLS LAST)
    TABLESPACE pg_default;