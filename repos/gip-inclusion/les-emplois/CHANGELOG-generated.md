## Changelog : les-emplois (30 derniers jours, au 2026-09-08)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration du suivi des parcours (PASS IAE) grâce à l'intégration d'outils de gestion internes et de notifications automatiques. L'expérience utilisateur a été enrichie par de nouveaux indicateurs pour anticiper les fins de contrat (pour les employeurs et les accompagnateurs) et par une refonte de l'identité visuelle de la plateforme pour garantir une meilleure cohérence.

### Évolutions fonctionnelles
- **Gestion des PASS IAE (Approvals) :** Remplacement des outils externes (Tally) par un formulaire interne pour la clôture des dossiers, mise en place de notifications automatiques pour les candidats lors de la clôture, et possibilité pour le support de générer des liens de prolongation hors délais.
- **Accompagnement et suivi des candidats :** Création d'un onglet "Accompagnateurs" dans la vue candidat, ajout de bannières d'alerte et de compteurs pour anticiper les fins de contrat, et nouveaux filtres de recherche spécifiques aux acteurs IAE.
- **Interface et Expérience Utilisateur :** Refonte globale de l'identité visuelle (branding), réorganisation du menu "Structure" pour les employeurs, et amélioration de l'affichage des candidatures (tri par nom, meilleure gestion des espaces).
- **Insertion et Offres :** Importation des offres d'emploi des employeurs "Handi Engagés" via France Travail, sauvegarde automatique des pièces jointes lors des orientations, et ajout d'un filtre "handicap" pour les offres d'emploi.

### Évolutions techniques
- **Architecture et Refactoring :** Suppression de modules obsolètes (`gps`, `recommendations`, `SPS`) et centralisation de la logique métier (éligibilité, clôture) dans des utilitaires pour faciliter la maintenance.
- **Données et API :** Optimisation des performances des requêtes pour les vues candidats, ajout de nouveaux champs de suivi (dates de dernière action), extension des droits d'accès (scopes) des API, et création de nouvelles tables pour le tableau de bord GEIQ.
- **Automatisation et Maintenance :** Mise en place de nouvelles commandes de gestion pour la détection de fichiers manquants ou perdus et la mise à jour automatique des affectations des candidats.

### Autres changements
- Amélioration significative de la couverture et de la robustesse des tests automatisés.
- Mise à jour de la documentation technique (notamment sur l'alternative Podman à Docker).
- Optimisation des workflows CI/CD et de la cohérence du formatage du code.
