## Changelog : api-subventions-asso (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des données Osiris, notamment des actions de subvention, avec l'ajout de nouvelles DTOs et routes API. Des corrections et refactorings ont également été effectués pour optimiser la performance et la robustesse de l'API. Enfin, des améliorations ont été apportées à l'intégration avec Brevo et à la gestion des fichiers Osiris.

### Évolutions fonctionnelles
- Ajout de nouvelles DTOs (Data Transfer Objects) pour les associations et les détails des fournisseurs et d'Osiris.
- Implémentation de routes API pour récupérer les détails des subventions et des actions Osiris.
- Affichage des actions Osiris dans la modale de détail des subventions sur le frontend.
- Amélioration de la détection des nouveaux fichiers Chorus sur le bucket S3.
- Correction de la gestion des formats de nombres européens avec la virgule comme séparateur décimal.
- Correction de l'envoi de paramètres vides à l'API Brevo Transaction.
- Suppression des fichiers vides du répertoire de téléchargements Osiris grâce à un nouveau script.

### Évolutions techniques
- Refactoring de la gestion des entités Osiris (actions et requêtes) avec des DTOs et des migrations.
- Amélioration de la validation des requêtes API.
- Mise à jour de la configuration TypeScript pour inclure les TODOs.
- Remplacement de Lerna par pnpm workspaces pour la gestion des dépendances.
- Optimisation de l'indexation des données Osiris (actions et requêtes) - temporairement désactivée puis réactivée avec des corrections.
- Refactoring du service `api-asso` vers une architecture basée sur des adaptateurs et des ports.
- Suppression de champs potentiellement inconnus dans les entités Osiris.
- Utilisation d'une fonction de sanitisation des nombres à virgule flottante.

### Autres changements
- Ajout de documentation pour le script de récupération des données LCA-OSIRIS.
- Mise à jour des dépendances du frontend.
- Corrections mineures du fichier `CHANGELOG.md`.
- Corrections de la configuration du `Procfile`.
- Ajout du fichier `.versionrc.json`.
