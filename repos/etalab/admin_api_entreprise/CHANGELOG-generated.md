## Changelog : admin_api_entreprise (30 derniers jours)

### Résumé
Les dernières mises à jour de l'admin API entreprise se concentrent sur l'amélioration de l'expérience utilisateur, notamment en ajoutant des fonctionnalités pour la gestion des requêtes API et l'accès aux données, ainsi que sur la correction de bugs et l'amélioration de la sécurité. Des efforts ont également été déployés pour améliorer la documentation et la maintenance du code.

### Évolutions fonctionnelles
- Ajout d'un lien vers un dashboard Metabase pour visualiser les requêtes API dans l'interface d'administration (#2130).
- Possibilité de contourner l'authentification en local pour faciliter le développement et les tests (#2106, #2105, #2103).
- Affichage des tokens valides dans l'interface d'administration (#2031).
- Amélioration de l'interface pour la soumission de requêtes API, avec désactivation du bouton tant qu'un endpoint n'est pas sélectionné (#2132).
- Correction du mois renvoyé par l'API QF v2 (correction d'un décalage de 1 mois) (#2114).
- Ajout de la gestion des données FD URSSAF/MSA dans l'API effectifs (#2113).
- Ajout de la possibilité de demander des informations SIADE via l'interface d'administration (#2116).
- Ajout d'une fonctionnalité pour gérer les paramètres de sécurité des requêtes d'autorisation (limitation de débit, liste blanche d'IP) (#2120).

### Évolutions techniques
- Refactorisation de la gestion des requêtes API en utilisant un pattern facade pour une meilleure organisation du code (#2120).
- Mise à jour de plusieurs dépendances : Rack (3.2.4 -> 3.2.5), Faraday (2.14.0 -> 2.14.1), Rubocop (1.82.1 -> 1.84.1), Brakeman (7.1.2 -> 8.0.1), RSpec-rails, Nokogiri.
- Amélioration de la documentation pour gérer les erreurs HTTP 409 Conflict (#2104).
- Suppression des endpoints dépréciés de l'API Particulier (#2130).
- Ajout de tests et correction de warnings dans les spécifications (#2097).
- Mise à jour des fichiers OpenAPI locaux avec les dernières définitions (#2133).

### Autres changements
- Ajout d'une documentation pour l'utilisation du skill Claude Code pour le bump de version (#2135).
- Ajout d'un utilisateur administrateur dans les seeds pour faciliter les tests (#2120).
- Ajout d'une adresse email administrateur dans le README (#2116).
- Mise à jour du statut de l'API cnav/psu en "beta" (#2127).
- Ignorer le répertoire `sandbox/` dans le contrôle de version (#2107).
- Amélioration de la documentation CLAUDE.md (#2103).
