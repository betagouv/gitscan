## Changelog : csplab (30 derniers jours, au 2026-06-16)

### Résumé
Ce mois-ci, l'équipe a continué à développer et améliorer les fonctionnalités de csplab, notamment en se concentrant sur l'ingestion de données, l'interface utilisateur et la gestion des utilisateurs. Des améliorations significatives ont été apportées à l'authentification, à la présentation des offres d'emploi et à l'infrastructure globale du projet. L'ajout de tests et l'amélioration de la documentation sont également des points importants de cette période.

### Évolutions fonctionnelles
- Ajout d'une page de connexion avec une interface utilisateur améliorée [#752](https://github.com/betagouv/csplab/issues/752).
- Affichage du métier de l'utilisateur dans la liste des offres [#747](https://github.com/betagouv/csplab/issues/747).
- Implémentation de la soumission de candidature [#729](https://github.com/betagouv/csplab/issues/729).
- Ajout de badges et de composants d'avatar pour l'interface utilisateur [#682](https://github.com/betagouv/csplab/issues/682), [#683](https://github.com/betagouv/csplab/issues/683).
- Amélioration de l'affichage des composants de formulaire de base [#646](https://github.com/betagouv/csplab/issues/646).
- Possibilité de créer des utilisateurs avec un profil candidat ou agent [#735](https://github.com/betagouv/csplab/issues/735), [#722](https://github.com/betagouv/csplab/issues/722).
- Ajout d'une authentification à deux facteurs (2FA) pour l'administration Django [#699](https://github.com/betagouv/csplab/issues/699).
- Ajout d'une fonctionnalité pour lister les sources de données [#574](https://github.com/betagouv/csplab/issues/574).

### Évolutions techniques
- Refactorisation de l'architecture pour utiliser Celery pour le traitement asynchrone des webhooks [#737](https://github.com/betagouv/csplab/issues/737).
- Amélioration de la gestion des dépendances et des tests, avec des mises à jour régulières et des refactorisations [#793](https://github.com/betagouv/csplab/issues/793), [#792](https://github.com/betagouv/csplab/issues/792), [#791](https://github.com/betagouv/csplab/issues/791), [#785](https://github.com/betagouv/csplab/issues/785), [#783](https://github.com/betagouv/csplab/issues/783), [#745](https://github.com/betagouv/csplab/issues/745).
- Migration vers un modèle utilisateur personnalisé pour une meilleure flexibilité et sécurité [#614](https://github.com/betagouv/csplab/issues/614), [#616](https://github.com/betagouv/csplab/issues/616), [#630](https://github.com/betagouv/csplab/issues/630), [#632](https://github.com/betagouv/csplab/issues/632).
- Amélioration de l'infrastructure de test et de déploiement, notamment avec l'ajout de workflows GitHub Actions [#606](https://github.com/betagouv/csplab/issues/606), [#658](https://github.com/betagouv/csplab/issues/658), [#718](https://github.com/betagouv/csplab/issues/718).
- Utilisation de composants React et Storybook pour le développement de l'interface utilisateur [#596](https://github.com/betagouv/csplab/issues/596), [#716](https://github.com/betagouv/csplab/issues/716).
- Ajout d'index manquants sur les bases de données pour améliorer les performances [#786](https://github.com/betagouv/csplab/issues/786), [#789](https://github.com/betagouv/csplab/issues/789).
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité [#662](https://github.com/betagouv/csplab/issues/662), [#672](https://github.com/betagouv/csplab/issues/672), [#673](https://github.com/betagouv/csplab/issues/673).

### Autres changements
- Ajout d'un fichier `security.txt` pour la divulgation responsable des vulnérabilités [#695](https://github.com/betagouv/csplab/issues/695).
- Mise à jour de la documentation et des modèles de pull request [#619](https://github.com/betagouv/csplab/issues/619), [#721](https://github.com/betagouv/csplab/issues/721).
- Amélioration de la configuration de GitHub Pages [#727](https://github.com/betagouv/csplab/issues/727).
- Ajout de tests pour l'accessibilité de l'interface utilisateur [#740](https://github.com/betagouv/csplab/issues/740).
- Publication du notebook sur GitHub Pages [#641](https://github.com/betagouv/csplab/issues/641).
- Correction de bugs divers et amélioration de la stabilité du projet.
