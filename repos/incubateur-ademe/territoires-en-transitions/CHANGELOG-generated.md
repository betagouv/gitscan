## Changelog : territoires-en-transitions (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des référentiels, des rapports, des notifications et de l'expérience utilisateur globale. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de la plateforme, notamment concernant l'import de données et l'affichage des informations. Des améliorations ont également été apportées à l'interface utilisateur, notamment au niveau des badges et des formulaires.

### Évolutions fonctionnelles
- Ajout de l'information COT (Code Type d'Occupation) dans la liste des collectivités et les informations utilisateur.
- Possibilité de définir des préférences de notification pour les utilisateurs (activation/désactivation des notifications d'affectation).
- Amélioration de l'import de plans avec gestion du texte enrichi.
- Correction de l'affichage des indicateurs enfants.
- Correction de l'affichage des actions liées depuis la page indicateur pour le rôle contributeur.
- Correction du comportement du titre éditable avec des valeurs vides.
- Les filtres de FA par plan ont été corrigés.
- Ajout d'un lien vers la page de désinscription des notifications dans les emails.
- Affichage d'un toast et reset du formulaire après un import de plan réussi.
- Ajout d'une date max à la saisie de date de fin d'une sous-action.
- Amélioration de l'affichage des badges dans l'export PDF.
- Possibilité de n'activer que certains cron jobs pour les outils.
- Possibilité de créer des demandes de support depuis Crisp.
- Suppression du feature flag de génération de rapports, la fonctionnalité est maintenant activée par défaut.

### Évolutions techniques
- Migration des endpoints de la liste des membres vers trpc.
- Migration de la mise à jour des réponses aux questions de personnalisation vers tRPC.
- Utilisation de tRPC pour la mise à jour des commentaires dans les référentiels.
- Passage des instances de gouvernance de string à tag.
- Amélioration du schéma Zod pour le parsing des fiches venant d'un fichier Excel.
- Refactor de l'import de plan pour utiliser les snapshots.
- Mise à jour des packages Supabase.
- Ajout de la gestion backend des types 'prefecture_region' et 'prefecture_departement'.
- Ajout d'un correlationId dans les requêtes tRPC et log des erreurs avec le correlationId.
- Suppression de Datadog Logs et activation de Sentry Logs.
- Amélioration des performances des suppressions dans `indicateur_source_metadonnee`.
- Correction de l'ordre des migrations sqitch.
- Suppression de code obsolète (vues SQL, fonctions, tests).
- Amélioration de la gestion des erreurs et des timeouts.

### Autres changements
- Ajout d'un event à l'ouverture de la modale de modification d'une action.
- Ajout de tests pour la mise à jour des réponses aux questions de personnalisation.
- Documentation améliorée.
- Correction de divers bugs d'interface utilisateur et de rendu.
- Mise à jour de la version du sheet d'import personnalisation.
- Amélioration des tests e2e.
- Correction de coquilles et amélioration des libellés.
- Ajout de commentaires et de documentation.
- Refactoring de code pour améliorer la lisibilité et la maintenabilité.
- Suppression de composants inutilisés.
- Correction de problèmes de linting.
- Ajout de clés React pour éviter les erreurs d'affichage.
- Amélioration de la gestion des erreurs dans les notifications.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des dépendances.
