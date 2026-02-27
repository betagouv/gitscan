## Changelog : qualicharge (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à qualicharge au cours des 30 derniers jours. Les modifications incluent des corrections de bugs dans les indicateurs de qualité Prefect, une meilleure gestion des points de recharge hors service dans les vérifications de refroidissement des données, et des mises à jour de plusieurs dépendances pour assurer la sécurité et la stabilité du système. Des améliorations techniques ont également été apportées, notamment des refactorisations et l'activation de linters.

### Évolutions fonctionnelles
- Correction d'un bug dans l'indicateur de qualité PDCM dans Prefect (#50bfa31).
- Prise en compte des points de recharge hors service dans les vérifications de refroidissement des données (#aacb98a).
- Amélioration de la gestion des flux de refroidissement pour permettre une détection précoce des erreurs (#08aa38b).
- Correction de l'unité d'énergie envoyée par CARBURE (#45bba03).
- Publication de la version 0.32.0 de l'API, incluant des corrections pour la gestion des fuseaux horaires des champs de date et heure Status et Session (#6f76b05, #af8d0f0).

### Évolutions techniques
- Refactorisation des flux de refroidissement dans Prefect pour une meilleure maintenabilité (#2a9556e).
- Activation des linters pour tous les modules afin d'améliorer la qualité du code (#c1a254c).
- Mises à jour de plusieurs dépendances, notamment :
    - `astral-sh/uv` (plusieurs mises à jour vers les versions 0.9.28, 0.9.29, 0.9.30, 0.10.0, 0.10.2, 0.10.4)
    - `metabase/metabase` (plusieurs mises à jour vers les versions 0.58.4, 0.58.5, 0.58.7)
    - `locustio/locust` (plusieurs mises à jour vers les versions 2.43.2, 2.43.3)
    - `hashicorp/terraform` (plusieurs mises à jour vers les versions 1.14.4, 1.14.5)
    - `Django` (mise à jour vers la version 6.0.2)
    - `cryptography` (mise à jour vers la version 46.0.5)
    - `orjson` (mise à jour vers la version 3.11.5)
    - `python-multipart` (mise à jour vers la version 0.0.22)
- Mises à jour des actions GitHub `astral-sh/setup-uv` et `zizmorcore/zizmor-action`.

### Autres changements
- Actualisation des indicateurs pour les attentes de qualité Prefect (#fa4f1f9).
- Mise à jour de la documentation et de la configuration du projet (non spécifié dans les commits).
