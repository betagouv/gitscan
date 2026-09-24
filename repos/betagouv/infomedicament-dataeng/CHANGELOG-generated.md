## Changelog : infomedicament-dataeng (30 derniers jours, au 21 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'enrichissement des données via l'importation automatique de sources externes (DataGouv) et la modernisation de la structure de la base de données. Le système de traitement a également été renforcé pour améliorer la précision de l'analyse des documents et la fiabilité des imports.

### Évolutions fonctionnelles
- Automatisation de l'importation des données de l'ANSM depuis la plateforme DataGouv [#21](https://github.com/betagouv/infomedicament-dataeng/issues/21)

### Évolutions techniques
- **Base de données** : Extension du schéma avec l'ajout de nouvelles tables et colonnes, incluant de nouvelles tables dédiées aux génériques [#19](https://github.com/betagouv/infomedicament-dataeng/issues/19), [#22](https://github.com/betagouv/infomedicament-dataeng/issues/22)
- **Parsing et traitement** : Implémentation d'un parseur HTML sémantique [#16](https://github.com/betagouv/infomedicament-dataeng/issues/16) et ajout d'une logique de gestion de préfixes [#20](https://github.com/betagouv/infomedicament-dataeng/issues/20)
- **Fiabilité et monitoring** : Renforcement du processus d'importation avec l'ajout d'un contrôle de dérive des séquences d'identifiants (ID sequence drift) et de diagnostics plus détaillés [#17](https://github.com/betagouv/infomedicament-dataeng/issues/17)
