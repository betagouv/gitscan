## Changelog : qualicharge (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la maintenance et la sécurité du projet. Plusieurs dépendances ont été mises à jour pour corriger des vulnérabilités et bénéficier des dernières améliorations. Une évolution fonctionnelle a été apportée pour améliorer la gestion des utilisateurs en supprimant les requêtes API en cache.

### Évolutions fonctionnelles
- Suppression des requêtes API en cache pour les utilisateurs [#7149d5d](https://github.com/MTES-MCT/qualicharge/commit/7149d5d).
- Extension des indicateurs de volume au niveau OperationalUnit [#1527322](https://github.com/MTES-MCT/qualicharge/commit/1527322).

### Évolutions techniques
- Mise à jour de Django en version 6.0.5 incluant des correctifs de sécurité [#f7364a3](https://github.com/MTES-MCT/qualicharge/commit/f7364a3).
- Mises à jour des images Docker pour Metabase (v0.60.4 et v0.60.2) et curl (v8.20.0) pour bénéficier des dernières corrections et améliorations.
- Mises à jour de plusieurs actions et librairies utilisées dans le projet (uv, setup-uv, zizmor-action, python-multipart, python-dotenv, terraform) pour bénéficier des dernières corrections et améliorations.

### Autres changements
- Mise à jour de la librairie Mako en version 1.3.12 [#41f2480](https://github.com/MTES-MCT/qualicharge/commit/41f2480).
