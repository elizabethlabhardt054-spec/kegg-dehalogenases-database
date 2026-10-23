import json
import sqlite3
import os

def init_db(db_path="dehalogenases.db"):
    """Inicializa a base de dados SQLite e cria a tabela se não existir."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dehalogenases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gene_symbol TEXT UNIQUE,
            ec_number TEXT,
            enzyme_name TEXT,
            pathway TEXT,
            mechanism TEXT,
            cofactors TEXT,
            kegg_orthology TEXT
        )
    ''')
    conn.commit()
    return conn

def validate_and_insert(json_path="dehalogenases_catalog.json", db_path="dehalogenases.db"):
    """Lê o ficheiro JSON, valida e insere os registos na base de dados."""
    if not os.path.exists(json_path):
        print(f"Erro: O ficheiro {json_path} não foi encontrado.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Erro ao descodificar o JSON: {e}")
            return

    conn = init_db(db_path)
    cursor = conn.cursor()

    success_count = 0
    for item in data:
        # Validação básica de campos obrigatórios
        if not item.get("gene_symbol") or not item.get("enzyme_name"):
            print(f"Aviso: Entrada ignorada por falta de campos obrigatórios: {item}")
            continue

        cofactors = item.get("cofactors")
        cofactors_str = ", ".join(cofactors) if cofactors else "Nenhum"

        try:
            cursor.execute('''
                INSERT OR REPLACE INTO dehalogenases 
                (gene_symbol, ec_number, enzyme_name, pathway, mechanism, cofactors, kegg_orthology)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                item.get("gene_symbol"),
                item.get("ec_number"),
                item.get("enzyme_name"),
                item.get("pathway"),
                item.get("mechanism"),
                cofactors_str,
                item.get("kegg_orthology")
            ))
            success_count += 1
        except sqlite3.Error as e:
            print(f"Erro ao inserir o registo {item.get('gene_symbol')}: {e}")

    conn.commit()
    conn.close()
    print(f"Processo concluído com sucesso! {success_count} registos inseridos/atualizados na base de dados.")

if __name__ == "__main__":
    validate_and_insert()