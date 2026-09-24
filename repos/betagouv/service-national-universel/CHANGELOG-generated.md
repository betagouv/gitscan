## Changelog : service-national-universel (30 derniers jours, au 23 septembre 2026)

### Résumé
Ce mois a été principalement consacré à un renforcement massif de la sécurité de la plateforme et à une simplification de l'écosystème. De nombreux correctifs ont été apportés pour garantir la confidentialité des données (protection des informations personnelles et des secrets) et pour mieux cloisonner les accès entre les différents types d'utilisateurs (jeunes, référents, administration). Parallèlement, plusieurs parcours de gestion obsolètes ont été supprimés pour alléger le service.

### Évolutions fonctionnelles
- **Simplification des parcours :**
    - Suppression des tunnels d'inscription et de réinscription ([#5358](https://github.com/betagouv/service-national-universel/issues/5358)).
    - Suppression du parcours dédié aux représentants légaux ([#5357](https://github.com/betagouv/service-national-universel/issues/5357)).
    - Suppression des fonctionnalités d'inscription pour les structures ([#5290](https://github.com/betagouv/service-national-universel/issues/5290)).
- **Information utilisateur :**
    - Ajout de bandeaux d'information concernant l'indisponibilité du service sur les pages de connexion et la base de connaissance ([#5296](https://github.com/betagouv/service-national-universel/issues/5296), [#5289](https://github.com/betagouv/service-national-universel/issues/5289)).
- **Nouveauté :**
    - Mise en place de l'import en masse pour les remboursements liés au code de la route ([#5286](https://github.com/betagouv/service-national-universel/issues/5286)).

### Évolutions techniques
- **Sécurité (Renforcement majeur) :**
    - **Contrôle d'accès et cloisonnement :** Application stricte de la matrice de rôles côté serveur et cloisonnement des données (dossiers jeunes, missions, centres de cohésion, candidatures) pour éviter qu'un utilisateur n'accède aux données d'un autre ([#5378](https://github.com/betagouv/service-national-universel/issues/5378), [#5375](https://github.com/betagouv/service-national-universel/issues/5375), [#5338](https://github.com/betagouv/service-national-universel/issues/5338), [#5319](https://github.com/betagouv/service-national-universel/issues/5319)).
    - **Protection de la vie privée (PII) :** Masquage des données personnelles et des secrets dans les logs, les outils de télémétrie (Sentry, Plausible) et les flux d'emails ([#5370](https://github.com/betagouv/service-national-universel/issues/5370), [#5337](https://github.com/betagouv/service-national-universel/issues/5337), [#5330](https://github.com/betagouv/service-national-universel/issues/5330), [#5293](https://github.com/betagouv/service-national-universel/issues/5293)).
    - **Correction de vulnérabilités :** Résolution de nombreuses failles de type IDOR (accès non autorisé via l'ID d'une ressource) sur les tickets support et les données utilisateurs ([#5302](https://github.com/betagouv/service-national-universel/issues/5302), [#5294](https://github.com/betagouv/service-national-universel/issues/5294), [#5298](https://github.com/betagouv/service-national-universel/issues/5298), [#5299](https://github.com/betagouv/service-national-universel/issues/5299), [#5300](https://github.com/betagouv/service-national-universel/issues/5300)).
    - **Prévention des injections :** Contrôle des injections HTML et sécurisation des redirections après connexion ([#5377](https://github.com/betagouv/service-national-universel/issues/5377), [#5366](https://github.com/betagouv/service-national-universel/issues/5366)).
    - **Authentification :** Sécurisation des jetons de signature, de la gestion des sessions et du processus 2FA ([#5368](https://github.com/betagouv/service-national-universel/issues/5368), [#5348](https://github.com/betagouv/service-national-universel/issues/5348), [#5325](https://github.com/betagouv/service-national-universel/issues/5325)).
- **Infrastructure & CI/CD :**
    - Optimisation des workflows GitHub Actions (gestion du cache et pilotage des runners) ([#5329](https://github.com/betagouv/service-national-universel/issues/5329), [#5327](https://github.com/betagouv/service-national-universel/issues/5327), [#5326](https://github.com/betagouv/service-national-universel/issues/5326), [#5316](https://github.com/betagouv/service-national-universel/issues/5316)).
    - Nettoyage de l'environnement de test (suppression de conteneurs MongoDB résiduels et sécurisation des fixtures de test) ([#5328](https://github.com/betagouv/service-national-universel/issues/5328), [#5324](https://github.com/betagouv/service-national-universel/issues/5324), [#5331](https://github.com/betagouv/service-national-universel/issues/5331)).
- **Architecture :**
    - Décommissionnement de l'administration CLE ([#5315](https://github.com/betagouv/service-national-universel/issues/5315)) et retrait de schémas de données obsolètes ([#5356](https://github.com/betagouv/service-national-universel/issues/5356)).
