## Changelog : sylvasan (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la création et de la gestion des enquêtes, notamment en ajoutant de nouveaux types de champs et en permettant leur réorganisation. Des améliorations significatives ont également été apportées à l'application mobile, avec l'ajout de la possibilité de télécharger des cartes hors ligne et l'affichage des enquêtes. De nombreuses mises à jour de dépendances ont été effectuées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer des enquêtes avec différents types de champs : radio, texte, zone de texte, switch et select [#142](https://github.com/betagouv/sylvasan/pull/142).
- Possibilité de réorganiser les champs dans le formulaire de création d'enquête.
- Ajout de l'affichage des réponses aux enquêtes dans l'interface web [#139](https://github.com/betagouv/sylvasan/pull/139).
- Création des pages individuelles pour visualiser les détails des enquêtes et de leurs réponses [#141](https://github.com/betagouv/sylvasan/pull/141).
- L'application mobile peut maintenant télécharger des cartes hors ligne pour une utilisation sans connexion internet.
- L'application mobile affiche la liste des enquêtes.
- Confirmation demandée avant la suppression d'un champ dans le formulaire [#158](https://github.com/betagouv/sylvasan/pull/158).

### Évolutions techniques
- Mise à jour de nombreuses dépendances (Django, React, Vue, TailwindCSS, PostgreSQL, Sentry, Capacitor) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- Refactor du code pour améliorer la maintenabilité et la lisibilité.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Mise en place d'un système de gestion des types partagés entre le web et le mobile.
- Configuration de Vite pour une meilleure performance de l'application web.
- Mise à jour de l'action GitHub CodeQL pour une analyse de sécurité plus approfondie.

### Autres changements
- Ajout d'une ADR (Architecture Decision Record) expliquant la décision d'utiliser des types partagés [#110](https://github.com/betagouv/sylvasan/pull/110).
- Amélioration de la documentation interne.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour des fichiers de configuration.
- Correction d'une vulnérabilité de sécurité liée à la gestion des archives [#78](https://github.com/betagouv/sylvasan/pull/78).
