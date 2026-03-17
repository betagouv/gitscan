## Changelog : admin_api_entreprise (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par des améliorations de la gestion des accès et des tokens, l'ajout de nouvelles API (CNOUS étudiant boursier, MSA alerte date ressource), et des mises à jour de documentation. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la maintenabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité pour les administrateurs de créer un nouveau token pour une demande d'autorisation validée. [#2152](https://github.com/etalab/admin_api_entreprise/pull/2152)
- Affichage des tokens valides dans l'interface d'administration. [#2031](https://github.com/etalab/admin_api_entreprise/pull/2031)
- Intégration de l'API CNOUS étudiant boursier v4 avec les champs de radiation. [#2129](https://github.com/etalab/admin_api_entreprise/pull/2129)
- Ajout de l'API MSA alerte date ressource. [#2126](https://github.com/etalab/admin_api_entreprise/pull/2126)
- Ajout d'un lien vers un dashboard Metabase pour les requêtes API dans l'interface d'administration. [#2132](https://github.com/etalab/admin_api_entreprise/pull/2132)
- Ajout de la version 3 vers 4 de l'API fiche MEN scolarités avec périmètre géographique. [#2145](https://github.com/etalab/admin_api_entreprise/pull/2145)
- Amélioration de l'affichage de l'historique des versions pour les endpoints GIP MDS effectifs. [#2154](https://github.com/etalab/admin_api_entreprise/pull/2154)

### Évolutions techniques
- Rotation annuelle du token webhook pour renforcer la sécurité. [#2155](https://github.com/etalab/admin_api_entreprise/pull/2155)
- Migration des scopes des tokens vers les demandes d'autorisation pour une meilleure gestion. [#2146](https://github.com/etalab/admin_api_entreprise/pull/2146)
- Amélioration de la gestion des erreurs Sentry en ignorant les erreurs ActionView::MissingTemplate. [#2133](https://github.com/etalab/admin_api_entreprise/pull/2133)
- Refactorisation du code pour respecter les nouvelles limites de longueur de classe Rubocop (150 lignes). [#2143](https://github.com/etalab/admin_api_entreprise/pull/2143)
- Suppression des endpoints dépréciés du catalogue de l'API Particulier. [#2130](https://github.com/etalab/admin_api_entreprise/pull/2130)
- Chargement asynchrone du statut de ping des endpoints via Turbo Frame pour améliorer la performance. [#2151](https://github.com/etalab/admin_api_entreprise/pull/2151)

### Autres changements
- Mise à jour de la documentation pour les APIs EAJE et QF. [#2125](https://github.com/etalab/admin_api_entreprise/pull/2125)
- Ajout du skill Claude Code bump-version. [#2131](https://github.com/etalab/admin_api_entreprise/pull/2131)
- Correction de l'affichage du lien "Historique de version" dans la barre latérale.
- Diverses mises à jour de dépendances (nokogiri, rack, rubocop, rspec-rails, faker, etc.).
- Correction de warnings dans les specs. [#2097](https://github.com/etalab/admin_api_entreprise/pull/2097)
- Mise à jour des fichiers OpenAPI locaux. [#2133](https://github.com/etalab/admin_api_entreprise/pull/2133)
