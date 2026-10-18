## Changelog : etape (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de la plateforme, tant sur le plan visuel que technique. L'interface a été intégralement modernisée grâce à l'adoption d'un nouveau design system, offrant une meilleure lisibilité et une expérience utilisateur plus fluide. En parallèle, l'infrastructure a été profondément restructurée pour séparer le front-office du back-office et renforcer la sécurité globale du système.

### Évolutions fonctionnelles
- **Refonte visuelle complète** : Adoption d'un nouveau design system incluant de nouvelles typographies (Geist, Bricolage Grotesque), une nouvelle palette de couleurs et des composants d'interface améliorés (dialogues d'alerte, états des champs). [#78](https://github.com/betagouv/etape/pull/78)
- **Amélioration de l'accessibilité** : Optimisation des contrastes pour les textes secondaires et meilleure visibilité des surfaces de l'interface.
- **Nouvelles fonctionnalités d'authentification** : Intégration de FranceConnect [#16](https://github.com/betagouv/etape/issues/16).
- **Expérience utilisateur (UX) de session** : Amélioration de la gestion des sessions (écrans d'attente, gestion des erreurs de connexion et de l'expiration de session) pour éviter les boucles de redirection. [#73](https://github.com/betagouv/etape/pull/73)
- **Documents PDF** : Mise à jour du style et des polices des documents de résultats générés.

### Évolutions techniques
- **Modernisation de la stack front-end** : Migration des applications front-office et back-office vers Vite pour des performances accrues. [#71](https://github.com/betagouv/etape/pull/71)
- **Migration de l'API** : Passage de NestJS vers la version 12.
- **Nouvelle architecture de déploiement** : Séparation physique du front-office et du back-office avec des origines distinctes et des domaines (realms) Keycloak dédiés. [#75](https://github.com/betagouv/etape/pull/75)
- **Navigation** : Intégration de TanStack Router pour une gestion plus robuste du routage.
- **Renforcement de la sécurité** : 
    - Mise en place de protections CSRF sur les requêtes de modification de données.
    - Sécurisation des cookies de session via le préfixe `__Host-`.
    - Retrait des secrets et valeurs sensibles des fichiers versionnés et des exemples d'environnement.
- **Optimisation du client API** : Ajout d'intercepteurs Axios et amélioration de la gestion des erreurs et des sessions au sein du client.
- **Qualité et Infrastructure** : 
    - Ajout de tests de bout en bout (E2E) pour le registre Harbor. [#57](https://github.com/betagouv/etape/pull/57)
    - Correction d'un conflit de dépendances sur le `ThrottlerGuard` de NestJS. [#68](https://github.com/betagouv/etape/pull/68)

### Autres changements
- **Documentation** : Mise à jour importante des guides sur l'authentification, le routage, la gestion des sessions et les bonnes pratiques React. [#54](https://github.com/betagouv/etape/pull/54)
- **Nettoyage** : Optimisation du lockfile Vite et nettoyage des fichiers de configuration.
