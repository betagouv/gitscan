## Changelog : les-emplois (30 derniers jours, au 05 septembre 2026)

### Résumé
Ce mois-ci, le projet a bénéficié d'une refonte de son identité visuelle et de sa terminologie pour gagner en clarté. L'expérience utilisateur a été enrichie par de nouveaux outils de suivi, notamment des alertes de fin de parcours et des tableaux de bord pour les employeurs. Parallèlement, des optimisations techniques importantes ont été réalisées pour améliorer la performance des processus automatiques et renforcer la sécurité des échanges de données via les API.

### Évolutions fonctionnelles
- **Identité et interface** : Refonte de l'identité visuelle (branding), réorganisation du menu de structure et mise à jour de la terminologie métier (notamment pour les PASS IAE).
- **Expérience utilisateur** : Ajout de bannières d'information (difficultés techniques, webinaires, fins de contrat), amélioration du tri des candidatures par nom et optimisation de la navigation (redirections automatiques).
- **Suivi et accompagnement** : Création d'un onglet "Accompagnateurs" avec une boîte de revue, ajout de compteurs de fin de contrat pour les employeurs IAE et de suggestions de prochaines étapes pour les bénéficiaires.
- **Données et intégration** : Importation des offres d'emploi des "Employeurs Handi Engagés" via l'API France Travail.

### Évolutions techniques
- **Performance** : Optimisation des requêtes de listes et accélération des tâches planifiées (cron) pour le traitement des résumés.
- **API et Sécurité** : Ajustement des périmètres de sécurité (scopes) des API (France Travail, h2a, RQTH) et mise en place d'un middleware de redirection automatique vers le nouveau domaine.
- **Architecture et Base de données** : Création de nouvelles tables pour le suivi GEIQ, refactorisation de la logique de gestion des prolongations et automatisation de la gestion des dates de création/mise à jour des enregistrements.
- **Qualité logicielle** : Amélioration significative de la robustesse et de la couverture de la suite de tests.

### Autres changements
- **Documentation et outils** : Ajout de documentation sur l'utilisation de Podman comme alternative à Docker et mise à jour des workflows CI/CD et du Makefile.
