## Changelog : mon-indemnisation-justice (30 derniers jours, au 23/10/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec la modernisation de son infrastructure (passage à FrankenPHP) pour gagner en performance et en stabilité. Des améliorations de sécurité majeures ont été déployées pour protéger les échanges et les documents téléchargés, tandis que le parcours d'inscription et les outils de gestion pour les agents ont été simplifiés et harmonisés.

### Évolutions fonctionnelles
- **Expérience Agent :** Harmonisation des avis d'intervention pour l'ensemble des agents FDO [#177](https://github.com/betagouv/mon-indemnisation-justice/pull/177) et création d'une nouvelle vue de données pour les agents de l'administration [#183](https://github.com/betagouv/mon-indemnisation-justice/pull/183).
- **Parcours Utilisateur :** Amélioration du processus de création de compte par invitation via FranceConnect et correction de plusieurs erreurs de saisie dans les formulaires.
- **Information :** Mise en place d'une page de maintenance statique pour informer les utilisateurs lors des périodes d'indisponibilité du service.

### Évolutions techniques
- **Infrastructure & Déploiement :** Migration de l'environnement de production vers FrankenPHP, simplification de l'usage de Docker (désormais limité à l'environnement de développement) et optimisation de la stratégie de déploiement.
- **Sécurité :** Renforcement de la protection contre les failles XSS lors du téléchargement de pièces jointes et masquage des headers HTTP sensibles via la configuration Caddy [#184](https://github.com/betagouv/mon-indemnisation-justice/pull/184).
- **Base de données :** Création d'une nouvelle vue via une migration pour optimiser l'accès aux données.
- **CI/CD & Tests :** Optimisation de la chaîne d'intégration continue (correction de l'installation de `poppler-utils`) et mise à jour des suites de tests fonctionnels.

### Autres changements
- Mise à jour de certains textes de l'interface utilisateur.
- Nettoyage des anciens scripts et méthodes de déploiement.
