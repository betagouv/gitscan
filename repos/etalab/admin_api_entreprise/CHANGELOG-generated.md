## Changelog : admin_api_entreprise (30 derniers jours)

### Résumé
Les dernières mises à jour de l'admin API entreprise se concentrent sur l'amélioration de la gestion des API, l'ajout de nouvelles fonctionnalités pour les utilisateurs (notamment pour les requêtes API et l'accès aux données des étudiants boursiers), et le renforcement de la sécurité. Des corrections de bugs et des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un lien vers un tableau de bord Metabase pour visualiser les requêtes API dans l'interface d'administration (#2130).
- Possibilité de demander des informations SIADE via l'interface d'administration (#2132).
- Affichage des tokens valides dans l'interface d'administration (#2031).
- Ajout de la fiche CNOUS étudiant boursier v4 avec la gestion des radiations (#2129).
- Correction du mois renvoyé par l'API QF v2 (correction d'un décalage) (#2114).
- Ajout d'une interface pour contourner l'authentification en environnement de test (staging et sandbox) (#2106, #2105, #2103).
- Documentation de la gestion des erreurs HTTP 409 (Conflit) pour les requêtes concurrentes (#2104).
- Ajout de la gestion de l'authentification multi-facteur (MFA) pour les utilisateurs MonComptePro via ProConnect (#2099).
- Suppression des endpoints dépréciés du catalogue de l'API Particulier (#2130).

### Évolutions techniques
- Refactorisation de la gestion des requêtes API via un pattern facade (#2125).
- Ajout de paramètres de sécurité pour les requêtes d'autorisation (limitation de débit, liste blanche d'IP) (#2122).
- Mise à jour de plusieurs dépendances :
    - Nokogiri (1.19.0 -> 1.19.1) (#2136)
    - Rack (3.2.4 -> 3.2.5) (#2128)
    - Faraday (2.14.0 -> 2.14.1) (#2119)
    - Rubocop (plusieurs mises à jour mineures) (#2124, #2118, #2110, #2109, #2108)
    - Brakeman (7.1.2 -> 8.0.1) (#2101)
    - Faker (3.5.3 -> 3.6.0) (#2101)
- Amélioration de la gestion des tests et correction d'avertissements (#2097).

### Autres changements
- Ajout d'un skill Claude Code pour automatiser le bump de version (#2135).
- Ajout d'une nouvelle version pour l'API cnous/statut_etudiant_boursier (#2135).
- Mise à jour des fichiers OpenAPI locaux (#2133).
- Ajout d'un email administrateur dans le README (#2125).
- Amélioration de la documentation CLAUDE.md (#2103).
- Ignorer le dossier `sandbox/` dans le dépôt (#2107).
