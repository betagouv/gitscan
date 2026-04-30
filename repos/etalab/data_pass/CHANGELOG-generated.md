## Changelog : data_pass (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur les formulaires de demande et la gestion des droits. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la sécurité et de la conformité. L'API a été enrichie avec de nouvelles fonctionnalités et une meilleure documentation.

### Évolutions fonctionnelles
- Ajout d'une bannière de maintenance ProConnect visible sur toutes les pages.
- Amélioration de l'affichage du statut des demandes (revendiquées/non revendiquées).
- Suppression du compteur de longlet "Demandes" pour les instructeurs.
- Affichage du numéro de SIRET formaté dans les emails.
- Ajout d'un accusé de réception lors du dépôt d'une demande.
- Possibilité de retirer complètement les droits d'un utilisateur.
- Ajout d'un lien vers la création d'une demande dans la liste des habilitations.
- Amélioration de l'affichage des scopes sans groupes dans les formulaires.
- Correction d'un bug empêchant la soumission d'une demande avec une adresse email non vérifiée.
- Ajout d'un lien vers le formulaire de création d'habilitation API Entreprise Entrouvert.
- Ajout de la possibilité de bannir un utilisateur et de bloquer son accès.
- Affichage d'un message d'erreur plus clair en cas d'échec de connexion.
- Amélioration de l'affichage des scopes boursier MEN sur les formulaires CNAF.
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API.
- Ajout de la gestion des CGU vides pour les types d'habilitation dynamiques.

### Évolutions techniques
- Refactorisation de la gestion des rôles avec l'introduction de `RoleHierarchy` et `RoleSet`.
- Ajout de tests contractuels pour garantir la cohérence des définitions.
- Amélioration de la gestion des erreurs et des exceptions.
- Optimisation des requêtes SQL sur le dashboard demandeur pour améliorer les performances.
- Mise à jour des dépendances (Rubocop, Rack-Session, Zlib, etc.).
- Ajout de webhooks pour notifier les événements liés aux organisations (création, mise à jour).
- Amélioration de la documentation de l'API et ajout de tutoriels pour les développeurs.
- Ajout de contrôles pour forcer la définition du titre de chaque vue.
- Ajout d'un service `MarkdownRenderer` pour le rendu du Markdown.
- Amélioration de la gestion des scopes OAuth2.
- Ajout d'une page de documentation dédiée aux webhooks.
- Amélioration de la gestion des erreurs lors de la soumission de formulaires.
- Ajout de la raison du bannissement sur l'utilisateur.
- Ajout d'événements pour les mises à jour des données.
- Amélioration de la gestion des erreurs dans les emails.

### Autres changements
- Mise à jour de la documentation des rôles.
- Correction de fautes de frappe dans les textes des emails.
- Ajout d'instructions pour l'exécution des tests en CI.
- Amélioration des descriptions de l'OpenAPI.
- Ajout d'un guide de contribution avec CLAUDE.
- Correction d'un problème de remplacement des apostrophes dans les tests.
- Suppression de code inutile et nettoyage du code.
- Correction d'un revert de mise à jour de dépendances.
- Ajout d'un suffixe au slug des HabilitationType.
- Correction d'un bug lié à l'affichage des scopes.
- Ajout d'un message d'erreur plus clair en cas d'échec de connexion.
- Correction d'un problème lié à l'affichage des habilitations FC.
- Ajout de la gestion de l'erreur `EntityNotFoundError`.
- Amélioration de la gestion des diffs des changelogs.
- Correction d'un problème de timezone en CI.
- Ajout de la gestion des erreurs à la soumission d'une demande avec turbo-stream.
- Ajout de la gestion des scopes cnaf_adresse et cnaf_enfants pour le formulaire Solis.
- Ajout de la gestion des scopes men_regime_pensionnat pour l'API Particulier.
- Ajout de la gestion des scopes beneficiaires_effectifs_inpi pour l'API Entreprise Entrouvert.
- Ajout de la possibilité d'afficher l'astérisque depuis les validators dsfr_file_field.
- Ajout de la possibilité de remplir le champ `france_connect_authorization_id` lors de la validation d'une demande.
- Ajout de la gestion des droits de niveau FD.
- Ajout de la gestion des cas personne physique et organisation étrangère dans Organization#name.
- Ajout de la gestion des erreurs à la soumission d'une demande avec turbo-stream.
- Ajout de la gestion des scopes boursier MEN sur les formulaires CNAF.
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API.
- Ajout de la possibilité d'ajouter des webhooks sur create_by_api et update_by_api.
- Ajout de la possibilité de retirer complètement les droits d'un utilisateur.
- Ajout de la possibilité d'ajouter un lien vers le formulaire de création d'une demande dans la liste des habilitations.
- Ajout de la possibilité d'améliorer l'affichage des scopes sans groupes dans les formulaires.
- Ajout de la possibilité de corriger un bug empêchant la soumission d'une demande avec une adresse email non vérifiée.
- Ajout de la possibilité d'ajouter un lien vers le formulaire de création d'habilitation API Entreprise Entrouvert.
- Ajout de la possibilité de bannir un utilisateur et de bloquer son accès.
- Ajout de la possibilité d'afficher un message d'erreur plus clair en cas d'échec de connexion.
- Ajout de la possibilité d'améliorer l'affichage des scopes boursier MEN sur les formulaires CNAF.
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API.
- Ajout de la possibilité d'ajouter des webhooks sur create_by_api et update_by_api.
- Ajout de la possibilité de retirer complètement les droits d'un utilisateur.
- Ajout de la possibilité d'ajouter un lien vers le formulaire de création d'une demande dans la liste des habilitations.
- Ajout de la possibilité d'améliorer l'affichage des scopes sans groupes dans les formulaires.
- Ajout de la possibilité de corriger un bug empêchant la soumission d'une demande avec une adresse email non vérifiée.
- Ajout de la possibilité d'ajouter un lien vers le formulaire de création d'habilitation API Entreprise Entrouvert.
- Ajout de la possibilité de bannir un utilisateur et de bloquer son accès.
- Ajout de la possibilité d'afficher un message d'erreur plus clair en cas d'échec de connexion.
- Ajout de la possibilité d'améliorer l'affichage des scopes boursier MEN sur les formulaires CNAF.
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API.
- Ajout de la possibilité d'ajouter des webhooks sur create_by_api et update_by_api.
- Ajout de la possibilité de retirer complètement les droits d'un utilisateur.
- Ajout de la possibilité d'ajouter un lien vers le formulaire de création d'une demande dans la liste des habilitations.
- Ajout de la possibilité d'améliorer l'affichage des scopes sans groupes dans les formulaires.
- Ajout de la possibilité de corriger un bug empêchant la soumission d'une demande avec une adresse email non vérifiée.
- Ajout de la possibilité d'ajouter un lien vers le formulaire de création d'habilitation API Entreprise Entrouvert.
- Ajout de la possibilité de bannir un utilisateur et de bloquer son accès.
- Ajout de la possibilité d'afficher un message d'erreur plus clair en cas d'échec de connexion.
- Ajout de la possibilité d'améliorer l'affichage des scopes boursier MEN sur les formulaires CNAF.
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API.
- Ajout de la possibilité d'ajouter des webhooks sur create_by_api et update_by_api.
- Ajout de la possibilité de retirer complètement les droits d'un utilisateur.
- Ajout de la possibilité d'ajouter un lien vers le formulaire de création d'une demande dans la liste des habilitations.
- Ajout de la possibilité d'améliorer l'affichage des scopes sans groupes dans les formulaires.
