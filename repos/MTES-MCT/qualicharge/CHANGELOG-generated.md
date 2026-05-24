## Changelog : qualicharge (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'automatisation de la mise à jour des unités opérationnelles via l'API, l'ajout d'indicateurs de volume au niveau des unités opérationnelles et la correction de vulnérabilités de sécurité grâce à la mise à jour de plusieurs dépendances. Des mises à jour régulières de l'infrastructure (Docker, Metabase) et des librairies Python ont également été effectuées.

### Évolutions fonctionnelles
- L'API permet désormais d'automatiser la mise à jour des unités opérationnelles. [#42f10b9](https://github.com/MTES-MCT/qualicharge/pull/42f10b9)
- Les indicateurs de volume sont désormais disponibles au niveau des unités opérationnelles, offrant une granularité accrue dans l'analyse des données. [#1527322](https://github.com/MTES-MCT/qualicharge/pull/1527322)

### Évolutions techniques
- Mise à jour de Django vers la version 6.0.5, incluant des correctifs de sécurité. [#f7364a3](https://github.com/MTES-MCT/qualicharge/pull/f7364a3)
- Mises à jour régulières des images Docker utilisées (uv, curl, metabase) pour bénéficier des dernières corrections et améliorations.
- Mises à jour de plusieurs dépendances Python (urllib3, idna, mako, prefect) pour corriger des vulnérabilités de sécurité et améliorer la stabilité.

### Autres changements
- Aucune documentation ou configuration n'a été modifiée durant cette période.
