## Changelog : qualicharge (30 derniers jours, au 11 mai 2026)

### Résumé
Les récentes mises à jour de qualicharge se concentrent sur la maintenance et la sécurité du système. Plusieurs dépendances ont été mises à jour pour corriger des vulnérabilités et bénéficier des dernières améliorations. Une évolution fonctionnelle permet d'étendre les indicateurs de volume au niveau des unités opérationnelles, améliorant ainsi la granularité des données disponibles.

### Évolutions fonctionnelles
- Extension des indicateurs de volume aux unités opérationnelles. [#1527322](https://github.com/MTES-MCT/qualicharge/pull/1527322)

### Évolutions techniques
- Mise à jour de Django vers la version 6.0.5, incluant des correctifs de sécurité.
- Mise à jour de l'outil de gestion des dépendances `uv` vers les versions 0.11.8, 0.11.11, 0.11.12 et 0.11.13.
- Mise à jour de l'image Docker Metabase vers les versions 0.60.2 et 0.60.4.
- Mise à jour de l'image Docker curl vers la version 8.20.0.
- Mise à jour de Terraform vers la version 1.14.9.
- Mise à jour de urllib3 vers la version 2.7.0.
- Mise à jour de python-dotenv vers la version 1.2.2.
- Mise à jour de mako vers la version 1.3.12.

### Autres changements
- Application de correctifs de sécurité via Dependabot.
- Mises à jour régulières des images Docker utilisées par le projet.
