## Changelog : mycollections (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la sécurité et l'administration du projet. Des améliorations significatives ont été apportées pour protéger les données sensibles, renforcer l'authentification et affiner les permissions d'accès. L'interface utilisateur a également été améliorée avec des éléments visuels plus cohérents et des fonctionnalités d'administration dédiées.

### Évolutions fonctionnelles
- Les actions de création et d'exploration sont désormais distinctes de l'administration, améliorant l'expérience utilisateur.
- Un menu et des routes d'administration dédiés ont été implémentés, accessibles uniquement aux super-administrateurs.
- Les échecs de synchronisation entre Keycloak et OpenRAG sont maintenant visibles, avec un client d'administration dédié pour faciliter le diagnostic.
- Les collections sont cloisonnées par groupe Keycloak, renforçant la sécurité et le contrôle d'accès [#A01].

### Évolutions techniques
- Renforcement de la sécurité :
    - Implémentation de garde-fous anti-leak pour prévenir la fuite d'informations sensibles.
    - Validation des URL lors des requêtes serveur pour se protéger contre les attaques SSRF.
    - Confinement des chemins dérivés d'entrées utilisateur pour éviter les vulnérabilités potentielles.
    - Assainissement du rendu HTML du Markdown non fiable côté front-end.
    - Isolation du contenu non fiable inséré dans les prompts LLM.
    - Configuration CORS plus stricte et suppression de la combinaison wildcard + credentials.
    - Ajout d'une garde d'authentification JWT sur les routes XHR.
    - Réduction de la divulgation d'informations sur l'endpoint de diagnostic.
- Amélioration de l'interface utilisateur :
    - Logo et titre de service alignés sur le look de myvault, avec un logo en slot opérateur DSFR.
    - Ajout d'une icône d'application DSFR (collections + graphe de références).

### Autres changements
- Ajout d'une batterie de tests d'identification et de corrections (backend pytest + front vitest).
- Checkpoint avant les correctifs de sécurité pour faciliter le rollback si nécessaire.
