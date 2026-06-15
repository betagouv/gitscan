## Changelog : api-subventions-asso (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'intégration avec Osiris, notamment pour la gestion des actions et subventions, et sur la refactorisation du code pour une meilleure maintenabilité. Des corrections ont également été apportées pour gérer correctement les formats de données et les erreurs potentielles.

### Évolutions fonctionnelles
- Ajout de la possibilité de détecter les nouveaux fichiers Chorus sur le bucket S3. [#3937](https://github.com/betagouv/api-subventions-asso/issues/3937)
- Amélioration de l'affichage des actions Osiris dans l'interface utilisateur (modal). [#3910](https://github.com/betagouv/api-subventions-asso/issues/3910)
- Les détails des subventions Osiris sont désormais accessibles via une nouvelle route API. [#3840](https://github.com/betagouv/api-subventions-asso/issues/3840)
- Prise en charge d'un nouveau DTO (Data Transfer Object) pour les associations. [#3921](https://github.com/betagouv/api-subventions-asso/issues/3921)
- Gestion améliorée des formats de nombres européens avec la virgule comme séparateur décimal. [#3956](https://github.com/betagouv/api-subventions-asso/issues/3956)
- Correction d'un problème empêchant l'envoi de paramètres vides à l'API Brevo Transaction. [#3951](https://github.com/betagouv/api-subventions-asso/issues/3951)

### Évolutions techniques
- Refactorisation de la validation des requêtes. [#3935](https://github.com/betagouv/api-subventions-asso/issues/3935)
- Refactorisation du service `api-asso` vers une architecture adaptateur/port. [#3907](https://github.com/betagouv/api-subventions-asso/issues/3907)
- Refactorisation des entités brutes Osiris pour améliorer la qualité du code et la gestion des champs. [#3918](https://github.com/betagouv/api-subventions-asso/issues/3918)
- Migration du système de gestion de paquets de Lerna à pnpm workspaces. [#3917](https://github.com/betagouv/api-subventions-asso/issues/3917)
- Mise à jour des configurations TypeScript pour inclure des annotations `TODO`. [#3907](https://github.com/betagouv/api-subventions-asso/issues/3907)
- Renommage de certaines variables et fonctions pour plus de clarté et de cohérence. [#3960](https://github.com/betagouv/api-subventions-asso/issues/3960)

### Autres changements
- Ajout de documentation expliquant la différence entre les points de terminaison de téléchargement par association et par document. [#3938](https://github.com/betagouv/api-subventions-asso/issues/3938)
- Ajout d'agrégations récentes à la documentation de l'API. [#3952](https://github.com/betagouv/api-subventions-asso/issues/3952)
- Correction du fichier `Procfile`. [#3957](https://github.com/betagouv/api-subventions-asso/issues/3957)
- Ajout d'un fichier `.versionrc.json`. [#3959](https://github.com/betagouv/api-subventions-asso/issues/3959)
- Suppression de fichiers vides du répertoire des téléchargements Osiris. [#3920](https://github.com/betagouv/api-subventions-asso/issues/3920)
- Réactivation temporaire des index pour les requêtes et actions Osiris (avec des désactivations temporaires pour maintenance).
