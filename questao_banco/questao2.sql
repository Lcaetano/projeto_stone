CREATE INDEX fki_fk_tipo_transacao
    ON banco.transacao USING btree
    (tipo_transacao ASC NULLS LAST)
    TABLESPACE pg_default;

SELECT DATE_PART('MONTH', data_transacao) as mes, sum(valor) as total_pagamento
FROM banco.transacao
WHERE DATE_PART('YEAR', data_transacao) = 2022
      and tipo_transacao = 'BOLETO'
GROUP BY 1;