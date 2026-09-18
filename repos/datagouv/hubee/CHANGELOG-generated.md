## Changelog : hubee (30 derniers jours, au 15 septembre 2026)

### Résumé
Ce mois-ci, hubee a franchi une étape importante dans la sécurisation des échanges et l'amélioration de l'expérience utilisateur. Les agents bénéficient désormais de fonctionnalités de recherche et de filtrage plus performantes sur le portail, ainsi que de la possibilité de télécharger des pièces jointes. Parallèlement, la sécurité a été considérablement renforcée par l'intégration de l'authentification multi-facteur (MFA) et la mise en place d'un socle OAuth2 pour l'API.

### Évolutions fonctionnelles
- **Portail** : possibilité de télécharger les pièces reçues [#163](https://github.com/datagouv/hubee/issues/163).
- **Portail** : amélioration de la recherche et du filtrage des démarches (recherche par numéro, filtrage sur plusieurs flux simultanés et maintien du tri).
- **Portail** : consultation des démarches liées à son organisation [#128](https://github.com/datagouv/hubee/issues/128).
- **Portail** : amélioration de la gestion des erreurs (affichage de pages 404 pour les démarches introuvables [#149](https://github.com/datagouv/hubee/issues/149) et pages 503 en cas de panne du service amont).
- **Sécurité** : support de l'authentification multi-facteur (MFA) imposée par le fournisseur d'identité et exigence d'un second facteur pour les comptes à privilèges.
- **Sécurité** : renforcement de la validation de l'identité pour les liens d'organisation (SIRET/INSEE).

### Évolutions techniques
- **API & Sécurité** : mise en place du socle OAuth2 (mode `client_credentials`) et protection des endpoints par token avec attribution des appels.
- **API & Sécurité** : intégration du protocole OpenID Connect (OIDC) avec ProConnect.
- **API & Sécurité** : gestion automatique de la purge quotidienne des tokens expirés et uniformisation des réponses d'erreur (401 Unauthorized).
- **Architecture** : refonte majeure de la logique du portail (organisation des données, gestion des accès via Pundit et séparation des responsabilités de livraison).
- **CI/CD & Tests** : mise en place de "Review Apps" pour les Pull Requests [#134](https://github.com/datagouv/hubee/issues/134).
- **CI/CD & Tests** : enrôlement automatique de comptes de test dans les environnements déployés [#154](https://github.com/datagouv/hubee/issues/154).

### Autres changements
- **Documentation** : mise à jour des guides d'utilisation de l'API (runbooks), des processus de lecture du portail et des couches d'authentification.
- **Maintenance** : amélioration de la journalisation (logging) des erreurs et des décisions d'accès.
