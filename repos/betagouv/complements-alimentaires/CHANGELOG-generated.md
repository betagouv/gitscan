## Changelog : complements-alimentaires (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité du site avec l'implémentation d'une politique de sécurité du contenu (CSP), des corrections de vulnérabilités et des améliorations de l'accessibilité. Des ajustements ont également été apportés à l'administration, notamment pour la gestion des entreprises mandatées et des substances, ainsi que des mises à jour techniques et de dépendances.

### Évolutions fonctionnelles
- Ajout de la possibilité d'inclure l'entreprise mandatée lors de la duplication d'une demande. (#2708)
- Amélioration de la validation automatique des articles 15, réduisant le temps d'attente pour les utilisateurs. (#2703)
- Ajout du SIRET et de la TVA dans l'export des données pour les SD. (#2682)
- Correction d'un bug d'overflow sur la page de déclaration. (#2643)
- Ajout de l'URL de l'admin Django personnalisable. (#2661)
- Ajout de l'entreprise mandatée dans l'interface d'administration. (#2706)
- Amélioration de l'accessibilité des liens et des boutons, notamment avec des titres et des noms explicites pour les lecteurs d'écran. (#2628, #2720)
- Correction de liens de téléchargement sur les pages de certificats et de résultats. (#2720)

### Évolutions techniques
- Implémentation initiale d'une politique de sécurité du contenu (CSP) pour renforcer la sécurité du site. (#2662)
- Mise à jour de plusieurs dépendances : Django (6.0.2), Vue.js (3.5.27), babel, prettier, eslint, et autres.
- Suppression des styles inline dans l'administration et le frontend. (#2660, #2657)
- Mise à jour de l'image Docker. (#2677)
- Suppression de l'utilisation de `mark_safe` dans l'administration pour des raisons de sécurité. (#2685)

### Autres changements
- Ajout de Metabase dans la configuration CSP. (#2700)
- Mise à jour du logo du ministère dans les certificats. (#2687)
- Amélioration de la structure des breadcrumbs. (#2661)
- Correction de bugs mineurs et améliorations de la qualité du code.
