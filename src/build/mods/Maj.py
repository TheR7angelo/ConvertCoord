import os.path
import sqlite3

from src.config.config import Configue
from src.lib.globals.v_gb import GUID

class Maj:

    def get_maj(self):
        nom = Configue().cfg['infos']['nom']
        version = float(Configue().cfg['infos']['version'])

        bdd = r"T:\- 4 Suivi Appuis\18-Partage\BARRENTO ANTUNES Raphael\6_Programme python\Centre macro.db"
        if os.path.isfile(bdd):
            with sqlite3.connect(bdd) as conn:
                cursor = conn.cursor()

                cursor.execute(f"""
                                SELECT ad_nom
                                FROM t_gr
                                WHERE ad_nom='{GUID}';
                                """)
                row = cursor.fetchone()

                if row is None:
                    cursor.execute(f"""
                                    INSERT INTO t_gr (ad_nom, ad_grade)
                                    VALUES ('{GUID}', 4);
                                    """)

                cursor.execute(f"""
                        SELECT ver, lien
                        FROM v_centre_logiciel
                        WHERE nom='{nom}';
                        """)

                row = cursor.fetchone()
            if row is not None:
                if row[0] > version:
                    return row
                else:
                    return False
            else:
                return False
        else:
            return False
