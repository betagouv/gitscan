## Changelog : agreste (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, agreste a franchi des étapes importantes en renforçant la sécurité des utilisateurs, notamment avec l'introduction de l'authentification à deux facteurs. L'expérience de recherche a été considérablement améliorée pour être plus intuitive et précise, tandis que l'infrastructure technique a été simplifiée et sécurisée pour garantir une meilleure stabilité et une maintenance facilitée.

### Évolutions fonctionnelles
- **Sécurité** : Mise en place de l'authentification à deux facteurs (MFA) pour sécuriser l'accès aux interfaces [#516](https://github.com/betagouv/agreste/issues/516).
- **Améliorations de la recherche** :
    - Ajout de compteurs sur les filtres de recherche et masquage automatique des filtres n'ayant aucun résultat [#65](https://github.com/betagouv/agreste/issues/65).
    - Possibilité de trier les résultats par date en complément du tri par pertinence [#90](https://github.com/betagouv/agreste/issues/90).
    - Support de la recherche insensible aux accents (unaccented) pour plus de souplesse [#78](https://github.com/betagouv/agreste/issues/78).
    - Optimisation de l'interface de recherche : suppression de la double pagination et de la navigation automatique vers les résultats pour une navigation plus fluide [#91](https://github.com/betagouv/agreste/issues/91) [#64](https://github.com/betagouv/agreste/issues/64).
    - Correction d'un bug empêchant la mise à jour des résultats lors de la suppression d'un filtre sur les pages CatalogIndex [#578](https://github.com/betagouv/agreste/issues/578).
- **Gestion de contenu** :
    - Personnalisation accrue des blocs "Articles récents" (Blog/Événements) : possibilité de modifier le texte et le lien du bouton "Voir tous les articles" [#542](https://github.com/betagouv/agreste/issues/542).
    - Introduction de nouveaux hooks pour permettre une personnalisation plus fine des résultats de recherche [#561](https://github.com/betagouv/agreste/issues/561).

### Évolutions techniques
- **Sécurité et CI/CD** :
    - Mise en place d'un contrôle automatique des vulnérabilités (CVE) lors de chaque changement de dépendance [#97](https://github.com/betagouv/agreste/issues/97).
    - Instauration d'un délai de "refroidissement" (cooldown) de 7 jours pour les dépendances Python et JS afin de limiter l'impact des mises à jour instables [#98](https://github.com/betagouv/agreste/issues/98).
    - Activation des contrôles de malwares pour l'outil de gestion de paquets `uv` [#82](https://github.com/betagouv/agreste/issues/82).
    - Automatisation du processus de release via une commande en ligne de commande [#77](https://github.com/betagouv/agreste/issues/77).
- **Architecture et maintenance** :
    - Refonte majeure du système de recherche à facettes.
    - Simplification de la stack technique par la suppression de toute dépendance à `npm` [#72](https://github.com/betagouv/agreste/issues/72).
    - Suppression de la dépendance `modelsearch` [#94](https://github.com/betagouv/agreste/issues/94).
    - Optimisation de la suite de tests pour réduire le temps d'exécution (tests plus rapides et fixtures allégées) [#80](https://github.com/betagouv/agreste/issues/80).
    - Mise à jour de l'environnement de développement Docker vers Python 3.14.

### Autres changements
- **Documentation** : Centralisation et réorganisation complète de la documentation technique via Sphinx [#558](https://github.com/betagouv/agreste/issues/558).
- **Nettoyage** : Suppression de la démo d'intégration pour réduire la surface d'attaque et éliminer les alertes de sécurité inutiles [#87](https://github.com/betagouv/agreste/issues/87).
