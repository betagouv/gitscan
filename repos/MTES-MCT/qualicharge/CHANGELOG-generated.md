## Changelog : qualicharge (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à qualicharge au cours du dernier mois. Les modifications incluent des validations plus strictes des données API, des corrections de bugs dans les workflows Prefect pour l'analyse de la qualité de la recharge, et des mises à jour de sécurité et de dépendances. Des améliorations de la robustesse et de la fiabilité du système ont également été implémentées.

### Évolutions fonctionnelles
- Amélioration de la validation des données transmises via l'API :
    - Vérification de la validité du numéro SIREN (checksum) [#issue à retrouver].
    - Restriction des valeurs maximales de `Statique.puissance_nominale` [#issue à retrouver].
    - Limitation de la durée maximale d'une session à une semaine [#issue à retrouver].
    - Restriction des valeurs de `Session.energy` [#issue à retrouver].
    - Exigence d'un `num_pdl` pour les connexions directes [#issue à retrouver].
    - Vérification que le point de recharge se trouve sur le territoire français [#issue à retrouver].
    - Exigence du champ `raccordement` pour les données statiques [#issue à retrouver].
- Correction d'un bug dans les indicateurs de qualité Prefect pour le PDCM [#issue à retrouver].
- Correction de l'unité d'énergie envoyée par CARBURE [#issue à retrouver].
- Prise en compte des points de recharge hors service dans les vérifications de refroidissement des données [#issue à retrouver].
- Amélioration de la gestion des erreurs dans les workflows de refroidissement, permettant une détection plus rapide des problèmes [#issue à retrouver].

### Évolutions techniques
- Activation des linters pour tous les modules du projet afin d'améliorer la qualité du code [#issue à retrouver].
- Refactorisation des workflows de refroidissement Prefect pour une meilleure organisation et maintenabilité [#issue à retrouver].
- Ajout de la possibilité d'allouer un pseudo-TTY pour la commande `psql` [#issue à retrouver].
- Mise en place d'un mécanisme pour déclencher les CI/CD même lorsque la branche cible n'est pas `main` [#issue à retrouver].
- Passage des champs `Status` et `Session` à des types datetime avec fuseau horaire (TZ-aware) [#issue à retrouver].
- Mise à jour de plusieurs dépendances : FastAPI, Werkzeug, Django, Locust, Terraform, Metabase, UV, orjson, python-multipart.

### Autres changements
- Publication d'une nouvelle version de l'API (0.32.0) [#issue à retrouver].
- Actualisation des indicateurs pour les attentes de qualité dans Prefect [#issue à retrouver].
- Mises à jour des images Docker utilisées par le projet.
- Amélioration des actions GitHub pour l'utilisation de UV.
