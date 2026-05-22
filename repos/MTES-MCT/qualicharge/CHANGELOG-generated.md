## Changelog : qualicharge (30 derniers jours, au 18 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à qualicharge au cours du dernier mois. Les principales évolutions concernent l'automatisation de la mise à jour des unités opérationnelles via l'API, l'extension des indicateurs de volume au niveau des unités opérationnelles, ainsi que des mises à jour de sécurité et de dépendances pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- L'API permet désormais de mettre à jour automatiquement les unités opérationnelles. [#42f10b9](https://github.com/MTES-MCT/qualicharge/commit/42f10b9)
- Les indicateurs de volume sont désormais disponibles au niveau des unités opérationnelles, offrant une granularité plus fine pour l'analyse des données. [#1527322](https://github.com/MTES-MCT/qualicharge/commit/1527322)

### Évolutions techniques
- Mise à jour de Django en version 6.0.5 incluant des correctifs de sécurité.
- Mises à jour de plusieurs images Docker (curl, uv, metabase, terraform) vers leurs dernières versions stables.
- Mise à jour de la librairie Mako en version 1.3.12.
- Application de correctifs de sécurité pour les dépendances urllib3 et python-dotenv.

### Autres changements
- Mises à jour de la librairie astral-sh/uv vers les versions 0.11.8, 0.11.11, 0.11.12 et 0.11.13.
