## Changelog : qualicharge (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à qualicharge au cours des 30 derniers jours. Les modifications incluent des validations plus strictes sur les données ingérées via l'API, des corrections de bugs dans les workflows de supervision (préfect), des mises à jour de sécurité pour certaines dépendances et des optimisations de performance. Des mises à jour de versions de dépendances et d'images Docker ont également été effectuées.

### Évolutions fonctionnelles
- Amélioration de la validation des données d'itinérance via l'API. [#issue à retrouver]
- Restriction de la durée maximale d'une session à une semaine via l'API. [#issue à retrouver]
- Vérification de la validité du numéro SIREN (checksum) avant ingestion via l'API. [#issue à retrouver]
- Vérification que les points de recharge se trouvent sur le territoire français via l'API. [#issue à retrouver]
- Exigence d'un numéro de point de livraison (num_pdl) pour les connexions directes via l'API. [#issue à retrouver]
- Correction de l'indicateur de qualité PDCM dans les workflows de supervision (préfect). [#issue à retrouver]
- Prise en compte des points de recharge hors service dans les vérifications de refroidissement des données (data cooling). [#issue à retrouver]

### Évolutions techniques
- Autorisation de l'allocation de pseudo-TTY pour la commande `psql` dans les conteneurs. [#issue à retrouver]
- Refactorisation des workflows de refroidissement des données (préfect). [#issue à retrouver]
- Amélioration de la gestion des erreurs et de la résilience des workflows de refroidissement des données (préfect). [#issue à retrouver]
- Déclenchement du CI même lorsque la branche cible n'est pas `main`. [#issue à retrouver]
- Mise à jour de Django vers la version 6.0.3 (incluant des correctifs de sécurité). [#issue à retrouver]

### Autres changements
- Mise à jour de plusieurs images Docker (Metabase, Terraform, Locust, UV).
- Mise à jour de plusieurs dépendances (Flask, Werkzeug, SQLParse, Cryptography).
- Actualisation des indicateurs de qualité pour les attentes (Expectations) dans Prefect.
