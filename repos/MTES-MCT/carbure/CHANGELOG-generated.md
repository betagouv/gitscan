## Changelog : carbure (30 derniers jours)

### Résumé
Les dernières mises à jour de Carbure se concentrent sur l'amélioration de la gestion des données biogaz et biométhane, notamment pour les utilisateurs DREAL. De nouvelles fonctionnalités ont été ajoutées pour faciliter la gestion des déclarations annuelles, le suivi des données énergétiques et l'intégration de données UDB. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité pour les utilisateurs DREAL de créer manuellement des déclarations annuelles. (#1693)
- Amélioration de l'interface d'administration pour la gestion des données QualiCharge, incluant l'affichage de quantités en kWh et la validation en masse.
- Ajout de filtres et d'une page de gestion des entreprises pour les utilisateurs DREAL.
- Ajout d'une page de gestion des contacts pour les DREAL.
- Possibilité pour les DREAL de modifier le statut "ouvert" des déclarations annuelles.
- Amélioration de la gestion des données UDB, incluant la conversion des quantités et la gestion des erreurs.
- Ajout de la possibilité de valider l'ensemble des données Qualicharge.
- Ajout de la gestion des digestats (tonnage brut, etc.) et de l'efficacité énergétique.
- Ajout de la gestion des organismes d'aide aux contrats.
- Amélioration de l'affichage des données d'injection de biométhane.
- Ajout de la gestion des codes INSEE et des champs propane.

### Évolutions techniques
- Refactorisation du code pour améliorer la performance et la lisibilité.
- Mise à jour des dépendances et corrections de bugs.
- Amélioration de la gestion des erreurs et ajout de logs plus détaillés.
- Utilisation de feature flags pour activer/désactiver certaines fonctionnalités (SAF logistics validation).
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Optimisation des requêtes en base de données pour améliorer les performances.
- Intégration de Sentry pour la surveillance des erreurs.
- Amélioration de la gestion des erreurs UDB et ajout de tests associés.

### Autres changements
- Mise à jour des traductions.
- Correction de problèmes d'affichage et de validation de formulaires.
- Nettoyage du code et suppression de code obsolète.
- Mise à jour des données de référence (dépôts DGDDI, listes de producteurs de biométhane).
- Correction de bugs mineurs et amélioration de l'expérience utilisateur.
- Ajout de commentaires et documentation pour faciliter la maintenance du code.
- Correction de problèmes liés à la gestion des identifiants des dépôts.
- Ajout de la gestion des unités UDB et des conversions de quantités.
- Correction d'un problème de validation des certificats Qualicharge.
- Correction d'un bug lié à l'affichage des filtres de certificats.
- Correction d'un problème d'affichage des quantités d'énergie renouvelable.
- Correction d'un bug lié à la validation des tickets SAF.
- Ajout de la gestion des routes de transport pour les SAF.
- Amélioration de la gestion des erreurs lors de l'importation de fichiers Excel pour les SAF.
- Ajout de la possibilité d'importer des données SAF via un fichier Excel.
- Ajout de la gestion des types de dépôts SAF.
- Correction de bugs et amélioration de la performance de l'interface utilisateur SAF.
