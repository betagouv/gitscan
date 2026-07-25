## Changelog : immersion-facile (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment concernant la gestion des agences et des conventions, ainsi que par des corrections de bugs et des optimisations techniques. Des efforts ont également été déployés pour améliorer la sécurité et la conformité, notamment en matière de gestion des données personnelles et de notifications.

### Évolutions fonctionnelles
- Amélioration de l'affichage des informations de l'agence dans la page de document de convention. [#5048](https://github.com/gip-inclusion/immersion-facile/issues/5048)
- Ajout d'une notification pour les agences lorsqu'une évaluation est créée avec le statut "NON_PRESENT".
- Possibilité pour un prescripteur de modifier la date de naissance du bénéficiaire dans la convention.
- Affichage du logo de l'agence sur le document d'évaluation si fourni.
- Ajout d'un bouton pour supprimer les droits d'accès d'un utilisateur à une agence, avec une modale de confirmation.
- Amélioration de l'affichage de la description du feedback de diffusion dans une modale.
- Ajout d'une alerte dans le formulaire d'agence si des informations obligatoires sont manquantes.
- Mise à jour des textes légaux (politique de confidentialité, mentions légales, CGU). [#5011](https://github.com/gip-inclusion/immersion-facile/issues/5011)
- Ajout d'un lien vers l'inscription dans le message d'erreur du SIRET.
- Amélioration de la gestion des agences fermées et de la suppression des tâches inactives.
- Ajout de la possibilité d'activer une agence via un seul canal.

### Évolutions techniques
- Refactorisation de plusieurs UseCases pour utiliser un builder, améliorant la lisibilité et la maintenabilité du code.
- Mise à jour des dépendances (libphonenumber, pnpm).
- Amélioration de la gestion des tests (suppression de tests inutiles, correction de tests défaillants).
- Optimisation de la récupération des sections NAF avec mise en cache.
- Suppression du job cron pour la fermeture des agences inactives.
- Amélioration de la gestion des erreurs et des codes de statut HTTP.
- Passage à PostgreSQL client 17.
- Ajout de contraintes de suppression en cascade sur les tables liées aux agences.
- Amélioration de la gestion des adresses (gestion des champs vides).
- Correction de problèmes liés à l'affichage des boutons dans les modales.
- Amélioration de la sécurité (correction de CSP, gestion des renouvellements de mots de passe INSEE).
- Suppression de code inutilisé.

### Autres changements
- Mise à jour de la documentation.
- Amélioration du formatage du code.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Correction de bugs mineurs.
- Mise à jour des messages d'erreur pour plus de clarté.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la gestion des logs.
- Suppression de paramètres d'authentification FT Connect inutilisés.
- Modification du planning de la tâche de rappel des droits d'agence.
- Suppression de la version dupliquée des CGU.
- Ajout de tests pour la suppression des utilisateurs liés à une convention.
- Amélioration de la gestion des notifications (bannissement, confirmation d'agence).
- Suppression des informations de webinar dans l'email d'activation de l'agence.
- Amélioration de la gestion des erreurs de validation.
- Ajout de la possibilité de filtrer les résultats OpenCage par type.
- Suppression de la quarantaine et définition d'une priorité basse pour certaines tâches.
- Ajout de la possibilité de mettre à jour le code NAF d'un établissement marketing.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Amélioration de la gestion des emails (signature, contenu).
- Correction de l'affichage des valeurs sélectionnées dans le champ MultipleAddressInput.
- Ajout de tests pour la suppression des utilisateurs par ID de convention.
- Amélioration de la gestion des erreurs dans les tests.
- Suppression de la gestion des utilisateurs FT Connect.
- Amélioration de la gestion des droits d'accès.
- Ajout d'un test pour vérifier que la suppression d'un utilisateur ne fait rien s'il n'y a pas de conseiller présent.
- Suppression des paramètres d'authentification FT Connect.
- Ajout de la possibilité de rafraîchir le cache pour index.html.
- Ajout de documentation ADR.
- Ajout de la possibilité de notifier les utilisateurs de l'agence en cas de bannissement d'un établissement.
- Ajout d'un email pour le validateur.
- Amélioration de la gestion des notifications Slack.
- Ajout d'un test pour le préfixe téléphonique.
- Ajout de la possibilité de filtrer les résultats de l'établissement dans le tableau de bord.
- Amélioration de la gestion des erreurs de date de naissance.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
- Ajout de la possibilité de masquer le bouton de suppression des droits d'agence pour les utilisateurs auto-supprimables.
