## Changelog : data_pass (30 derniers jours, au 28 septembre 2026)

### Résumé
Ce mois-ci, data_pass a franchi des étapes importantes pour enrichir le parcours lié aux services EAJE et renforcer la fiabilité des échanges avec l'INSEE. Le système de gestion des demandes a également été affiné pour mieux détecter les modifications (champs ou documents) nécessitant une réouverture de dossier, tout en améliorant la fluidité du tunnel de saisie pour les utilisateurs.

### Évolutions fonctionnelles
- **Parcours EAJE** : Intégration de l'option EAJE au préfiltrage des demandeurs, référencement des éditeurs (CapCreche, Osmia, optiCreche) et ajout de fonctionnalités dédiées au parcours. [#1720](https://github.com/etalab/data_pass/pull/1720), [#1779](https://github.com/etalab/data_pass/pull/1779)
- **Demandes externes** : Enrichissement des données pour la DGFiP (ajout de l'adresse IP publique et de nouveaux champs) et simplification du processus pour l'API Entreprise par la suppression de l'obligation de renseigner un responsable de traitement. [#1762](https://github.com/etalab/data_pass/pull/1762), [#1764](https://github.com/etalab/data_pass/pull/1764)
- **Gestion des dossiers** : Amélioration de la détection des changements (nouveaux champs renseignés ou documents ajoutés/retirés) pour identifier automatiquement les demandes nécessitant une réouverture.
- **Notifications** : Mise en place d'un système de notification vers HubEE lors de la validation des demandes FQF, avec possibilité de configurer les destinataires. [#1766](https://github.com/etalab/data_pass/pull/1766)
- **Expérience utilisateur** : Optimisation du tunnel de formulaire (meilleure validation des étapes, gestion des brouillons via cookies) et corrections d'affichage des bannières d'accès. [#1761](https://github.com/etalab/data_pass/pull/1761), [#1730](https://github.com/etalab/data_pass/pull/1730), [#1754](https://github.com/etalab/data_pass/pull/1754)
- **Mise à jour des contenus** : Actualisation des informations relatives à la direction de la DINUM et personnalisation du cadre juridique pour les produits DINUM. [#1780](https://github.com/etalab/data_pass/pull/1780), [#1749](https://github.com/etalab/data_pass/pull/1749)
- **Volumétrie** : Alignement du troisième palier de volumétrie pour le FICOBA à 750. [#1777](https://github.com/etalab/data_pass/pull/1777)

### Évolutions techniques
- **Fiabilisation de l'intégration INSEE** : Optimisation majeure des appels vers l'INSEE via l'utilisation d'une file d'attente dédiée, la mise en place de coupe-circuits (*circuit breakers*) en cas d'échec d'authentification et une meilleure résilience en cas d'indisponibilité du service. [#1771](https://github.com/etalab/data_pass/pull/1771), [#1772](https://github.com/etalab/data_pass/pull/1772), [#1773](https://github.com/etalab/data_pass/pull/1773), [#1774](https://github.com/etalab/data_pass/pull/1774)
- **API & OAuth** : Automatisation de l'attribution du scope `read_webhooks` pour les nouvelles applications et les clés API. [#1753](https://github.com/etalab/data_pass/pull/1753)
- **Sécurité & Infrastructure** : Restriction de l'accès par authentification locale (`local-sign-in`) sur l'environnement de staging [#1693](https://github.com/etalab/data_pass/pull/1693), amélioration du watchdog de déploiement [#1778](https://github.com/etalab/data_pass/pull/1778) et renforcement de la validation des adresses IP publiques.
