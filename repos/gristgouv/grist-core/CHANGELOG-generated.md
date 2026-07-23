## Changelog : grist-core (30 derniers jours, au 2026-07-21)

### Résumé
Cette version apporte des améliorations significatives à la gestion des autorisations OAuth, à la stabilité de l'application (notamment en corrigeant des crashes et des comportements inattendus), et à l'expérience utilisateur avec des options de personnalisation de l'affichage des lignes et des améliorations de l'interface. Des corrections de bugs et des traductions ont également été intégrées.

### Évolutions fonctionnelles
- Possibilité de masquer les numéros de ligne dans la grille, ou de les remplacer par les IDs des lignes. [#2448](https://github.com/gristgouv/grist-core/issues/2448)
- Amélioration de la gestion des applications OAuth, incluant la correction du comportement de ré-autorisation et la persistance des tokens. [#2465](https://github.com/grist-core/issues/2465)
- Ajout d'un message d'aide pour configurer les Notifications & Automations dans l'interface d'administration. [#2464](https://github.com/grist-core/issues/2464)
- Possibilité de substituer l'ID dans l'URL de redirection des formulaires. [#1831](https://github.com/gristgouv/grist-core/issues/1831)
- Amélioration de la gestion des URLs personnalisées pour les widgets.
- Recommandation d'utiliser l'authentification getgrist.com lors de la configuration rapide. [#2410](https://github.com/grist-core/issues/2410)
- Correction d'un bug empêchant l'annulation de certaines actions avec des renommages. [#2387](https://github.com/grist-core/issues/2387)

### Évolutions techniques
- Ajout d'un proxy pour le fleet Grist, permettant la communication entre serveurs. [#2458](https://github.com/grist-core/issues/2458)
- Refonte du chargement des fichiers pour permettre le proxying des requêtes.
- Amélioration de la gestion des erreurs lors de la déconnexion client avec un proxy HTTP.
- Correction d'un test SQLiteDB pour éviter les faux échecs liés à la vitesse d'écriture après un "unpause".
- Support de l'enregistrement dynamique des clients OAuth (RFC 7591).
- Amélioration de la gestion des appels MCP (Mobile Client Proxy) pour résoudre les problèmes d'ID de documents.
- Suppression d'une ancienne vérification de "reachability" et correction d'une redirection lorsque les organisations personnelles sont désactivées.
- Mise à jour de plusieurs dépendances (tmp, @babel/core, http-proxy-middleware, launch-editor, ws, undici, js-yaml, dompurify, piscina, typeorm).

### Autres changements
- Amélioration de la documentation de la base de données.
- Corrections de traductions en français, japonais, suédois et hongrois.
- Suppression de styles CSS inutiles dans l'interface d'administration.
- Corrections de quelques chaînes de caractères non traduites.
- Ajout d'un toggle de télémétrie au flux de configuration rapide.
- Mise à jour des clés de traduction automatisées.
- Publication de la version v1.7.16. [#2442](https://github.com/gristgouv/grist-core/issues/2442)
- Correction d'un problème d'affichage dans les éditeurs de choix. [#2474](https://github.com/gristgouv/grist-core/issues/2474)
- Suppression d'un avertissement lint concernant l'union ServerMode. [#2473](https://github.com/gristgouv/grist-core/issues/2473)
- Correction d'un bug dans les colonnes de comptage Airtable avec des colonnes de référence. [#2447](https://github.com/gristgouv/grist-core/issues/2447)
- Correction d'un bug empêchant la résolution correcte des valeurs des colonnes de référence importées. [#2446](https://github.com/gristgouv/grist-core/issues/2446)
