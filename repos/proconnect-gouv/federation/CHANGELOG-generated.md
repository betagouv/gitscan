## Changelog : federation (30 derniers jours, au 11 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes importantes en matière de sécurité et de robustesse. Les évolutions se sont concentrées sur l'amélioration de l'expérience utilisateur via des communications par email plus claires et sécurisées (notamment sur l'authentification multi-facteur), ainsi que sur une restructuration technique majeure visant à transformer plusieurs composants en services autonomes pour une meilleure maintenance.

### Évolutions fonctionnelles
- **Sécurité & Authentification** :
    - Mise en place d'un mode de secours (fallback) par email pour le MFA afin de supporter les fournisseurs d'identité ne le permettant pas [#1348](https://github.com/proconnect-gouv/federation/issues/1348).
    - Amélioration de la gestion des sessions MFA pour réutiliser les sessions lorsque les exigences ACR sont satisfaites [#1450](https://github.com/proconnect-gouv/federation/issues/1450).
    - Possibilité de tester le MFA via des alias d'emails (ex: `+mfa`) [#1348](https://github.com/proconnect-gouv/federation/issues/1348).
    - Blocage par défaut des emails de domaine lors de la création d'un fournisseur d'identité (IdP) dans l'administration [#1476](https://github.com/proconnect-gouv/federation/issues/1476).
- **Expérience Utilisateur (UX) & Emails** :
    - Refonte des emails de code OTP : utilisation de modèles dédiés, réduction de la longueur du code et clarification des sujets pour une meilleure lisibilité [#1477](https://github.com/proconnect-gouv/federation/issues/1477).
    - Amélioration de la clarté des messages et des sujets d'emails de vérification [#1425](https://github.com/proconnect-gouv/federation/issues/1425), [#855942c](https://github.com/proconnect-gouv/federation/issues/855942c).
    - Mise à jour de la terminologie : "Fournisseur de données" devient "Serveur de ressources" pour plus de clarté [#8542d4d](https://github.com/proconnect-gouv/federation/issues/8542d4d).
    - Simplification de l'interface d'administration : suppression de l'autocomplétion et de l'autofill sur les champs "collaborateurs" [#06120f9](https://github.com/proconnect-gouv/federation/issues/06120f9).
- **API** :
    - Ajout d'un point de terminaison pour la suppression de clients OIDC via l'API [#1390](https://github.com/proconnect-gouv/federation/issues/1390).

### Évolutions techniques
- **Architecture & Refactoring** :
    - **Modularisation** : Extraction de plusieurs services de simulation (mock-data-provider, mock-identity-provider, mock-service-provider, csmr-rie) en applications autonomes pour alléger le dépôt principal [#1413](https://github.com/proconnect-gouv/federation/issues/1413), [#1416](https://github.com/proconnect-gouv/federation/issues/1416), [#1424](https://github.com/proconnect-gouv/federation/issues/1424), [#1428](https://github.com/proconnect-gouv/federation/issues/1428).
    - **Gestion des emails** : Introduction de la bibliothèque `@fc/mailer` permettant de gérer différents adaptateurs (SMTP, Brevo, noop) [#1343](https://github.com/proconnect-gouv/federation/issues/1343).
    - **Standardisation** : Migration de la gestion des erreurs vers les filtres d'exception NestJS [#38ecea7](https://github.com/proconnect-gouv/federation/issues/38ecea7).
    - **Nettoyage** : Suppression de nombreuses références obsolètes (champs `fqdn`, fonctions de calcul de tokens inutilisées, services `pcdbapi`) [#1427](https://github.com/proconnect-gouv/federation/issues/1427), [#1485](https://github.com/proconnect-gouv/federation/issues/1485), [#1370](https://github.com/proconnect-gouv/federation/issues/1370).
- **Performance & Infrastructure** :
    - Optimisation des performances via l'utilisation de correspondances de chaînes exactes pour les requêtes MongoDB [#1369](https://github.com/proconnect-gouv/federation/issues/1369).
    - Accélération du "watcher" MongoDB local pour le développement [#1451](https://github.com/proconnect-gouv/federation/issues/1451).
    - Ajout de points de contrôle de santé (healthchecks `livez`/`readyz`) pour l'interface d'administration [#1391](https://github.com/proconnect-gouv/federation/issues/1391).
- **Qualité & Tests** :
    - Amélioration de la fiabilité des tests E2E via une meilleure gestion de la base de données (utilisation de `TRUNCATE` et `reseed`) [#1449](https://github.com/proconnect-gouv/federation/issues/1449).
    - Standardisation des commandes de tests Cypress [#f757a4a](https://github.com/proconnect-gouv/federation/issues/f757a4a).

### Autres changements
- **Documentation** : Mise à jour du fichier README et ajout de la documentation concernant `hyyyperbridge` [#1448](https://github.com/proconnect-gouv/federation/issues/1448), [#888e759](https://github.com/proconnect-gouv/federation/issues/888e759).
